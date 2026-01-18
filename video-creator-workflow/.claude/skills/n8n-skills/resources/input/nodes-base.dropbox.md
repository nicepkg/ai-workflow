# Dropbox

## Basic Information

- Node Type: `nodes-base.dropbox`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Access data on Dropbox

## Available Operations

### Copy
Copy a file
- Value: `copy`

### Delete
Delete a file
- Value: `delete`

### Download
Download a file
- Value: `download`

### Move
Move a file
- Value: `move`

### Upload
Upload a file
- Value: `upload`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `path` | string | Yes | `""` | The path of file or folder to copy |
| `path` | string | Yes | `""` | The path to delete. Can be a single file or a whole folder. |
| `path` | string | Yes | `""` | The path of file or folder to move |
| `path` | string | Yes | `""` | The file path of the file to download. Has to contain the full path. |
| `path` | string | Yes | `""` | The file path of the file to upload. Has to contain the full path. The parent folder has to exist. Existing files get overwritten. |
| `query` | string | Yes | `""` | The string to search for. May match across multiple fields based on the request arguments. |
| `path` | string | Yes | `""` | The folder to create. The parent folder has to exist. |
| `toPath` | string | Yes | `""` | The destination path of file or folder |
| `toPath` | string | Yes | `""` | The new path of file or folder |
| `binaryPropertyName` | string | Yes | `"data"` | - |

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
9. GitHub - via `main` connection
10. Google Drive - via `main` connection
## JSON Configuration Examples

### Basic Configuration
```json
{
  "name": "Dropbox",
  "type": "nodes-base.dropbox",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "path": "",
    "query": "",
    "toPath": "",
    "binaryPropertyName": "data"
  }
}
```

### Copy Example
```json
{
  "name": "Dropbox",
  "type": "nodes-base.dropbox",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "path": "",
    "query": "",
    "toPath": "",
    "binaryPropertyName": "data",
    "operation": "copy"
  }
}
```

### Delete Example
```json
{
  "name": "Dropbox",
  "type": "nodes-base.dropbox",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "path": "",
    "query": "",
    "toPath": "",
    "binaryPropertyName": "data",
    "operation": "delete"
  }
}
```
