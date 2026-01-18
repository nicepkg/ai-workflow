# @watzon/n8n-nodes-perplexity

## Basic Information

- Package: `@watzon/n8n-nodes-perplexity`
- Category: 🤖 AI & Voice Tools
- Version: 0.5.2
- Maintainer: watzon
- npm: [View Package](https://www.npmjs.com/package/@watzon/n8n-nodes-perplexity)
- Repository: [View Source](https://github.com/watzon/n8n-nodes-perplexity)

## Description

n8n node to interact with the Perplexity AI API

## Installation

```
@watzon/n8n-nodes-perplexity
```

## Nodes (1)

### Perplexity

- Node Type: `@watzon/n8n-nodes-perplexity.perplexity`
- Version: 1
- Requires Credentials: Yes

Interact with Perplexity AI API

#### Available Operations

- **Chat Completion** (`chatCompletion`)
  Create a chat completion

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `model` | options | Yes | `"sonar"` |
| `operation` | options | No | `"chatCompletion"` |
| `messages` | fixedCollection | No | `{}` |
| `additionalFields` | collection | No | `{}` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Perplexity",
  "type": "@watzon/n8n-nodes-perplexity.perplexity",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "model": "sonar",
    "operation": "chatCompletion"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
