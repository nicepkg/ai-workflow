#!/usr/bin/env python3
"""
Download and extract a skill from compressed archive.

Supported formats: .zip, .tar.gz, .tgz, .skill (renamed zip)

Usage:
    python download_from_archive.py <url-or-path> --output <output-dir>

Examples:
    python download_from_archive.py https://example.com/my-skill.zip --output ./.claude/skills/
    python download_from_archive.py ./downloads/my-skill.tar.gz --output ./.claude/skills/
    python download_from_archive.py https://skillhub.club/download/skill.skill --output ./.claude/skills/
"""

import argparse
import os
import shutil
import sys
import tarfile
import tempfile
import urllib.request
import zipfile
from pathlib import Path
from urllib.parse import urlparse


def is_url(source: str) -> bool:
    """Check if source is a URL."""
    parsed = urlparse(source)
    return parsed.scheme in ('http', 'https')


def get_archive_type(path: str) -> str:
    """Determine archive type from path/extension."""
    path_lower = path.lower()

    if path_lower.endswith('.zip') or path_lower.endswith('.skill'):
        return 'zip'
    elif path_lower.endswith('.tar.gz') or path_lower.endswith('.tgz'):
        return 'tar.gz'
    elif path_lower.endswith('.tar'):
        return 'tar'
    else:
        # Try to detect by content
        return 'unknown'


def download_file(url: str, target_path: Path) -> None:
    """Download file from URL."""
    print(f"📥 Downloading from {url}...")

    # Create request with User-Agent
    request = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (skill-downloader)'}
    )

    with urllib.request.urlopen(request, timeout=60) as response:
        with open(target_path, 'wb') as f:
            shutil.copyfileobj(response, f)

    print(f"   Downloaded to {target_path}")


def extract_archive(archive_path: Path, extract_dir: Path, archive_type: str) -> Path:
    """
    Extract archive and return path to skill directory.

    Returns:
        Path to the extracted skill directory containing SKILL.md
    """
    print(f"📦 Extracting {archive_type} archive...")

    if archive_type == 'zip':
        with zipfile.ZipFile(archive_path, 'r') as zf:
            zf.extractall(extract_dir)
    elif archive_type in ('tar.gz', 'tar'):
        mode = 'r:gz' if archive_type == 'tar.gz' else 'r'
        with tarfile.open(archive_path, mode) as tf:
            tf.extractall(extract_dir)
    else:
        # Try zip first, then tar
        try:
            with zipfile.ZipFile(archive_path, 'r') as zf:
                zf.extractall(extract_dir)
        except zipfile.BadZipFile:
            try:
                with tarfile.open(archive_path, 'r:*') as tf:
                    tf.extractall(extract_dir)
            except tarfile.TarError:
                raise ValueError("Unable to extract archive. Unsupported format.")

    # Find SKILL.md in extracted content
    skill_md_path = find_skill_md(extract_dir)
    if not skill_md_path:
        raise FileNotFoundError("SKILL.md not found in archive")

    return skill_md_path.parent


def find_skill_md(directory: Path) -> Path | None:
    """Recursively find SKILL.md in directory."""
    # Check current directory first
    skill_md = directory / "SKILL.md"
    if skill_md.exists():
        return skill_md

    # Search subdirectories (max depth 3)
    for root, dirs, files in os.walk(directory):
        depth = len(Path(root).relative_to(directory).parts)
        if depth > 3:
            continue
        if "SKILL.md" in files:
            return Path(root) / "SKILL.md"

    return None


def validate_skill_md(skill_md_path: Path) -> str:
    """Validate SKILL.md and return skill name."""
    content = skill_md_path.read_text()

    if not content.startswith('---'):
        raise ValueError("SKILL.md missing YAML frontmatter")

    # Extract frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        raise ValueError("SKILL.md has invalid frontmatter format")

    frontmatter = parts[1]

    if 'name:' not in frontmatter:
        raise ValueError("SKILL.md missing required 'name' field")
    if 'description:' not in frontmatter:
        raise ValueError("SKILL.md missing required 'description' field")

    # Extract name
    for line in frontmatter.split('\n'):
        if line.strip().startswith('name:'):
            name = line.split(':', 1)[1].strip().strip('"\'')
            return name

    raise ValueError("Could not parse skill name from SKILL.md")


def download_from_archive(
    source: str,
    output_dir: str,
    force: bool = False,
    skill_name: str | None = None
) -> Path:
    """
    Download and extract skill from archive.

    Args:
        source: URL or local path to archive
        output_dir: Directory to install skill
        force: Overwrite if exists
        skill_name: Override skill name

    Returns:
        Path to installed skill directory
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        # Get archive to local path
        if is_url(source):
            # Extract filename from URL
            url_path = urlparse(source).path
            filename = os.path.basename(url_path) or 'skill.zip'
            archive_path = temp_path / filename
            download_file(source, archive_path)
        else:
            archive_path = Path(source)
            if not archive_path.exists():
                raise FileNotFoundError(f"Archive not found: {source}")

        # Determine archive type
        archive_type = get_archive_type(str(archive_path))

        # Extract archive
        extract_dir = temp_path / "extracted"
        extract_dir.mkdir()
        skill_source = extract_archive(archive_path, extract_dir, archive_type)

        # Validate and get skill name
        skill_md = skill_source / "SKILL.md"
        extracted_name = validate_skill_md(skill_md)
        final_name = skill_name or extracted_name

        # Check if exists
        target_dir = output_path / final_name
        if target_dir.exists():
            if force:
                print(f"⚠️  Removing existing skill '{final_name}'...")
                shutil.rmtree(target_dir)
            else:
                print(f"⚠️  Skill '{final_name}' already exists at {target_dir}")
                print("   Use --force to overwrite")
                return target_dir

        # Copy to output
        print(f"📦 Installing skill to {target_dir}...")
        shutil.copytree(skill_source, target_dir)

        # Remove any .git directory
        git_dir = target_dir / ".git"
        if git_dir.exists():
            shutil.rmtree(git_dir)

    print(f"✅ Installed skill '{final_name}' to {target_dir}")
    return target_dir


def main():
    parser = argparse.ArgumentParser(
        description="Download and extract skill from archive"
    )
    parser.add_argument(
        "source",
        help="URL or local path to archive (.zip, .tar.gz, .skill)"
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
    parser.add_argument(
        "--name", "-n",
        help="Override skill name"
    )

    args = parser.parse_args()

    try:
        download_from_archive(args.source, args.output, args.force, args.name)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
