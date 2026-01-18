# @mendable/n8n-nodes-firecrawl

## Basic Information

- Package: `@mendable/n8n-nodes-firecrawl`
- Category: 🕷️ Web Scraping & Browser Automation
- Version: 1.0.6
- Maintainer: hello_sideguide
- npm: [View Package](https://www.npmjs.com/package/@mendable/n8n-nodes-firecrawl)
- Repository: [View Source](https://github.com/mendableai/n8n-nodes-firecrawl)

## Description

Firecrawl node for n8n

## Installation

```
@mendable/n8n-nodes-firecrawl
```

## Nodes (1)

### Firecrawl

- Node Type: `@mendable/n8n-nodes-firecrawl.firecrawl`
- Version: 1
- Requires Credentials: Yes

Get data from Firecrawl API

#### Available Operations

- **Search and optionally scrape search results** (`search`)
- **Map a website and get urls** (`map`)
- **Scrape a url and get its content** (`scrape`)
- **Crawl a website** (`crawl`)
- **Batch scrape multiple URLs** (`batchScrape`)
- **Get batch scrape status** (`batchScrapeStatus`)
- **Get batch scrape errors** (`batchScrapeErrors`)
- **List active crawls** (`crawlActive`)
- **Preview crawl params from prompt** (`crawlParamsPreview`)
- **Cancel a crawl job** (`cancelCrawl`)
- ... and 10 more operations

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `query` | string | Yes | `""` |
| `batchId` | string | Yes | `""` |
| `batchId` | string | Yes | `""` |
| `prompt` | string | Yes | `""` |
| `crawlId` | string | Yes | `""` |
| `crawlId` | string | Yes | `""` |
| `batchId` | string | Yes | `""` |
| `crawlId` | string | Yes | `""` |
| `extractId` | string | Yes | `""` |
| `resource` | hidden | No | `"Default"` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Firecrawl",
  "type": "@mendable/n8n-nodes-firecrawl.firecrawl",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "batchId": "",
    "prompt": "",
    "crawlId": "",
    "operation": "search"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
