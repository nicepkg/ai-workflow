# AWS SNS Trigger

## Basic Information

- Node Type: `nodes-base.awsSnsTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Handle AWS SNS events via webhooks

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `topic` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `authentication` | options | No | `"iam"` | - |

### Property Details

#### Authentication (`authentication`)

Optional values:
- `iam`: AWS (IAM)
- `assumeRole`: AWS (Assume Role)

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
  "name": "AWS SNS Trigger",
  "type": "nodes-base.awsSnsTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "topic": {
      "mode": "list",
      "value": ""
    }
  }
}
```
