# Affinity

## Basic Information

- Node Type: `nodes-base.affinity`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Consume Affinity API

## Available Operations

### Get
Get a list
- Value: `get`

### Get Many
Get many lists
- Value: `getAll`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `listId` | string | Yes | `""` | The unique ID of the list object to be retrieved |
| `listId` | options | Yes | `""` | The unique ID of the list whose list entries are to be retrieved. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `entityId` | string | Yes | `""` | The unique ID of the entity (person, organization, or opportunity) to add to this list |
| `listId` | options | Yes | `""` | The unique ID of the list that contains the specified list\_entry\_id. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `listEntryId` | string | Yes | `""` | The unique ID of the list entry object to be retrieved |
| `listId` | options | Yes | `""` | The unique ID of the list that contains the specified list\_entry\_id. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `listEntryId` | string | Yes | `""` | The unique ID of the list entry object to be deleted |
| `name` | string | Yes | `""` | The name of the organization |
| `domain` | string | Yes | `""` | The domain name of the organization |
| `organizationId` | string | Yes | `""` | Unique identifier for the organization |

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
  "name": "Affinity",
  "type": "nodes-base.affinity",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "listId": "",
    "entityId": "",
    "listEntryId": "",
    "name": "",
    "domain": "",
    "organizationId": ""
  }
}
```

### Get Example
```json
{
  "name": "Affinity",
  "type": "nodes-base.affinity",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "listId": "",
    "entityId": "",
    "listEntryId": "",
    "name": "",
    "domain": "",
    "organizationId": "",
    "operation": "get"
  }
}
```

### Get Many Example
```json
{
  "name": "Affinity",
  "type": "nodes-base.affinity",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "listId": "",
    "entityId": "",
    "listEntryId": "",
    "name": "",
    "domain": "",
    "organizationId": "",
    "operation": "getAll"
  }
}
```
