# n8n-nodes-chatwoot

## Basic Information

- Package: `n8n-nodes-chatwoot`
- Category: 💬 Communication & Messaging
- Version: 0.1.40
- Maintainer: hugodeco
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-chatwoot)
- Repository: [View Source](https://github.com/sufficit/n8n-nodes-chatwoot)

## Description

This is an n8n community node. It lets you use ChatWoot in your n8n workflows.

## Installation

```
n8n-nodes-chatwoot
```

## Nodes (1)

### ChatWoot

- Node Type: `n8n-nodes-chatwoot.chatwoot`
- Version: 1
- Requires Credentials: Yes

Consume ChatWoot API

#### Available Operations

- **Information** (`accountInformation`)
  Get details about an account

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `authentication` | options | Yes | `"parametersCredentialType"` |
| `resource` | options | Yes | `"public"` |
| `baseUrl` | string | Yes | `""` |
| `accessToken` | string | Yes | `""` |
| `contactSearchQuery` | string | Yes | `""` |
| `contactId` | number | Yes | `""` |
| `inboxIdentifier` | string | Yes | `""` |
| `conversationId` | string | Yes | `""` |
| `operation` | options | No | `"accountInformation"` |
| `operation` | options | No | `"contactDetails"` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "ChatWoot",
  "type": "n8n-nodes-chatwoot.chatwoot",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "authentication": "parametersCredentialType",
    "resource": "public",
    "baseUrl": "",
    "accessToken": "",
    "contactSearchQuery": "",
    "operation": "accountInformation"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
