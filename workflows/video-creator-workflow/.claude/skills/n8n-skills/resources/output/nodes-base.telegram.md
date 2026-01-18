# Telegram

## Basic Information

- Node Type: `nodes-base.telegram`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Sends data to Telegram

## Available Operations

### Get
Get up to date information about a chat
- Value: `get`

### Get Administrators
Get the Administrators of a chat
- Value: `administrators`

### Get Member
Get the member of a chat
- Value: `member`

### Leave
Leave a group, supergroup or channel
- Value: `leave`

### Set Description
Set the description of a chat
- Value: `setDescription`

### Set Title
Set the title of a chat
- Value: `setTitle`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `chatId` | string | Yes | `""` | Unique identifier for the target chat or username, To find your chat ID ask @get\_id\_bot |
| `messageId` | string | Yes | `""` | Unique identifier of the message to delete |
| `messageId` | string | Yes | `""` | Unique identifier of the message to pin or unpin |
| `userId` | string | Yes | `""` | Unique identifier of the target user |
| `description` | string | Yes | `""` | New chat description, 0-255 characters |
| `title` | string | Yes | `""` | New chat title, 1-255 characters |
| `queryId` | string | Yes | `""` | Unique identifier for the query to be answered |
| `queryId` | string | Yes | `""` | Unique identifier for the answered query |
| `results` | string | Yes | `""` | A JSON-serialized array of results for the inline query |
| `fileId` | string | Yes | `""` | The ID of the file |

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
  "name": "Telegram",
  "type": "nodes-base.telegram",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "chatId": "",
    "messageId": "",
    "userId": "",
    "description": "",
    "title": "",
    "queryId": "",
    "results": "",
    "fileId": ""
  }
}
```

### Get Example
```json
{
  "name": "Telegram",
  "type": "nodes-base.telegram",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "chatId": "",
    "messageId": "",
    "userId": "",
    "description": "",
    "title": "",
    "queryId": "",
    "results": "",
    "fileId": "",
    "operation": "get"
  }
}
```

### Get Administrators Example
```json
{
  "name": "Telegram",
  "type": "nodes-base.telegram",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "chatId": "",
    "messageId": "",
    "userId": "",
    "description": "",
    "title": "",
    "queryId": "",
    "results": "",
    "fileId": "",
    "operation": "administrators"
  }
}
```
