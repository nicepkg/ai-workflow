# Asana

## Basic Information

- Node Type: `nodes-base.asana`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Consume Asana REST API

## Available Operations

### Create
Create a subtask
- Value: `create`

### Get Many
Get many subtasks
- Value: `getAll`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `taskId` | string | Yes | `""` | The task to operate on |
| `name` | string | Yes | `""` | The name of the subtask to create |
| `taskId` | string | Yes | `""` | The task to operate on |
| `workspace` | options | Yes | `""` | The workspace to create the task in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `name` | string | Yes | `""` | The name of the task to create |
| `id` | string | Yes | `""` | The ID of the task to delete |
| `id` | string | Yes | `""` | The ID of the task to get the data of |
| `id` | string | Yes | `""` | The ID of the task to be moved |
| `projectId` | options | Yes | `""` | Project to show the sections of. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `section` | options | Yes | `""` | The Section to move the task to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

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
  "name": "Asana",
  "type": "nodes-base.asana",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "taskId": "",
    "name": "",
    "workspace": "",
    "id": "",
    "projectId": "",
    "section": ""
  }
}
```

### Create Example
```json
{
  "name": "Asana",
  "type": "nodes-base.asana",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "taskId": "",
    "name": "",
    "workspace": "",
    "id": "",
    "projectId": "",
    "section": "",
    "operation": "create"
  }
}
```

### Get Many Example
```json
{
  "name": "Asana",
  "type": "nodes-base.asana",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "taskId": "",
    "name": "",
    "workspace": "",
    "id": "",
    "projectId": "",
    "section": "",
    "operation": "getAll"
  }
}
```
