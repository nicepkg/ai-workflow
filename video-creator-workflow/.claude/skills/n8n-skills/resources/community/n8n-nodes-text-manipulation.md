# n8n-nodes-text-manipulation

## Basic Information

- Package: `n8n-nodes-text-manipulation`
- Category: 🔄 Data Processing
- Version: 1.4.0
- Maintainer: lublak
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-text-manipulation)
- Repository: [View Source](https://github.com/lublak/n8n-nodes-text-manipulation)

## Description

This node allows to modify texts.

## Installation

```
n8n-nodes-text-manipulation
```

## Nodes (1)

### TextManipulation

- Node Type: `n8n-nodes-text-manipulation.textManipulation`
- Version: 1

Allows you to manipulate string values.

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `textsWithManipulations` | fixedCollection | No | `{}` |
| `keepOnlySet` | boolean | No | `false` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "TextManipulation",
  "type": "n8n-nodes-text-manipulation.textManipulation",
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
