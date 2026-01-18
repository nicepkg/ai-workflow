#!/usr/bin/env python3
"""
File operations for YouTube to Markdown: backup and cleanup.

Usage:
    python file_ops.py backup <file>
        Create timestamped backup: {file}_backup_{YYYYMMDD}.md

    python file_ops.py cleanup <output_dir> <video_id>
        Remove intermediate work files for given video_id
"""

import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

from shared_types import FileOperationError, FileSystem, RealFileSystem


# Intermediate file patterns (from finalize.py)
INTERMEDIATE_PATTERNS = [
    "{base_name}_title.txt",
    "{base_name}_metadata.md",
    "{base_name}_summary.md",
    "{base_name}_summary_tight.md",
    "{base_name}_description.md",
    "{base_name}_chapters.json",
    "{base_name}_transcript.vtt",
    "{base_name}_transcript_dedup.md",
    "{base_name}_transcript_no_timestamps.txt",
    "{base_name}_transcript_paragraphs.txt",
    "{base_name}_transcript_paragraphs.md",
    "{base_name}_transcript_cleaned.md",
    "{base_name}_transcript.md",
]


class FileOps:
    """File operations: backup and cleanup."""

    def __init__(self, fs: Optional[FileSystem] = None):
        self.fs = fs or RealFileSystem()

    def backup(self, file_path: Path) -> Path:
        """
        Create timestamped backup of file.

        Args:
            file_path: Path to file to backup

        Returns:
            Path to backup file

        Raises:
            FileOperationError: If file does not exist
        """
        if not self.fs.exists(file_path):
            raise FileOperationError(f"File not found: {file_path}")

        content = self.fs.read_text(file_path)

        today = datetime.now().strftime("%Y%m%d")
        stem = file_path.stem
        suffix = file_path.suffix
        backup_name = f"{stem}_backup_{today}{suffix}"
        backup_path = file_path.parent / backup_name

        self.fs.write_text(backup_path, content)
        return backup_path

    def cleanup(self, output_dir: Path, video_id: str) -> int:
        """
        Remove intermediate work files for video.

        Args:
            output_dir: Directory containing work files
            video_id: YouTube video ID

        Returns:
            Number of files removed
        """
        base_name = f"youtube_{video_id}"
        removed_count = 0

        for pattern in INTERMEDIATE_PATTERNS:
            filename = pattern.format(base_name=base_name)
            file_path = output_dir / filename
            if self.fs.exists(file_path):
                self.fs.remove(file_path)
                removed_count += 1

        return removed_count


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "backup":
        if len(sys.argv) != 3:
            print("Usage: python file_ops.py backup <file>")
            sys.exit(1)

        file_path = Path(sys.argv[2])
        file_ops = FileOps()
        backup_path = file_ops.backup(file_path)
        print(f"Created backup: {backup_path}")

    elif command == "cleanup":
        if len(sys.argv) != 4:
            print("Usage: python file_ops.py cleanup <output_dir> <video_id>")
            sys.exit(1)

        output_dir = Path(sys.argv[2])
        video_id = sys.argv[3]
        file_ops = FileOps()
        removed = file_ops.cleanup(output_dir, video_id)
        print(f"Removed {removed} intermediate files")

    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
