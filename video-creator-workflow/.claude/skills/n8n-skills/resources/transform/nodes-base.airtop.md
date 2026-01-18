# Airtop

## Basic Information

- Node Type: `nodes-base.airtop`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Scrape and control any site with Airtop

## Available Operations

### Run
Run an Airtop agent
- Value: `run`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | URL to load in the window |
| `url` | string | Yes | `""` | URL from where to fetch the file to upload |
| `url` | string | Yes | `""` | URL to load in the window |
| `scrollingMode` | options | Yes | `"automatic"` | Choose the mode of scrolling |
| `webhookUrl` | string | Yes | `""` | Webhook URL to invoke the Airtop agent. Visit <a href="https://portal.airtop.ai/agents" target="\_blank">Airtop Agents</a> for more information. |
| `agentParameters` | json | Yes | `"{}"` | Agent's input parameters in JSON format. Visit <a href="https://portal.airtop.ai/agents" target="\_blank">Airtop Agents</a> for more information. |
| `sessionId` | string | Yes | `"={{ $json[\"sessionId\"] }}"` | The ID of the <a href="https://docs.airtop.ai/guides/how-to/creating-a-session" target="\_blank">Session</a> to use |
| `profileName` | string | Yes | `""` | The name of the <a href="https://docs.airtop.ai/guides/how-to/saving-a-profile" target="\_blank">Profile</a> to save |
| `sessionId` | string | Yes | `"={{ $json[\"sessionId\"] }}"` | The ID of the <a href="https://docs.airtop.ai/guides/how-to/creating-a-session" target="\_blank">Session</a> to use |
| `sessionId` | string | Yes | `"={{ $json[\"sessionId\"] }}"` | The ID of the <a href="https://docs.airtop.ai/guides/how-to/creating-a-session" target="\_blank">Session</a> to use |

### Property Details

#### Scroll Mode (`scrollingMode`)

Choose the mode of scrolling

Optional values:
- `automatic`: Automatic - Describe with natural language the element to scroll to
- `manual`: Manual - Define the direction and amount to scroll by

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
  "name": "Airtop",
  "type": "nodes-base.airtop",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "scrollingMode": "automatic",
    "webhookUrl": "",
    "agentParameters": "{}",
    "sessionId": "={{ $json[\"sessionId\"] }}",
    "profileName": ""
  }
}
```

### Run Example
```json
{
  "name": "Airtop",
  "type": "nodes-base.airtop",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "scrollingMode": "automatic",
    "webhookUrl": "",
    "agentParameters": "{}",
    "sessionId": "={{ $json[\"sessionId\"] }}",
    "profileName": "",
    "operation": "run"
  }
}
```
