# AWS Cognito

## Basic Information

- Node Type: `nodes-base.awsCognito`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Sends data to AWS Cognito

## Available Operations

### Create
Create a new group
- Value: `create`

### Delete
Delete an existing group
- Value: `delete`

### Get
Retrieve details of an existing group
- Value: `get`

### Get Many
Retrieve a list of groups
- Value: `getAll`

### Update
Update an existing group
- Value: `update`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `userAttributes` | fixedCollection | Yes | `{"attributes":[]}` | Attributes to update for the user |
| `userPool` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the user pool to use |
| `newGroupName` | string | Yes | `""` | The name of the new group to create |
| `userPool` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the user pool to use |
| `group` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the group you want to delete |
| `userPool` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the user pool to use |
| `group` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the group you want to retrieve |
| `userPool` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the user pool to use |
| `limit` | number | Yes | `50` | Max number of results to return |
| `userPool` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the user pool to use |

### Property Details

#### User Attributes (`userAttributes`)

Attributes to update for the user

Optional values:
- `undefined`: attributes

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
  "name": "AWS Cognito",
  "type": "nodes-base.awsCognito",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "userAttributes": {
      "attributes": []
    },
    "userPool": {
      "mode": "list",
      "value": ""
    },
    "newGroupName": "",
    "group": {
      "mode": "list",
      "value": ""
    },
    "limit": 50
  }
}
```

### Create Example
```json
{
  "name": "AWS Cognito",
  "type": "nodes-base.awsCognito",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "userAttributes": {
      "attributes": []
    },
    "userPool": {
      "mode": "list",
      "value": ""
    },
    "newGroupName": "",
    "group": {
      "mode": "list",
      "value": ""
    },
    "limit": 50,
    "operation": "create"
  }
}
```

### Delete Example
```json
{
  "name": "AWS Cognito",
  "type": "nodes-base.awsCognito",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "userAttributes": {
      "attributes": []
    },
    "userPool": {
      "mode": "list",
      "value": ""
    },
    "newGroupName": "",
    "group": {
      "mode": "list",
      "value": ""
    },
    "limit": 50,
    "operation": "delete"
  }
}
```
