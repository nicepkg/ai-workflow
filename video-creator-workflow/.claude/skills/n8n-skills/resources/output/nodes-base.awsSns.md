# AWS SNS

## Basic Information

- Node Type: `nodes-base.awsSns`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Sends data to AWS SNS

## Available Operations

### Create
Create a topic
- Value: `create`

### Delete
Delete a topic
- Value: `delete`

### Publish
Publish a message to a topic
- Value: `publish`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `subject` | string | Yes | `""` | Subject when the message is delivered to email endpoints |
| `message` | string | Yes | `""` | The message you want to send |
| `name` | string | Yes | `""` | - |
| `topic` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `authentication` | options | No | `"iam"` | - |
| `operation` | options | No | `"publish"` | - |
| `options` | collection | No | `{}` | - |

### Property Details

#### Authentication (`authentication`)

Optional values:
- `iam`: AWS (IAM)
- `assumeRole`: AWS (Assume Role)

#### Operation (`operation`)

Optional values:
- `create`: Create - Create a topic
- `delete`: Delete - Delete a topic
- `publish`: Publish - Publish a message to a topic

#### Options (`options`)

Optional values:
- `undefined`: displayName - The display name to use for a topic with SMS subscriptions
- `undefined`: fifoTopic - Whether the topic you want to create is a FIFO (first-in-first-out) topic

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
  "name": "AWS SNS",
  "type": "nodes-base.awsSns",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "subject": "",
    "message": "",
    "name": "",
    "topic": {
      "mode": "list",
      "value": ""
    }
  }
}
```

### Create Example
```json
{
  "name": "AWS SNS",
  "type": "nodes-base.awsSns",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "subject": "",
    "message": "",
    "name": "",
    "topic": {
      "mode": "list",
      "value": ""
    },
    "operation": "create"
  }
}
```

### Delete Example
```json
{
  "name": "AWS SNS",
  "type": "nodes-base.awsSns",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "subject": "",
    "message": "",
    "name": "",
    "topic": {
      "mode": "list",
      "value": ""
    },
    "operation": "delete"
  }
}
```
