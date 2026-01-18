# Code

## Basic Information

- Node Type: `nodes-base.code`
- Category: transform
- Package: n8n-nodes-base

## Description

Run custom JavaScript or Python code

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `mode` | options | No | `"runOnceForAllItems"` | - |
| `language` | options | No | `"javaScript"` | - |
| `jsCode` | string | No | `""` | JavaScript code to execute.<br><br>Tip: You can use luxon vars like <code>$today</code> for dates and <code>$jmespath</code> for querying JSON structures. <a href="https://docs.n8n.io/nodes/n8n-nodes-base.function">Learn more</a>. |
| `jsCode` | string | No | `""` | JavaScript code to execute.<br><br>Tip: You can use luxon vars like <code>$today</code> for dates and <code>$jmespath</code> for querying JSON structures. <a href="https://docs.n8n.io/nodes/n8n-nodes-base.function">Learn more</a>. |
| `jsCode` | string | No | `""` | JavaScript code to execute.<br><br>Tip: You can use luxon vars like <code>$today</code> for dates and <code>$jmespath</code> for querying JSON structures. <a href="https://docs.n8n.io/nodes/n8n-nodes-base.function">Learn more</a>. |
| `jsCode` | string | No | `""` | JavaScript code to execute.<br><br>Tip: You can use luxon vars like <code>$today</code> for dates and <code>$jmespath</code> for querying JSON structures. <a href="https://docs.n8n.io/nodes/n8n-nodes-base.function">Learn more</a>. |
| `pythonCode` | string | No | `""` | Python code to execute.<br><br>Tip: You can use built-in methods and variables like <code>\_today</code> for dates and <code>\_jmespath</code> for querying JSON structures. <a href="https://docs.n8n.io/code/builtin/">Learn more</a>. |
| `pythonCode` | string | No | `""` | Python code to execute.<br><br>Tip: You can use built-in methods and variables like <code>\_today</code> for dates and <code>\_jmespath</code> for querying JSON structures. <a href="https://docs.n8n.io/code/builtin/">Learn more</a>. |
| `language` | hidden | No | `"javaScript"` | - |
| `notice` | notice | No | `""` | - |

### Property Details

#### Mode (`mode`)

Optional values:
- `runOnceForAllItems`: Run Once for All Items - Run this code only once, no matter how many input items there are
- `runOnceForEachItem`: Run Once for Each Item - Run this code as many times as there are input items

#### Language (`language`)

Optional values:
- `javaScript`: JavaScript
- `python`: Python (Beta)
- `pythonNative`: Python (Native) (Beta)

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

1. Function - via `main` connection
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
  "name": "Code",
  "type": "nodes-base.code",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```
