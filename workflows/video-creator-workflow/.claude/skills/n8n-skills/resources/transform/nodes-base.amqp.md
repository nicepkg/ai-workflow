# AMQP Sender

## Basic Information

- Node Type: `nodes-base.amqp`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Sends a raw-message via AMQP 1.0, executed once per item

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | - |
| `sink` | string | No | `""` | Name of the queue of topic to publish to |
| `headerParametersJson` | json | No | `""` | Header parameters as JSON (flat object). Sent as application\_properties in amqp-message meta info. |

### Property Details

#### Options (`options`)

Optional values:
- `undefined`: containerId - Will be used to pass to the RHEA Backend as container\_id
- `undefined`: dataAsObject - Whether to send the data as an object
- `undefined`: reconnect - Whether to automatically reconnect if disconnected
- `undefined`: reconnectLimit - Maximum number of reconnect attempts
- `undefined`: sendOnlyProperty - The only property to send. If empty the whole item will be sent.

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
  "name": "AMQP Sender",
  "type": "nodes-base.amqp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```
