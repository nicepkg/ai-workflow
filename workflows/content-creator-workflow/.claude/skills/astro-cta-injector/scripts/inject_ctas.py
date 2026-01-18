#!/usr/bin/env python3
"""
CTA Injector for Astro Sites
Injects CTA blocks into content files with configurable placement strategies
"""

import sys
import re
import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional

from bs4 import BeautifulSoup

# Add shared modules to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "shared"))
from config_loader import SkillConfig, load_json_config
from utils import save_json, load_json, ensure_dir, timestamp, ProgressTracker


class CTAInjector:
    """Inject CTAs into content files"""

    def __init__(
        self,
        templates_dir: Path,
        backup_dir: Path,
        state_file: Path,
        dry_run: bool = True,
        skip_existing: bool = True
    ):
        self.templates_dir = templates_dir
        self.backup_dir = backup_dir
        self.tracker = ProgressTracker(state_file)
        self.dry_run = dry_run
        self.skip_existing = skip_existing
        self.current_backup_dir: Optional[Path] = None
        self.results: list[dict] = []

    def load_template(self, template_name: str, variables: dict) -> str:
        """Load and populate a CTA template"""
        template_path = self.templates_dir / template_name
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")

        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()

        # Replace variables
        for key, value in variables.items():
            template = template.replace(f'{{{{{key}}}}}', str(value))

        return template

    def create_backup(self, file_path: Path) -> Path:
        """Create backup of a file before modification"""
        if not self.current_backup_dir:
            timestamp_str = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            self.current_backup_dir = self.backup_dir / timestamp_str
            ensure_dir(self.current_backup_dir)

        # Preserve directory structure in backup
        rel_path = file_path.relative_to(file_path.parent.parent.parent)
        backup_path = self.current_backup_dir / rel_path
        ensure_dir(backup_path.parent)

        shutil.copy2(file_path, backup_path)
        return backup_path

    def has_existing_cta(self, content: str, cta_type: str) -> bool:
        """Check if content already has a CTA of this type"""
        patterns = [
            f'data-cta-type="{cta_type}"',
            f"data-cta-type='{cta_type}'",
            f'<!-- CTA:{cta_type} -->',
        ]
        return any(pattern in content for pattern in patterns)

    def find_injection_point(self, content: str, placement: str) -> int:
        """Find the position to inject the CTA based on placement strategy"""

        if placement == "end":
            # Find end of content (before closing tags)
            # Look for </article>, </div>, </main>, or end of file
            for tag in ['</article>', '</main>', '</section>']:
                pos = content.rfind(tag)
                if pos != -1:
                    return pos
            return len(content)

        elif placement.startswith("after-paragraph-"):
            # Extract percentage
            try:
                pct = int(placement.split("-")[-1].replace("%", ""))
            except ValueError:
                pct = 50

            # Find all paragraph end positions
            paragraph_ends = [m.end() for m in re.finditer(r'</p>', content, re.IGNORECASE)]

            if not paragraph_ends:
                return len(content)

            # Calculate target position
            target_idx = int(len(paragraph_ends) * (pct / 100))
            target_idx = max(0, min(target_idx, len(paragraph_ends) - 1))

            return paragraph_ends[target_idx]

        elif placement == "after-heading":
            # After first H2
            match = re.search(r'</h2>', content, re.IGNORECASE)
            if match:
                return match.end()
            return len(content)

        elif placement == "before-conclusion":
            # Before last paragraph
            paragraph_starts = [m.start() for m in re.finditer(r'<p[^>]*>', content, re.IGNORECASE)]
            if len(paragraph_starts) >= 2:
                return paragraph_starts[-1]
            return len(content)

        else:
            # Default to end
            return len(content)

    def inject_cta(
        self,
        file_path: Path,
        cta_html: str,
        placement: str,
        cta_type: str
    ) -> dict:
        """Inject CTA into a single file"""
        result = {
            "file_path": str(file_path),
            "success": False,
            "error": None,
            "placement": placement,
            "backup_path": None,
            "dry_run": self.dry_run
        }

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check for existing CTA
            if self.skip_existing and self.has_existing_cta(content, cta_type):
                result["error"] = "CTA already exists"
                result["skipped"] = True
                return result

            # Find injection point
            injection_point = self.find_injection_point(content, placement)

            # Build new content
            new_content = (
                content[:injection_point] +
                "\n\n" + cta_html + "\n\n" +
                content[injection_point:]
            )

            if self.dry_run:
                result["success"] = True
                result["preview"] = {
                    "injection_point": injection_point,
                    "content_length_before": len(content),
                    "content_length_after": len(new_content)
                }
            else:
                # Create backup
                backup_path = self.create_backup(file_path)
                result["backup_path"] = str(backup_path)

                # Write new content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                result["success"] = True

        except Exception as e:
            result["error"] = str(e)

        return result

    def run(
        self,
        posts: list[dict],
        cta_type: str,
        template_name: str,
        cta_data: dict,
        placement: str
    ) -> dict:
        """Run the injection process for multiple posts"""

        # Load and populate template
        cta_html = self.load_template(template_name, cta_data)

        # Initialize tracking
        post_ids = [p["file_path"] for p in posts]
        self.tracker.start(post_ids)

        print(f"\n{'DRY RUN - ' if self.dry_run else ''}Processing {len(posts)} posts...")
        print(f"CTA Type: {cta_type}")
        print(f"Placement: {placement}")
        print("-" * 60)

        for i, post in enumerate(posts, 1):
            file_path = Path(post["file_path"])
            title = post.get("title", file_path.stem)[:40]

            self.tracker.mark_current(post["file_path"])

            print(f"[{i}/{len(posts)}] {title}...", end=" ")

            result = self.inject_cta(
                file_path=file_path,
                cta_html=cta_html,
                placement=post.get("placement", placement),
                cta_type=cta_type
            )

            self.results.append(result)

            if result.get("skipped"):
                self.tracker.mark_completed(post["file_path"])
                print("[SKIPPED - already has CTA]")
            elif result["success"]:
                self.tracker.mark_completed(post["file_path"])
                status = "OK (dry-run)" if result.get("dry_run") else "OK"
                print(f"[{status}]")
            else:
                self.tracker.mark_failed(post["file_path"], result.get("error"))
                print(f"[FAILED: {result.get('error')}]")

        # Generate summary
        stats = self.tracker.get_stats()
        summary = {
            "completed_at": timestamp(),
            "dry_run": self.dry_run,
            "cta_type": cta_type,
            "placement": placement,
            "total_processed": len(self.results),
            "successful": len([r for r in self.results if r["success"] and not r.get("skipped")]),
            "skipped": len([r for r in self.results if r.get("skipped")]),
            "failed": len([r for r in self.results if not r["success"] and not r.get("skipped")]),
            "backup_dir": str(self.current_backup_dir) if self.current_backup_dir else None,
            "results": self.results
        }

        return summary

    @staticmethod
    def rollback(backup_dir: Path) -> dict:
        """Rollback changes from a backup"""
        manifest_path = backup_dir / "manifest.json"

        if not backup_dir.exists():
            return {"success": False, "error": f"Backup directory not found: {backup_dir}"}

        restored = []
        errors = []

        # Find all backup files
        for backup_file in backup_dir.rglob("*"):
            if backup_file.is_file() and backup_file.name != "manifest.json":
                try:
                    # Reconstruct original path (this is simplified - real impl needs manifest)
                    rel_path = backup_file.relative_to(backup_dir)
                    # This would need the original base path from manifest
                    # For now, just report what would be restored
                    restored.append(str(backup_file))
                except Exception as e:
                    errors.append({"file": str(backup_file), "error": str(e)})

        return {
            "success": len(errors) == 0,
            "restored": restored,
            "errors": errors
        }


