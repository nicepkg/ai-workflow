#!/usr/bin/env python3
"""
Download a skill from GitHub repository.

Usage:
    python download_from_github.py <repo-url> <skill-path> --output <output-dir>

Examples:
    python download_from_github.py https://github.com/anthropics/skills skills/docx --output ./.claude/skills/
    python download_from_github.py https://github.com/gked2121/claude-skills social-repurposer --output ./.claude/skills/
"""

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def parse_github_url(url: str) -> tuple[str, str | None]:
    """
    Parse GitHub URL and extract repo URL and optional path.

    Handles:
    - https://github.com/user/repo
    - https://github.com/user/repo/tree/main/path/to/skill
    - github.com/user/repo

    Returns:
        Tuple of (repo_url, skill_path or None)
    """
    # Remove trailing slash
    url = url.rstrip('/')

    # Add https if missing
    if not url.startswith('http'):
        url = 'https://' + url

    # Match GitHub URL with optional path
    pattern = r'https://github\.com/([^/]+)/([^/]+)(?:/tree/[^/]+/(.+))?'
    match = re.match(pattern, url)

    if match:
        user, repo, path = match.groups()
        repo_url = f'https://github.com/{user}/{repo}.git'
        return repo_url, path

    # Simple repo URL
    if 'github.com' in url:
        if not url.endswith('.git'):
            url = url + '.git'
        return url, None

    raise ValueError(f"Invalid GitHub URL: {url}")


def download_skill(repo_url: str, skill_path: str, output_dir: str, force: bool = False) -> Path:
    """
    Download a skill folder from a GitHub repository.

    Args:
        repo_url: GitHub repository URL
        skill_path: Path to skill within repository
        output_dir: Local directory to save the skill
        force: Overwrite if exists

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
        if force:
            print(f"⚠️  Removing existing skill '{skill_name}'...")
            shutil.rmtree(target_dir)
        else:
            print(f"⚠️  Skill '{skill_name}' already exists at {target_dir}")
            print("   Use --force to overwrite")
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
        except subprocess.CalledProcessError:
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
            # Try alternative paths
            alternatives = [
                repo_path / skill_name,
                repo_path / f".claude/skills/{skill_name}",
                repo_path / f"skills/{skill_name}",
            ]
            for alt in alternatives:
                if alt.exists():
                    skill_source = alt
                    break
            else:
                raise FileNotFoundError(
                    f"Skill not found at {skill_path}\n"
                    f"Tried: {skill_path}, {skill_name}, .claude/skills/{skill_name}, skills/{skill_name}"
                )

        # Verify SKILL.md exists
        skill_md = skill_source / "SKILL.md"
        if not skill_md.exists():
            raise FileNotFoundError(f"SKILL.md not found in {skill_source}")

        # Validate SKILL.md has required frontmatter
        validate_skill_md(skill_md)

        # Copy skill to output directory
        print(f"📦 Copying skill to {target_dir}...")
        shutil.copytree(skill_source, target_dir)

        # Remove .git if present
        git_dir = target_dir / ".git"
        if git_dir.exists():
            shutil.rmtree(git_dir)

    print(f"✅ Downloaded skill '{skill_name}' to {target_dir}")
    return target_dir


def validate_skill_md(skill_md_path: Path) -> None:
    """Validate SKILL.md has required YAML frontmatter."""
    content = skill_md_path.read_text()

    if not content.startswith('---'):
        raise ValueError("SKILL.md missing YAML frontmatter (must start with ---)")

    # Extract frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        raise ValueError("SKILL.md has invalid frontmatter format")

    frontmatter = parts[1]

    if 'name:' not in frontmatter:
        raise ValueError("SKILL.md missing required 'name' field")
    if 'description:' not in frontmatter:
        raise ValueError("SKILL.md missing required 'description' field")


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
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Overwrite existing skill"
    )

    args = parser.parse_args()

    try:
        # Parse URL to get clean repo URL
        repo_url, url_path = parse_github_url(args.repo_url)

        # Use path from URL if skill_path not explicitly provided
        skill_path = args.skill_path
        if url_path and args.skill_path == '.':
            skill_path = url_path

        download_skill(repo_url, skill_path, args.output, args.force)
    except Exception as e:
        print(f"❌ Error downloading skill: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
