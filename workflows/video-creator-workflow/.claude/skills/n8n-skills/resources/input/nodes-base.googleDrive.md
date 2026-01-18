# Google Drive

## Basic Information

- Node Type: `nodes-base.googleDrive`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Access data on Google Drive

## Available Operations

### Create
Create a shared drive
- Value: `create`

### Delete
Permanently delete a shared drive
- Value: `deleteDrive`

### Get
Get a shared drive
- Value: `get`

### Get Many
Get the list of shared drives
- Value: `list`

### Update
Update a shared drive
- Value: `update`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `driveId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The shared drive to delete |
| `driveId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The shared drive to get |
| `driveId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The shared drive to update |
| `fileId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The file to copy |
| `driveId` | resourceLocator | Yes | `{"mode":"list","value":"My Drive"}` | The drive where to save the copied file |
| `folderId` | resourceLocator | Yes | `{"mode":"list","value":"root","cachedResultName":"/ (Root folder)"}` | The folder where to save the copied file |
| `fileId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The file to delete |
| `fileId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The file to download |
| `fileId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The file to move |
| `driveId` | resourceLocator | Yes | `{"mode":"list","value":"My Drive"}` | The drive where to move the file |

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
  "name": "Google Drive",
  "type": "nodes-base.googleDrive",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "driveId": {
      "mode": "list",
      "value": "My Drive"
    },
    "fileId": {
      "mode": "list",
      "value": ""
    },
    "folderId": {
      "mode": "list",
      "value": "root",
      "cachedResultName": "/ (Root folder)"
    }
  }
}
```

### Create Example
```json
{
  "name": "Google Drive",
  "type": "nodes-base.googleDrive",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "driveId": {
      "mode": "list",
      "value": "My Drive"
    },
    "fileId": {
      "mode": "list",
      "value": ""
    },
    "folderId": {
      "mode": "list",
      "value": "root",
      "cachedResultName": "/ (Root folder)"
    },
    "operation": "create"
  }
}
```

### Delete Example
```json
{
  "name": "Google Drive",
  "type": "nodes-base.googleDrive",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "driveId": {
      "mode": "list",
      "value": "My Drive"
    },
    "fileId": {
      "mode": "list",
      "value": ""
    },
    "folderId": {
      "mode": "list",
      "value": "root",
      "cachedResultName": "/ (Root folder)"
    },
    "operation": "deleteDrive"
  }
}
```