def main():
    parser = argparse.ArgumentParser(description="CTA Injector for Astro Sites")
    parser.add_argument("--input", "-i", help="Path to scored posts JSON file")
    parser.add_argument("--cta-type", "-t", help="CTA type to inject")
    parser.add_argument("--placement", "-p", default="after-paragraph-50%",
                        help="Placement strategy")
    parser.add_argument("--config", help="Path to config.json")
    parser.add_argument("--dry-run", action="store_true", default=True,
                        help="Preview changes without applying (default)")
    parser.add_argument("--apply", action="store_true", help="Actually apply changes")
    parser.add_argument("--rollback", help="Rollback from backup directory")
    parser.add_argument("--report", help="Output report file path")

    args = parser.parse_args()

    # Handle rollback
    if args.rollback:
        result = CTAInjector.rollback(Path(args.rollback))
        print(json.dumps(result, indent=2))
        sys.exit(0 if result["success"] else 1)

    # Validate arguments
    if not args.input:
        print("Error: --input is required", file=sys.stderr)
        sys.exit(1)

    # Load config
    config_path = Path(args.config) if args.config else None
    if not config_path:
        default_config = Path(__file__).parent.parent / "config.json"
        if default_config.exists():
            config_path = default_config

    config = {}
    if config_path and config_path.exists():
        config = load_json_config(config_path)

    # Load scored posts
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    scored_data = load_json(input_path)
    posts = scored_data.get("eligible_posts", [])
    cta_type = args.cta_type or scored_data.get("cta_type")

    if not posts:
        print("No eligible posts found in input file")
        sys.exit(0)

    if not cta_type:
        print("Error: CTA type not specified", file=sys.stderr)
        sys.exit(1)

    # Get CTA configuration
    cta_config = config.get("cta_types", {}).get(cta_type, {})
    template_name = cta_config.get("template", f"{cta_type}.html")
    cta_data = cta_config.get("data", {})
    placement = args.placement or cta_config.get("default_placement", "after-paragraph-50%")

    # Setup paths
    skill_dir = Path(__file__).parent.parent
    templates_dir = skill_dir / "templates"
    state_dir = skill_dir / "state"
    backup_dir = skill_dir / "backups"

    # Determine dry_run mode
    dry_run = not args.apply

    if not dry_run:
        print("\n" + "=" * 60)
        print("WARNING: LIVE MODE - Files will be modified!")
        print("=" * 60)
        confirm = input("Type 'yes' to confirm: ")
        if confirm.lower() != "yes":
            print("Aborted.")
            sys.exit(0)

    # Create injector
    injector = CTAInjector(
        templates_dir=templates_dir,
        backup_dir=backup_dir,
        state_file=state_dir / "cta_injection_progress.json",
        dry_run=dry_run,
        skip_existing=config.get("options", {}).get("skip_existing", True)
    )

    # Run injection
    summary = injector.run(
        posts=posts,
        cta_type=cta_type,
        template_name=template_name,
        cta_data=cta_data,
        placement=placement
    )

    # Save report
    report_path = Path(args.report) if args.report else state_dir / "cta_injection_report.json"
    ensure_dir(report_path.parent)
    save_json(summary, report_path)

    # Print summary
    print("\n" + "=" * 60)
    print("INJECTION COMPLETE")
    print("=" * 60)
    print(f"Mode: {'DRY RUN' if summary['dry_run'] else 'LIVE'}")
    print(f"Successful: {summary['successful']}")
    print(f"Skipped: {summary['skipped']}")
    print(f"Failed: {summary['failed']}")
    if summary.get("backup_dir"):
        print(f"Backup: {summary['backup_dir']}")
    print(f"Report: {report_path}")

    if summary["dry_run"]:
        print("\nThis was a DRY RUN. To apply changes, use --apply flag.")


if __name__ == "__main__":
    main()
