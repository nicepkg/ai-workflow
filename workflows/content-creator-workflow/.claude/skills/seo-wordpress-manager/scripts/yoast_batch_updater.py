#!/usr/bin/env python3
"""
Yoast SEO Batch Updater
Applies SEO changes to WordPress posts via GraphQL with progress tracking
"""

import sys
import json
import time
import argparse
from pathlib import Path
from typing import Optional
from datetime import datetime

# Add shared modules to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "shared"))
from config_loader import SkillConfig
from utils import ProgressTracker, save_json, load_json, ensure_dir, timestamp

from wp_graphql_client import WPGraphQLClient, load_credentials_from_config


class YoastBatchUpdater:
    """Batch update Yoast SEO fields with progress tracking"""

    def __init__(
        self,
        client: WPGraphQLClient,
        state_file: Path,
        backup_file: Path,
        batch_size: int = 10,
        delay_seconds: float = 1.0,
        dry_run: bool = True
    ):
        self.client = client
        self.tracker = ProgressTracker(state_file)
        self.backup_file = backup_file
        self.batch_size = batch_size
        self.delay_seconds = delay_seconds
        self.dry_run = dry_run
        self.backup_data: list[dict] = []
        self.results: list[dict] = []

    def load_changes(self, changes_file: Path) -> list[dict]:
        """Load changes from JSON file"""
        data = load_json(changes_file)
        return data.get("updates", [])

    def backup_current_values(self, updates: list[dict]) -> None:
        """Backup current SEO values before making changes"""
        self.backup_data = [
            {
                "post_id": u["post_id"],
                "post_title": u.get("post_title", ""),
                "original_values": u.get("current", {}),
                "backup_timestamp": timestamp()
            }
            for u in updates
        ]
        ensure_dir(self.backup_file.parent)
        save_json({"backups": self.backup_data, "created_at": timestamp()}, self.backup_file)
        print(f"Backup saved to: {self.backup_file}")

    def apply_update(self, update: dict) -> dict:
        """Apply a single update and return result"""
        post_id = update["post_id"]
        new_values = update.get("new", {})

        result = {
            "post_id": post_id,
            "post_title": update.get("post_title", ""),
            "success": False,
            "error": None,
            "changes_applied": {},
            "timestamp": timestamp()
        }

        if self.dry_run:
            result["success"] = True
            result["dry_run"] = True
            result["changes_applied"] = new_values
            return result

        try:
            # Apply the update via GraphQL
            response = self.client.update_post_seo(
                post_id=post_id,
                title=new_values.get("seo_title"),
                meta_desc=new_values.get("meta_desc"),
                focus_keyphrase=new_values.get("focus_keyphrase")
            )

            update_result = response.get("updatePostSeo", {})
            if update_result.get("success"):
                result["success"] = True
                result["changes_applied"] = new_values
            else:
                result["error"] = "Update returned success=false"

        except Exception as e:
            result["error"] = str(e)

        return result

    def run(self, changes_file: Path, resume: bool = False) -> dict:
        """Run the batch update process"""
        updates = self.load_changes(changes_file)

        if not updates:
            return {"error": "No updates found in changes file"}

        # Determine which updates to process
        if resume and not self.tracker.is_complete():
            remaining_ids = set(self.tracker.get_remaining())
            updates_to_process = [u for u in updates if str(u["post_id"]) in remaining_ids]
            print(f"Resuming: {len(updates_to_process)} posts remaining")
        else:
            updates_to_process = updates
            # Start fresh tracking
            self.tracker.start([str(u["post_id"]) for u in updates])
            # Backup current values
            self.backup_current_values(updates)

        print(f"\n{'DRY RUN - ' if self.dry_run else ''}Processing {len(updates_to_process)} updates...")
        print(f"Batch size: {self.batch_size}, Delay: {self.delay_seconds}s")
        print("-" * 60)

        # Process updates
        for i, update in enumerate(updates_to_process, 1):
            post_id = str(update["post_id"])
            post_title = update.get("post_title", "Unknown")[:40]

            self.tracker.mark_current(post_id)

            print(f"[{i}/{len(updates_to_process)}] Processing: {post_title} (ID: {post_id})...", end=" ")

            result = self.apply_update(update)
            self.results.append(result)

            if result["success"]:
                self.tracker.mark_completed(post_id)
                status = "OK (dry-run)" if result.get("dry_run") else "OK"
                print(f"[{status}]")
            else:
                self.tracker.mark_failed(post_id, result.get("error"))
                print(f"[FAILED: {result.get('error', 'Unknown error')}]")

            # Rate limiting
            if i < len(updates_to_process):
                time.sleep(self.delay_seconds)

        # Generate summary
        stats = self.tracker.get_stats()
        summary = {
            "completed_at": timestamp(),
            "dry_run": self.dry_run,
            "total_processed": len(self.results),
            "successful": stats["completed"],
            "failed": stats["failed"],
            "results": self.results
        }

        return summary

    def generate_report(self, summary: dict, output_file: Optional[Path] = None) -> str:
        """Generate a markdown report of the update process"""
        lines = [
            "# SEO Batch Update Report",
            "",
            f"**Completed:** {summary.get('completed_at', 'N/A')}",
            f"**Mode:** {'DRY RUN' if summary.get('dry_run') else 'LIVE'}",
            "",
            "## Summary",
            "",
            f"- Total processed: {summary.get('total_processed', 0)}",
            f"- Successful: {summary.get('successful', 0)}",
            f"- Failed: {summary.get('failed', 0)}",
            "",
        ]

        # Successful updates
        successful = [r for r in summary.get("results", []) if r.get("success")]
        if successful:
            lines.extend([
                "## Successful Updates",
                "",
            ])
            for result in successful[:20]:  # Limit to first 20
                lines.append(f"- **{result['post_title']}** (ID: {result['post_id']})")
                changes = result.get("changes_applied", {})
                if changes.get("seo_title"):
                    lines.append(f"  - Title: {changes['seo_title'][:50]}...")
                if changes.get("meta_desc"):
                    lines.append(f"  - Description: {changes['meta_desc'][:50]}...")

            if len(successful) > 20:
                lines.append(f"\n... and {len(successful) - 20} more")
            lines.append("")

        # Failed updates
        failed = [r for r in summary.get("results", []) if not r.get("success")]
        if failed:
            lines.extend([
                "## Failed Updates",
                "",
            ])
            for result in failed:
                lines.append(f"- **{result['post_title']}** (ID: {result['post_id']})")
                lines.append(f"  - Error: {result.get('error', 'Unknown')}")
            lines.append("")

        report = "\n".join(lines)

        if output_file:
            ensure_dir(output_file.parent)
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(report)

        return report


