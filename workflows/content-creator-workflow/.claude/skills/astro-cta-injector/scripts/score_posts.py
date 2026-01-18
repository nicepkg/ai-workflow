#!/usr/bin/env python3
"""
Score posts for CTA relevance
Analyzes content and assigns relevance scores based on keywords and content length
"""

import sys
import json
import re
import argparse
from pathlib import Path
from typing import Optional
from dataclasses import dataclass, asdict
from glob import glob

from bs4 import BeautifulSoup

# Add shared modules to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "shared"))
from config_loader import SkillConfig, load_json_config
from utils import save_json


@dataclass
class PostScore:
    """Scoring result for a single post"""
    file_path: str
    title: str
    word_count: int
    keyword_score: float
    length_score: float
    title_score: float
    total_score: float
    matched_keywords: list[str]
    has_existing_cta: bool
    eligible: bool


def extract_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter from content"""
    frontmatter = {}
    body = content

    # Check for YAML frontmatter (---)
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                import yaml
                frontmatter = yaml.safe_load(parts[1]) or {}
            except:
                # Simple key: value parsing fallback
                for line in parts[1].strip().split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        frontmatter[key.strip()] = value.strip().strip('"\'')
            body = parts[2]

    return frontmatter, body


def extract_text_from_html(html: str) -> str:
    """Extract plain text from HTML content"""
    soup = BeautifulSoup(html, 'html.parser')
    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()
    return soup.get_text(separator=' ', strip=True)


def extract_text_from_astro(content: str) -> str:
    """Extract text content from Astro file"""
    # Remove frontmatter
    _, body = extract_frontmatter(content)

    # Remove Astro script section (between ---)
    if '---' in body:
        parts = body.split('---')
        if len(parts) >= 2:
            body = parts[-1]

    # Remove JSX/JS expressions
    body = re.sub(r'\{[^}]+\}', '', body)

    # Extract text from remaining HTML
    return extract_text_from_html(body)


def calculate_keyword_score(content: str, keywords: list[str]) -> tuple[float, list[str]]:
    """Calculate score based on keyword frequency"""
    content_lower = content.lower()
    word_count = len(content.split())

    matched = []
    total_matches = 0

    for keyword in keywords:
        kw_lower = keyword.lower()
        count = content_lower.count(kw_lower)
        if count > 0:
            matched.append(keyword)
            total_matches += count

    # Normalize by content length (per 1000 words)
    if word_count > 0:
        normalized = (total_matches / word_count) * 1000
    else:
        normalized = 0

    # Cap at 5.0 points
    score = min(normalized, 5.0)
    return score, matched


def calculate_length_score(word_count: int) -> float:
    """Calculate score based on content length"""
    if word_count < 300:
        return 0.0
    elif word_count < 600:
        return 1.0
    elif word_count < 1000:
        return 2.0
    elif word_count < 2000:
        return 3.0
    else:
        return 4.0


def calculate_title_score(title: str, keywords: list[str]) -> float:
    """Calculate score based on title keyword match"""
    title_lower = title.lower()
    matches = sum(1 for kw in keywords if kw.lower() in title_lower)
    return min(matches * 0.5, 1.0)


def has_existing_cta(content: str, cta_type: str) -> bool:
    """Check if content already has a CTA of this type"""
    patterns = [
        f'data-cta-type="{cta_type}"',
        f"data-cta-type='{cta_type}'",
        f'class="cta-{cta_type}"',
        f"class='cta-{cta_type}'",
        f'<!-- CTA:{cta_type} -->',
    ]
    return any(pattern in content for pattern in patterns)


def score_post(
    file_path: Path,
    keywords: list[str],
    cta_type: str,
    min_word_count: int = 300,
    min_score: float = 5.0
) -> PostScore:
    """Score a single post for CTA relevance"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract frontmatter for title
    frontmatter, _ = extract_frontmatter(content)
    title = frontmatter.get('title', file_path.stem)

    # Extract text content
    if file_path.suffix == '.astro':
        text = extract_text_from_astro(content)
    else:
        text = extract_text_from_html(content)

    word_count = len(text.split())

    # Calculate scores
    keyword_score, matched_keywords = calculate_keyword_score(text + ' ' + title, keywords)
    length_score = calculate_length_score(word_count)
    title_score = calculate_title_score(title, keywords)

    total_score = keyword_score + length_score + title_score

    # Check for existing CTA
    existing_cta = has_existing_cta(content, cta_type)

    # Determine eligibility
    eligible = (
        word_count >= min_word_count and
        total_score >= min_score and
        not existing_cta
    )

    return PostScore(
        file_path=str(file_path),
        title=title,
        word_count=word_count,
        keyword_score=round(keyword_score, 2),
        length_score=round(length_score, 2),
        title_score=round(title_score, 2),
        total_score=round(total_score, 2),
        matched_keywords=matched_keywords,
        has_existing_cta=existing_cta,
        eligible=eligible
    )


