# n8n-nodes-elevenlabs

## Basic Information

- Package: `n8n-nodes-elevenlabs`
- Category: 🤖 AI & Voice Tools
- Version: 0.0.6
- Maintainer: n8ninja
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-elevenlabs)
- Repository: [View Source](https://github.com/n8n-ninja/n8n-nodes-elevenlabs)

## Description

Complete implementation of ElevenLabs AI voice generation into n8n workflows.

## Installation

```
n8n-nodes-elevenlabs
```

## Nodes (1)

### ElevenLabs

- Node Type: `n8n-nodes-elevenlabs.elevenLabs`
- Version: 1
- Requires Credentials: Yes

WIP

#### Available Operations

- **Text to Speech** (`text-to-speech`)
  Generate a speech from a text
- **Speech to Speech** (`speech-to-speech`)
  Generate a speech from a speech

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `text` | string | Yes | `"Be good to people!"` |
| `voice_id` | resourceLocator | Yes | `{"mode":"list","value":null}` |
| `gender` | options | Yes | `""` |
| `accent` | options | Yes | `""` |
| `age` | options | Yes | `""` |
| `generated_voice_id` | string | Yes | `""` |
| `voice_id` | resourceLocator | Yes | `{"mode":"list","value":null}` |
| `history_item_id` | string | Yes | `""` |
| `history_item_id` | string | Yes | `""` |
| `resource` | options | No | `"speech"` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "ElevenLabs",
  "type": "n8n-nodes-elevenlabs.elevenLabs",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "text": "Be good to people!",
    "voice_id": {
      "mode": "list",
      "value": null
    },
    "gender": "",
    "accent": "",
    "age": "",
    "operation": "text-to-speech"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
