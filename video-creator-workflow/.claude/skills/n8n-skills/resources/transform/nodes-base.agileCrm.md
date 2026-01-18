# Agile CRM

## Basic Information

- Node Type: `nodes-base.agileCrm`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Consume Agile CRM API

## Available Operations

### Create
Create a new contact
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
Update contact properties
- Value: `update`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `contactId` | string | Yes | `""` | Unique identifier for a particular contact |
| `contactId` | string | Yes | `""` | ID of contact to delete |
| `contactId` | string | Yes | `""` | Unique identifier for a particular contact |
| `companyId` | string | Yes | `""` | Unique identifier for a particular company |
| `companyId` | string | Yes | `""` | ID of company to delete |
| `companyId` | string | Yes | `""` | Unique identifier for a particular company |
| `dealId` | string | Yes | `""` | Unique identifier for a particular deal |
| `closeDate` | dateTime | Yes | `""` | Closing date of deal |
| `expectedValue` | number | Yes | `1` | Expected Value of deal |
| `milestone` | string | Yes | `""` | Milestone of deal |

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
  "name": "Agile CRM",
  "type": "nodes-base.agileCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contactId": "",
    "companyId": "",
    "dealId": "",
    "closeDate": "",
    "expectedValue": 1,
    "milestone": ""
  }
}
```

### Create Example
```json
{
  "name": "Agile CRM",
  "type": "nodes-base.agileCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contactId": "",
    "companyId": "",
    "dealId": "",
    "closeDate": "",
    "expectedValue": 1,
    "milestone": "",
    "operation": "create"
  }
}
```

### Delete Example
```json
{
  "name": "Agile CRM",
  "type": "nodes-base.agileCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contactId": "",
    "companyId": "",
    "dealId": "",
    "closeDate": "",
    "expectedValue": 1,
    "milestone": "",
    "operation": "delete"
  }
}
```
