#!/usr/bin/env python3
"""
Checks if a YouTube video has already been processed.
Usage: check_existing.py <YOUTUBE_URL> <OUTPUT_DIR>
Output: JSON with existence status, file paths, format versions, and stored metadata.
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from shared_types import extract_video_id


def find_existing_files(video_id: str, output_dir: Path) -> dict:
    """Find existing summary and comment files for a video ID."""
    # Use broad pattern first, then filter
    all_files = list(output_dir.glob(f"youtube - * ({video_id}).md"))

    # Filter out backups
    all_files = [f for f in all_files if "_backup_" not in f.name]

    summary_file = None
    comment_file = None
    transcript_file = None

    for f in all_files:
        name = f.name
        if " - comments " in name:
            comment_file = f
        elif " - transcript " in name:
            transcript_file = f
        else:
            # Main summary file (no suffix before video ID)
            summary_file = f

    return {
        "summary_file": str(summary_file) if summary_file else None,
        "comment_file": str(comment_file) if comment_file else None,
        "transcript_file": str(transcript_file) if transcript_file else None,
    }


def detect_v1_summary(content: str) -> bool:
    """
    Detect if summary uses v1.0 format (universal W5H for all videos).

    V1.0 markers:
    - Contains **What**: AND **Why**: AND **How**: pattern
    - Does NOT contain type-specific markers
    """
    has_w5h = all(marker in content for marker in ["**What**:", "**Why**:", "**How**:"])

    # Type-specific markers from v2.0
    type_markers = [
        "### Prerequisites",  # TUTORIAL
        "**Result**:",  # TUTORIAL
        "- **[",  # TIPS bullet pattern
    ]
    has_type_markers = any(marker in content for marker in type_markers)

    return has_w5h and not has_type_markers


def detect_v1_comments(content: str) -> bool:
    """
    Detect if comment insights use v1.0 format (no type-specific sections).
    """
    type_sections = [
        "**Common Failures**",
        "**Success Patterns**",
        "**What Worked/Didn't**",
        "**Alternatives Mentioned**",
        "**Points of Agreement**",
        "**Points of Debate**",
        "**Related Stories**",
        "**Corrections/Extensions**",
        "**Debates**",
    ]
    return not any(section in content for section in type_sections)


def has_section_content(content: str, section: str) -> bool:
    """Check if section header exists AND has non-empty content after it."""
    pattern = rf"{re.escape(section)}\s*\n(.*?)(?=\n## |\Z)"
    match = re.search(pattern, content, re.DOTALL)
    return match is not None and len(match.group(1).strip()) > 0


def validate_summary_integrity(content: str) -> tuple[bool, list[str]]:
    """
    Validate that summary file has all required elements with content.
    Returns (is_valid, list_of_issues).
    """
    issues = []

    if not has_section_content(content, "## Video"):
        issues.append("empty_video_section")

    if not has_section_content(content, "## Summary"):
        issues.append("empty_summary_section")
    elif "**TL;DR**" not in content:
        issues.append("missing_tldr")

    return (len(issues) == 0, issues)


def validate_transcript_integrity(content: str) -> tuple[bool, list[str]]:
    """Validate transcript file has required elements with content."""
    issues = []

    if not has_section_content(content, "## Transcription"):
        issues.append("empty_transcription_section")

    return (len(issues) == 0, issues)


def validate_comments_integrity(content: str) -> tuple[bool, list[str]]:
    """Validate comments file has required elements with content."""
    issues = []

    if not has_section_content(content, "## Comment Insights"):
        issues.append("empty_insights_section")

    return (len(issues) == 0, issues)


def extract_metadata_from_file(content: str) -> dict:
    """
    Extract metadata from existing summary file.

    Supports both formats:
    - New: "- **Engagement:** 2.2M views · 71.2K likes · 2.2K comments"
    - Old: "- **Views:** 2,183,167 | Likes: 71,220 | Duration: 05:28"
    """
    metadata = {
        "views": None,
        "likes": None,
        "comments": None,
        "published": None,
        "extracted": None,
    }

    # Try new engagement format first
    engagement_match = re.search(
        r"\*\*Engagement:\*\*\s*([^\s]+)\s*views\s*·\s*([^\s]+)\s*likes\s*·\s*([^\s]+)\s*comments",
        content,
    )
    if engagement_match:
        metadata["views"] = engagement_match.group(1)
        metadata["likes"] = engagement_match.group(2)
        metadata["comments"] = engagement_match.group(3)
    else:
        # Try old format: **Views:** X | Likes: Y | Duration: Z
        old_format_match = re.search(
            r"\*\*Views:\*\*\s*([^\s|]+)\s*\|\s*Likes:\s*([^\s|]+)",
            content,
        )
        if old_format_match:
            metadata["views"] = old_format_match.group(1)
            metadata["likes"] = old_format_match.group(2)

    # Parse published line
    published_match = re.search(
        r"\*\*Published:\*\*\s*(\d{4}-\d{2}-\d{2})\s*\|\s*Extracted:\s*(\d{4}-\d{2}-\d{2})",
        content,
    )
    if published_match:
        metadata["published"] = published_match.group(1)
        metadata["extracted"] = published_match.group(2)

    return metadata


def check_existing(video_url: str, output_dir: Path) -> dict:
    """
    Check if video has been processed and analyze existing files.

    Returns:
        Dictionary with:
        - exists: bool
        - summary_file: path or None
        - comment_file: path or None
        - transcript_file: path or None
        - summary_v1: bool (if summary exists)
        - comments_v1: bool (if comments exist)
        - stored_metadata: dict (if summary exists)
    """
    video_id = extract_video_id(video_url)
    files = find_existing_files(video_id, output_dir)

    result = {
        "video_id": video_id,
        "exists": files["summary_file"] is not None,
        **files,
    }

    # Analyze summary if it exists
    if files["summary_file"]:
        content = Path(files["summary_file"]).read_text()
        result["summary_v1"] = detect_v1_summary(content)
        result["stored_metadata"] = extract_metadata_from_file(content)
        valid, issues = validate_summary_integrity(content)
        result["summary_valid"] = valid
        result["summary_issues"] = issues

    # Analyze transcript if it exists
    if files["transcript_file"]:
        content = Path(files["transcript_file"]).read_text()
        valid, issues = validate_transcript_integrity(content)
        result["transcript_valid"] = valid
        result["transcript_issues"] = issues

    # Analyze comments if they exist
    if files["comment_file"]:
        content = Path(files["comment_file"]).read_text()
        result["comments_v1"] = detect_v1_comments(content)
        valid, issues = validate_comments_integrity(content)
        result["comments_valid"] = valid
        result["comments_issues"] = issues

    return result


def main() -> None:
    """CLI entry point."""
    if len(sys.argv) != 3:
        print("Usage: check_existing.py <YOUTUBE_URL> <OUTPUT_DIR>", file=sys.stderr)
        sys.exit(1)

    video_url = sys.argv[1]
    output_dir = Path(sys.argv[2])

    if not output_dir.exists():
        print(json.dumps({"exists": False, "video_id": extract_video_id(video_url)}))
        sys.exit(0)

    result = check_existing(video_url, output_dir)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