def find_posts(content_path: Path, patterns: list[str]) -> list[Path]:
    """Find all post files matching patterns"""
    posts = []
    for pattern in patterns:
        matched = list(content_path.glob(pattern))
        posts.extend(matched)
    return sorted(set(posts))


def main():
    parser = argparse.ArgumentParser(description="Score posts for CTA relevance")
    parser.add_argument("--content-path", "-c", required=True, help="Path to content directory")
    parser.add_argument("--cta-type", "-t", required=True, help="CTA type to score for")
    parser.add_argument("--config", help="Path to config.json")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--min-score", type=float, default=5.0, help="Minimum score threshold")
    parser.add_argument("--keywords", nargs="+", help="Override keywords from config")

    args = parser.parse_args()

    # Load config
    config_path = Path(args.config) if args.config else None
    if not config_path:
        default_config = Path(__file__).parent.parent / "config.json"
        if default_config.exists():
            config_path = default_config

    config = {}
    if config_path and config_path.exists():
        config = load_json_config(config_path)

    # Get CTA type configuration
    cta_config = config.get("cta_types", {}).get(args.cta_type, {})

    # Determine keywords
    if args.keywords:
        keywords = args.keywords
    else:
        keywords = cta_config.get("keywords", [])

    if not keywords:
        print(f"Error: No keywords defined for CTA type '{args.cta_type}'", file=sys.stderr)
        print("Use --keywords to specify, or define in config.json", file=sys.stderr)
        sys.exit(1)

    # Get file patterns
    patterns = config.get("file_patterns", ["**/*.astro", "**/*.md", "**/*.mdx"])

    # Get scoring settings
    scoring_config = config.get("scoring", {})
    min_word_count = scoring_config.get("min_word_count", 300)
    min_score = args.min_score or cta_config.get("min_score", 5.0)

    # Find posts
    content_path = Path(args.content_path)
    if not content_path.exists():
        print(f"Error: Content path does not exist: {content_path}", file=sys.stderr)
        sys.exit(1)

    posts = find_posts(content_path, patterns)
    print(f"Found {len(posts)} posts to analyze...")

    # Score each post
    results = []
    for post_path in posts:
        try:
            score = score_post(
                post_path,
                keywords=keywords,
                cta_type=args.cta_type,
                min_word_count=min_word_count,
                min_score=min_score
            )
            results.append(asdict(score))
        except Exception as e:
            print(f"Error scoring {post_path}: {e}", file=sys.stderr)

    # Sort by score (highest first)
    results.sort(key=lambda x: x["total_score"], reverse=True)

    # Separate eligible and ineligible
    eligible = [r for r in results if r["eligible"]]
    ineligible = [r for r in results if not r["eligible"]]

    # Output
    output_data = {
        "cta_type": args.cta_type,
        "keywords": keywords,
        "min_score": min_score,
        "summary": {
            "total_posts": len(results),
            "eligible": len(eligible),
            "ineligible": len(ineligible),
            "already_have_cta": sum(1 for r in results if r["has_existing_cta"])
        },
        "eligible_posts": eligible,
        "ineligible_posts": ineligible
    }

    if args.output:
        output_path = Path(args.output)
        save_json(output_data, output_path)
        print(f"\nResults saved to: {output_path}")
    else:
        print(json.dumps(output_data, indent=2))

    # Print summary
    print(f"\n{'=' * 60}")
    print(f"SCORING SUMMARY")
    print(f"{'=' * 60}")
    print(f"CTA Type: {args.cta_type}")
    print(f"Keywords: {', '.join(keywords[:5])}{'...' if len(keywords) > 5 else ''}")
    print(f"Min Score: {min_score}")
    print(f"Total Posts: {len(results)}")
    print(f"Eligible: {len(eligible)}")
    print(f"Already Have CTA: {sum(1 for r in results if r['has_existing_cta'])}")
    print()

    if eligible:
        print("TOP 10 ELIGIBLE POSTS:")
        print("-" * 60)
        for i, post in enumerate(eligible[:10], 1):
            print(f"{i}. {post['title'][:40]}... (score: {post['total_score']})")


if __name__ == "__main__":
    main()
