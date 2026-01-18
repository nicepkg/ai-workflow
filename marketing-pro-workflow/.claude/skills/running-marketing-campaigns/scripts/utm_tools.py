#!/usr/bin/env python3
"""
UTM Campaign Tracking Tools

Enhanced UTM parameter management with:
- UTM generation and validation
- GA4 channel alignment checking
- Batch processing from CSV
- Case inconsistency auditing
- QR code generation (requires: pip install qrcode pillow)
- URL shortening via bit.ly API (requires: BITLY_API_KEY env var)

Usage:
    python utm_tools.py generate --source facebook --medium paid-social --campaign spring-2025
    python utm_tools.py build --url https://example.com --source email --medium newsletter --campaign q1-launch
    python utm_tools.py validate --url "https://example.com?utm_source=email&utm_medium=cpc"
    python utm_tools.py batch --file campaigns.csv --url https://example.com --output tracking.csv
    python utm_tools.py audit --file urls.txt
    python utm_tools.py qr --url "https://example.com?utm_source=qr&utm_medium=offline" --output code.png
    python utm_tools.py ga4-check --source facebook --medium paid-social
"""

import argparse
import csv
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import parse_qs, urlencode, urlparse

# Optional imports for extended features
try:
    import qrcode
    from PIL import Image
    HAS_QRCODE = True
except ImportError:
    HAS_QRCODE = False

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


# GA4 Default Channel Grouping definitions
# Based on: https://support.google.com/analytics/answer/9756891
GA4_CHANNEL_DEFINITIONS = {
    "Paid Search": {
        "sources": ["google", "bing", "yahoo", "baidu", "duckduckgo"],
        "mediums": ["cpc", "ppc", "paidsearch", "paid-search", "paid_search"],
        "description": "Traffic from paid search campaigns"
    },
    "Paid Social": {
        "sources": ["facebook", "instagram", "linkedin", "twitter", "x", "tiktok", "pinterest", "snapchat"],
        "mediums": ["cpc", "ppc", "paid-social", "paid_social", "paidsocial"],
        "description": "Traffic from paid social media ads"
    },
    "Organic Social": {
        "sources": ["facebook", "instagram", "linkedin", "twitter", "x", "tiktok", "pinterest", "youtube"],
        "mediums": ["social", "organic-social", "organic_social"],
        "description": "Traffic from organic social media posts"
    },
    "Email": {
        "sources": ["*"],  # Any source
        "mediums": ["email", "e-mail", "e_mail", "newsletter"],
        "description": "Traffic from email campaigns"
    },
    "Affiliates": {
        "sources": ["*"],
        "mediums": ["affiliate", "affiliates"],
        "description": "Traffic from affiliate partners"
    },
    "Referral": {
        "sources": ["*"],
        "mediums": ["referral"],
        "description": "Traffic from referral links"
    },
    "Display": {
        "sources": ["*"],
        "mediums": ["display", "banner", "cpm", "interstitial"],
        "description": "Traffic from display advertising"
    },
    "Organic Search": {
        "sources": ["google", "bing", "yahoo", "baidu", "duckduckgo"],
        "mediums": ["organic"],
        "description": "Traffic from organic search results"
    }
}

# Standard source values
STANDARD_SOURCES = {
    "google": "Google (search, ads, display)",
    "facebook": "Facebook / Meta",
    "instagram": "Instagram",
    "linkedin": "LinkedIn",
    "twitter": "Twitter / X",
    "x": "X (formerly Twitter)",
    "tiktok": "TikTok",
    "youtube": "YouTube",
    "pinterest": "Pinterest",
    "snapchat": "Snapchat",
    "bing": "Microsoft Bing",
    "newsletter": "Email newsletter",
    "email": "Email (general)",
    "qr": "QR code",
    "sms": "SMS / Text message",
    "partner": "Partner / Co-marketing",
}

