# Automizy

## Basic Information

- Node Type: `nodes-base.automizy`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Consume Automizy API

## Available Operations

### Create
Create a contact
- Value: `create`

### Delete
Delete a contact
- Value: `delete`

### Get
Get a contact
- Value: `get`

### Get Many
Get many contacts
- Value: `getAll`

### Update
Update a contact
- Value: `update`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `email` | string | Yes | `""` | The email address of the contact |
| `listId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `contactId` | string | Yes | `""` | Can be ID or email |
| `contactId` | string | Yes | `""` | Can be ID or email |
| `listId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `email` | string | Yes | `""` | - |
| `name` | string | Yes | `""` | - |
| `listId` | string | Yes | `""` | - |
| `listId` | string | Yes | `""` | - |
| `listId` | string | Yes | `""` | - |

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
  "name": "Automizy",
  "type": "nodes-base.automizy",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "listId": "",
    "contactId": "",
    "name": ""
  }
}
```

### Create Example
```json
{
  "name": "Automizy",
  "type": "nodes-base.automizy",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "listId": "",
    "contactId": "",
    "name": "",
    "operation": "create"
  }
}
```

### Delete Example
```json
{
  "name": "Automizy",
  "type": "nodes-base.automizy",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "listId": "",
    "contactId": "",
    "name": "",
    "operation": "delete"
  }
}
```
