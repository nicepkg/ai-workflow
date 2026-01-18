# Gmail

## Basic Information

- Node Type: `nodes-base.gmail`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Consume the Gmail API

## Available Operations

### Create
- Value: `create`

### Delete
- Value: `delete`

### Get
- Value: `get`

### Get Many
- Value: `getAll`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `emailType` | options | Yes | `"text"` | - |
| `emailType` | options | Yes | `"html"` | - |
| `emailType` | options | Yes | `"html"` | - |
| `emailType` | options | Yes | `"text"` | - |
| `name` | string | Yes | `""` | Label Name |
| `labelId` | string | Yes | `""` | The ID of the label |
| `sendTo` | string | Yes | `""` | The email addresses of the recipients. Multiple addresses can be separated by a comma. e.g. jay@getsby.com, jon@smith.com. |
| `labelIds` | multiOptions | Yes | `[]` | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `threadId` | string | Yes | `""` | The ID of the thread you are operating on |
| `labelIds` | multiOptions | Yes | `[]` | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

### Property Details

#### Email Type (`emailType`)

Optional values:
- `html`: HTML
- `text`: Text

#### Email Type (`emailType`)

Optional values:
- `text`: Text
- `html`: HTML

#### Email Type (`emailType`)

Optional values:
- `text`: Text
- `html`: HTML

#### Email Type (`emailType`)

Optional values:
- `text`: Text
- `html`: HTML

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
  "name": "Gmail",
  "type": "nodes-base.gmail",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "emailType": "text",
    "name": "",
    "labelId": "",
    "sendTo": "",
    "labelIds": [],
    "threadId": ""
  }
}
```

### Create Example
```json
{
  "name": "Gmail",
  "type": "nodes-base.gmail",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "emailType": "text",
    "name": "",
    "labelId": "",
    "sendTo": "",
    "labelIds": [],
    "threadId": "",
    "operation": "create"
  }
}
```

### Delete Example
```json
{
  "name": "Gmail",
  "type": "nodes-base.gmail",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "emailType": "text",
    "name": "",
    "labelId": "",
    "sendTo": "",
    "labelIds": [],
    "threadId": "",
    "operation": "delete"
  }
}
```
