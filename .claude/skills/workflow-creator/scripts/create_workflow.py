#!/usr/bin/env python3
"""
Create a new workflow directory structure with multi-AI tool support.

Usage:
    python create_workflow.py <workflow-name> [--path <output-directory>]

Example:
    python create_workflow.py media-creator --path ./workflows
    python create_workflow.py developer-workflow --path ./workflows

Creates:
    workflows/<workflow-name>/
    ├── README.md
    ├── AGENTS.md
    ├── .claude/
    │   ├── settings.json
    │   └── skills/           # Primary storage
    ├── .codex/
    │   └── skills -> ../.claude/skills
    ├── .cursor/
    │   └── skills -> ../.claude/skills
    ├── .opencode/
    │   └── skill -> ../.claude/skills
    ├── .agents/
    │   └── skills -> ../.claude/skills
    ├── .kilocode/
    │   └── skills -> ../.claude/skills
    ├── .roo/
    │   └── skills -> ../.claude/skills
    ├── .goose/
    │   └── skills -> ../.claude/skills
    ├── .gemini/
    │   └── skills -> ../.claude/skills
    ├── .agent/
    │   └── skills -> ../.claude/skills
    ├── .github/
    │   └── skills -> ../.claude/skills
    ├── skills -> .claude/skills
    ├── .factory/
    │   └── skills -> ../.claude/skills
    └── .windsurf/
        └── skills -> ../.claude/skills
"""

import argparse
import os
import sys
from pathlib import Path


# AI tool symlink configurations
# Format: (directory_name, symlink_name, symlink_target)
AI_TOOL_SYMLINKS = [
    (".codex", "skills", "../.claude/skills"),
    (".cursor", "skills", "../.claude/skills"),
    (".opencode", "skill", "../.claude/skills"),  # Note: singular "skill"
    (".agents", "skills", "../.claude/skills"),   # Amp
    (".kilocode", "skills", "../.claude/skills"),
    (".roo", "skills", "../.claude/skills"),
    (".goose", "skills", "../.claude/skills"),
    (".gemini", "skills", "../.claude/skills"),
    (".agent", "skills", "../.claude/skills"),    # Antigravity
    (".github", "skills", "../.claude/skills"),   # GitHub Copilot
    (".factory", "skills", "../.claude/skills"),  # Droid
    (".windsurf", "skills", "../.claude/skills"),
]

# Root-level symlink for Clawdbot (skills/ -> .claude/skills)
ROOT_SYMLINK = ("skills", ".claude/skills")


def create_workflow(name: str, output_path: str = "workflows") -> Path:
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
    for dir_name, link_name, target in AI_TOOL_SYMLINKS:
        tool_dir = workflow_dir / dir_name
        tool_dir.mkdir(exist_ok=True)
        link_path = tool_dir / link_name
        if not link_path.exists():
            link_path.symlink_to(target)

    # Create root-level symlink for Clawdbot
    root_link = workflow_dir / ROOT_SYMLINK[0]
    if not root_link.exists():
        root_link.symlink_to(ROOT_SYMLINK[1])

    # Create placeholder files
    (workflow_dir / "README.md").touch()
    (workflow_dir / "AGENTS.md").touch()
    (workflow_dir / ".claude" / "settings.json").write_text('{\n  "permissions": {}\n}\n')

    print(f"✅ Created workflow directory: {workflow_dir}")
    print(f"   ├── README.md")
    print(f"   ├── AGENTS.md")
    print(f"   ├── .claude/")
    print(f"   │   ├── settings.json")
    print(f"   │   └── skills/           (primary storage)")
    print(f"   ├── .codex/skills -> ../.claude/skills")
    print(f"   ├── .cursor/skills -> ../.claude/skills")
    print(f"   ├── .opencode/skill -> ../.claude/skills")
    print(f"   ├── .agents/skills -> ../.claude/skills")
    print(f"   ├── .kilocode/skills -> ../.claude/skills")
    print(f"   ├── .roo/skills -> ../.claude/skills")
    print(f"   ├── .goose/skills -> ../.claude/skills")
    print(f"   ├── .gemini/skills -> ../.claude/skills")
    print(f"   ├── .agent/skills -> ../.claude/skills")
    print(f"   ├── .github/skills -> ../.claude/skills")
    print(f"   ├── skills -> .claude/skills")
    print(f"   ├── .factory/skills -> ../.claude/skills")
    print(f"   └── .windsurf/skills -> ../.claude/skills")

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
        default="workflows",
        help="Output directory (default: workflows)"
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
