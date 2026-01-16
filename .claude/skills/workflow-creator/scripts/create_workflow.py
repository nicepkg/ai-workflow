#!/usr/bin/env python3
"""
Create a new workflow directory structure with multi-AI tool support.

Usage:
    python create_workflow.py <workflow-name> [--path <output-directory>]

Example:
    python create_workflow.py media-creator --path ./
    python create_workflow.py developer-workflow

Creates:
    workflow-name/
    ├── README.md
    ├── AGENTS.md
    ├── .claude/
    │   ├── settings.json
    │   └── skills/
    ├── .codex/
    │   └── skills -> ../.claude/skills
    ├── .cursor/
    │   └── skills -> ../.claude/skills
    └── .opencode/
        └── skill -> ../.claude/skills
"""

import argparse
import os
import sys
from pathlib import Path


def create_workflow(name: str, output_path: str = ".") -> Path:
    """
    Create a new workflow directory with standard structure.
    Supports multiple AI tools via symlinks.

    Args:
        name: Workflow name (e.g., "media-creator", "developer-workflow")
        output_path: Parent directory for the workflow

    Returns:
        Path to the created workflow directory
    """
    # Normalize name
    workflow_name = name.lower().replace(" ", "-")
    if not workflow_name.endswith("-workflow"):
        workflow_name = f"{workflow_name}-workflow"

    # Create workflow directory
    workflow_dir = Path(output_path) / workflow_name

    if workflow_dir.exists():
        print(f"⚠️  Warning: {workflow_dir} already exists")
        return workflow_dir

    # Create main directory structure
    workflow_dir.mkdir(parents=True, exist_ok=True)
    (workflow_dir / ".claude").mkdir(exist_ok=True)
    (workflow_dir / ".claude" / "skills").mkdir(exist_ok=True)

    # Create multi-AI tool directories with symlinks
    # .codex/skills -> ../.claude/skills
    (workflow_dir / ".codex").mkdir(exist_ok=True)
    codex_skills = workflow_dir / ".codex" / "skills"
    if not codex_skills.exists():
        codex_skills.symlink_to("../.claude/skills")

    # .cursor/skills -> ../.claude/skills
    (workflow_dir / ".cursor").mkdir(exist_ok=True)
    cursor_skills = workflow_dir / ".cursor" / "skills"
    if not cursor_skills.exists():
        cursor_skills.symlink_to("../.claude/skills")

    # .opencode/skill -> ../.claude/skills (note: singular "skill")
    (workflow_dir / ".opencode").mkdir(exist_ok=True)
    opencode_skill = workflow_dir / ".opencode" / "skill"
    if not opencode_skill.exists():
        opencode_skill.symlink_to("../.claude/skills")

    # Create placeholder files
    (workflow_dir / "README.md").touch()
    (workflow_dir / "AGENTS.md").touch()
    (workflow_dir / ".claude" / "settings.json").write_text('{\n  "permissions": {}\n}\n')

    print(f"✅ Created workflow directory: {workflow_dir}")
    print(f"   ├── README.md")
    print(f"   ├── AGENTS.md")
    print(f"   ├── .claude/")
    print(f"   │   ├── settings.json")
    print(f"   │   └── skills/")
    print(f"   ├── .codex/")
    print(f"   │   └── skills -> ../.claude/skills")
    print(f"   ├── .cursor/")
    print(f"   │   └── skills -> ../.claude/skills")
    print(f"   └── .opencode/")
    print(f"       └── skill -> ../.claude/skills")

    return workflow_dir


def main():
    parser = argparse.ArgumentParser(
        description="Create a new workflow directory structure"
    )
    parser.add_argument(
        "name",
        help="Workflow name (e.g., 'media-creator', 'developer')"
    )
    parser.add_argument(
        "--path",
        default=".",
        help="Output directory (default: current directory)"
    )

    args = parser.parse_args()

    try:
        workflow_dir = create_workflow(args.name, args.path)
        print(f"\n✅ Workflow '{args.name}' created successfully at {workflow_dir}")
        print("\nNext steps:")
        print("1. Download skills to .claude/skills/")
        print("2. Edit README.md with user documentation")
        print("3. Edit AGENTS.md with AI instructions")
    except Exception as e:
        print(f"❌ Error creating workflow: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
