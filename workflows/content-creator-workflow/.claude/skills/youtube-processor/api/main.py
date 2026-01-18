"""
YouTube Transcript API
FastAPI endpoint for extracting YouTube transcripts.
Deployed on Vercel for Claude.ai/Mac client access.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import re

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable
)

app = FastAPI(
    title="YouTube Transcript API",
    description="Extract transcripts from YouTube videos",
    version="1.0.0"
)

# Allow CORS for web clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


def extract_video_id(url: str) -> str:
    """Extract YouTube video ID from various URL formats."""
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


def get_transcript(video_id: str) -> tuple:
    """Fetch transcript from YouTube video."""
    ytt_api = YouTubeTranscriptApi()

    try:
        transcript_data = ytt_api.fetch(video_id, languages=['en'])
        full_text = " ".join([item.text for item in transcript_data])
        return full_text, 'en'
    except:
        # Fall back to any available transcript
        transcript_list = ytt_api.list(video_id)
        for transcript in transcript_list:
            transcript_data = transcript.fetch()
            full_text = " ".join([item.text for item in transcript_data])
            return full_text, transcript.language_code

    raise ValueError("No transcript found")


@app.get("/")
async def root():
    """Root endpoint with usage info."""
    return {
        "service": "YouTube Transcript API",
        "usage": "GET /transcript?url=YOUTUBE_URL",
        "example": "/transcript?url=https://youtu.be/dQw4w9WgXcQ"
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}


@app.get("/transcript")
async def transcript(url: str):
    """
    Extract transcript from a YouTube video.

    Args:
        url: YouTube video URL (supports youtube.com/watch, youtu.be, embed formats)

    Returns:
        JSON with video_id, language, transcript text, and character count
    """
    try:
        video_id = extract_video_id(url)
        text, language = get_transcript(video_id)

        return {
            "success": True,
            "video_id": video_id,
            "language": language,
            "transcript": text,
            "char_count": len(text),
            "word_count": len(text.split())
        }

    except TranscriptsDisabled:
        raise HTTPException(
            status_code=400,
            detail="Transcripts are disabled for this video"
        )
    except NoTranscriptFound:
        raise HTTPException(
            status_code=404,
            detail="No transcript found for this video"
        )
    except VideoUnavailable:
        raise HTTPException(
            status_code=404,
            detail="Video is unavailable or does not exist"
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
