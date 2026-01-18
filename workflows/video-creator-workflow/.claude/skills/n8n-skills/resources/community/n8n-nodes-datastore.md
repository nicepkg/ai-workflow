# n8n-nodes-datastore

## Basic Information

- Package: `n8n-nodes-datastore`
- Category: 🔄 Data Processing
- Version: 0.1.18
- Maintainer: korotovsky
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-datastore)
- Repository: [View Source](https://github.com/korotovsky/n8n-nodes-datastore)

## Description

Datastore for n8n within the workflow

## Installation

```
n8n-nodes-datastore
```

## Nodes (1)

### Datastore

- Node Type: `n8n-nodes-datastore.datastore`
- Version: 1

A simple in-memory key-value datastore for sharing data within the n8n instance.

#### Available Operations

- **Set** (`set`)
  Store a value associated with a key
- **Get** (`get`)
  Retrieve a value using its key
- **Clear** (`clear`)
  Remove a specific key-value pair
- **Clear All** (`clearAll`)
  Remove all key-value pairs from the store

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `keyName` | string | Yes | `""` |
| `valueString` | string | Yes | `""` |
| `valueJson` | json | Yes | `""` |
| `operation` | options | No | `"set"` |
| `valueDataType` | options | No | `"string"` |
| `outputForSetClear` | options | No | `"passThrough"` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Datastore",
  "type": "n8n-nodes-datastore.datastore",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "keyName": "",
    "valueString": "",
    "valueJson": "",
    "operation": "set"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
