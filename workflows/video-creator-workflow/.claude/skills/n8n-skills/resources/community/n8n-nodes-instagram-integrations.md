# n8n-nodes-instagram-integrations

## Basic Information

- Package: `n8n-nodes-instagram-integrations`
- Category: 🔧 Utilities & Tools
- Version: 1.6.0
- Maintainer: msameim181
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-instagram-integrations)
- Repository: [View Source](https://github.com/Msameim181/n8n-nodes-instagram-integrations)

## Description

N8N nodes for Instagram API integration with OAuth2 authentication

## Installation

```
n8n-nodes-instagram-integrations
```

## Nodes (2)

### Instagram

- Node Type: `n8n-nodes-instagram-integrations.instagram`
- Version: 1
- Requires Credentials: Yes

Send messages and interact with Instagram users via Messaging API

#### Available Operations

- **Delete** (`deleteComment`)
  Delete a comment on your media
- **Get Comments** (`getComments`)
  Get comments on a media post
- **Get Replies** (`getReplies`)
  Get replies to a comment
- **Hide/Unhide** (`toggleVisibility`)
  Hide or unhide a comment
- **Reply** (`replyToComment`)
  Reply to a comment publicly
- **Send Private Reply** (`sendPrivateReply`)
  Send a private DM to a commenter

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `hideAction` | options | Yes | `"hide"` |
| `postMediaType` | options | Yes | `"IMAGE"` |
| `carouselChildren` | fixedCollection | Yes | `{}` |
| `storyMediaType` | options | Yes | `"IMAGE"` |
| `commentMediaId` | string | Yes | `""` |
| `commentId` | string | Yes | `""` |
| `commentId` | string | Yes | `""` |
| `replyMessage` | string | Yes | `""` |
| `commentId` | string | Yes | `""` |
| `privateMessage` | string | Yes | `""` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Instagram",
  "type": "n8n-nodes-instagram-integrations.instagram",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "hideAction": "hide",
    "postMediaType": "IMAGE",
    "carouselChildren": {},
    "storyMediaType": "IMAGE",
    "commentMediaId": "",
    "operation": "deleteComment"
  }
}
```

---

### Instagram Trigger

- Node Type: `n8n-nodes-instagram-integrations.instagramTrigger`
- Version: 1
- Requires Credentials: Yes

Triggers workflow on Instagram webhook events (messages, postbacks, etc.)

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `events` | multiOptions | No | `["messages"]` |
| `ignoreEcho` | boolean | No | `true` |
| `notice` | notice | No | `""` |

#### Connection

- Input Types: 
- Output Types: `main`
- Output Count: 5

#### Example Configuration

```json
{
  "name": "Instagram Trigger",
  "type": "n8n-nodes-instagram-integrations.instagramTrigger",
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
