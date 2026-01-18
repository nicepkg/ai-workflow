"""
YouTube Processor Core
Shared library for transcript extraction and summarization.
Used by both the Agent Skill (CLI) and FastAPI (HTTP).
"""

import re
import os
from datetime import datetime
from typing import Optional, Tuple
from dataclasses import dataclass

# Transcript extraction
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable
)

# Claude API
import anthropic


@dataclass
class ProcessingResult:
    """Result from processing a YouTube video"""
    success: bool
    video_id: str
    title: Optional[str] = None
    transcript: Optional[str] = None
    summary: Optional[str] = None
    markdown_output: Optional[str] = None
    error: Optional[str] = None
    saved_to: Optional[str] = None


def extract_video_id(url: str) -> str:
    """
    Extract YouTube video ID from various URL formats.
    Handles: youtube.com/watch?v=ID, youtu.be/ID, youtube.com/embed/ID
    """
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
        r'youtu\.be\/([0-9A-Za-z_-]{11})',
        r'embed\/([0-9A-Za-z_-]{11})',
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    raise ValueError(f"Could not extract video ID from URL: {url}")


def get_transcript(video_id: str) -> Tuple[str, str]:
    """
    Fetch transcript from YouTube video.
    Returns: (transcript_text, language_code)

    Raises:
        ValueError: If transcript unavailable (with reason)
    """
    try:
        # New API is instance-based
        ytt_api = YouTubeTranscriptApi()

        # Try to fetch English transcript directly
        try:
            transcript_data = ytt_api.fetch(video_id, languages=['en'])
            full_text = " ".join([item.text for item in transcript_data])
            return full_text, 'en'
        except:
            # Fall back to listing and finding any available
            transcript_list = ytt_api.list(video_id)
            for transcript in transcript_list:
                transcript_data = transcript.fetch()
                full_text = " ".join([item.text for item in transcript_data])
                return full_text, transcript.language_code

        raise ValueError("No transcript found for this video")

    except TranscriptsDisabled:
        raise ValueError("Transcripts are disabled for this video")
    except NoTranscriptFound:
        raise ValueError("No transcript found for this video")
    except VideoUnavailable:
        raise ValueError("Video is unavailable or does not exist")
    except Exception as e:
        raise ValueError(f"Error fetching transcript: {str(e)}")


# Summary prompt templates
SUMMARY_PROMPTS = {
    "brief": "Provide a concise 2-3 sentence summary of this video transcript.",

    "detailed": """Analyze this video transcript and provide:
1. A headline summary (1 sentence)
2. Key points (3-5 bullets)
3. Main takeaways
4. Any action items or recommendations mentioned

Format in clean markdown.""",

    "bullets": "Extract the key points from this video transcript as a bulleted list. Focus on actionable insights and main ideas.",

    "newsletter": """You are helping Ed extract newsletter content from this video.

Analyze this transcript and provide:
1. **Hook** - A compelling opening line that would grab readers
2. **Core Insight** - The main lesson or framework from this video
3. **Story Beats** - Key moments that could become anecdotes
4. **Takeaways** - 3-5 actionable points for readers
5. **Newsletter Angle** - How Ed could teach this in The Little Blue Report

Write in Ed's voice: conversational, first-person, teaching through story."""
}


def summarize_with_claude(
    transcript: str,
    summary_type: str = "detailed",
    api_key: Optional[str] = None
) -> str:
    """
    Send transcript to Claude for summarization.

    Args:
        transcript: The video transcript text
        summary_type: One of "brief", "detailed", "bullets", "newsletter"
        api_key: Anthropic API key (defaults to ANTHROPIC_API_KEY env var)

    Returns:
        The summary text
    """
    key = api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise ValueError("ANTHROPIC_API_KEY not set")

    client = anthropic.Anthropic(api_key=key)
    prompt = SUMMARY_PROMPTS.get(summary_type, SUMMARY_PROMPTS["detailed"])

    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=2000,
        messages=[
            {
                "role": "user",
                "content": f"{prompt}\n\nTranscript:\n{transcript}"
            }
        ]
    )

    return message.content[0].text


def format_for_obsidian(
    video_id: str,
    url: str,
    summary: str,
    transcript: str,
    title: Optional[str] = None
) -> str:
    """
    Format output as Obsidian-compatible markdown with YAML frontmatter.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    date_tag = datetime.now().strftime("%Y-%m-%d")

    display_title = title or f"YouTube Video {video_id}"

    markdown = f"""---
source: YouTube
video_id: {video_id}
url: {url}
processed: {timestamp}
tags: [youtube, video-notes]
---

# {display_title}

**Link**: [{url}]({url})
**Processed**: {timestamp}

## Summary

{summary}

---

## Full Transcript

{transcript}

---

_Generated by youtube-processor skill_
"""
    return markdown


def save_to_obsidian(
    content: str,
    video_id: str,
    vault_path: str = "/Users/eddale/Documents/COPYobsidian/MAGI/Zettelkasten",
    title: Optional[str] = None
) -> str:
    """
    Save markdown to Obsidian vault.

    Returns: Path where file was saved
    """
    if not os.path.exists(vault_path):
        raise ValueError(f"Vault path does not exist: {vault_path}")

    timestamp = datetime.now().strftime("%Y-%m-%d")

    # Clean title for filename
    if title:
        clean_title = re.sub(r'[^\w\s-]', '', title)[:50]
        filename = f"YT - {clean_title} - {timestamp}.md"
    else:
        filename = f"YT - {video_id} - {timestamp}.md"

    filepath = os.path.join(vault_path, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath


def process_video(
    url: str,
    summary_type: str = "detailed",
    save_to_vault: bool = False,
    vault_path: Optional[str] = None
) -> ProcessingResult:
    """
    Full pipeline: URL -> Transcript -> Summary -> Obsidian markdown

    This is the main entry point for both CLI and API usage.
    """
    try:
        # Step 1: Extract video ID
        video_id = extract_video_id(url)

        # Step 2: Get transcript
        transcript, language = get_transcript(video_id)

        # Step 3: Summarize with Claude
        summary = summarize_with_claude(transcript, summary_type)

        # Step 4: Format for Obsidian
        markdown = format_for_obsidian(
            video_id=video_id,
            url=url,
            summary=summary,
            transcript=transcript
        )

        # Step 5: Optionally save
        saved_path = None
        if save_to_vault:
            default_vault = "/Users/eddale/Documents/COPYobsidian/MAGI/Zettelkasten"
            saved_path = save_to_obsidian(
                content=markdown,
                video_id=video_id,
                vault_path=vault_path or default_vault
            )

        return ProcessingResult(
            success=True,
            video_id=video_id,
            transcript=transcript,
            summary=summary,
            markdown_output=markdown,
            saved_to=saved_path
        )

    except ValueError as e:
        return ProcessingResult(
            success=False,
            video_id="unknown",
            error=str(e)
        )
    except Exception as e:
        return ProcessingResult(
            success=False,
            video_id="unknown",
            error=f"Unexpected error: {str(e)}"
        )
