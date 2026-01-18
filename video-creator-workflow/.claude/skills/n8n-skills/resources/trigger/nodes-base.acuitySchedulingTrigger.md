# Acuity Scheduling Trigger

## Basic Information

- Node Type: `nodes-base.acuitySchedulingTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Handle Acuity Scheduling events via webhooks

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `""` | - |
| `authentication` | options | No | `"apiKey"` | - |
| `resolveData` | boolean | No | `true` | By default does the webhook-data only contain the ID of the object. If this option gets activated, it will resolve the data automatically. |

### Property Details

#### Event (`event`)

Optional values:
- `appointment.canceled`: appointment.canceled - Is called whenever an appointment is canceled
- `appointment.changed`: appointment.changed - Is called when the appointment is changed in any way
- `appointment.rescheduled`: appointment.rescheduled - Is called when the appointment is rescheduled to a new time
- `appointment.scheduled`: appointment.scheduled - Is called once when an appointment is initially booked
- `order.completed`: order.completed - Is called when an order is completed

#### Authentication (`authentication`)

Optional values:
- `apiKey`: API Key
- `oAuth2`: OAuth2

## Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

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
  "name": "Acuity Scheduling Trigger",
  "type": "nodes-base.acuitySchedulingTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": ""
  }
}
```
