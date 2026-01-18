# Autopilot

## Basic Information

- Node Type: `nodes-base.autopilot`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Consume Autopilot API

## Available Operations

### Create or Update
Create a new contact, or update the current one if it already exists (upsert)
- Value: `upsert`

### Delete
Delete a contact
- Value: `delete`

### Get
Get a contact
- Value: `get`

### Get Many
Get many contacts
- Value: `getAll`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `email` | string | Yes | `""` | Email address of the contact |
| `contactId` | string | Yes | `""` | Can be ID or email |
| `contactId` | string | Yes | `""` | Can be ID or email |
| `triggerId` | options | Yes | `""` | List ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `contactId` | string | Yes | `""` | Can be ID or email |
| `listId` | options | Yes | `""` | ID of the list to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `contactId` | string | Yes | `""` | Can be ID or email |
| `name` | string | Yes | `""` | Name of the list to create |
| `resource` | options | No | `"contact"` | - |
| `operation` | options | No | `"upsert"` | - |

### Property Details

#### Resource (`resource`)

Optional values:
- `contact`: Contact
- `contactJourney`: Contact Journey
- `contactList`: Contact List
- `list`: List

#### Operation (`operation`)

Optional values:
- `upsert`: Create or Update - Create a new contact, or update the current one if it already exists (upsert)
- `delete`: Delete - Delete a contact
- `get`: Get - Get a contact
- `getAll`: Get Many - Get many contacts

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
  "name": "Autopilot",
  "type": "nodes-base.autopilot",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "contactId": "",
    "triggerId": "",
    "listId": "",
    "name": ""
  }
}
```

### Create or Update Example
```json
{
  "name": "Autopilot",
  "type": "nodes-base.autopilot",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "contactId": "",
    "triggerId": "",
    "listId": "",
    "name": "",
    "operation": "upsert"
  }
}
```

### Delete Example
```json
{
  "name": "Autopilot",
  "type": "nodes-base.autopilot",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "contactId": "",
    "triggerId": "",
    "listId": "",
    "name": "",
    "operation": "delete"
  }
}
```
