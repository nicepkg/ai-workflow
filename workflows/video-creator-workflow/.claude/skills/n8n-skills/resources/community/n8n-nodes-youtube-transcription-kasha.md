# n8n-nodes-youtube-transcription-kasha

## Basic Information

- Package: `n8n-nodes-youtube-transcription-kasha`
- Category: 🔧 Utilities & Tools
- Version: 1.0.1
- Maintainer: briananderson2793
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-youtube-transcription-kasha)
- Repository: [View Source](https://github.com/leonardogrig/n8n-nodes-youtube-transcript)

## Description

A custom n8n node for fetching YouTube video transcripts using the youtube-transcript library.

## Installation

```
n8n-nodes-youtube-transcription-kasha
```

## Nodes (1)

### YouTube Transcript

- Node Type: `n8n-nodes-youtube-transcription-kasha.youtubeTranscripter`
- Version: 1

Fetches the transcript of a YouTube video using the video ID.

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `videoId` | string | Yes | `""` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "YouTube Transcript",
  "type": "n8n-nodes-youtube-transcription-kasha.youtubeTranscripter",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "videoId": ""
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
