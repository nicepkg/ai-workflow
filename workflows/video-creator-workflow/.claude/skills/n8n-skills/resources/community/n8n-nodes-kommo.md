# n8n-nodes-kommo

## Basic Information

- Package: `n8n-nodes-kommo`
- Category: 🔧 Utilities & Tools
- Version: 0.0.16
- Maintainer: yatolstoy
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-kommo)
- Repository: [View Source](https://github.com/yatolstoy/n8n-node-kommo)

## Description

n8n node for Kommo Api

## Installation

```
n8n-nodes-kommo
```

## Nodes (1)

### Kommo

- Node Type: `n8n-nodes-kommo.kommo`
- Version: 1
- Requires Credentials: Yes

Consume Kommo API

#### Available Operations

- **Get Info** (`getInfo`)
  Get account info

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `collection` | fixedCollection | Yes | `[]` |
| `collection` | fixedCollection | Yes | `[]` |
| `collection` | fixedCollection | Yes | `[]` |
| `collection` | fixedCollection | Yes | `[]` |
| `collection` | fixedCollection | Yes | `[]` |
| `collection` | fixedCollection | Yes | `[]` |
| `catalog_id` | options | Yes | `""` |
| `catalog_id` | options | Yes | `""` |
| `catalog_id` | options | Yes | `""` |
| `authentication` | options | No | `"oAuth2"` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Kommo",
  "type": "n8n-nodes-kommo.kommo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "collection": [],
    "operation": "getInfo"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
