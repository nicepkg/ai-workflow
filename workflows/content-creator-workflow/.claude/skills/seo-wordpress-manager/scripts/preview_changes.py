#!/usr/bin/env python3
"""
Preview SEO changes before applying them
Shows side-by-side comparison of current vs proposed changes
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Optional

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


def truncate(text: str, max_len: int = 60) -> str:
    """Truncate text with ellipsis"""
    if not text:
        return "(empty)"
    if len(text) <= max_len:
        return text
    return text[:max_len - 3] + "..."


def length_indicator(text: str, max_len: int) -> str:
    """Show length with warning if over limit"""
    if not text:
        return "0"
    length = len(text)
    if length > max_len:
        return f"{length} (OVER by {length - max_len})"
    return str(length)


def print_plain_preview(changes: dict) -> None:
    """Print preview without rich formatting"""
    updates = changes.get("updates", [])

    print("=" * 80)
    print("SEO CHANGES PREVIEW")
    print("=" * 80)
    print(f"Total posts to update: {len(updates)}")
    print()

    for i, update in enumerate(updates, 1):
        post_id = update.get("post_id")
        post_title = update.get("post_title", "Unknown")
        current = update.get("current", {})
        new = update.get("new", {})

        print(f"\n{'─' * 80}")
        print(f"[{i}/{len(updates)}] Post ID: {post_id}")
        print(f"Title: {post_title}")
        print()

        # SEO Title
        if new.get("seo_title"):
            print("SEO Title:")
            print(f"  CURRENT: {truncate(current.get('seo_title', ''), 70)}")
            print(f"  NEW:     {truncate(new.get('seo_title', ''), 70)}")
            print(f"  Length:  {length_indicator(current.get('seo_title', ''), 60)} → {length_indicator(new.get('seo_title', ''), 60)}")
            print()

        # Meta Description
        if new.get("meta_desc"):
            print("Meta Description:")
            print(f"  CURRENT: {truncate(current.get('meta_desc', ''), 70)}")
            print(f"  NEW:     {truncate(new.get('meta_desc', ''), 70)}")
            print(f"  Length:  {length_indicator(current.get('meta_desc', ''), 160)} → {length_indicator(new.get('meta_desc', ''), 160)}")
            print()

        # Focus Keyphrase
        if new.get("focus_keyphrase"):
            print("Focus Keyphrase:")
            print(f"  CURRENT: {current.get('focus_keyphrase', '(none)')}")
            print(f"  NEW:     {new.get('focus_keyphrase', '(none)')}")
            print()

    print("=" * 80)
    print(f"SUMMARY: {len(updates)} posts will be updated")
    print("=" * 80)


def print_rich_preview(changes: dict) -> None:
    """Print preview with rich formatting"""
    console = Console()
    updates = changes.get("updates", [])

    console.print(Panel.fit(
        f"[bold]SEO Changes Preview[/bold]\nTotal posts: {len(updates)}",
        border_style="blue"
    ))

    for i, update in enumerate(updates, 1):
        post_id = update.get("post_id")
        post_title = update.get("post_title", "Unknown")
        current = update.get("current", {})
        new = update.get("new", {})

        table = Table(title=f"[{i}/{len(updates)}] {truncate(post_title, 50)} (ID: {post_id})")
        table.add_column("Field", style="cyan")
        table.add_column("Current", style="red")
        table.add_column("New", style="green")
        table.add_column("Length", style="yellow")

        # SEO Title
        if new.get("seo_title"):
            curr_title = current.get("seo_title", "")
            new_title = new.get("seo_title", "")
            table.add_row(
                "SEO Title",
                truncate(curr_title, 40),
                truncate(new_title, 40),
                f"{len(curr_title)} → {len(new_title)}"
            )

        # Meta Description
        if new.get("meta_desc"):
            curr_desc = current.get("meta_desc", "")
            new_desc = new.get("meta_desc", "")
            table.add_row(
                "Meta Desc",
                truncate(curr_desc, 40),
                truncate(new_desc, 40),
                f"{len(curr_desc)} → {len(new_desc)}"
            )

        # Focus Keyphrase
        if new.get("focus_keyphrase"):
            table.add_row(
                "Keyphrase",
                current.get("focus_keyphrase", "(none)"),
                new.get("focus_keyphrase", "(none)"),
                "-"
            )

        console.print(table)
        console.print()

    # Summary
    title_changes = sum(1 for u in updates if u.get("new", {}).get("seo_title"))
    desc_changes = sum(1 for u in updates if u.get("new", {}).get("meta_desc"))
    kw_changes = sum(1 for u in updates if u.get("new", {}).get("focus_keyphrase"))

    summary = Table(title="Summary", show_header=False)
    summary.add_column("Metric", style="cyan")
    summary.add_column("Count", style="yellow")
    summary.add_row("Total posts", str(len(updates)))
    summary.add_row("Title changes", str(title_changes))
    summary.add_row("Description changes", str(desc_changes))
    summary.add_row("Keyphrase changes", str(kw_changes))

    console.print(Panel(summary, border_style="green"))


def validate_changes(changes: dict) -> list[str]:
    """Validate changes and return list of warnings"""
    warnings = []
    updates = changes.get("updates", [])

    for update in updates:
        post_id = update.get("post_id")
        new = update.get("new", {})

        # Check title length
        if new.get("seo_title") and len(new["seo_title"]) > 60:
            warnings.append(f"Post {post_id}: SEO title is {len(new['seo_title'])} chars (max 60)")

        # Check description length
        if new.get("meta_desc"):
            desc_len = len(new["meta_desc"])
            if desc_len > 160:
                warnings.append(f"Post {post_id}: Meta description is {desc_len} chars (max 160)")
            elif desc_len < 120:
                warnings.append(f"Post {post_id}: Meta description is {desc_len} chars (min 120 recommended)")

    return warnings


def main():
    parser = argparse.ArgumentParser(description="Preview SEO changes")
    parser.add_argument("--input", "-i", required=True, help="Path to changes JSON file")
    parser.add_argument("--validate", "-v", action="store_true", help="Show validation warnings")
    parser.add_argument("--plain", action="store_true", help="Use plain text output (no colors)")

    args = parser.parse_args()

    # Load changes
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: File not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        changes = json.load(f)

    # Validate
    if args.validate:
        warnings = validate_changes(changes)
        if warnings:
            print("VALIDATION WARNINGS:")
            print("-" * 40)
            for warning in warnings:
                print(f"  ! {warning}")
            print()

    # Preview
    if args.plain or not RICH_AVAILABLE:
        print_plain_preview(changes)
    else:
        print_rich_preview(changes)


if __name__ == "__main__":
    main()