# Standard medium values
STANDARD_MEDIUMS = {
    "cpc": "Cost per click (paid search)",
    "ppc": "Pay per click (alternative to cpc)",
    "paid-social": "Paid social media",
    "social": "Organic social",
    "organic": "Organic search",
    "email": "Email campaign",
    "newsletter": "Newsletter",
    "display": "Display advertising",
    "banner": "Banner ads",
    "cpm": "Cost per mille (display)",
    "affiliate": "Affiliate marketing",
    "referral": "Referral traffic",
    "offline": "Offline sources (QR, print)",
    "retargeting": "Retargeting campaigns",
    "video": "Video advertising",
}


@dataclass
class ValidationResult:
    """Result of URL validation."""
    url: str
    valid: bool
    issues: List[str]
    warnings: List[str]
    utm_params: Dict[str, str]
    ga4_channel: Optional[str]


def validate_utm_value(value: str, param_name: str) -> List[str]:
    """Validate a single UTM parameter value."""
    issues = []

    # Check for spaces
    if " " in value:
        issues.append(f"{param_name} contains spaces - use hyphens instead")

    # Check for uppercase
    if value != value.lower():
        issues.append(f"{param_name} contains uppercase - GA4 is case-sensitive")

    # Check for special characters (allow hyphens and underscores)
    if not re.match(r'^[a-zA-Z0-9_-]+$', value):
        issues.append(f"{param_name} contains invalid characters")

    return issues


def generate_utm_parameters(
    source: str,
    medium: str,
    campaign: str,
    content: Optional[str] = None,
    term: Optional[str] = None,
    strict: bool = True
) -> Tuple[Dict[str, str], List[str]]:
    """
    Generate UTM parameters with validation.

    Args:
        source: utm_source (e.g., "google", "facebook", "newsletter")
        medium: utm_medium (e.g., "cpc", "email", "social")
        campaign: utm_campaign (e.g., "spring-sale-2025")
        content: utm_content (optional, e.g., "hero-cta")
        term: utm_term (optional, for paid search keywords)
        strict: If True, enforce lowercase and no spaces

    Returns:
        Tuple of (parameters dict, list of warnings)
    """
    warnings = []

    # Validate required parameters
    if not all([source, medium, campaign]):
        raise ValueError("source, medium, and campaign are required")

    # Normalize values
    if strict:
        source = source.lower().replace(" ", "-")
        medium = medium.lower().replace(" ", "-")
        campaign = campaign.lower().replace(" ", "-")
        if content:
            content = content.lower().replace(" ", "-")
        if term:
            term = term.lower().replace(" ", "-")

    # Check against standards
    if source.lower() not in STANDARD_SOURCES:
        warnings.append(f"Non-standard source '{source}' - verify GA4 alignment")

    if medium.lower() not in STANDARD_MEDIUMS:
        warnings.append(f"Non-standard medium '{medium}' - verify GA4 alignment")

    params = {
        "utm_source": source,
        "utm_medium": medium,
        "utm_campaign": campaign,
    }

    if content:
        params["utm_content"] = content
    if term:
        params["utm_term"] = term

    return params, warnings


def build_tracking_url(base_url: str, utm_params: Dict[str, str]) -> str:
    """Build a complete tracking URL with UTM parameters."""
    if not base_url.startswith(("http://", "https://")):
        raise ValueError("URL must start with http:// or https://")

    parsed = urlparse(base_url)
    existing_params = parse_qs(parsed.query)

    # Flatten existing params
    flat_params = {k: v[0] if isinstance(v, list) and v else v for k, v in existing_params.items()}

    # Merge (UTM takes precedence)
    all_params = {**flat_params, **utm_params}

    # Rebuild URL
    query_string = urlencode(all_params)
    base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

    return f"{base}?{query_string}"


