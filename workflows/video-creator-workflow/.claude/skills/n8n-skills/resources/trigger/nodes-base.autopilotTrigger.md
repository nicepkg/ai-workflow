# Autopilot Trigger

## Basic Information

- Node Type: `nodes-base.autopilotTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Handle Autopilot events via webhooks

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `""` | - |

### Property Details

#### Event (`event`)

Optional values:
- `contactAdded`: Contact Added
- `contactAddedToList`: Contact Added To List
- `contactEnteredSegment`: Contact Entered Segment
- `contactLeftSegment`: Contact Left Segment
- `contactRemovedFromList`: Contact Removed From List
- `contactUnsubscribed`: Contact Unsubscribed
- `contactUpdated`: Contact Updated

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
  "name": "Autopilot Trigger",
  "type": "nodes-base.autopilotTrigger",
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
