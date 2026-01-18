"""
Shared types, protocols, and exceptions for YouTube to Markdown conversion.

This module defines the interfaces for external dependencies (file system, subprocess)
to enable dependency injection and improve testability.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, Optional, Any
import json


# Custom Exceptions
class YouTubeToMarkdownError(Exception):
    """Base exception for YouTube to Markdown operations."""
    pass


class VideoIdExtractionError(YouTubeToMarkdownError):
    """Failed to extract video ID from URL."""
    pass


class CommandNotFoundError(YouTubeToMarkdownError):
    """Required command not found."""
    pass


class TranscriptNotAvailableError(YouTubeToMarkdownError):
    """No transcript available for the video."""
    pass


class FileOperationError(YouTubeToMarkdownError):
    """File operation failed."""
    pass


# Data Classes
@dataclass
class VideoMetadata:
    """Video metadata extracted from YouTube."""
    video_id: str
    title: str
    webpage_url: str
    uploader: str
    channel_url: str
    channel_follower_count: Optional[int]
    channel_is_verified: bool
    upload_date: str
    view_count: int
    like_count: int
    comment_count: Optional[int]
    duration: int
    description: str
    chapters: list[dict[str, Any]]
    language: str
    categories: list[str]
    tags: list[str]
    license: Optional[str]


@dataclass
class TranscriptLine:
    """Single line of transcript with timestamp."""
    timestamp: str
    text: str


# Protocols for Dependency Injection
class FileSystem(Protocol):
    """Protocol for file system operations."""

    def read_text(self, path: Path, encoding: str = "utf-8") -> str:
        """Read text from file."""
        ...

    def write_text(self, path: Path, content: str, encoding: str = "utf-8") -> None:
        """Write text to file."""
        ...

    def exists(self, path: Path) -> bool:
        """Check if path exists."""
        ...

    def mkdir(self, path: Path, parents: bool = True, exist_ok: bool = True) -> None:
        """Create directory."""
        ...

    def remove(self, path: Path) -> None:
        """Remove file."""
        ...

    def glob(self, pattern: str, directory: Path) -> list[Path]:
        """Find files matching pattern."""
        ...


class CommandRunner(Protocol):
    """Protocol for running external commands."""

    def run(
        self,
        command: list[str],
        capture_output: bool = False,
        text: bool = False,
        check: bool = False,
        timeout: Optional[int] = None,
        stdout: Any = None,
        stderr: Any = None
    ) -> "CommandResult":
        """Run command and return result."""
        ...


@dataclass
class CommandResult:
    """Result of command execution."""
    returncode: int
    stdout: str
    stderr: str


# Real Implementations
class RealFileSystem:
    """Real file system implementation."""

    def read_text(self, path: Path, encoding: str = "utf-8") -> str:
        """Read text from file."""
        return path.read_text(encoding=encoding)

    def write_text(self, path: Path, content: str, encoding: str = "utf-8") -> None:
        """Write text to file."""
        path.write_text(content, encoding=encoding)

    def exists(self, path: Path) -> bool:
        """Check if path exists."""
        return path.exists()

    def mkdir(self, path: Path, parents: bool = True, exist_ok: bool = True) -> None:
        """Create directory."""
        path.mkdir(parents=parents, exist_ok=exist_ok)

    def remove(self, path: Path) -> None:
        """Remove file."""
        path.unlink()

    def glob(self, pattern: str, directory: Path) -> list[Path]:
        """Find files matching pattern."""
        return list(directory.glob(pattern))


class RealCommandRunner:
    """Real command runner using subprocess."""

    def run(
        self,
        command: list[str],
        capture_output: bool = False,
        text: bool = False,
        check: bool = False,
        timeout: Optional[int] = None,
        stdout: Any = None,
        stderr: Any = None
    ) -> CommandResult:
        """Run command and return result."""
        import subprocess

        result = subprocess.run(
            command,
            capture_output=capture_output,
            text=text,
            check=check,
            timeout=timeout,
            stdout=stdout,
            stderr=stderr
        )

        return CommandResult(
            returncode=result.returncode,
            stdout=result.stdout if text else "",
            stderr=result.stderr if text else ""
        )


# Utility Functions
def extract_video_id(url: str) -> str:
    """
    Extract video ID from YouTube URL.

    Args:
        url: YouTube URL (youtu.be or youtube.com format)

    Returns:
        Video ID string

    Raises:
        VideoIdExtractionError: If video ID cannot be extracted
    """
    import re

    # Handle youtu.be format
    if 'youtu.be/' in url:
        video_id = url.split('youtu.be/')[-1].split('?')[0]
        if video_id:
            return video_id

    # Handle youtube.com format with v= parameter
    match = re.search(r'[?&]v=([^&]+)', url)
    if match:
        return match.group(1)

    raise VideoIdExtractionError(f"Could not extract video ID from URL: {url}")


def format_upload_date(upload_date: str) -> str:
    """
    Format upload date from YYYYMMDD to YYYY-MM-DD.

    Args:
        upload_date: Date string in YYYYMMDD format

    Returns:
        Formatted date string or 'Unknown' if invalid
    """
    if upload_date != 'Unknown' and len(str(upload_date)) == 8:
        return f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"
    return upload_date


def format_subscribers(subscribers: Optional[int]) -> str:
    """
    Format subscriber count.

    Args:
        subscribers: Subscriber count or None

    Returns:
        Formatted subscriber string
    """
    if isinstance(subscribers, int):
        return f"{subscribers:,} subscribers"
    return "N/A subscribers"


def format_duration(duration: int) -> str:
    """
    Format duration from seconds to HH:MM:SS or MM:SS.

    Args:
        duration: Duration in seconds

    Returns:
        Formatted duration string
    """
    if duration:
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        seconds = duration % 60
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            return f"{minutes:02d}:{seconds:02d}"
    return "Unknown"


def format_count(count: Optional[int]) -> str:
    """
    Format large numbers with K/M suffix.

    Args:
        count: Number to format

    Returns:
        Formatted string (e.g., "2.2M", "71K", "500")
    """
    if count is None:
        return "N/A"
    if count >= 1_000_000:
        return f"{count / 1_000_000:.1f}M".replace(".0M", "M")
    if count >= 1_000:
        return f"{count / 1_000:.1f}K".replace(".0K", "K")
    return str(count)


def clean_title_for_filename(title: str, max_length: int = 60) -> str:
    """
    Clean title for use in filename.

    Args:
        title: Original title
        max_length: Maximum length for filename

    Returns:
        Cleaned title suitable for filename
    """
    import re

    # Remove or replace problematic characters
    cleaned = re.sub(r'[<>:"/\\|?*]', '', title)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    cleaned = cleaned.strip()

    # Truncate if too long
    if len(cleaned) > max_length:
        cleaned = cleaned[:max_length].rsplit(' ', 1)[0]

    return cleaned
