#!/usr/bin/env python3
"""
Fallback transcription using Whisper when no subtitles available
Usage: extract_transcript_whisper.py [--mq|--hq] <YOUTUBE_URL> <OUTPUT_DIR>
Options:
  --mq    Use medium model (~5GB download)
  --hq    Use large model for highest quality (slower, ~10GB download)
  default: small model (~2GB download)

On macOS: Uses MLX Whisper if available (faster, Apple Silicon optimized). That uses only large model.
Otherwise: Uses OpenAI Whisper.
  
Output: SUCCESS: youtube_{VIDEO_ID}_transcript.vtt, Audio file: youtube_{VIDEO_ID}_audio.mp3 (ask user about deletion)
"""

import sys
import os
import subprocess
import re

def extract_video_id(url):
    """Extract video ID from YouTube URL"""
    # Handle youtu.be format
    if 'youtu.be/' in url:
        video_id = url.split('youtu.be/')[-1].split('?')[0]
        return video_id

    # Handle youtube.com format with v= parameter
    match = re.search(r'[?&]v=([^&]+)', url)
    if match:
        return match.group(1)

    return None

def check_yt_dlp():
    """Check if yt-dlp is installed"""
    try:
        subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("ERROR: yt-dlp is not installed", file=sys.stderr)
        sys.exit(1)

