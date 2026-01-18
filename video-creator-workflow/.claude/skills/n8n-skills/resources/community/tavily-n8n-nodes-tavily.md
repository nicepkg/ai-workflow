# @tavily/n8n-nodes-tavily

## Basic Information

- Package: `@tavily/n8n-nodes-tavily`
- Category: 🕷️ Web Scraping & Browser Automation
- Version: 0.2.6
- Maintainer: mayramati
- npm: [View Package](https://www.npmjs.com/package/@tavily/n8n-nodes-tavily)
- Repository: [View Source](https://github.com/tavily-ai/tavily-n8n-node)

## Description

A community node for n8n to integrate Tavily API for web search and content extraction.

## Installation

```
@tavily/n8n-nodes-tavily
```

## Nodes (1)

### Tavily

- Node Type: `@tavily/n8n-nodes-tavily.tavily`
- Version: 1
- Requires Credentials: Yes

Tavily API

#### Available Operations

- **URLs** (`urls`)
  Extract raw content from URLs

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `query` | string | Yes | `""` |
| `url` | string | Yes | `""` |
| `urls` | string | Yes | `[]` |
| `resource` | options | No | `"search"` |
| `operation` | options | No | `"urls"` |
| `operation` | options | No | `"query"` |
| `operation` | options | No | `"url"` |
| `options` | collection | No | `{}` |
| `options` | collection | No | `{}` |
| `options` | collection | No | `{}` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Tavily",
  "type": "@tavily/n8n-nodes-tavily.tavily",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "url": "",
    "urls": [],
    "operation": "urls"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
