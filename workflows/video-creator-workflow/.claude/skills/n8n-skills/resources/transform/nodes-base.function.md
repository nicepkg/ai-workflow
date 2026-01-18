# Function

## Basic Information

- Node Type: `nodes-base.function`
- Category: transform
- Package: n8n-nodes-base

## Description

Run custom function code which gets executed once and allows you to add, remove, change and replace items

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `functionCode` | string | No | `"// Code here will run only once, no matter how many input items there are.\n// More info and help:https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.function/\n// Tip: You can use luxon for dates and $jmespath for querying JSON structures\n\n// Loop over inputs and add a new field called 'myNewField' to the JSON of each one\nfor (item of items) {\n  item.json.myNewField = 1;\n}\n\n// You can write logs to the browser console\nconsole.log('Done!');\n\nreturn items;"` | The JavaScript code to execute |
| `notice` | notice | No | `""` | - |

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
2. HTTP Request - via `main` connection
3. If - via `main` connection
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
  "name": "Function",
  "type": "nodes-base.function",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```
