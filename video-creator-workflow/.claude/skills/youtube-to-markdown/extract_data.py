#!/usr/bin/env python3
"""
Extracts YouTube video data: metadata, description, and chapters
Usage: extract_data.py <YOUTUBE_URL> <OUTPUT_DIR>
Output: Creates youtube_{VIDEO_ID}_metadata.md, youtube_{VIDEO_ID}_description.md, youtube_{VIDEO_ID}_chapters.json
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))
from shared_types import (
    FileSystem, CommandRunner, RealFileSystem, RealCommandRunner,
    VideoMetadata, extract_video_id, format_upload_date, format_subscribers,
    format_duration, format_count, CommandNotFoundError, FileOperationError
)


class YouTubeDataExtractor:
    """Extracts and processes YouTube video data."""

    def __init__(
        self,
        fs: FileSystem = RealFileSystem(),
        cmd: CommandRunner = RealCommandRunner()
    ):
        """
        Initialize extractor with dependencies.

        Args:
            fs: File system implementation
            cmd: Command runner implementation
        """
        self.fs = fs
        self.cmd = cmd

    def check_yt_dlp(self) -> None:
        """
        Check if yt-dlp is installed.

        Raises:
            CommandNotFoundError: If yt-dlp is not installed
        """
        try:
            result = self.cmd.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except Exception:
            raise CommandNotFoundError(
                "yt-dlp is not installed\n"
                "Install options:\n"
                "  - macOS: brew install yt-dlp\n"
                "  - Ubuntu/Debian: sudo apt update && sudo apt install -y yt-dlp\n"
                "  - All systems: pip3 install yt-dlp"
            )

    def fetch_video_data(self, video_url: str, output_dir: Path) -> dict:
        """
        Fetch video metadata from YouTube.

        Args:
            video_url: YouTube URL
            output_dir: Directory for temporary files

        Returns:
            Dictionary containing video metadata

        Raises:
            FileOperationError: If metadata extraction fails
        """
        temp_json = output_dir / "video_data.json"

        try:
            # Run yt-dlp and write JSON to temp file
            with open(temp_json, 'w') as f:
                result = self.cmd.run(
                    ['yt-dlp', '--dump-single-json', '--skip-download', video_url],
                    stdout=f,
                    stderr=None,
                    text=True
                )

            if result.returncode != 0:
                raise FileOperationError("Failed to extract video metadata")

            # Read and parse JSON
            data_str = self.fs.read_text(temp_json)
            data = json.loads(data_str)

            return data

        except json.JSONDecodeError as e:
            raise FileOperationError(f"Failed to parse JSON: {e}")
        except Exception as e:
            raise FileOperationError(f"Failed to extract video metadata: {e}")
        finally:
            # Clean up temp file
            if self.fs.exists(temp_json):
                self.fs.remove(temp_json)

    def parse_video_metadata(self, data: dict, video_id: str) -> VideoMetadata:
        """
        Parse raw video data into VideoMetadata object.

        Args:
            data: Raw data from yt-dlp
            video_id: Video ID

        Returns:
            VideoMetadata object
        """
        return VideoMetadata(
            video_id=video_id,
            title=data.get('title', 'Untitled'),
            webpage_url=data.get('webpage_url', 'N/A'),
            uploader=data.get('uploader', 'Unknown'),
            channel_url=data.get('channel_url', data.get('uploader_url', '')),
            channel_follower_count=data.get('channel_follower_count'),
            channel_is_verified=data.get('channel_is_verified', False),
            upload_date=data.get('upload_date', 'Unknown'),
            view_count=data.get('view_count', 0),
            like_count=data.get('like_count', 0),
            comment_count=data.get('comment_count'),
            duration=data.get('duration', 0),
            description=data.get('description', 'No description'),
            chapters=data.get('chapters', []),
            language=data.get('language', 'unknown'),
            categories=data.get('categories', []),
            tags=data.get('tags', []),
            license=data.get('license')
        )

    def create_metadata_file(
        self,
        metadata: VideoMetadata,
        base_name: str,
        output_dir: Path
    ) -> Path:
        """
        Create metadata markdown file.

        Args:
            metadata: Video metadata
            base_name: Base filename (youtube_{VIDEO_ID})
            output_dir: Output directory

        Returns:
            Path to created metadata file
        """
        filename = output_dir / f"{base_name}_metadata.md"

        # Save title to separate file for finalize.py
        title_file = output_dir / f"{base_name}_title.txt"
        self.fs.write_text(title_file, metadata.title)

        # Format values
        upload_date = format_upload_date(metadata.upload_date)
        extraction_date = datetime.now().strftime('%Y-%m-%d')
        sub_text = format_subscribers(metadata.channel_follower_count)
        duration_text = format_duration(metadata.duration)
        views_text = format_count(metadata.view_count)
        likes_text = format_count(metadata.like_count)
        comments_text = format_count(metadata.comment_count)
        verified_text = " ✓" if metadata.channel_is_verified else ""

        # Build content
        lines = [
            f"- **Title:** [{metadata.title}]({metadata.webpage_url}) · {duration_text}"
        ]

        if metadata.channel_url:
            lines.append(
                f"- **Channel:** [{metadata.uploader}]({metadata.channel_url}){verified_text} ({sub_text})"
            )
        else:
            lines.append(f"- **Channel:** {metadata.uploader}{verified_text} ({sub_text})")

        lines.extend([
            f"- **Engagement:** {views_text} views · {likes_text} likes · {comments_text} comments",
            f"- **Published:** {upload_date} | Extracted: {extraction_date}"
        ])

        # Add category and license if available
        category_license = []
        if metadata.categories:
            category_license.append(f"**Category:** {', '.join(metadata.categories)}")
        if metadata.license:
            category_license.append(f"**License:** {metadata.license}")
        if category_license:
            lines.append(f"- {' | '.join(category_license)}")

        # Add tags if available (limit to 8)
        if metadata.tags:
            tags_display = metadata.tags[:8]
            lines.append(f"- **Tags:** {', '.join(tags_display)}")

        content = '\n'.join(lines)
        self.fs.write_text(filename, content)

        print(f"SUCCESS: {filename}")
        return filename

    def create_description_file(
        self,
        metadata: VideoMetadata,
        base_name: str,
        output_dir: Path
    ) -> Path:
        """
        Create description markdown file.

        Args:
            metadata: Video metadata
            base_name: Base filename
            output_dir: Output directory

        Returns:
            Path to created description file
        """
        filename = output_dir / f"{base_name}_description.md"
        self.fs.write_text(filename, metadata.description)

        print(f"SUCCESS: {filename}")
        return filename

    def create_chapters_file(
        self,
        metadata: VideoMetadata,
        base_name: str,
        output_dir: Path
    ) -> Path:
        """
        Create chapters JSON file.

        Args:
            metadata: Video metadata
            base_name: Base filename
            output_dir: Output directory

        Returns:
            Path to created chapters file
        """
        chapters_file = output_dir / f"{base_name}_chapters.json"
        chapters_json = json.dumps(metadata.chapters, indent=2)
        self.fs.write_text(chapters_file, chapters_json)

        if metadata.chapters:
            print(f"CHAPTERS: {chapters_file}")
        else:
            print(f"CHAPTERS: {chapters_file} (no chapters in video)")

        return chapters_file

    def extract_all(self, video_url: str, output_dir: Path) -> tuple[Path, Path, Path]:
        """
        Extract all video data (metadata, description, chapters).

        Args:
            video_url: YouTube URL
            output_dir: Output directory

        Returns:
            Tuple of (metadata_file, description_file, chapters_file)

        Raises:
            Various exceptions from component methods
        """
        # Check dependencies
        self.check_yt_dlp()

        # Extract video ID
        video_id = extract_video_id(video_url)
        base_name = f"youtube_{video_id}"

        # Create output directory
        self.fs.mkdir(output_dir)

        # Fetch and parse data
        raw_data = self.fetch_video_data(video_url, output_dir)
        metadata = self.parse_video_metadata(raw_data, video_id)

        # Create output files
        metadata_file = self.create_metadata_file(metadata, base_name, output_dir)
        description_file = self.create_description_file(metadata, base_name, output_dir)
        chapters_file = self.create_chapters_file(metadata, base_name, output_dir)

        return metadata_file, description_file, chapters_file


def main() -> None:
    """CLI entry point."""
    # Parse arguments
    if len(sys.argv) != 3:
        print("Usage: extract_data.py <YOUTUBE_URL> <OUTPUT_DIR>", file=sys.stderr)
        sys.exit(1)

    video_url = sys.argv[1]
    output_dir = Path(sys.argv[2])

    # Validate arguments
    if not video_url:
        print("ERROR: No YouTube URL provided", file=sys.stderr)
        sys.exit(1)

    try:
        extractor = YouTubeDataExtractor()
        extractor.extract_all(video_url, output_dir)
    except Exception as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
