# Google Sheets

## Basic Information

- Node Type: `nodes-base.googleSheets`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Read, update and write data to Google Sheets

## Available Operations

### Append or Update Row
Append a new row or update an existing one (upsert)
- Value: `appendOrUpdate`

### Append Row
Create a new row in a sheet
- Value: `append`

### Clear
Delete all the contents or a part of a sheet
- Value: `clear`

### Create
Create a new sheet
- Value: `create`

### Delete
Permanently delete a sheet
- Value: `remove`

### Delete Rows or Columns
Delete columns or rows from a sheet
- Value: `delete`

### Get Row(s)
Retrieve one or more rows from a sheet
- Value: `read`

### Update Row
Update an existing row in a sheet
- Value: `update`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `range` | string | Yes | `"A:F"` | The table range to read from or to append data to. See the Google <a href="https://developers.google.com/sheets/api/guides/values#writing">documentation</a> for the details. If it contains multiple sheets it can also be added like this: "MySheet!A:F" |
| `title` | string | Yes | `"n8n-sheet"` | The name of the sheet |
| `documentId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `sheetName` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `documentId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |

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
  "name": "Google Sheets",
  "type": "nodes-base.googleSheets",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "range": "A:F",
    "title": "n8n-sheet",
    "documentId": {
      "mode": "list",
      "value": ""
    },
    "sheetName": {
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

### Append or Update Row Example
```json
{
  "name": "Google Sheets",
  "type": "nodes-base.googleSheets",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "range": "A:F",
    "title": "n8n-sheet",
    "documentId": {
      "mode": "list",
      "value": ""
    },
    "sheetName": {
      "mode": "list",
      "value": ""
    },
    "columns": {
      "mappingMode": "defineBelow",
      "value": null
    },
    "operation": "appendOrUpdate"
  }
}
```

### Append Row Example
```json
{
  "name": "Google Sheets",
  "type": "nodes-base.googleSheets",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "range": "A:F",
    "title": "n8n-sheet",
    "documentId": {
      "mode": "list",
      "value": ""
    },
    "sheetName": {
      "mode": "list",
      "value": ""
    },
    "columns": {
      "mappingMode": "defineBelow",
      "value": null
    },
    "operation": "append"
  }
}
```
