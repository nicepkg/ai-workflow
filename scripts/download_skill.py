#!/usr/bin/env python3
"""
Unified skill downloader - auto-detects source type.

Supports:
- GitHub repositories (full URL or tree URL)
- Compressed archives (.zip, .tar.gz, .tgz, .skill)
- Direct URLs to archives
- Local archive files

Usage:
    python download_skill.py <source> [skill-path] --output <output-dir>

Examples:
    # GitHub (auto-detect)
    python download_skill.py https://github.com/anthropics/skills skills/docx --output ./.claude/skills/
    python download_skill.py https://github.com/anthropics/skills/tree/main/skills/docx --output ./.claude/skills/

    # Archive (auto-detect)
    python download_skill.py https://example.com/my-skill.zip --output ./.claude/skills/
    python download_skill.py ./downloads/my-skill.tar.gz --output ./.claude/skills/
"""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

# Import the specialized downloaders
from download_from_github import download_skill as download_github, parse_github_url
from download_from_archive import download_from_archive, is_url, get_archive_type


def detect_source_type(source: str) -> str:
    """
    Detect the type of source.

    Returns:
        'github', 'archive', 'local_archive', or 'unknown'
    """
    # Check for GitHub URL
    if 'github.com' in source.lower():
        return 'github'

    # Check for archive URL
    if is_url(source):
        path = urlparse(source).path.lower()
        if any(path.endswith(ext) for ext in ['.zip', '.tar.gz', '.tgz', '.tar', '.skill']):
            return 'archive'
        # Might still be an archive with no extension
        return 'archive'

    # Check for local file
    source_path = Path(source)
    if source_path.exists():
        if source_path.is_file():
            return 'local_archive'
        elif source_path.is_dir():
            return 'local_dir'

    return 'unknown'


def download_skill(
    source: str,
    skill_path: str | None = None,
    output_dir: str = "./.claude/skills/",
    force: bool = False
) -> Path:
    """
    Download skill from any supported source.

    Args:
        source: GitHub URL, archive URL, or local path
        skill_path: Path within repo (for GitHub sources)
        output_dir: Directory to install skill
        force: Overwrite if exists

    Returns:
        Path to installed skill directory
    """
    source_type = detect_source_type(source)

    if source_type == 'github':
        # Parse GitHub URL
        repo_url, url_path = parse_github_url(source)

        # Determine skill path
        if url_path:
            # URL contains path (e.g., .../tree/main/skills/docx)
            final_path = url_path
        elif skill_path:
            final_path = skill_path
        else:
            raise ValueError(
                "For GitHub repositories, provide either:\n"
                "1. Full tree URL: https://github.com/user/repo/tree/main/path/to/skill\n"
                "2. Skill path argument: download_skill.py <repo-url> <skill-path>"
            )

        return download_github(repo_url, final_path, output_dir, force)

    elif source_type in ('archive', 'local_archive'):
        return download_from_archive(source, output_dir, force)

    elif source_type == 'local_dir':
        # Copy local directory
        import shutil

        source_path = Path(source)
        skill_md = source_path / "SKILL.md"

        if not skill_md.exists():
            raise FileNotFoundError(f"SKILL.md not found in {source_path}")

        # Read skill name
        content = skill_md.read_text()
        name = None
        if content.startswith('---'):
            for line in content.split('---')[1].split('\n'):
                if line.strip().startswith('name:'):
                    name = line.split(':', 1)[1].strip().strip('"\'')
                    break

        if not name:
            name = source_path.name

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        target_dir = output_path / name

        if target_dir.exists():
            if force:
                shutil.rmtree(target_dir)
            else:
                print(f"⚠️  Skill '{name}' already exists at {target_dir}")
                return target_dir

        shutil.copytree(source_path, target_dir)
        print(f"✅ Copied skill '{name}' to {target_dir}")
        return target_dir

    else:
        raise ValueError(
            f"Unable to determine source type for: {source}\n"
            "Supported: GitHub URLs, archive URLs/files (.zip, .tar.gz, .skill)"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Download skill from GitHub, archive, or URL (auto-detect)"
    )
    parser.add_argument(
        "source",
        help="GitHub URL, archive URL, or local path"
    )
    parser.add_argument(
        "skill_path",
        nargs="?",
        default=None,
        help="Path to skill within repository (for GitHub sources)"
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
        download_skill(args.source, args.skill_path, args.output, args.force)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