def check_uv():
    """Check if uv is available"""
    try:
        subprocess.run(['uv', '-V'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_mlx_whisper():
    """Check if MLX Whisper is available, returns (variant, command_array)"""
    # Try uv run mlx_whisper first
    if check_uv():
        try:
            subprocess.run(['uv', 'run', 'mlx_whisper', '--help'], capture_output=True, check=True, timeout=10)
            return ('uv-mlx', ['uv', 'run', 'mlx_whisper'])
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            pass

    # Try mlx-whisper command
    try:
        subprocess.run(['mlx-whisper', '--help'], capture_output=True, check=True)
        return ('mlx-whisper', ['mlx-whisper'])
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    return (None, None)

def check_whisper():
    """Check if OpenAI Whisper is installed"""
    try:
        subprocess.run(['whisper', '--help'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("ERROR: Whisper is not installed", file=sys.stderr)
        print("Install options:", file=sys.stderr)
        print("  - macOS (slow): brew install openai-whisper", file=sys.stderr)
        print("  - macOS (faster): brew install ffmpeg uv; uv venv .venv; source .venv/bin/activate; uv pip install mlx-whisper", file=sys.stderr)
        print("    (Ask your AI what the above does. At the moment pipx, python 3.14, and mlx-whisper conflict, but uv works - 11/2025)", file=sys.stderr)
        print("  - All systems: pip3 install openai-whisper", file=sys.stderr)
        sys.exit(1)

def check_audio_size(youtube_url):
    """Get audio file size estimate"""
    print("Checking audio file size...")
    result = subprocess.run(
        ['yt-dlp', '--print', '%(filesize,filesize_approx)s %(duration)s', youtube_url],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(result.stdout.strip())

def download_audio(youtube_url, audio_file):
    """Download audio from YouTube video"""
    print("Downloading audio...")
    result = subprocess.run(
        ['yt-dlp', '-x', '--audio-format', 'mp3', '--output', audio_file, youtube_url],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("ERROR: Failed to download audio", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(audio_file):
        print("ERROR: Audio file not found", file=sys.stderr)
        sys.exit(1)

def get_video_language(youtube_url):
    """Get video language from YouTube"""
    result = subprocess.run(
        ['yt-dlp', '--print', '%(language)s', youtube_url],
        capture_output=True,
        text=True
    )
    video_lang = result.stdout.strip() if result.returncode == 0 else "unknown"
    return video_lang

def transcribe_with_whisper(audio_file, output_dir, mlx_command=None, quality='default'):
    """Transcribe audio file with Whisper (MLX or OpenAI)"""
    if mlx_command:
        # MLX Whisper - default large-v3 as faster processing and better quality, supports other models
        print(f"Transcribing with MLX Whisper (Apple Silicon optimized, large-v3 model) - this may take a while...")
        command = mlx_command
        model = 'mlx-community/whisper-large-v3-mlx'
        # MLX uses hyphens in arguments
        output_format_arg = '--output-format'
        output_dir_arg = '--output-dir'
    else:
        # OpenAI Whisper - configurable quality
        # All models are multilingual and support ~99 languages
        # Model sizes: tiny (~1GB, fast), base (~1GB, balanced), small (~2GB), medium (~5GB), large (~10GB, best)
        command = ['whisper']
        if quality == 'hq':
            model = 'large'
            size_info = '~10GB'
        elif quality == 'mq':
            model = 'medium'
            size_info = '~5GB'
        else:
            model = 'small'
            size_info = '~2GB'
        print(f"Transcribing with OpenAI Whisper model '{model}' ({size_info}) - this may take a while...")
        # OpenAI uses underscores in arguments
        output_format_arg = '--output_format'
        output_dir_arg = '--output_dir'

    result = subprocess.run(
        command + [audio_file, '--model', model, output_format_arg, 'vtt', output_dir_arg, output_dir],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"ERROR: {' '.join(command)} transcription failed", file=sys.stderr)
        if os.path.exists(audio_file):
            os.remove(audio_file)
        sys.exit(1)

    if not mlx_command and quality == 'default':
        print("NOTE: If transcription quality is poor, try --mq (medium, ~5GB) or --hq (large, ~10GB)")

def rename_vtt_file(audio_file, base_name, output_dir):
    """Rename VTT file to standard name"""
    # Whisper creates VTT file with same name as audio file
    audio_basename = os.path.splitext(os.path.basename(audio_file))[0]
    vtt_file = os.path.join(output_dir, f"{audio_basename}.vtt")
    final_vtt = os.path.join(output_dir, f"{base_name}_transcript.vtt")

    if os.path.exists(vtt_file):
        try:
            os.rename(vtt_file, final_vtt)
        except Exception as e:
            print(f"ERROR: Failed to rename VTT file: {e}", file=sys.stderr)
            if os.path.exists(audio_file):
                os.remove(audio_file)
            sys.exit(1)

        print(f"SUCCESS: {final_vtt}")
        print(f"Audio file: {audio_file} (delete with: rm {audio_file})")
        return final_vtt
    else:
        print("ERROR: VTT file not created", file=sys.stderr)
        if os.path.exists(audio_file):
            os.remove(audio_file)
        sys.exit(1)

def main():
    # Parse options
    quality = 'default'
    args = []
    for arg in sys.argv[1:]:
        if arg == '--hq':
            quality = 'hq'
        elif arg == '--mq':
            quality = 'mq'
        else:
            args.append(arg)

    # Parse arguments
    if len(args) != 2:
        print("Usage: extract_transcript_whisper.py [--mq|--hq] <YOUTUBE_URL> <OUTPUT_DIR>", file=sys.stderr)
        sys.exit(1)

    youtube_url = args[0]
    output_dir = args[1]

    # Validate arguments
    if not youtube_url:
        print("ERROR: No YouTube URL provided", file=sys.stderr)
        sys.exit(1)

    # Check required commands
    check_yt_dlp()

    # Check which Whisper variant is available
    mlx_variant, mlx_command = check_mlx_whisper()
    if mlx_variant:
        print(f"Using MLX Whisper via {mlx_variant} (Apple Silicon optimized)")
        if quality != 'default':
            print("NOTE: Quality flags (--mq, --hq) are ignored with MLX Whisper (always uses large-v3)")
    else:
        check_whisper()
        print("Using OpenAI Whisper")
        mlx_command = None

    # Extract video ID from URL
    video_id = extract_video_id(youtube_url)
    if not video_id:
        print("ERROR: Could not extract video ID from URL", file=sys.stderr)
        sys.exit(1)

    base_name = f"youtube_{video_id}"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Check audio size
    check_audio_size(youtube_url)

    # Get video language
    video_lang = get_video_language(youtube_url)
    print(f"Video language: {video_lang}")

    # Download audio
    audio_file = os.path.join(output_dir, f"{base_name}_audio.mp3")
    download_audio(youtube_url, audio_file)

    # Transcribe with Whisper (MLX or OpenAI variant)
    transcribe_with_whisper(audio_file, output_dir, mlx_command=mlx_command, quality=quality)

    # Rename VTT file
    rename_vtt_file(audio_file, base_name, output_dir)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)
