#!/usr/bin/env python3
"""
WhisperKit Audio/Video Transcription Script

This script downloads and transcribes audio/video from URLs using WhisperKit.
Supports YouTube, direct video URLs, and audio URLs.

Dependencies:
- yt-dlp: For downloading media from URLs
- whisperkit-cli: For local transcription using WhisperKit
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime
import json
import shutil


def check_dependencies():
    """Check if required tools are installed."""
    dependencies = {
        'yt-dlp': 'Install with: pip install yt-dlp or brew install yt-dlp',
        'whisperkit-cli': 'Install from: https://github.com/argmaxinc/WhisperKit'
    }

    missing = []
    for cmd, install_msg in dependencies.items():
        if not shutil.which(cmd):
            missing.append(f"  - {cmd}: {install_msg}")

    if missing:
        print("❌ Missing dependencies:\n" + "\n".join(missing), file=sys.stderr)
        return False
    return True


def download_media(url, output_dir):
    """Download audio from URL using yt-dlp.

    Args:
        url: URL to download from
        output_dir: Directory to save downloaded file

    Returns:
        Path to downloaded audio file
    """
    print(f"📥 Downloading media from URL...")

    # Create temp directory for download
    download_path = Path(output_dir) / "temp_download"
    download_path.mkdir(parents=True, exist_ok=True)

    # Use yt-dlp to download and extract audio
    output_template = str(download_path / "audio.%(ext)s")

    cmd = [
        'yt-dlp',
        '--extract-audio',
        '--audio-format', 'mp3',
        '--output', output_template,
        url
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)

        # Find the downloaded file
        audio_files = list(download_path.glob("audio.*"))
        if not audio_files:
            print("❌ Download failed: No audio file found", file=sys.stderr)
            return None

        print(f"✅ Downloaded: {audio_files[0].name}")
        return audio_files[0]

    except subprocess.CalledProcessError as e:
        print(f"❌ Download failed: {e.stderr}", file=sys.stderr)
        return None


def transcribe_with_whisperkit(audio_path, model="small", timestamps=True):
    """Transcribe audio file using WhisperKit CLI.

    Args:
        audio_path: Path to audio file
        model: WhisperKit model size (tiny, base, small, medium, large)
        timestamps: Include timestamps in output

    Returns:
        Transcription text or None if failed
    """
    print(f"🎤 Transcribing with WhisperKit ({model} model)...")

    cmd = [
        'whisperkit-cli',
        'transcribe',
        '--model', model,
        '--audio-path', str(audio_path)
    ]

    if timestamps:
        cmd.append('--verbose')

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ Transcription complete")
        return result.stdout

    except subprocess.CalledProcessError as e:
        print(f"❌ Transcription failed: {e.stderr}", file=sys.stderr)
        return None


def format_transcription(raw_output, url, timestamps=True):
    """Format transcription output with metadata.

    Args:
        raw_output: Raw transcription from WhisperKit
        url: Original source URL
        timestamps: Whether to include timestamps

    Returns:
        Formatted markdown string
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    output = f"""# Transcription

**Source:** {url}
**Transcribed:** {now}
**Tool:** WhisperKit

---

"""

    if timestamps:
        output += raw_output
    else:
        # Parse and remove timestamps if present
        lines = raw_output.split('\n')
        text_only = []
        for line in lines:
            # Remove timestamp patterns like [00:00:00.000 --> 00:00:05.000]
            if '-->' not in line and line.strip():
                text_only.append(line)
        output += '\n'.join(text_only)

    return output


def get_output_path(base_dir, url, auto_timestamp=True):
    """Generate output file path.

    Args:
        base_dir: Base output directory
        url: Source URL (used to generate filename)
        auto_timestamp: Add timestamp if file exists

    Returns:
        Path object for output file
    """
    # Create sanitized filename from URL
    import re
    from urllib.parse import urlparse

    parsed = urlparse(url)
    filename = parsed.path.split('/')[-1] or 'transcription'
    filename = re.sub(r'[^\w\-_.]', '_', filename)

    if not filename.endswith('.md'):
        filename = filename.rsplit('.', 1)[0] + '.md'

    output_path = Path(base_dir) / filename

    # Handle existing file
    if output_path.exists() and auto_timestamp:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        stem = output_path.stem
        output_path = output_path.parent / f"{stem}_{timestamp}.md"

    return output_path


def cleanup_temp_files(temp_dir):
    """Remove temporary download directory."""
    if temp_dir.exists():
        shutil.rmtree(temp_dir)


def main():
    parser = argparse.ArgumentParser(
        description='Transcribe audio/video from URLs using WhisperKit'
    )
    parser.add_argument('url', help='URL to YouTube video, video file, or audio file')
    parser.add_argument(
        '--output-dir', '-o',
        default='./whisper-transcriptions',
        help='Output directory for transcription (default: ./whisper-transcriptions)'
    )
    parser.add_argument(
        '--model', '-m',
        default='small',
        choices=['tiny', 'base', 'small', 'medium', 'large'],
        help='WhisperKit model size (default: small)'
    )
    parser.add_argument(
        '--no-timestamps',
        action='store_true',
        help='Exclude timestamps from transcription'
    )
    parser.add_argument(
        '--filename', '-f',
        help='Custom output filename (default: auto-generated from URL)'
    )

    args = parser.parse_args()

    # Check dependencies
    if not check_dependencies():
        return 1

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Download media
    audio_file = download_media(args.url, output_dir)
    if not audio_file:
        return 1

    # Transcribe
    transcription = transcribe_with_whisperkit(
        audio_file,
        model=args.model,
        timestamps=not args.no_timestamps
    )

    if not transcription:
        cleanup_temp_files(audio_file.parent)
        return 1

    # Format output
    formatted = format_transcription(
        transcription,
        args.url,
        timestamps=not args.no_timestamps
    )

    # Determine output path
    if args.filename:
        output_path = output_dir / args.filename
        if not output_path.suffix:
            output_path = output_path.with_suffix('.md')
    else:
        output_path = get_output_path(output_dir, args.url, auto_timestamp=True)

    # Save transcription
    output_path.write_text(formatted)
    print(f"💾 Saved transcription to: {output_path}")

    # Cleanup
    cleanup_temp_files(audio_file.parent)

    return 0


if __name__ == '__main__':
    sys.exit(main())
