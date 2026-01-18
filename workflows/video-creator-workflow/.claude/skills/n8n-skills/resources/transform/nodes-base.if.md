# If

## Basic Information

- Node Type: `nodes-base.if`
- Category: transform
- Package: n8n-nodes-base

## Description

Route items to different branches (true/false)

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | - |
| `looseTypeValidation` | boolean | No | `false` | If the type of an expression doesn't match the type of the comparison, n8n will try to cast the expression to the required type. E.g. for booleans <code>"false"</code> or <code>0</code> will be cast to <code>false</code> |
| `conditions` | filter | No | `{}` | - |

### Property Details

#### Options (`options`)

Optional values:
- `undefined`: ignoreCase - Whether to ignore letter case when evaluating conditions
- `undefined`: looseTypeValidation - If the type of an expression doesn't match the type of the comparison, n8n will try to cast the expression to the required type. E.g. for booleans \<code\>"false"\</code\> or \<code\>0\</code\> will be cast to \<code\>false\</code\>

## Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 2

Output Details:
1. `true` - Output when condition is true
2. `false` - Output when condition is false

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
4. Set - via `main` connection
5. Merge - via `main` connection
6. Airtable - via `main` connection
7. Discord - via `main` connection
8. Dropbox - via `main` connection
9. GitHub - via `main` connection
10. Google Drive - via `main` connection
## JSON Configuration Examples

### Basic Configuration
```json
{
  "name": "If",
  "type": "nodes-base.if",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```
