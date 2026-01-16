#!/usr/bin/env python3
"""
Download a skill from GitHub repository.

Usage:
    python download_skill.py <repo-url> <skill-path> --output <output-dir>

Example:
    python download_skill.py https://github.com/anthropics/skills skills/docx --output ./.claude/skills/
    python download_skill.py https://github.com/gked2121/claude-skills social-repurposer --output ./.claude/skills/
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def download_skill(repo_url: str, skill_path: str, output_dir: str) -> Path:
    """
    Download a skill folder from a GitHub repository.

    Args:
        repo_url: GitHub repository URL
        skill_path: Path to skill within repository (e.g., "skills/docx" or "social-repurposer")
        output_dir: Local directory to save the skill

    Returns:
        Path to the downloaded skill directory
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Extract skill name from path
    skill_name = Path(skill_path).name

    # Check if skill already exists
    target_dir = output_path / skill_name
    if target_dir.exists():
        print(f"⚠️  Skill '{skill_name}' already exists at {target_dir}")
        return target_dir

    # Create temp directory
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Clone repository with depth 1 for speed
        print(f"📥 Cloning {repo_url}...")
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse", repo_url, "repo"],
                cwd=temp_path,
                capture_output=True,
                text=True,
                check=True
            )
        except subprocess.CalledProcessError as e:
            # Fallback to full clone if sparse checkout fails
            print("   Sparse checkout not supported, using full clone...")
            subprocess.run(
                ["git", "clone", "--depth", "1", repo_url, "repo"],
                cwd=temp_path,
                capture_output=True,
                text=True,
                check=True
            )

        repo_path = temp_path / "repo"

        # Try sparse checkout for efficiency
        try:
            subprocess.run(
                ["git", "sparse-checkout", "set", skill_path],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True
            )
        except subprocess.CalledProcessError:
            pass  # Sparse checkout optional, continue with full clone

        # Find the skill directory
        skill_source = repo_path / skill_path
        if not skill_source.exists():
            # Try without "skills/" prefix
            skill_source = repo_path / skill_name
            if not skill_source.exists():
                raise FileNotFoundError(f"Skill not found at {skill_path} or {skill_name}")

        # Verify SKILL.md exists
        skill_md = skill_source / "SKILL.md"
        if not skill_md.exists():
            raise FileNotFoundError(f"SKILL.md not found in {skill_source}")

        # Copy skill to output directory
        print(f"📦 Copying skill to {target_dir}...")
        shutil.copytree(skill_source, target_dir)

        # Remove .git if present
        git_dir = target_dir / ".git"
        if git_dir.exists():
            shutil.rmtree(git_dir)

    print(f"✅ Downloaded skill '{skill_name}' to {target_dir}")
    return target_dir


def main():
    parser = argparse.ArgumentParser(
        description="Download a skill from GitHub repository"
    )
    parser.add_argument(
        "repo_url",
        help="GitHub repository URL"
    )
    parser.add_argument(
        "skill_path",
        help="Path to skill within repository (e.g., 'skills/docx')"
    )
    parser.add_argument(
        "--output", "-o",
        default="./.claude/skills/",
        help="Output directory (default: ./.claude/skills/)"
    )

    args = parser.parse_args()

    try:
        download_skill(args.repo_url, args.skill_path, args.output)
    except Exception as e:
        print(f"❌ Error downloading skill: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
