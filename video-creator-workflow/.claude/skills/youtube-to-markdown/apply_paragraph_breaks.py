#!/usr/bin/env python3
"""
Apply paragraph breaks to deduplicated transcript
Usage: python3 apply_paragraph_breaks.py <INPUT_MD> <BREAKS_FILE> <OUTPUT_MD>
BREAKS_FILE: file containing comma-separated line numbers (e.g., "15,42,78,103")
"""

import sys
import re
from pathlib import Path
from dataclasses import dataclass

sys.path.insert(0, str(Path(__file__).parent))
from shared_types import FileSystem, RealFileSystem, FileOperationError


@dataclass
class ParsedLine:
    """Represents a parsed transcript line."""
    timestamp: str | None
    text: str


class ParagraphBreaker:
    """Applies paragraph breaks to transcript."""

    def __init__(self, fs: FileSystem = RealFileSystem(), video_id: str | None = None):
        """
        Initialize paragraph breaker with dependencies.

        Args:
            fs: File system implementation
            video_id: YouTube video ID for timestamp links
        """
        self.fs = fs
        self.video_id = video_id

    def parse_break_points(self, break_points_str: str) -> set[int]:
        """
        Parse break points string into set of line numbers.

        Args:
            break_points_str: Comma-separated line numbers

        Returns:
            Set of line numbers

        Raises:
            ValueError: If format is invalid
        """
        try:
            return {int(x.strip()) for x in break_points_str.split(',')}
        except ValueError as e:
            raise ValueError(f"Invalid break points format: {e}")

    def convert_timestamp_to_link(self, timestamp: str) -> str:
        """
        Convert timestamp to clickable YouTube link.

        Args:
            timestamp: Timestamp in format "[HH:MM:SS.mmm]" or "[MM:SS.mmm]"

        Returns:
            Markdown link with timestamp or original timestamp if no video_id
        """
        if not self.video_id:
            return timestamp

        # Extract timestamp components
        match = re.match(r'\[(\d{2}):(\d{2}):(\d{2})\.\d{3}\]', timestamp)
        if match:
            hours, minutes, seconds = map(int, match.groups())
            total_seconds = hours * 3600 + minutes * 60 + seconds
            display_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            # Try MM:SS format
            match = re.match(r'\[(\d{2}):(\d{2})\.\d{3}\]', timestamp)
            if match:
                minutes, seconds = map(int, match.groups())
                total_seconds = minutes * 60 + seconds
                display_time = f"{minutes:02d}:{seconds:02d}"
            else:
                return timestamp

        youtube_url = f"https://youtube.com/watch?v={self.video_id}&t={total_seconds}s"
        return f"[[{display_time}]]({youtube_url})"

    def parse_transcript_line(self, line: str) -> ParsedLine:
        """
        Parse transcript line with timestamp.

        Args:
            line: Line in format "[00:00:00.080] Text here"

        Returns:
            ParsedLine object
        """
        if line.startswith('[') and len(line) > 15:
            timestamp = line[:14]  # [00:00:00.080] is 14 chars
            text = line[15:]  # Text starts at position 15
            return ParsedLine(timestamp=timestamp, text=text)
        return ParsedLine(timestamp=None, text=line)

    def apply_breaks(
        self,
        input_path: Path,
        output_path: Path,
        break_points: set[int]
    ) -> int:
        """
        Apply paragraph breaks at specified line numbers.

        Args:
            input_path: Path to input file with timestamps
            output_path: Path to output file with paragraphs
            break_points: Set of line numbers for breaks

        Returns:
            Number of paragraphs created

        Raises:
            FileOperationError: If file operations fail
        """
        if not self.fs.exists(input_path):
            raise FileOperationError(f"{input_path} not found")

        # Read and parse input file
        content = self.fs.read_text(input_path)
        lines = content.split('\n')
        parsed_lines = [self.parse_transcript_line(line) for line in lines]

        # Build paragraphs based on break points
        paragraphs = []
        current_paragraph = []
        paragraph_start_timestamp = None

        for i, parsed in enumerate(parsed_lines, start=1):
            # Track first timestamp in paragraph
            if parsed.timestamp and not paragraph_start_timestamp:
                paragraph_start_timestamp = parsed.timestamp

            # Add text
            if parsed.text:
                current_paragraph.append(parsed.text)

            # Check if this is a break point or last line
            if i in break_points or i == len(parsed_lines):
                # Finish current paragraph
                if current_paragraph and paragraph_start_timestamp:
                    paragraph_text = ' '.join(current_paragraph)
                    timestamp_link = self.convert_timestamp_to_link(paragraph_start_timestamp)
                    paragraphs.append(f"{paragraph_text} {timestamp_link}")
                    current_paragraph = []
                    paragraph_start_timestamp = None

        # Validate output
        if not paragraphs:
            raise FileOperationError(f"No paragraphs created from {input_path}")

        # Write to output file
        output_content = '\n\n'.join(paragraphs) + '\n\n'
        self.fs.write_text(output_path, output_content)

        print(f"SUCCESS: Created {len(paragraphs)} paragraphs -> {output_path}")
        return len(paragraphs)


def extract_video_id_from_path(file_path: Path) -> str | None:
    """
    Extract video ID from file path with pattern youtube_{VIDEO_ID}_*.

    Args:
        file_path: Path to file

    Returns:
        Video ID or None if not found
    """
    match = re.match(r'youtube_([a-zA-Z0-9_-]+)_', file_path.name)
    return match.group(1) if match else None


def main() -> None:
    """CLI entry point."""
    if len(sys.argv) != 4:
        print("Usage: python3 apply_paragraph_breaks.py <INPUT_MD> <BREAKS_FILE> <OUTPUT_MD>", file=sys.stderr)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    breaks_file = Path(sys.argv[2])
    output_path = Path(sys.argv[3])

    # Read breaks from file
    if not breaks_file.exists():
        print(f"ERROR: Breaks file not found: {breaks_file}", file=sys.stderr)
        sys.exit(1)
    break_points_str = breaks_file.read_text().strip()

    # Extract video ID from input file path
    video_id = extract_video_id_from_path(input_path)

    try:
        breaker = ParagraphBreaker(video_id=video_id)
        break_points = breaker.parse_break_points(break_points_str)
        breaker.apply_breaks(input_path, output_path, break_points)
    except Exception as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
