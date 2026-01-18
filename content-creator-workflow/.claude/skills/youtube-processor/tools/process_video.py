#!/usr/bin/env python3
"""
YouTube Processor CLI
Command-line interface for the youtube-processor skill.

Usage:
    python process_video.py --url "https://youtube.com/watch?v=..." [options]

Options:
    --url           YouTube video URL (required)
    --type          Summary type: brief, detailed, bullets, newsletter (default: detailed)
    --save          Save to Obsidian vault
    --vault         Custom vault path (default: Ed's Zettelkasten)
    --transcript    Only extract transcript, no summary
    --json          Output as JSON
"""

import argparse
import json
import sys
import os

# Add the tools directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from youtube_core import (
    process_video,
    extract_video_id,
    get_transcript,
    ProcessingResult
)


def main():
    parser = argparse.ArgumentParser(
        description="Process YouTube videos into summaries and Obsidian notes"
    )
    parser.add_argument(
        "--url", "-u",
        required=True,
        help="YouTube video URL"
    )
    parser.add_argument(
        "--type", "-t",
        default="detailed",
        choices=["brief", "detailed", "bullets", "newsletter"],
        help="Summary type (default: detailed)"
    )
    parser.add_argument(
        "--save", "-s",
        action="store_true",
        help="Save to Obsidian vault"
    )
    parser.add_argument(
        "--vault", "-v",
        default="/Users/eddale/Documents/COPYobsidian/MAGI/Zettelkasten",
        help="Path to Obsidian vault"
    )
    parser.add_argument(
        "--transcript-only",
        action="store_true",
        help="Only extract transcript, skip summarization"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON"
    )

    args = parser.parse_args()

    # Transcript-only mode
    if args.transcript_only:
        try:
            video_id = extract_video_id(args.url)
            transcript, lang = get_transcript(video_id)

            if args.json:
                print(json.dumps({
                    "success": True,
                    "video_id": video_id,
                    "language": lang,
                    "transcript": transcript
                }, indent=2))
            else:
                print(f"Video ID: {video_id}")
                print(f"Language: {lang}")
                print(f"\n--- TRANSCRIPT ---\n")
                print(transcript)

        except Exception as e:
            if args.json:
                print(json.dumps({"success": False, "error": str(e)}))
            else:
                print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        return

    # Full processing
    result = process_video(
        url=args.url,
        summary_type=args.type,
        save_to_vault=args.save,
        vault_path=args.vault
    )

    if args.json:
        print(json.dumps({
            "success": result.success,
            "video_id": result.video_id,
            "summary": result.summary,
            "markdown_output": result.markdown_output,
            "saved_to": result.saved_to,
            "error": result.error
        }, indent=2))
    else:
        if result.success:
            print(f"Video ID: {result.video_id}")
            print(f"\n--- SUMMARY ---\n")
            print(result.summary)

            if result.saved_to:
                print(f"\n--- SAVED TO ---")
                print(result.saved_to)
        else:
            print(f"Error: {result.error}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
