# Airtable

## Basic Information

- Node Type: `nodes-base.airtable`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Read, update, write and delete data from Airtable

## Available Operations

### Create
Create a new record in a table
- Value: `create`

### Create or Update
Create a new record, or update the current one if it already exists (upsert)
- Value: `upsert`

### Delete
Delete a record from a table
- Value: `deleteRecord`

### Get
Retrieve a record from a table
- Value: `get`

### Search
Search for specific records or list all
- Value: `search`

### Update
Update a record in a table
- Value: `update`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `id` | string | Yes | `""` | ID of the record to delete. <a href="https://support.airtable.com/docs/record-id" target="\_blank">More info</a>. |
| `id` | string | Yes | `""` | ID of the record to get. <a href="https://support.airtable.com/docs/record-id" target="\_blank">More info</a>. |
| `base` | resourceLocator | Yes | `{"mode":"list","value":""}` | The Airtable Base to retrieve the schema from |
| `base` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `table` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `authentication` | options | No | `"airtableTokenApi"` | - |
| `resource` | options | No | `"record"` | - |

### Property Details

#### Authentication (`authentication`)

Optional values:
- `airtableTokenApi`: Access Token
- `airtableOAuth2Api`: OAuth2

#### Resource (`resource`)

Optional values:
- `base`: Base
- `record`: Record

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
7. Discord - via `main` connection
8. Dropbox - via `main` connection
9. GitHub - via `main` connection
10. Google Drive - via `main` connection
## JSON Configuration Examples

### Basic Configuration
```json
{
  "name": "Airtable",
  "type": "nodes-base.airtable",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "id": "",
    "base": {
      "mode": "list",
      "value": ""
    },
    "table": {
      "mode": "list",
      "value": ""
    },
    "columns": {
      "mappingMode": "defineBelow",
      "value": null
    }
  }
}
```

### Create Example
```json
{
  "name": "Airtable",
  "type": "nodes-base.airtable",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "id": "",
    "base": {
      "mode": "list",
      "value": ""
    },
    "table": {
      "mode": "list",
      "value": ""
    },
    "columns": {
      "mappingMode": "defineBelow",
      "value": null
    },
    "operation": "create"
  }
}
```

### Create or Update Example
```json
{
  "name": "Airtable",
  "type": "nodes-base.airtable",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "id": "",
    "base": {
      "mode": "list",
      "value": ""
    },
    "table": {
      "mode": "list",
      "value": ""
    },
    "columns": {
      "mappingMode": "defineBelow",
      "value": null
    },
    "operation": "upsert"
  }
}
```
