# @elevenlabs/n8n-nodes-elevenlabs

## Basic Information

- Package: `@elevenlabs/n8n-nodes-elevenlabs`
- Category: 🤖 AI & Voice Tools
- Version: 0.2.2
- Maintainer: angelogiacco11labs
- npm: [View Package](https://www.npmjs.com/package/@elevenlabs/n8n-nodes-elevenlabs)
- Repository: [View Source](https://github.com/elevenlabs/elevenlabs-n8n)

## Description

Official ElevenLabs node for n8n

## Installation

```
@elevenlabs/n8n-nodes-elevenlabs
```

## Nodes (1)

### ElevenLabs

- Node Type: `@elevenlabs/n8n-nodes-elevenlabs.elevenLabs`
- Version: 1
- Requires Credentials: Yes

Interact with ElevenLabs API

#### Available Operations

- **Get** (`get`)
  Returns metadata about a specific voice
- **Get Many** (`getAll`)
  Returns metadata about all voices
- **Create Clone** (`createClone`)
  Create a voice clone from audio files
- **Delete** (`delete`)
  Delete a specific voice

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `voice` | resourceLocator | Yes | `{"mode":"list","value":null}` |
| `voice` | resourceLocator | Yes | `{"mode":"list","value":null}` |
| `text` | string | Yes | `""` |
| `file` | string | Yes | `"data"` |
| `file` | string | Yes | `"data"` |
| `voice` | resourceLocator | Yes | `{"mode":"list","value":null}` |
| `resource` | options | No | `"voice"` |
| `operation` | options | No | `"get"` |
| `operation` | options | No | `"textToSpeech"` |
| `additionalFields` | collection | No | `{}` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "ElevenLabs",
  "type": "@elevenlabs/n8n-nodes-elevenlabs.elevenLabs",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "voice": {
      "mode": "list",
      "value": null
    },
    "text": "",
    "file": "data",
    "operation": "get"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
