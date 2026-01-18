# AWS DynamoDB

## Basic Information

- Node Type: `nodes-base.awsDynamoDb`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Consume the AWS DynamoDB API

## Available Operations

### Create or Update
Create a new record, or update the current one if it already exists (upsert)
- Value: `upsert`

### Delete
Delete an item
- Value: `delete`

### Get
Get an item
- Value: `get`

### Get Many
Get many items
- Value: `getAll`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `eavUi` | fixedCollection | Yes | `{}` | Substitution tokens for attribute names in an expression |
| `tableName` | options | Yes | `[]` | Table to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `keyConditionExpression` | string | Yes | `""` | Condition to determine the items to be retrieved. The condition must perform an equality test on a single partition key value, in this format: <code>partitionKeyName = :partitionkeyval</code> |
| `authentication` | options | No | `"iam"` | - |
| `resource` | options | No | `"item"` | - |
| `operation` | options | No | `"upsert"` | - |
| `dataToSend` | options | No | `"defineBelow"` | Whether to insert the input data this node receives in the new row |
| `returnValues` | options | No | `"NONE"` | Use ReturnValues if you want to get the item attributes as they appeared before they were deleted |
| `keysUi` | fixedCollection | No | `{}` | Item's primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key. |
| `keysUi` | fixedCollection | No | `{}` | Item's primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key. |

### Property Details

#### Expression Attribute Values (`eavUi`)

Substitution tokens for attribute names in an expression

Optional values:
- `undefined`: eavValues

#### Authentication (`authentication`)

Optional values:
- `iam`: AWS (IAM)
- `assumeRole`: AWS (Assume Role)

#### Resource (`resource`)

Optional values:
- `item`: Item

#### Operation (`operation`)

Optional values:
- `upsert`: Create or Update - Create a new record, or update the current one if it already exists (upsert)
- `delete`: Delete - Delete an item
- `get`: Get - Get an item
- `getAll`: Get Many - Get many items

#### Data to Send (`dataToSend`)

Whether to insert the input data this node receives in the new row

Optional values:
- `autoMapInputData`: Auto-Map Input Data to Columns - Use when node input properties match destination column names
- `defineBelow`: Define Below for Each Column - Set the value for each destination column

#### Return (`returnValues`)

Use ReturnValues if you want to get the item attributes as they appeared before they were deleted

Optional values:
- `ALL_OLD`: Attribute Values - The content of the old item is returned
- `NONE`: Nothing - Nothing is returned

#### Keys (`keysUi`)

Item's primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.

Optional values:
- `undefined`: keyValues

#### Keys (`keysUi`)

Item's primary key. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.

Optional values:
- `undefined`: keyValues

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
  "name": "AWS DynamoDB",
  "type": "nodes-base.awsDynamoDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "eavUi": {},
    "tableName": [],
    "keyConditionExpression": ""
  }
}
```

### Create or Update Example
```json
{
  "name": "AWS DynamoDB",
  "type": "nodes-base.awsDynamoDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "eavUi": {},
    "tableName": [],
    "keyConditionExpression": "",
    "operation": "upsert"
  }
}
```

### Delete Example
```json
{
  "name": "AWS DynamoDB",
  "type": "nodes-base.awsDynamoDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "eavUi": {},
    "tableName": [],
    "keyConditionExpression": "",
    "operation": "delete"
  }
}
```
