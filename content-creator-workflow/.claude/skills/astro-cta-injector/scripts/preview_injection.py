#!/usr/bin/env python3
"""
Preview CTA injections before applying
Shows what will be injected and where
"""

import sys
import re
import json
import argparse
from pathlib import Path
from typing import Optional

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.syntax import Syntax
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

# Add shared modules to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "shared"))
from config_loader import load_json_config
from utils import load_json


def get_context_around_position(content: str, position: int, context_chars: int = 100) -> str:
    """Get content context around injection point"""
    start = max(0, position - context_chars)
    end = min(len(content), position + context_chars)

    before = content[start:position]
    after = content[position:end]

    # Clean up for display
    before = before.replace('\n', ' ').strip()
    after = after.replace('\n', ' ').strip()

    return f"...{before[-50:]} [CTA HERE] {after[:50]}..."


def find_injection_point(content: str, placement: str) -> int:
    """Find the position to inject the CTA"""
    if placement == "end":
        for tag in ['</article>', '</main>', '</section>']:
            pos = content.rfind(tag)
            if pos != -1:
                return pos
        return len(content)

    elif placement.startswith("after-paragraph-"):
        try:
            pct = int(placement.split("-")[-1].replace("%", ""))
        except ValueError:
            pct = 50

        paragraph_ends = [m.end() for m in re.finditer(r'</p>', content, re.IGNORECASE)]
        if not paragraph_ends:
            return len(content)

        target_idx = int(len(paragraph_ends) * (pct / 100))
        target_idx = max(0, min(target_idx, len(paragraph_ends) - 1))
        return paragraph_ends[target_idx]

    elif placement == "after-heading":
        match = re.search(r'</h2>', content, re.IGNORECASE)
        if match:
            return match.end()
        return len(content)

    elif placement == "before-conclusion":
        paragraph_starts = [m.start() for m in re.finditer(r'<p[^>]*>', content, re.IGNORECASE)]
        if len(paragraph_starts) >= 2:
            return paragraph_starts[-1]
        return len(content)

    return len(content)


def count_paragraphs(content: str) -> int:
    """Count paragraphs in content"""
    return len(re.findall(r'<p[^>]*>', content, re.IGNORECASE))


def print_plain_preview(posts: list[dict], placement: str, cta_type: str) -> None:
    """Print preview without rich formatting"""
    print("=" * 80)
    print(f"CTA INJECTION PREVIEW")
    print(f"Type: {cta_type} | Placement: {placement}")
    print("=" * 80)
    print(f"Total posts to inject: {len(posts)}")
    print()

    for i, post in enumerate(posts[:20], 1):
        file_path = Path(post["file_path"])
        title = post.get("title", file_path.stem)
        score = post.get("total_score", 0)

        print(f"\n{'-' * 80}")
        print(f"[{i}] {title}")
        print(f"    File: {file_path.name}")
        print(f"    Score: {score}")

        # Try to read file and show context
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            post_placement = post.get("placement", placement)
            injection_point = find_injection_point(content, post_placement)
            total_paragraphs = count_paragraphs(content)

            print(f"    Paragraphs: {total_paragraphs}")
            print(f"    Injection at: character {injection_point}")
            print(f"    Context: {get_context_around_position(content, injection_point)}")

        except Exception as e:
            print(f"    Error reading file: {e}")

    if len(posts) > 20:
        print(f"\n... and {len(posts) - 20} more posts")

    print("\n" + "=" * 80)


def print_rich_preview(posts: list[dict], placement: str, cta_type: str) -> None:
    """Print preview with rich formatting"""
    console = Console()

    console.print(Panel.fit(
        f"[bold]CTA Injection Preview[/bold]\n"
        f"Type: [cyan]{cta_type}[/cyan] | "
        f"Placement: [cyan]{placement}[/cyan]\n"
        f"Total posts: [yellow]{len(posts)}[/yellow]",
        border_style="blue"
    ))

    table = Table(title="Posts to Inject")
    table.add_column("#", style="dim", width=4)
    table.add_column("Title", style="cyan", max_width=30)
    table.add_column("Score", style="yellow", width=6)
    table.add_column("Paragraphs", width=10)
    table.add_column("Injection Point", style="green")

    for i, post in enumerate(posts[:20], 1):
        file_path = Path(post["file_path"])
        title = post.get("title", file_path.stem)[:28]
        score = post.get("total_score", 0)

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            post_placement = post.get("placement", placement)
            injection_point = find_injection_point(content, post_placement)
            total_paragraphs = count_paragraphs(content)

            pct = int((injection_point / len(content)) * 100)
            injection_info = f"char {injection_point} ({pct}%)"

        except Exception as e:
            total_paragraphs = "?"
            injection_info = f"Error: {e}"

        table.add_row(
            str(i),
            title,
            f"{score:.1f}",
            str(total_paragraphs),
            injection_info
        )

    console.print(table)

    if len(posts) > 20:
        console.print(f"\n[dim]... and {len(posts) - 20} more posts[/dim]")

    # Summary
    console.print("\n[bold]Summary:[/bold]")
    console.print(f"  Posts to modify: [yellow]{len(posts)}[/yellow]")
    console.print(f"  Placement strategy: [cyan]{placement}[/cyan]")
    console.print(f"\n[dim]Run with --apply to inject CTAs[/dim]")


def main():
    parser = argparse.ArgumentParser(description="Preview CTA injections")
    parser.add_argument("--input", "-i", required=True, help="Path to scored posts JSON")
    parser.add_argument("--placement", "-p", default="after-paragraph-50%",
                        help="Placement strategy to preview")
    parser.add_argument("--config", help="Path to config.json")
    parser.add_argument("--plain", action="store_true", help="Use plain text output")
    parser.add_argument("--limit", type=int, help="Limit number of posts to preview")

    args = parser.parse_args()

    # Load scored posts
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    scored_data = load_json(input_path)
    posts = scored_data.get("eligible_posts", [])
    cta_type = scored_data.get("cta_type", "unknown")

    if not posts:
        print("No eligible posts found in input file")
        sys.exit(0)

    # Apply limit if specified
    if args.limit:
        posts = posts[:args.limit]

    # Load config for placement default
    if args.config:
        config = load_json_config(Path(args.config))
        cta_config = config.get("cta_types", {}).get(cta_type, {})
        placement = args.placement or cta_config.get("default_placement", "after-paragraph-50%")
    else:
        placement = args.placement

    # Print preview
    if args.plain or not RICH_AVAILABLE:
        print_plain_preview(posts, placement, cta_type)
    else:
        print_rich_preview(posts, placement, cta_type)


if __name__ == "__main__":
    main()
