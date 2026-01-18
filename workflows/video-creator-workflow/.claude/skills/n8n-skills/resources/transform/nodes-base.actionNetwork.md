# Action Network

## Basic Information

- Node Type: `nodes-base.actionNetwork`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Consume the Action Network API

## Available Operations

### Create
- Value: `create`

### Get
- Value: `get`

### Get Many
- Value: `getAll`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `personId` | string | Yes | `""` | ID of the person to create an attendance for |
| `eventId` | string | Yes | `""` | ID of the event to create an attendance for |
| `eventId` | string | Yes | `""` | ID of the event whose attendance to retrieve |
| `attendanceId` | string | Yes | `""` | ID of the attendance to retrieve |
| `eventId` | string | Yes | `""` | ID of the event to create an attendance for |
| `originSystem` | string | Yes | `""` | Source where the event originated |
| `title` | string | Yes | `""` | Title of the event to create |
| `eventId` | string | Yes | `""` | ID of the event to retrieve |
| `personId` | string | Yes | `""` | ID of the person to retrieve |
| `personId` | string | Yes | `""` | ID of the person to update |

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
  "name": "Action Network",
  "type": "nodes-base.actionNetwork",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "personId": "",
    "eventId": "",
    "attendanceId": "",
    "originSystem": "",
    "title": ""
  }
}
```

### Create Example
```json
{
  "name": "Action Network",
  "type": "nodes-base.actionNetwork",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "personId": "",
    "eventId": "",
    "attendanceId": "",
    "originSystem": "",
    "title": "",
    "operation": "create"
  }
}
```

### Get Example
```json
{
  "name": "Action Network",
  "type": "nodes-base.actionNetwork",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "personId": "",
    "eventId": "",
    "attendanceId": "",
    "originSystem": "",
    "title": "",
    "operation": "get"
  }
}
```
