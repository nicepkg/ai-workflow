# @devlikeapro/n8n-nodes-chatwoot

## Basic Information

- Package: `@devlikeapro/n8n-nodes-chatwoot`
- Category: 💬 Communication & Messaging
- Version: 1.0.2
- Maintainer: devlikeapro
- npm: [View Package](https://www.npmjs.com/package/@devlikeapro/n8n-nodes-chatwoot)
- Repository: [View Source](https://github.com/devlikeapro/n8n-nodes-chatwoot)

## Description

n8n node to connect with ChatWoot

## Installation

```
@devlikeapro/n8n-nodes-chatwoot
```

## Nodes (1)

### ChatWoot

- Node Type: `@devlikeapro/n8n-nodes-chatwoot.chatWoot`
- Version: 1
- Requires Credentials: Yes

Interact with ChatWoot API

#### Available Operations

- **Create An Account** (`Create An Account`)
  Create an Account
- **Get Details Of An Account** (`Get Details Of An Account`)
  Get the details of an account
- **Delete An Account** (`Delete An Account`)
  Delete an Account
- **Update An Account** (`Update An Account`)
  Update an account's attributes

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `role` | options | Yes | `"agent"` |
| `role` | options | Yes | `"agent"` |
| `attribute_model` | options | Yes | `"0"` |
| `status` | options | Yes | `"open"` |
| `priority` | options | Yes | `"urgent"` |
| `metric` | options | Yes | `"conversations_count"` |
| `type` | options | Yes | `"account"` |
| `type` | options | Yes | `"account"` |
| `type` | options | Yes | `"account"` |
| `type` | options | Yes | `"agent"` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "ChatWoot",
  "type": "@devlikeapro/n8n-nodes-chatwoot.chatWoot",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "role": "agent",
    "attribute_model": "0",
    "status": "open",
    "priority": "urgent",
    "operation": "Create An Account"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
