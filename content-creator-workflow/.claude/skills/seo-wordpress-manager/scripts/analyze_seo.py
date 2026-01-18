#!/usr/bin/env python3
"""
SEO Analyzer
Fetches posts and identifies SEO issues for Claude to optimize.
This script prepares data for Claude to analyze and generate improvements.
"""

import sys
import json
import argparse
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional

# Add shared modules to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "shared"))
from config_loader import SkillConfig
from utils import save_json, timestamp

from wp_graphql_client import WPGraphQLClient, load_credentials_from_config


@dataclass
class SEOIssue:
    """Represents an SEO issue found in a post"""
    post_id: int
    post_title: str
    post_url: str
    post_excerpt: str
    current_seo_title: str
    current_meta_desc: str
    current_focus_keyphrase: str
    issues: list[str]
    priority: str  # "high", "medium", "low"


def analyze_title(title: str, post_title: str) -> list[str]:
    """Analyze SEO title for issues"""
    issues = []

    if not title or title.strip() == "":
        issues.append("MISSING: No SEO title set")
        return issues

    length = len(title)
    if length > 60:
        issues.append(f"TOO_LONG: Title is {length} chars (max 60)")
    elif length < 30:
        issues.append(f"TOO_SHORT: Title is {length} chars (min 30 recommended)")

    # Check if it's just the post title (no optimization)
    if title.strip().lower() == post_title.strip().lower():
        issues.append("GENERIC: SEO title is same as post title (not optimized)")

    return issues


def analyze_description(description: str, default_patterns: list[str] = None) -> list[str]:
    """Analyze meta description for issues"""
    issues = []
    default_patterns = default_patterns or []

    if not description or description.strip() == "":
        issues.append("MISSING: No meta description set")
        return issues

    length = len(description)
    if length > 160:
        issues.append(f"TOO_LONG: Description is {length} chars (max 160)")
    elif length < 120:
        issues.append(f"TOO_SHORT: Description is {length} chars (min 120 recommended)")

    # Check for default/generic patterns
    desc_lower = description.lower()
    for pattern in default_patterns:
        if pattern.lower() in desc_lower:
            issues.append(f"DEFAULT: Contains generic text '{pattern}'")
            break

    return issues


def analyze_keyphrase(keyphrase: str) -> list[str]:
    """Analyze focus keyphrase for issues"""
    issues = []

    if not keyphrase or keyphrase.strip() == "":
        issues.append("MISSING: No focus keyphrase set")

    return issues


def determine_priority(issues: list[str]) -> str:
    """Determine priority based on issues"""
    if any("MISSING" in issue for issue in issues):
        return "high"
    if any("TOO_LONG" in issue or "DEFAULT" in issue for issue in issues):
        return "medium"
    return "low"


def analyze_posts(
    posts: list[dict],
    default_patterns: list[str] = None,
    check_keyphrase: bool = False
) -> list[SEOIssue]:
    """Analyze posts for SEO issues"""
    results = []

    for post in posts:
        seo = post.get("seo", {}) or {}

        issues = []

        # Analyze each field
        title_issues = analyze_title(
            seo.get("title", ""),
            post.get("title", "")
        )
        issues.extend(title_issues)

        desc_issues = analyze_description(
            seo.get("metaDesc", ""),
            default_patterns
        )
        issues.extend(desc_issues)

        if check_keyphrase:
            kw_issues = analyze_keyphrase(seo.get("focuskw", ""))
            issues.extend(kw_issues)

        # Only include posts with issues
        if issues:
            # Get excerpt from content if available
            excerpt = ""
            if post.get("excerpt"):
                excerpt = post["excerpt"][:300]
            elif post.get("content"):
                # Strip HTML and get first 300 chars
                import re
                text = re.sub(r'<[^>]+>', '', post["content"])
                excerpt = text[:300].strip()

            results.append(SEOIssue(
                post_id=post.get("databaseId", 0),
                post_title=post.get("title", ""),
                post_url=post.get("uri", ""),
                post_excerpt=excerpt,
                current_seo_title=seo.get("title", ""),
                current_meta_desc=seo.get("metaDesc", ""),
                current_focus_keyphrase=seo.get("focuskw", ""),
                issues=issues,
                priority=determine_priority(issues)
            ))

    return results


