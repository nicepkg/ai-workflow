# n8n-nodes-megaapi

## Basic Information

- Package: `n8n-nodes-megaapi`
- Category: 💬 Communication & Messaging
- Version: 1.3.1
- Maintainer: script7sistemas
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-megaapi)
- Repository: [View Source](https://github.com/megaapi/n8n-nodes-megaapi)

## Description

N8N Community Node for MegaAPI WhatsApp automation - Complete WhatsApp integration with messaging, groups, media, and more

## Installation

```
n8n-nodes-megaapi
```

## Nodes (1)

### MegaAPI

- Node Type: `n8n-nodes-megaapi.megaApi`
- Version: 1
- Requires Credentials: Yes

Interact with MegaAPI WhatsApp service

#### Available Operations

- **Delete Message From Me** (`deleteMessageFromMe`)
  Delete a specific message sent by you using message key and timestamp
- **Delete Message** (`deleteMessage`)
  Delete a specific message from the chat
- **Presence Update Chat** (`presenceUpdateChat`)
  Update presence status in a chat (typing, recording, online, etc.)

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `url` | string | Yes | `""` |
| `url` | string | Yes | `""` |
| `option` | options | Yes | `"composing"` |
| `mediaType` | options | Yes | `"document"` |
| `mimeType` | options | Yes | `"application/pdf"` |
| `mediaType` | options | Yes | `"document"` |
| `mimeType` | options | Yes | `"application/pdf"` |
| `messageType` | options | Yes | `"image"` |
| `webhookEnabled` | options | Yes | `true` |
| `chatwootMessageType` | options | Yes | `"incoming"` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "MegaAPI",
  "type": "n8n-nodes-megaapi.megaApi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "option": "composing",
    "mediaType": "document",
    "mimeType": "application/pdf",
    "operation": "deleteMessageFromMe"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
