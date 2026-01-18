# Adalo

## Basic Information

- Node Type: `nodes-base.adalo`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Consume Adalo API

## Available Operations

### Create
Create a row
- Value: `create`

### Delete
Delete a row
- Value: `delete`

### Get
Retrieve a row
- Value: `get`

### Get Many
Retrieve many rows
- Value: `getAll`

### Update
Update a row
- Value: `update`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `collectionId` | string | Yes | `""` | Open your Adalo application and click on the three buttons beside the collection name, then select API Documentation |
| `rowId` | string | Yes | `""` | - |
| `resource` | options | No | `"collection"` | - |
| `operation` | options | No | `"getAll"` | - |
| `dataToSend` | options | No | `"defineBelow"` | Whether to insert the input data this node receives in the new row |
| `fieldsUi` | fixedCollection | No | `{}` | Field must be defined in the collection, otherwise it will be ignored. If field defined in the collection is not set here, it will be set to null. |
| `inputsToIgnore` | string | No | `""` | List of input properties to avoid sending, separated by commas. Leave empty to send all properties. |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `100` | Max number of results to return |

### Property Details

#### Resource (`resource`)

Optional values:
- `collection`: Collection

#### Operation (`operation`)

Optional values:
- `create`: Create - Create a row
- `delete`: Delete - Delete a row
- `get`: Get - Retrieve a row
- `getAll`: Get Many - Retrieve many rows
- `update`: Update - Update a row

#### Data to Send (`dataToSend`)

Whether to insert the input data this node receives in the new row

Optional values:
- `autoMapInputData`: Auto-Map Input Data to Columns - Use when node input properties match destination column names
- `defineBelow`: Define Below for Each Column - Set the value for each destination column

#### Fields to Send (`fieldsUi`)

Field must be defined in the collection, otherwise it will be ignored. If field defined in the collection is not set here, it will be set to null.

Optional values:
- `undefined`: fieldValues

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
  "name": "Adalo",
  "type": "nodes-base.adalo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "collectionId": "",
    "rowId": ""
  }
}
```

### Create Example
```json
{
  "name": "Adalo",
  "type": "nodes-base.adalo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "collectionId": "",
    "rowId": "",
    "operation": "create"
  }
}
```

### Delete Example
```json
{
  "name": "Adalo",
  "type": "nodes-base.adalo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "collectionId": "",
    "rowId": "",
    "operation": "delete"
  }
}
```
