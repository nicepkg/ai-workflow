# @apify/n8n-nodes-apify

## Basic Information

- Package: `@apify/n8n-nodes-apify`
- Category: 🔧 Utilities & Tools
- Version: 0.6.4
- Maintainer: apify-service-account
- npm: [View Package](https://www.npmjs.com/package/@apify/n8n-nodes-apify)
- Repository: [View Source](https://github.com/apify/n8n-nodes-apify)

## Description

n8n nodes for Apify

## Installation

```
@apify/n8n-nodes-apify
```

## Nodes (2)

### Apify

- Node Type: `@apify/n8n-nodes-apify.apify`
- Version: 1
- Requires Credentials: Yes

Access Apify tools for web scraping, data extraction, and automation.

#### Available Operations

- **Run an Actor** (`Run actor`)
  Runs an Actor. You can override the Actor’s input configuration by providing a custom body, which will override the prefilled input values.
- **Run an Actor and Get Dataset** (`Run actor and get dataset`)
  Runs an Actor, waits for it to finish, and finally returns the dataset items
- **Scrape Single URL** (`Scrape single URL`)
  Scrape a single URL using the Apify Website Content Crawler Actor and get its content as text, markdown, and HTML
- **Get Last Run** (`Get last run`)
  Retrieves the most recent run of an Actor. This endpoint is useful for quickly accessing the latest run details, including its status and storages, without needing to specify a run ID.

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `actorId` | resourceLocator | Yes | `{"mode":"list","value":""}` |
| `actorId` | resourceLocator | Yes | `{"mode":"list","value":""}` |
| `userActorId` | resourceLocator | Yes | `{"mode":"list","value":""}` |
| `actorTaskId` | resourceLocator | Yes | `{"mode":"list","value":""}` |
| `actorTaskId` | resourceLocator | Yes | `{"mode":"list","value":""}` |
| `userActorId` | resourceLocator | Yes | `{"mode":"list","value":""}` |
| `datasetId` | string | Yes | `""` |
| `storeId` | resourceLocator | Yes | `{"mode":"list","value":""}` |
| `recordKey` | resourceLocator | Yes | `{"mode":"list","value":""}` |
| `runId` | resourceLocator | Yes | `{"mode":"list","value":""}` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Apify",
  "type": "@apify/n8n-nodes-apify.apify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "actorId": {
      "mode": "list",
      "value": ""
    },
    "userActorId": {
      "mode": "list",
      "value": ""
    },
    "actorTaskId": {
      "mode": "list",
      "value": ""
    },
    "operation": "Run actor"
  }
}
```

---

### Apify Trigger

- Node Type: `@apify/n8n-nodes-apify.apifyTrigger`
- Version: 1
- Requires Credentials: Yes

Triggers workflow on Apify Actor or task run events

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `actorId` | resourceLocator | Yes | `{"mode":"list","value":""}` |
| `authentication` | options | No | `"apifyApi"` |
| `resource` | options | No | `"actor"` |
| `actorSource` | options | No | `"recentlyUsed"` |
| `eventType` | multiOptions | No | `["ACTOR.RUN.SUCCEEDED"]` |
| `actorTaskId` | resourceLocator | No | `{"mode":"list","value":""}` |
| `actorSource` | hidden | No | `"recentlyUsed"` |

#### Connection

- Input Types: 
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Apify Trigger",
  "type": "@apify/n8n-nodes-apify.apifyTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "actorId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
