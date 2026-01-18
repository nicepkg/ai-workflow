# S3

## Basic Information

- Node Type: `nodes-base.s3`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Sends data to any S3-compatible service

## Available Operations

### Create
Create a bucket
- Value: `create`

### Delete
Delete a bucket
- Value: `delete`

### Get Many
Get many buckets
- Value: `getAll`

### Search
Search within a bucket
- Value: `search`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `name` | string | Yes | `""` | A succinct description of the nature, symptoms, cause, or effect of the bucket |
| `name` | string | Yes | `""` | Name of the AWS S3 bucket to delete |
| `sourcePath` | string | Yes | `""` | The name of the source bucket should start with (/) and key name of the source object, separated by a slash (/) |
| `destinationPath` | string | Yes | `""` | The name of the destination bucket and key name of the destination object, separated by a slash (/) |
| `bucketName` | string | Yes | `""` | - |
| `bucketName` | string | Yes | `""` | - |
| `folderName` | string | Yes | `""` | - |
| `bucketName` | string | Yes | `""` | - |
| `folderKey` | string | Yes | `""` | - |
| `bucketName` | string | Yes | `""` | - |

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
  "name": "S3",
  "type": "nodes-base.s3",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "sourcePath": "",
    "destinationPath": "",
    "bucketName": "",
    "folderName": "",
    "folderKey": ""
  }
}
```

### Create Example
```json
{
  "name": "S3",
  "type": "nodes-base.s3",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "sourcePath": "",
    "destinationPath": "",
    "bucketName": "",
    "folderName": "",
    "folderKey": "",
    "operation": "create"
  }
}
```

### Delete Example
```json
{
  "name": "S3",
  "type": "nodes-base.s3",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "sourcePath": "",
    "destinationPath": "",
    "bucketName": "",
    "folderName": "",
    "folderKey": "",
    "operation": "delete"
  }
}
```