def determine_ga4_channel(source: str, medium: str) -> Optional[str]:
    """Determine which GA4 default channel a source/medium maps to."""
    source_lower = source.lower()
    medium_lower = medium.lower()

    for channel, rules in GA4_CHANNEL_DEFINITIONS.items():
        source_match = rules["sources"] == ["*"] or source_lower in rules["sources"]
        medium_match = medium_lower in rules["mediums"]

        if source_match and medium_match:
            return channel

    return None


def validate_tracking_url(url: str) -> ValidationResult:
    """Validate a tracking URL for UTM compliance."""
    issues = []
    warnings = []

    parsed = urlparse(url)
    params = parse_qs(parsed.query)

    # Extract UTM params
    utm_params = {k: v[0] if v else "" for k, v in params.items() if k.startswith("utm_")}

    # Check required params
    required = ["utm_source", "utm_medium", "utm_campaign"]
    missing = [p for p in required if p not in utm_params]
    if missing:
        issues.append(f"Missing required parameters: {', '.join(missing)}")

    # Validate each parameter
    for param, value in utm_params.items():
        param_issues = validate_utm_value(value, param)
        issues.extend(param_issues)

    # Check GA4 alignment
    ga4_channel = None
    if "utm_source" in utm_params and "utm_medium" in utm_params:
        ga4_channel = determine_ga4_channel(utm_params["utm_source"], utm_params["utm_medium"])
        if not ga4_channel:
            warnings.append("Source/medium may not map to a standard GA4 channel")

    return ValidationResult(
        url=url,
        valid=len(issues) == 0,
        issues=issues,
        warnings=warnings,
        utm_params=utm_params,
        ga4_channel=ga4_channel
    )


def audit_urls_for_inconsistencies(urls: List[str]) -> Dict:
    """Audit a list of URLs for case inconsistencies and non-standard values."""
    results = {
        "total_urls": len(urls),
        "valid_urls": 0,
        "invalid_urls": 0,
        "source_variants": {},
        "medium_variants": {},
        "campaign_variants": {},
        "issues": [],
    }

    for url in urls:
        validation = validate_tracking_url(url)

        if validation.valid:
            results["valid_urls"] += 1
        else:
            results["invalid_urls"] += 1
            results["issues"].append({
                "url": url,
                "issues": validation.issues
            })

        # Track variants for each parameter
        for param, value in validation.utm_params.items():
            if param == "utm_source":
                key = value.lower()
                if key not in results["source_variants"]:
                    results["source_variants"][key] = set()
                results["source_variants"][key].add(value)

            elif param == "utm_medium":
                key = value.lower()
                if key not in results["medium_variants"]:
                    results["medium_variants"][key] = set()
                results["medium_variants"][key].add(value)

            elif param == "utm_campaign":
                key = value.lower()
                if key not in results["campaign_variants"]:
                    results["campaign_variants"][key] = set()
                results["campaign_variants"][key].add(value)

    # Convert sets to lists for JSON serialization
    for key in ["source_variants", "medium_variants", "campaign_variants"]:
        results[key] = {k: list(v) for k, v in results[key].items()}

    # Flag case inconsistencies
    results["case_inconsistencies"] = []
    for param_type in ["source_variants", "medium_variants", "campaign_variants"]:
        for key, variants in results[param_type].items():
            if len(variants) > 1:
                results["case_inconsistencies"].append({
                    "type": param_type.replace("_variants", ""),
                    "canonical": key,
                    "variants": variants,
                    "recommendation": f"Standardize to: {key}"
                })

    return results