def generate_analysis_report(issues: list[SEOIssue]) -> dict:
    """Generate analysis report for Claude to process"""

    # Group by priority
    high = [i for i in issues if i.priority == "high"]
    medium = [i for i in issues if i.priority == "medium"]
    low = [i for i in issues if i.priority == "low"]

    # Count issue types
    issue_counts = {}
    for issue in issues:
        for i in issue.issues:
            issue_type = i.split(":")[0]
            issue_counts[issue_type] = issue_counts.get(issue_type, 0) + 1

    return {
        "metadata": {
            "analyzed_at": timestamp(),
            "total_posts_analyzed": len(issues),
            "posts_with_issues": len(issues)
        },
        "summary": {
            "high_priority": len(high),
            "medium_priority": len(medium),
            "low_priority": len(low),
            "issue_breakdown": issue_counts
        },
        "posts_needing_optimization": [asdict(i) for i in issues],
        "instructions_for_claude": """
## How to Process This Analysis

For each post in `posts_needing_optimization`, generate optimized SEO content:

### SEO Title Guidelines:
- Length: 50-60 characters
- Structure: Primary Keyword - Secondary | Brand
- Front-load important keywords
- Make it compelling and click-worthy

### Meta Description Guidelines:
- Length: 150-160 characters
- Include a call-to-action
- Include the focus keyphrase naturally
- Make it compelling - this is your ad copy in search results

### Focus Keyphrase Guidelines:
- One primary keyword/phrase per post
- Long-tail keywords often perform better
- Match search intent

### Output Format:
Generate a changes.json file with this structure:
```json
{
  "updates": [
    {
      "post_id": 123,
      "post_title": "Original Title",
      "current": {
        "seo_title": "old title",
        "meta_desc": "old description",
        "focus_keyphrase": "old keyword"
      },
      "new": {
        "seo_title": "New Optimized Title | Brand",
        "meta_desc": "Compelling 150-160 char description with CTA",
        "focus_keyphrase": "target keyword"
      }
    }
  ]
}
```
"""
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze WordPress posts for SEO issues")
    parser.add_argument("--config", help="Path to config.json")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--category", help="Filter by category slug")
    parser.add_argument("--limit", type=int, help="Limit number of posts")
    parser.add_argument("--all", action="store_true", help="Fetch all posts")
    parser.add_argument("--check-keyphrase", action="store_true",
                        help="Include focus keyphrase in analysis")
    parser.add_argument("--default-patterns", nargs="+",
                        help="Patterns to detect default/generic descriptions")

    args = parser.parse_args()

    # Load config
    config_path = Path(args.config) if args.config else None
    if not config_path:
        default_config = Path(__file__).parent.parent / "config.json"
        if default_config.exists():
            config_path = default_config

    try:
        credentials = load_credentials_from_config(config_path)
    except ValueError as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        sys.exit(1)

    client = WPGraphQLClient(credentials)

    # Fetch posts
    print("Fetching posts from WordPress...")
    if args.all:
        posts = client.get_all_posts_with_seo(category=args.category)
    else:
        limit = args.limit or 100
        result = client.get_posts_with_seo(limit=limit, category=args.category)
        posts = result.get("posts", {}).get("nodes", [])

    print(f"Fetched {len(posts)} posts")

    # Analyze posts
    print("Analyzing SEO issues...")
    default_patterns = args.default_patterns or []
    issues = analyze_posts(
        posts,
        default_patterns=default_patterns,
        check_keyphrase=args.check_keyphrase
    )

    print(f"Found {len(issues)} posts with SEO issues")

    # Generate report
    report = generate_analysis_report(issues)

    # Output
    if args.output:
        output_path = Path(args.output)
        save_json(report, output_path)
        print(f"\nAnalysis saved to: {output_path}")
    else:
        print(json.dumps(report, indent=2))

    # Print summary
    summary = report["summary"]
    print(f"\n{'=' * 60}")
    print("SEO ANALYSIS SUMMARY")
    print(f"{'=' * 60}")
    print(f"Posts with issues: {len(issues)}")
    print(f"  High priority: {summary['high_priority']}")
    print(f"  Medium priority: {summary['medium_priority']}")
    print(f"  Low priority: {summary['low_priority']}")
    print(f"\nIssue breakdown:")
    for issue_type, count in summary["issue_breakdown"].items():
        print(f"  {issue_type}: {count}")

    print(f"\nNext step: Have Claude review the analysis and generate changes.json")


if __name__ == "__main__":
    main()
