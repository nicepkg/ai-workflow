#!/usr/bin/env python3
"""
Detects video language, lists available subtitles, tries manual subtitles first, falls back to auto-generated
Usage: extract_transcript.py <YOUTUBE_URL> <OUTPUT_DIR> [SUBTITLE_LANG]
Output: SUCCESS: youtube_{VIDEO_ID}_transcript.vtt or ERROR: No subtitles available
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from shared_types import (
    FileSystem, CommandRunner, RealFileSystem, RealCommandRunner,
    extract_video_id, CommandNotFoundError, TranscriptNotAvailableError,
    FileOperationError
)


class TranscriptExtractor:
    """Extracts transcript/subtitles from YouTube videos."""

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
            self.cmd.run(['yt-dlp', '--version'], capture_output=True, check=True)
        except Exception:
            raise CommandNotFoundError("yt-dlp is not installed")

    def get_video_language(self, youtube_url: str) -> str:
        """
        Get video language from YouTube.

        Args:
            youtube_url: YouTube URL

        Returns:
            Language code (e.g., 'en', 'es') or 'unknown'
        """
        result = self.cmd.run(
            ['yt-dlp', '--print', '%(language)s', youtube_url],
            capture_output=True,
            text=True
        )
        video_lang = result.stdout.strip() if result.returncode == 0 else "unknown"
        print(f"Video language: {video_lang}")
        return video_lang

    def download_manual_subtitles(
        self,
        youtube_url: str,
        subtitle_lang: str,
        output_name: Path
    ) -> Path | None:
        """
        Try to download manual subtitles.

        Args:
            youtube_url: YouTube URL
            subtitle_lang: Subtitle language code
            output_name: Output path without extension

        Returns:
            Path to downloaded subtitle file, or None if not available
        """
        self.cmd.run(
            ['yt-dlp', '--write-sub', '--sub-langs', subtitle_lang,
             '--skip-download', '--output', str(output_name), youtube_url],
            capture_output=True
        )

        # Find the created VTT file
        temp_files = self.fs.glob(f"{output_name.name}.*.vtt", output_name.parent)
        if temp_files:
            print(f"Manual subtitles downloaded ({subtitle_lang})")
            return temp_files[0]
        return None

    def download_auto_subtitles(
        self,
        youtube_url: str,
        subtitle_lang: str,
        output_name: Path
    ) -> Path | None:
        """
        Try to download auto-generated subtitles.

        Args:
            youtube_url: YouTube URL
            subtitle_lang: Subtitle language code
            output_name: Output path without extension

        Returns:
            Path to downloaded subtitle file, or None if not available
        """
        self.cmd.run(
            ['yt-dlp', '--write-auto-sub', '--sub-langs', subtitle_lang,
             '--skip-download', '--output', str(output_name), youtube_url],
            capture_output=True
        )

        # Find the created VTT file
        temp_files = self.fs.glob(f"{output_name.name}.*.vtt", output_name.parent)
        if temp_files:
            print(f"Auto-generated subtitles downloaded ({subtitle_lang})")
            return temp_files[0]
        return None

    def download_subtitles(
        self,
        youtube_url: str,
        subtitle_lang: str,
        output_name: Path
    ) -> Path:
        """
        Download subtitles, trying manual first then auto-generated.

        Args:
            youtube_url: YouTube URL
            subtitle_lang: Subtitle language code
            output_name: Output path without extension

        Returns:
            Path to downloaded subtitle file

        Raises:
            TranscriptNotAvailableError: If no subtitles are available
        """
        # Try manual subtitles first
        subtitle_file = self.download_manual_subtitles(
            youtube_url, subtitle_lang, output_name
        )
        if subtitle_file:
            return subtitle_file

        # Fall back to auto-generated
        subtitle_file = self.download_auto_subtitles(
            youtube_url, subtitle_lang, output_name
        )
        if subtitle_file:
            return subtitle_file

        raise TranscriptNotAvailableError(
            f"No subtitles available for language: {subtitle_lang}"
        )

    def rename_subtitle_file(self, temp_file: Path, final_output: Path) -> Path:
        """
        Rename temporary subtitle file to final output name.

        Args:
            temp_file: Temporary file path
            final_output: Final output path

        Returns:
            Path to final file

        Raises:
            FileOperationError: If rename fails
        """
        try:
            # Use Path.rename which works across the same filesystem
            temp_file.rename(final_output)
        except Exception as e:
            raise FileOperationError(f"Failed to rename transcript file: {e}")

        if not self.fs.exists(final_output):
            raise FileOperationError(f"{final_output} not created")

        return final_output

    def extract_transcript(
        self,
        youtube_url: str,
        output_dir: Path,
        subtitle_lang: str = "en"
    ) -> Path:
        """
        Extract transcript from YouTube video.

        Args:
            youtube_url: YouTube URL
            output_dir: Output directory
            subtitle_lang: Subtitle language code (default: 'en')

        Returns:
            Path to created transcript file

        Raises:
            Various exceptions from component methods
        """
        # Check dependencies
        self.check_yt_dlp()

        # Extract video ID
        video_id = extract_video_id(youtube_url)
        base_name = f"youtube_{video_id}"

        # Create output directory
        self.fs.mkdir(output_dir)

        # Get video language (informational)
        self.get_video_language(youtube_url)

        # Download subtitles
        output_name = output_dir / f"{base_name}_transcript_temp"
        final_output = output_dir / f"{base_name}_transcript.vtt"
        temp_file = self.download_subtitles(youtube_url, subtitle_lang, output_name)

        # Rename to final filename
        final_file = self.rename_subtitle_file(temp_file, final_output)

        print(f"SUCCESS: {final_file}")
        return final_file


def main() -> None:
    """CLI entry point."""
    # Parse arguments
    youtube_url = sys.argv[1] if len(sys.argv) > 1 else None
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(".")
    subtitle_lang = sys.argv[3] if len(sys.argv) > 3 else "en"

    # Validate arguments
    if not youtube_url:
        print("ERROR: No YouTube URL provided", file=sys.stderr)
        sys.exit(1)

    try:
        extractor = TranscriptExtractor()
        extractor.extract_transcript(youtube_url, output_dir, subtitle_lang)
    except Exception as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
