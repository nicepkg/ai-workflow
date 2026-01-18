# n8n-nodes-evolution-api-media-downloader

## Basic Information

- Package: `n8n-nodes-evolution-api-media-downloader`
- Category: 💬 Communication & Messaging
- Version: 0.1.0
- Maintainer: betorcs
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-evolution-api-media-downloader)
- Repository: [View Source](https://github.com/betorcs/n8n-nodes-evolution-api-media-downloader)

## Description

Download Media from Evolution API data message

## Installation

```
n8n-nodes-evolution-api-media-downloader
```

## Nodes (1)

### Evolution Media Downloader

- Node Type: `n8n-nodes-evolution-api-media-downloader.downloadNode`
- Version: 1

Utility node to download media from Evolution API messages

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `data` | json | No | `"{{ $json.body.data }}"` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Evolution Media Downloader",
  "type": "n8n-nodes-evolution-api-media-downloader.downloadNode",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

---

[← Back to Community Nodes Index](README.md)
