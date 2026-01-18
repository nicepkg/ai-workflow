# Slack

## Basic Information

- Node Type: `nodes-base.slack`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Consume Slack API

## Available Operations

### Archive
Archives a conversation
- Value: `archive`

### Close
Closes a direct message or multi-person direct message
- Value: `close`

### Create
Initiates a public or private channel-based conversation
- Value: `create`

### Get
Get information about a channel
- Value: `get`

### Get Many
Get many channels in a Slack team
- Value: `getAll`

### History
Get a conversation's history of messages and events
- Value: `history`

### Invite
Invite a user to a channel
- Value: `invite`

### Join
Joins an existing conversation
- Value: `join`

### Kick
Removes a user from a channel
- Value: `kick`

### Leave
Leaves a conversation
- Value: `leave`

### Member
List members of a conversation
- Value: `member`

### Open
Opens or resumes a direct message or multi-person direct message
- Value: `open`

### Rename
Renames a conversation
- Value: `rename`

### Replies
Get a thread of messages posted to a channel
- Value: `replies`

### Set Purpose
Sets the purpose for a conversation
- Value: `setPurpose`

### Set Topic
Sets the topic for a conversation
- Value: `setTopic`

### Unarchive
Unarchives a conversation
- Value: `unarchive`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | The text to search for within messages |
| `channelVisibility` | options | Yes | `"public"` | Whether to create a Public or a Private Slack channel. <a href="https://slack.com/help/articles/360017938993-What-is-a-channel">More info</a>. |
| `target` | options | Yes | `""` | Choose whether to add a star to a message or a file |
| `select` | options | Yes | `""` | - |
| `select` | options | Yes | `""` | - |
| `select` | options | Yes | `"user"` | - |
| `channelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The Slack channel to close |
| `channelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The Slack channel to invite to |
| `userIds` | multiOptions | Yes | `[]` | The ID of the user to invite into channel. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `channelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The Slack channel to get |

### Property Details

#### Channel Visibility (`channelVisibility`)

Whether to create a Public or a Private Slack channel. \<a href="https://slack.com/help/articles/360017938993-What-is-a-channel"\>More info\</a\>.

Optional values:
- `public`: Public Channel
- `private`: Private Channel

#### Item to Add Star (`target`)

Choose whether to add a star to a message or a file

Optional values:
- `message`: Message
- `file`: File

#### Send Message To (`select`)

Optional values:
- `channel`: Channel
- `user`: User

#### Delete Message From (`select`)

Optional values:
- `channel`: Channel
- `user`: User

#### Send Message To (`select`)

Optional values:
- `channel`: Channel
- `user`: User

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
  "name": "Slack",
  "type": "nodes-base.slack",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "channelVisibility": "public",
    "target": "",
    "select": "user",
    "channelId": {
      "mode": "list",
      "value": ""
    },
    "userIds": []
  }
}
```

### Archive Example
```json
{
  "name": "Slack",
  "type": "nodes-base.slack",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "channelVisibility": "public",
    "target": "",
    "select": "user",
    "channelId": {
      "mode": "list",
      "value": ""
    },
    "userIds": [],
    "operation": "archive"
  }
}
```

### Close Example
```json
{
  "name": "Slack",
  "type": "nodes-base.slack",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "channelVisibility": "public",
    "target": "",
    "select": "user",
    "channelId": {
      "mode": "list",
      "value": ""
    },
    "userIds": [],
    "operation": "close"
  }
}
```