def batch_generate(
    campaigns: List[Dict[str, str]],
    base_url: str,
    output_file: Optional[str] = None
) -> List[Dict]:
    """Generate tracking URLs for multiple campaigns."""
    results = []

    for campaign in campaigns:
        try:
            params, warnings = generate_utm_parameters(
                source=campaign.get("source", campaign.get("channel", "unknown")),
                medium=campaign.get("medium", campaign.get("content_type", "content")),
                campaign=campaign.get("campaign", campaign.get("name", "campaign")),
                content=campaign.get("content", campaign.get("variant")),
                term=campaign.get("term"),
            )

            tracking_url = build_tracking_url(base_url, params)
            ga4_channel = determine_ga4_channel(params["utm_source"], params["utm_medium"])

            results.append({
                "campaign_name": campaign.get("campaign", campaign.get("name")),
                "source": params["utm_source"],
                "medium": params["utm_medium"],
                "content": params.get("utm_content", ""),
                "term": params.get("utm_term", ""),
                "ga4_channel": ga4_channel or "Unassigned",
                "tracking_url": tracking_url,
                "warnings": "; ".join(warnings) if warnings else "",
                "generated_at": datetime.now().isoformat(),
            })

        except Exception as e:
            results.append({
                "campaign_name": campaign.get("campaign", campaign.get("name")),
                "error": str(e),
                "tracking_url": "",
            })

    if output_file:
        with open(output_file, 'w', newline='') as f:
            if results:
                writer = csv.DictWriter(f, fieldnames=results[0].keys())
                writer.writeheader()
                writer.writerows(results)
        print(f"Results saved to {output_file}")

    return results


def generate_qr_code(
    url: str,
    output_path: str,
    size: int = 10,
    border: int = 2,
    fill_color: str = "black",
    back_color: str = "white"
) -> bool:
    """
    Generate a QR code for a tracking URL.

    Requires: pip install qrcode pillow
    """
    if not HAS_QRCODE:
        print("Error: QR code generation requires 'qrcode' and 'pillow' packages", file=sys.stderr)
        print("Install with: pip install qrcode pillow", file=sys.stderr)
        return False

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size,
            border=border,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(output_path)

        print(f"QR code saved to {output_path}")
        return True

    except Exception as e:
        print(f"Error generating QR code: {e}", file=sys.stderr)
        return False


def shorten_url(url: str, api_key: Optional[str] = None) -> Optional[str]:
    """
    Shorten a URL using bit.ly API.

    Requires: BITLY_API_KEY environment variable or api_key parameter
    """
    if not HAS_REQUESTS:
        print("Error: URL shortening requires 'requests' package", file=sys.stderr)
        print("Install with: pip install requests", file=sys.stderr)
        return None

    api_key = api_key or os.environ.get("BITLY_API_KEY")
    if not api_key:
        print("Error: BITLY_API_KEY environment variable not set", file=sys.stderr)
        return None

    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        payload = {"long_url": url}

        response = requests.post(
            "https://api-ssl.bitly.com/v4/shorten",
            headers=headers,
            json=payload,
            timeout=10
        )

        if response.status_code == 200 or response.status_code == 201:
            return response.json().get("link")
        else:
            print(f"Error from bit.ly: {response.status_code} - {response.text}", file=sys.stderr)
            return None

    except Exception as e:
        print(f"Error shortening URL: {e}", file=sys.stderr)
        return None


