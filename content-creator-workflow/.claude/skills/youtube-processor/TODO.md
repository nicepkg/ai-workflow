# YouTube Processor - API Deployment TODO

## The Problem

The local skill works perfectly in Claude Code (filesystem access). But Claude.ai and the Mac client can't access local paths - they need an API endpoint.

## Current State

```
✅ Working: Claude Code → runs python3 get_transcript.py → returns transcript
❌ Blocked: Claude.ai/Mac → no filesystem access → can't run local scripts
```

## The Solution: FastAPI on Vercel

Deploy a simple API that Claude.ai can call via WebFetch:

```
Claude.ai → WebFetch → https://your-vercel-app.vercel.app/transcript?url=VIDEO_URL
                                        ↓
                              Returns JSON transcript
```

## Implementation Steps

### 1. Create FastAPI App

```python
# api/main.py
from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi
import re

app = FastAPI()

@app.get("/transcript")
async def get_transcript(url: str):
    """Extract transcript from YouTube URL"""
    # Extract video ID
    video_id = extract_video_id(url)

    # Get transcript
    ytt_api = YouTubeTranscriptApi()
    transcript_data = ytt_api.fetch(video_id)
    full_text = " ".join([item.text for item in transcript_data])

    return {
        "video_id": video_id,
        "transcript": full_text,
        "word_count": len(full_text.split())
    }

@app.get("/health")
async def health():
    return {"status": "ok"}
```

### 2. Vercel Configuration

```json
// vercel.json
{
  "builds": [
    {"src": "api/main.py", "use": "@vercel/python"}
  ],
  "routes": [
    {"src": "/(.*)", "dest": "api/main.py"}
  ]
}
```

### 3. Requirements

```
# requirements.txt
fastapi
youtube-transcript-api>=1.0.0
uvicorn
```

### 4. Deploy to Vercel

```bash
cd skills/youtube-processor
vercel --prod
```

### 5. Update SKILL.md for Claude.ai

Add alternative method for web/Mac clients:

```markdown
### For Claude.ai / Mac Client (API method)

If you don't have filesystem access, use the API:

```
WebFetch: https://youtube-processor.vercel.app/transcript?url=VIDEO_URL
```

Parse the JSON response to get the transcript.
```

## Files to Create

```
skills/youtube-processor/
├── api/
│   └── main.py          # FastAPI app
├── vercel.json          # Vercel config
├── requirements.txt     # Python deps (for Vercel)
└── SKILL.md            # Update with API instructions
```

## Testing Checklist

- [ ] Deploy to Vercel
- [ ] Test `/health` endpoint
- [ ] Test `/transcript?url=https://youtu.be/VIDEO_ID`
- [ ] Test from Claude.ai via WebFetch
- [ ] Update SKILL.md with API endpoint
- [ ] Repackage skill ZIP

## Notes

- No API key needed - youtube-transcript-api is free
- No Claude API needed for transcript extraction (summarization happens in Claude itself)
- Vercel free tier should be fine for personal use
- Consider rate limiting if sharing publicly

## Reference

Ed's Vercel account can host this. Consolidating services on Vercel (per daily note priority).
