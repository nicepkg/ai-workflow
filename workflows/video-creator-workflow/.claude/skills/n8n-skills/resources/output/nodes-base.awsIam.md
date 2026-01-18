# AWS IAM

## Basic Information

- Node Type: `nodes-base.awsIam`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Interacts with Amazon IAM

## Available Operations

### Add to Group
Add an existing user to a group
- Value: `addToGroup`

### Create
Create a new user
- Value: `create`

### Delete
Delete a user
- Value: `delete`

### Get
Retrieve a user
- Value: `get`

### Get Many
Retrieve a list of users
- Value: `getAll`

### Remove From Group
Remove a user from a group
- Value: `removeFromGroup`

### Update
Update a user
- Value: `update`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `user` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the user you want to add to the group |
| `group` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the group you want to add the user to |
| `userName` | string | Yes | `""` | The username of the new user to create |
| `user` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the user you want to delete |
| `user` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the user you want to retrieve |
| `user` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the user you want to update |
| `userName` | string | Yes | `""` | The new name of the user |
| `user` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the user you want to remove from the group |
| `group` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the group you want to remove the user from |
| `groupName` | string | Yes | `""` | The name of the new group to create |

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
  "name": "AWS IAM",
  "type": "nodes-base.awsIam",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "user": {
      "mode": "list",
      "value": ""
    },
    "group": {
      "mode": "list",
      "value": ""
    },
    "userName": "",
    "groupName": ""
  }
}
```

### Add to Group Example
```json
{
  "name": "AWS IAM",
  "type": "nodes-base.awsIam",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "user": {
      "mode": "list",
      "value": ""
    },
    "group": {
      "mode": "list",
      "value": ""
    },
    "userName": "",
    "groupName": "",
    "operation": "addToGroup"
  }
}
```

### Create Example
```json
{
  "name": "AWS IAM",
  "type": "nodes-base.awsIam",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "user": {
      "mode": "list",
      "value": ""
    },
    "group": {
      "mode": "list",
      "value": ""
    },
    "userName": "",
    "groupName": "",
    "operation": "create"
  }
}
```