def format_validation_result(result: ValidationResult) -> str:
    """Format validation result for display."""
    lines = []

    status = "VALID" if result.valid else "INVALID"
    lines.append(f"\n{'=' * 60}")
    lines.append(f"URL Validation: {status}")
    lines.append(f"{'=' * 60}")
    lines.append(f"\nURL: {result.url}")

    if result.utm_params:
        lines.append("\nUTM Parameters:")
        for param, value in result.utm_params.items():
            lines.append(f"  {param}: {value}")

    if result.ga4_channel:
        lines.append(f"\nGA4 Channel: {result.ga4_channel}")
    else:
        lines.append("\nGA4 Channel: Unassigned (may appear as 'Other')")

    if result.issues:
        lines.append("\nIssues:")
        for issue in result.issues:
            lines.append(f"  [X] {issue}")

    if result.warnings:
        lines.append("\nWarnings:")
        for warning in result.warnings:
            lines.append(f"  [!] {warning}")

    if result.valid and not result.warnings:
        lines.append("\nNo issues found!")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="UTM Campaign Tracking Tools - Generate, validate, and audit tracking URLs"
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Generate command
    gen_parser = subparsers.add_parser("generate", help="Generate UTM parameters")
    gen_parser.add_argument("--source", "-s", required=True, help="utm_source")
    gen_parser.add_argument("--medium", "-m", required=True, help="utm_medium")
    gen_parser.add_argument("--campaign", "-c", required=True, help="utm_campaign")
    gen_parser.add_argument("--content", help="utm_content (optional)")
    gen_parser.add_argument("--term", help="utm_term (optional)")
    gen_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Build command
    build_parser = subparsers.add_parser("build", help="Build complete tracking URL")
    build_parser.add_argument("--url", "-u", required=True, help="Base URL")
    build_parser.add_argument("--source", "-s", required=True, help="utm_source")
    build_parser.add_argument("--medium", "-m", required=True, help="utm_medium")
    build_parser.add_argument("--campaign", "-c", required=True, help="utm_campaign")
    build_parser.add_argument("--content", help="utm_content (optional)")
    build_parser.add_argument("--term", help="utm_term (optional)")

    # Validate command
    val_parser = subparsers.add_parser("validate", help="Validate tracking URL")
    val_parser.add_argument("--url", "-u", required=True, help="URL to validate")
    val_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Batch command
    batch_parser = subparsers.add_parser("batch", help="Process batch from CSV")
    batch_parser.add_argument("--file", "-f", required=True, help="Input CSV file")
    batch_parser.add_argument("--url", "-u", required=True, help="Base URL")
    batch_parser.add_argument("--output", "-o", help="Output CSV file")

    # Audit command
    audit_parser = subparsers.add_parser("audit", help="Audit URLs for inconsistencies")
    audit_parser.add_argument("--file", "-f", required=True, help="File with URLs (one per line)")
    audit_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # GA4 check command
    ga4_parser = subparsers.add_parser("ga4-check", help="Check GA4 channel mapping")
    ga4_parser.add_argument("--source", "-s", required=True, help="utm_source")
    ga4_parser.add_argument("--medium", "-m", required=True, help="utm_medium")

    # QR command
    qr_parser = subparsers.add_parser("qr", help="Generate QR code for URL")
    qr_parser.add_argument("--url", "-u", required=True, help="URL to encode")
    qr_parser.add_argument("--output", "-o", required=True, help="Output PNG file")
    qr_parser.add_argument("--size", type=int, default=10, help="Box size (default: 10)")

    # Shorten command
    short_parser = subparsers.add_parser("shorten", help="Shorten URL via bit.ly")
    short_parser.add_argument("--url", "-u", required=True, help="URL to shorten")
    short_parser.add_argument("--api-key", help="bit.ly API key (or use BITLY_API_KEY env)")

    # List standards command
    list_parser = subparsers.add_parser("list-standards", help="List standard sources and mediums")

    args = parser.parse_args()

    if args.command == "generate":
        try:
            params, warnings = generate_utm_parameters(
                source=args.source,
                medium=args.medium,
                campaign=args.campaign,
                content=args.content,
                term=args.term,
            )

            if args.json:
                output = {"params": params, "warnings": warnings}
                print(json.dumps(output, indent=2))
            else:
                print("\nUTM Parameters Generated:")
                print("-" * 40)
                for k, v in params.items():
                    print(f"  {k}: {v}")
                print(f"\nQuery string: {urlencode(params)}")

                if warnings:
                    print("\nWarnings:")
                    for w in warnings:
                        print(f"  [!] {w}")

        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "build":
        try:
            params, warnings = generate_utm_parameters(
                source=args.source,
                medium=args.medium,
                campaign=args.campaign,
                content=args.content,
                term=args.term,
            )
            tracking_url = build_tracking_url(args.url, params)
            ga4_channel = determine_ga4_channel(params["utm_source"], params["utm_medium"])

            print(f"\nTracking URL:")
            print(tracking_url)
            print(f"\nGA4 Channel: {ga4_channel or 'Unassigned'}")

            if warnings:
                print("\nWarnings:")
                for w in warnings:
                    print(f"  [!] {w}")

        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "validate":
        result = validate_tracking_url(args.url)

        if args.json:
            output = {
                "url": result.url,
                "valid": result.valid,
                "issues": result.issues,
                "warnings": result.warnings,
                "utm_params": result.utm_params,
                "ga4_channel": result.ga4_channel,
            }
            print(json.dumps(output, indent=2))
        else:
            print(format_validation_result(result))

        sys.exit(0 if result.valid else 1)

    elif args.command == "batch":
        try:
            with open(args.file) as f:
                reader = csv.DictReader(f)
                campaigns = list(reader)

            if not campaigns:
                print(f"No campaigns found in {args.file}", file=sys.stderr)
                sys.exit(1)

            results = batch_generate(campaigns, args.url, args.output)

            print(f"\nProcessed {len(results)} campaigns")
            valid = sum(1 for r in results if "error" not in r)
            print(f"  Valid: {valid}")
            print(f"  Errors: {len(results) - valid}")

        except FileNotFoundError:
            print(f"File not found: {args.file}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "audit":
        try:
            with open(args.file) as f:
                urls = [line.strip() for line in f if line.strip()]

            if not urls:
                print(f"No URLs found in {args.file}", file=sys.stderr)
                sys.exit(1)

            results = audit_urls_for_inconsistencies(urls)

            if args.json:
                print(json.dumps(results, indent=2))
            else:
                print(f"\nAudit Results")
                print("=" * 60)
                print(f"Total URLs: {results['total_urls']}")
                print(f"Valid: {results['valid_urls']}")
                print(f"Invalid: {results['invalid_urls']}")

                if results["case_inconsistencies"]:
                    print(f"\nCase Inconsistencies Found: {len(results['case_inconsistencies'])}")
                    print("-" * 60)
                    for inc in results["case_inconsistencies"]:
                        print(f"\n  Type: {inc['type']}")
                        print(f"  Variants: {', '.join(inc['variants'])}")
                        print(f"  Recommendation: {inc['recommendation']}")
                else:
                    print("\nNo case inconsistencies found!")

        except FileNotFoundError:
            print(f"File not found: {args.file}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "ga4-check":
        channel = determine_ga4_channel(args.source, args.medium)

        print(f"\nGA4 Channel Mapping")
        print("=" * 40)
        print(f"Source: {args.source}")
        print(f"Medium: {args.medium}")
        print(f"Maps to: {channel or 'Unassigned (will appear as Other)'}")

        if channel:
            print(f"\nChannel description: {GA4_CHANNEL_DEFINITIONS[channel]['description']}")

    elif args.command == "qr":
        if generate_qr_code(args.url, args.output, size=args.size):
            print(f"URL encoded: {args.url}")
        else:
            sys.exit(1)

    elif args.command == "shorten":
        short_url = shorten_url(args.url, args.api_key)
        if short_url:
            print(f"Original: {args.url}")
            print(f"Shortened: {short_url}")
        else:
            sys.exit(1)

    elif args.command == "list-standards":
        print("\nStandard UTM Sources")
        print("=" * 50)
        for source, desc in STANDARD_SOURCES.items():
            print(f"  {source}: {desc}")

        print("\nStandard UTM Mediums")
        print("=" * 50)
        for medium, desc in STANDARD_MEDIUMS.items():
            print(f"  {medium}: {desc}")

        print("\nGA4 Channel Definitions")
        print("=" * 50)
        for channel, rules in GA4_CHANNEL_DEFINITIONS.items():
            print(f"\n  {channel}:")
            print(f"    Mediums: {', '.join(rules['mediums'])}")
            print(f"    {rules['description']}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
