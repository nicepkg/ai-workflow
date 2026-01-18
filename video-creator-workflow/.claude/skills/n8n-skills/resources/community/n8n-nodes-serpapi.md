# n8n-nodes-serpapi

## Basic Information

- Package: `n8n-nodes-serpapi`
- Category: 🕷️ Web Scraping & Browser Automation
- Version: 0.1.8
- Maintainer: serpapi
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-serpapi)
- Repository: [View Source](https://github.com/serpapi/n8n-nodes-serpapi)

## Description

Official n8n node for SerpApi

## Installation

```
n8n-nodes-serpapi
```

## Nodes (1)

### SerpApi Official

- Node Type: `n8n-nodes-serpapi.serpApi`
- Version: 1
- Requires Credentials: Yes

Get live Google Search data and more from SerpApi's official node

#### Available Operations

- **Amazon Search** (`amazon`)
- **Baidu Search** (`baidu`)
- **Bing Images** (`bing_images`)
- **Bing Search** (`bing`)
- **DuckDuckGo Search** (`duckduckgo`)
- **eBay Search** (`ebay`)
- **Facebook Profile** (`facebook_profile`)
- **Google AI Mode** (`google_ai_mode`)
- **Google AI Overview** (`google_ai_overview`)
- **Google Autocomplete** (`google_autocomplete`)
- ... and 26 more operations

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `url` | string | Yes | `""` |
| `type` | options | Yes | `"search"` |
| `store` | options | Yes | `"apps"` |
| `q` | string | Yes | `"Barista"` |
| `q` | string | Yes | `"coffee"` |
| `q` | string | Yes | `"Coffee"` |
| `q` | string | Yes | `"Coffee"` |
| `product_id` | string | Yes | `""` |
| `q` | string | Yes | `"Coffee"` |
| `q` | string | Yes | `"Coffee"` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "SerpApi Official",
  "type": "n8n-nodes-serpapi.serpApi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "type": "search",
    "store": "apps",
    "q": "coffee",
    "operation": "amazon"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
