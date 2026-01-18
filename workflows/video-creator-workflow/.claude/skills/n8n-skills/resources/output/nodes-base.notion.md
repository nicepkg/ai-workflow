# Notion

## Basic Information

- Node Type: `nodes-base.notion`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Consume Notion API

## Available Operations

### Append After
Append a block
- Value: `append`

### Get Child Blocks
Get many child blocks
- Value: `getAll`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `blockId` | resourceLocator | Yes | `{"mode":"url","value":""}` | The Notion Block to append blocks to |
| `blockId` | resourceLocator | Yes | `{"mode":"url","value":""}` | The Notion Block to get all children from, when using 'By URL' mode make sure to use the URL of the block itself, you can find it in block parameters in Notion under 'Copy link to block' |
| `blockId` | resourceLocator | Yes | `{"mode":"url","value":""}` | The Notion Block to get all children from |
| `blockId` | resourceLocator | Yes | `{"mode":"url","value":""}` | The Notion Block to get all children from, when using 'By URL' mode make sure to use the URL of the block itself, you can find it in block parameters in Notion under 'Copy link to block' |
| `databaseId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The Notion Database to get |
| `databaseId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The Notion Database to operate on |
| `pageId` | resourceLocator | Yes | `{"mode":"url","value":""}` | The Notion Database Page to update |
| `pageId` | resourceLocator | Yes | `{"mode":"url","value":""}` | The Notion Database Page to get |
| `databaseId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The Notion Database to operate on |
| `pageId` | resourceLocator | Yes | `{"mode":"url","value":""}` | The Notion Page to archive |

## Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
## JSON Configuration Examples

### Basic Configuration
```json
{
  "name": "Notion",
  "type": "nodes-base.notion",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "blockId": {
      "mode": "url",
      "value": ""
    },
    "databaseId": {
      "mode": "list",
      "value": ""
    },
    "pageId": {
      "mode": "url",
      "value": ""
    }
  }
}
```

### Append After Example
```json
{
  "name": "Notion",
  "type": "nodes-base.notion",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "blockId": {
      "mode": "url",
      "value": ""
    },
    "databaseId": {
      "mode": "list",
      "value": ""
    },
    "pageId": {
      "mode": "url",
      "value": ""
    },
    "operation": "append"
  }
}
```

### Get Child Blocks Example
```json
{
  "name": "Notion",
  "type": "nodes-base.notion",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "blockId": {
      "mode": "url",
      "value": ""
    },
    "databaseId": {
      "mode": "list",
      "value": ""
    },
    "pageId": {
      "mode": "url",
      "value": ""
    },
    "operation": "getAll"
  }
}
```
