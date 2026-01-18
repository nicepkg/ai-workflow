# n8n-nodes-globals

## Basic Information

- Package: `n8n-nodes-globals`
- Category: 🔧 Utilities & Tools
- Version: 1.1.0
- Maintainer: umanamente
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-globals)
- Repository: [View Source](https://github.com/umanamente/n8n-nodes-globals)

## Description

N8N community node that allows users to create global constants and use them in all their workflows

## Installation

```
n8n-nodes-globals
```

## Nodes (1)

### Global Constants

- Node Type: `n8n-nodes-globals.globalConstants`
- Version: 1
- Requires Credentials: Yes

Global Constants

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `putAllInOneKey` | boolean | No | `true` |
| `constantsKeyName` | string | No | `"constants"` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Global Constants",
  "type": "n8n-nodes-globals.globalConstants",
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
