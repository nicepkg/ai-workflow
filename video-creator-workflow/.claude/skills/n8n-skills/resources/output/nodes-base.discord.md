# Discord

## Basic Information

- Node Type: `nodes-base.discord`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Sends data to Discord

## Available Operations

### Delete
Delete a message in a channel
- Value: `deleteMessage`

### Get
Get a message in a channel
- Value: `get`

### Get Many
Retrieve the latest messages in a channel
- Value: `getAll`

### React with Emoji
React to a message with an emoji
- Value: `react`

### Send
Send a message to a channel, thread, or member
- Value: `send`

### Send and Wait for Response
Send a message and wait for response
- Value: `sendAndWait`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `type` | options | Yes | `"0"` | The type of channel to create |
| `guildId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the server (guild) that your bot is connected to |
| `channelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the channel by name, URL, or ID |
| `channelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the channel by name, URL, or ID |
| `messageId` | string | Yes | `""` | The ID of the message |
| `emoji` | string | Yes | `""` | The emoji you want to react with |
| `channelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the channel by name, URL, or ID |
| `channelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the channel by name, URL, or ID |
| `messageId` | string | Yes | `""` | The ID of the message |
| `channelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the channel by name, URL, or ID |

### Property Details

#### Type (`type`)

The type of channel to create

Optional values:
- `0`: Guild Text
- `2`: Guild Voice
- `4`: Guild Category

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
8. Dropbox - via `main` connection
9. GitHub - via `main` connection
10. Google Drive - via `main` connection
## JSON Configuration Examples

### Basic Configuration
```json
{
  "name": "Discord",
  "type": "nodes-base.discord",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "type": "0",
    "guildId": {
      "mode": "list",
      "value": ""
    },
    "channelId": {
      "mode": "list",
      "value": ""
    },
    "messageId": "",
    "emoji": ""
  }
}
```

### Delete Example
```json
{
  "name": "Discord",
  "type": "nodes-base.discord",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "type": "0",
    "guildId": {
      "mode": "list",
      "value": ""
    },
    "channelId": {
      "mode": "list",
      "value": ""
    },
    "messageId": "",
    "emoji": "",
    "operation": "deleteMessage"
  }
}
```

### Get Example
```json
{
  "name": "Discord",
  "type": "nodes-base.discord",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "type": "0",
    "guildId": {
      "mode": "list",
      "value": ""
    },
    "channelId": {
      "mode": "list",
      "value": ""
    },
    "messageId": "",
    "emoji": "",
    "operation": "get"
  }
}
```
