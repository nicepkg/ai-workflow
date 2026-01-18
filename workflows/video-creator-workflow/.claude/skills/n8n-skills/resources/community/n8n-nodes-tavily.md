# n8n-nodes-tavily

## Basic Information

- Package: `n8n-nodes-tavily`
- Category: 🤖 AI & Voice Tools
- Version: 0.1.5
- Maintainer: musalabs
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-tavily)
- Repository: [View Source](https://github.com/musa-labs/n8n-nodes-tavily)

## Description

Tavily is a search engine tailored for AI agents, delivering real-time, accurate results, intelligent query suggestions, and in-depth research capabilities.

## Installation

```
n8n-nodes-tavily
```

## Nodes (1)

### Tavily

- Node Type: `n8n-nodes-tavily.tavily`
- Version: 1
- Requires Credentials: Yes

Consume Tavily API

#### Available Operations

- **URLs** (`urls`)
  Extract information from URLs

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `query` | string | Yes | `""` |
| `urls` | string | Yes | `""` |
| `resource` | options | No | `"search"` |
| `operation` | options | No | `"urls"` |
| `operation` | options | No | `"query"` |
| `options` | collection | No | `{}` |
| `options` | collection | No | `{}` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Tavily",
  "type": "n8n-nodes-tavily.tavily",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "urls": "",
    "operation": "urls"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
