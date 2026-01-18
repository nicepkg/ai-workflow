# AI Transform

## Basic Information

- Node Type: `nodes-base.aiTransform`
- Category: transform
- Package: n8n-nodes-base

## Description

Modify data based on instructions written in plain english

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `instructions` | button | No | `""` | Provide instructions on how you want to transform the data, then click 'Generate code'. Use dot notation to refer to nested fields (e.g. address.street). |
| `codeGeneratedForPrompt` | hidden | No | `""` | - |
| `jsCode` | string | No | `""` | - |

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
  "name": "AI Transform",
  "type": "nodes-base.aiTransform",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```
