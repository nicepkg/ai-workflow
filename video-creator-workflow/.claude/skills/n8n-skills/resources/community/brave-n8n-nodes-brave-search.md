# @brave/n8n-nodes-brave-search

## Basic Information

- Package: `@brave/n8n-nodes-brave-search`
- Category: 🕷️ Web Scraping & Browser Automation
- Version: 1.0.25
- Maintainer: brave.com
- npm: [View Package](https://www.npmjs.com/package/@brave/n8n-nodes-brave-search)
- Repository: [View Source](https://github.com/brave/n8n-nodes-brave-search)

## Description

A n8n node for the Brave Search API

## Installation

```
@brave/n8n-nodes-brave-search
```

## Nodes (1)

### Brave Search

- Node Type: `@brave/n8n-nodes-brave-search.braveSearch`
- Version: 1
- Requires Credentials: Yes

Search the web using Brave Search

#### Available Operations

- **Web Search** (`web`)
  Search the Web
- **News Search** (`news`)
  Search for News
- **Image Search** (`images`)
  Search for Images
- **Video Search** (`videos`)
  Search for Videos
- **Spellcheck** (`spellcheck`)
  Check spelling of a query
- **Suggest** (`suggest`)
  Get suggestions for a query

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `operation` | options | Yes | `"web"` |
| `query` | string | Yes | `""` |
| `query` | string | Yes | `""` |
| `query` | string | Yes | `""` |
| `query` | string | Yes | `""` |
| `query` | string | Yes | `""` |
| `query` | string | Yes | `""` |
| `additionalParameters` | collection | No | `{}` |
| `additionalParameters` | collection | No | `{}` |
| `additionalParameters` | collection | No | `{}` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Brave Search",
  "type": "@brave/n8n-nodes-brave-search.braveSearch",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "web",
    "query": ""
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