def main():
    parser = argparse.ArgumentParser(description="Yoast SEO Batch Updater")
    parser.add_argument("--input", "-i", help="Path to changes JSON file")
    parser.add_argument("--resume", action="store_true", help="Resume interrupted batch")
    parser.add_argument("--dry-run", action="store_true", default=True,
                        help="Preview changes without applying (default)")
    parser.add_argument("--apply", action="store_true", help="Actually apply changes")
    parser.add_argument("--config", type=str, help="Path to config.json")
    parser.add_argument("--batch-size", type=int, default=10, help="Batch size")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay between requests (seconds)")
    parser.add_argument("--report", type=str, help="Output report file path")

    args = parser.parse_args()

    # Validate arguments
    if not args.input and not args.resume:
        print("Error: --input is required (unless using --resume)", file=sys.stderr)
        sys.exit(1)

    # Load config
    config_path = Path(args.config) if args.config else None
    if not config_path:
        default_config = Path(__file__).parent.parent / "config.json"
        if default_config.exists():
            config_path = default_config

    skill_config = SkillConfig("seo-wordpress-manager", config_path)

    # Setup paths
    state_dir = Path(__file__).parent.parent / "state"
    state_file = state_dir / "seo_update_progress.json"
    backup_file = state_dir / "seo_backup.json"

    # Determine dry_run mode
    dry_run = not args.apply

    if not dry_run:
        print("\n" + "=" * 60)
        print("WARNING: LIVE MODE - Changes will be applied to WordPress!")
        print("=" * 60)
        confirm = input("Type 'yes' to confirm: ")
        if confirm.lower() != "yes":
            print("Aborted.")
            sys.exit(0)

    try:
        credentials = load_credentials_from_config(config_path)
    except ValueError as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        sys.exit(1)

    client = WPGraphQLClient(credentials)

    updater = YoastBatchUpdater(
        client=client,
        state_file=state_file,
        backup_file=backup_file,
        batch_size=args.batch_size,
        delay_seconds=args.delay,
        dry_run=dry_run
    )

    # Determine input file
    if args.resume:
        # Look for the original input file from state
        if not state_file.exists():
            print("Error: No state file found to resume from", file=sys.stderr)
            sys.exit(1)
        # We need the original changes file to resume
        if not args.input:
            print("Error: --input is required when resuming", file=sys.stderr)
            sys.exit(1)
        changes_file = Path(args.input)
    else:
        changes_file = Path(args.input)

    if not changes_file.exists():
        print(f"Error: Changes file not found: {changes_file}", file=sys.stderr)
        sys.exit(1)

    # Run the batch update
    summary = updater.run(changes_file, resume=args.resume)

    # Generate report
    report_file = Path(args.report) if args.report else state_dir / "seo_update_report.md"
    report = updater.generate_report(summary, report_file)

    print("\n" + "=" * 60)
    print("BATCH UPDATE COMPLETE")
    print("=" * 60)
    print(f"Successful: {summary.get('successful', 0)}")
    print(f"Failed: {summary.get('failed', 0)}")
    print(f"Report saved to: {report_file}")

    if summary.get("dry_run"):
        print("\nThis was a DRY RUN. To apply changes, use --apply flag.")


if __name__ == "__main__":
    main()
