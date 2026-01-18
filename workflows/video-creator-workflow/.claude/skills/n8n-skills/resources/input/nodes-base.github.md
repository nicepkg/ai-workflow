# GitHub

## Basic Information

- Node Type: `nodes-base.github`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Consume GitHub API

## Available Operations

### Get Repositories
Returns all repositories of an organization
- Value: `getRepositories`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `workflowId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The workflow to dispatch |
| `ref` | string | Yes | `"main"` | The git reference for the workflow dispatch (branch or tag name) |
| `ref` | resourceLocator | Yes | `{"mode":"list","value":""}` | The git reference for the workflow dispatch (branch, tag, or commit SHA) |
| `filePath` | string | Yes | `""` | The file path of the file. Has to contain the full path. |
| `binaryData` | boolean | Yes | `false` | Whether the data to upload should be taken from binary field |
| `fileContent` | string | Yes | `""` | The text content of the file |
| `title` | string | Yes | `""` | The title of the issue |
| `issueNumber` | number | Yes | `0` | The number of the issue on which to create the comment on |
| `issueNumber` | number | Yes | `0` | The number of the issue edit |
| `issueNumber` | number | Yes | `0` | The issue number to get data for |

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
10. Google Drive - via `main` connection
## JSON Configuration Examples

### Basic Configuration
```json
{
  "name": "GitHub",
  "type": "nodes-base.github",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workflowId": {
      "mode": "list",
      "value": ""
    },
    "ref": {
      "mode": "list",
      "value": ""
    },
    "filePath": "",
    "binaryData": false,
    "fileContent": "",
    "title": "",
    "issueNumber": 0
  }
}
```

### Get Repositories Example
```json
{
  "name": "GitHub",
  "type": "nodes-base.github",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workflowId": {
      "mode": "list",
      "value": ""
    },
    "ref": {
      "mode": "list",
      "value": ""
    },
    "filePath": "",
    "binaryData": false,
    "fileContent": "",
    "title": "",
    "issueNumber": 0,
    "operation": "getRepositories"
  }
}
```
