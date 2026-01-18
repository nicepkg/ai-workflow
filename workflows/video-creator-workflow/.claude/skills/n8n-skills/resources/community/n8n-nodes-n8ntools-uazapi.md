# n8n-nodes-n8ntools-uazapi

## Basic Information

- Package: `n8n-nodes-n8ntools-uazapi`
- Category: 💬 Communication & Messaging
- Version: 1.0.5
- Maintainer: n8ntools.oficial
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-n8ntools-uazapi)
- Repository: [View Source](https://github.com/paulocmbraga/n8ntools)

## Description

N8N Tools - Uazapi: Complete Uazapi integration - Premium WhatsApp API with advanced messaging, media handling, and automation features

## Installation

```
n8n-nodes-n8ntools-uazapi
```

## Nodes (1)

### N8N Tools - Uazapi

- Node Type: `n8n-nodes-n8ntools-uazapi.n8nToolsUazapi`
- Version: 1
- Requires Credentials: Yes

Complete Uazapi integration - Premium WhatsApp API with advanced messaging and automation

#### Available Operations

- **Send Text** (`sendText`)
  Send a text message
- **Send Template** (`sendTemplate`)
  Send a WhatsApp template message
- **Send Quick Reply** (`sendQuickReply`)
  Send message with quick reply buttons
- **Send List** (`sendList`)
  Send interactive list message
- **Send Location** (`sendLocation`)
  Send location message
- **Get Messages** (`getMessages`)
  Get message history
- **Mark as Read** (`markAsRead`)
  Mark messages as read

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `phoneNumber` | string | Yes | `""` |
| `messageText` | string | Yes | `""` |
| `messageText` | string | Yes | `""` |
| `messageText` | string | Yes | `""` |
| `latitude` | number | Yes | `0` |
| `longitude` | number | Yes | `0` |
| `mediaUrl` | string | Yes | `""` |
| `groupId` | string | Yes | `""` |
| `groupName` | string | Yes | `""` |
| `webhookUrl` | string | Yes | `""` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "N8N Tools - Uazapi",
  "type": "n8n-nodes-n8ntools-uazapi.n8nToolsUazapi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "phoneNumber": "",
    "messageText": "",
    "latitude": 0,
    "operation": "sendText"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
