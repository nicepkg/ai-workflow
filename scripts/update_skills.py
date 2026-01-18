#!/usr/bin/env python3
"""
Update skills from skill-source.json configuration.

Supports:
- Update single skill in a workflow
- Update all skills in a workflow
- Update all skills in all workflows

Usage:
    python scripts/update_skills.py --workflow content-creator --skill canvas-design
    python scripts/update_skills.py --workflow content-creator --all
    python scripts/update_skills.py --all-workflows

Examples:
    # Update single skill
    python scripts/update_skills.py -w content-creator -s canvas-design

    # Update all skills in a workflow
    python scripts/update_skills.py -w content-creator --all

    # Update all workflows
    python scripts/update_skills.py --all-workflows

    # Dry run (show what would be updated)
    python scripts/update_skills.py -w content-creator --all --dry-run
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

# Import existing downloaders
from download_from_github import download_skill as download_github, parse_github_url
from download_from_archive import download_from_archive


def get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent


def get_workflows_root() -> Path:
    """Get the workflows root directory."""
    root = get_project_root()
    workflows_root = root / "workflows"
    return workflows_root if workflows_root.exists() else root


def get_workflows() -> list[Path]:
    """Get all workflow directories."""
    root = get_workflows_root()
    workflows = []
    for item in root.iterdir():
        if item.is_dir() and item.name.endswith('-workflow'):
            skill_source = item / '.claude' / 'skill-source.json'
            if skill_source.exists():
                workflows.append(item)
    return sorted(workflows)


def load_skill_source(workflow_path: Path) -> dict[str, Any]:
    """Load skill-source.json from workflow."""
    skill_source_path = workflow_path / '.claude' / 'skill-source.json'
    if not skill_source_path.exists():
        raise FileNotFoundError(f"skill-source.json not found in {workflow_path}")

    with open(skill_source_path) as f:
        return json.load(f)


def update_skill(
    skill_config: dict[str, Any],
    output_dir: Path,
    force: bool = True,
    dry_run: bool = False
) -> bool:
    """
    Update a single skill based on its configuration.

    Args:
        skill_config: Skill configuration from skill-source.json
        output_dir: Directory to install skill (.claude/skills/)
        force: Overwrite existing
        dry_run: Just print what would happen

    Returns:
        True if successful, False otherwise
    """
    name = skill_config.get('name')
    source_type = skill_config.get('type', 'github')

    if dry_run:
        print(f"  [DRY RUN] Would update: {name} ({source_type})")
        return True

    print(f"  Updating: {name}...")

    try:
        if source_type == 'github':
            repo = skill_config.get('repo')
            path = skill_config.get('path', name)

            if not repo:
                print(f"    ❌ Missing 'repo' for GitHub skill: {name}")
                return False

            # Parse and download
            repo_url, _ = parse_github_url(repo)
            download_github(repo_url, path, str(output_dir), force)

        elif source_type == 'archive':
            url = skill_config.get('url')

            if not url:
                print(f"    ❌ Missing 'url' for archive skill: {name}")
                return False

            download_from_archive(url, str(output_dir), force, name)

        else:
            print(f"    ❌ Unknown source type: {source_type}")
            return False

        return True

    except Exception as e:
        print(f"    ❌ Failed to update {name}: {e}")
        return False


def update_workflow(
    workflow_path: Path,
    skill_name: str | None = None,
    force: bool = True,
    dry_run: bool = False
) -> tuple[int, int]:
    """
    Update skills in a workflow.

    Args:
        workflow_path: Path to workflow directory
        skill_name: Specific skill to update (None = all)
        force: Overwrite existing
        dry_run: Just print what would happen

    Returns:
        Tuple of (success_count, fail_count)
    """
    workflow_name = workflow_path.name
    print(f"\n📦 Workflow: {workflow_name}")

    config = load_skill_source(workflow_path)
    skills = config.get('skills', [])
    output_dir = workflow_path / '.claude' / 'skills'

    success = 0
    failed = 0

    for skill in skills:
        name = skill.get('name')

        # Filter by skill name if specified
        if skill_name and name != skill_name:
            continue

        if update_skill(skill, output_dir, force, dry_run):
            success += 1
        else:
            failed += 1

    if skill_name and success == 0 and failed == 0:
        print(f"  ⚠️  Skill '{skill_name}' not found in {workflow_name}")

    return success, failed


def main():
    parser = argparse.ArgumentParser(
        description="Update skills from skill-source.json configuration"
    )

    # Workflow selection
    parser.add_argument(
        '--workflow', '-w',
        help="Workflow name (e.g., 'content-creator' or 'content-creator-workflow')"
    )
    parser.add_argument(
        '--all-workflows',
        action='store_true',
        help="Update all workflows"
    )

    # Skill selection
    parser.add_argument(
        '--skill', '-s',
        help="Specific skill to update"
    )
    parser.add_argument(
        '--all', '-a',
        action='store_true',
        dest='all_skills',
        help="Update all skills in workflow"
    )

    # Options
    parser.add_argument(
        '--force', '-f',
        action='store_true',
        default=True,
        help="Force overwrite (default: True)"
    )
    parser.add_argument(
        '--no-force',
        action='store_false',
        dest='force',
        help="Don't overwrite existing skills"
    )
    parser.add_argument(
        '--dry-run', '-n',
        action='store_true',
        help="Show what would be updated without making changes"
    )
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help="List available workflows and skills"
    )

    args = parser.parse_args()

    root = get_workflows_root()

    # List mode
    if args.list:
        print("\n📋 Available Workflows:\n")
        for workflow_path in get_workflows():
            workflow_name = workflow_path.name.replace('-workflow', '')
            config = load_skill_source(workflow_path)
            skills = config.get('skills', [])
            print(f"  {workflow_name} ({len(skills)} skills)")
            for skill in skills:
                stype = skill.get('type', 'github')
                print(f"    - {skill.get('name')} [{stype}]")
            print()
        return

    # Validate arguments
    if not args.workflow and not args.all_workflows:
        parser.error("Specify --workflow or --all-workflows")

    if args.workflow and not args.skill and not args.all_skills:
        parser.error("Specify --skill or --all for the workflow")

    total_success = 0
    total_failed = 0

    # Determine which workflows to update
    if args.all_workflows:
        workflows = get_workflows()
    else:
        # Normalize workflow name
        workflow_name = args.workflow
        if not workflow_name.endswith('-workflow'):
            workflow_name = f"{workflow_name}-workflow"

        workflow_path = root / workflow_name
        if not workflow_path.exists():
            print(f"❌ Workflow not found: {workflow_name}")
            print(f"   Available: {', '.join(w.name for w in get_workflows())}")
            sys.exit(1)

        workflows = [workflow_path]

    # Update workflows
    for workflow_path in workflows:
        skill_name = args.skill if not args.all_skills else None
        success, failed = update_workflow(
            workflow_path,
            skill_name=skill_name,
            force=args.force,
            dry_run=args.dry_run
        )
        total_success += success
        total_failed += failed

    # Summary
    print(f"\n{'=' * 40}")
    if args.dry_run:
        print(f"[DRY RUN] Would update: {total_success} skills")
    else:
        print(f"✅ Updated: {total_success} skills")
        if total_failed:
            print(f"❌ Failed: {total_failed} skills")

    sys.exit(1 if total_failed else 0)


if __name__ == "__main__":
    main()
