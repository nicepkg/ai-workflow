# Postgres

## Basic Information

- Node Type: `nodes-base.postgres`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Get, add and update data in Postgres

## Available Operations

### Delete
Delete an entire table or rows in a table
- Value: `deleteTable`

### Execute Query
Execute an SQL query
- Value: `executeQuery`

### Insert
Insert rows in a table
- Value: `insert`

### Insert or Update
Insert or update rows in a table
- Value: `upsert`

### Select
Select rows from a table
- Value: `select`

### Update
Update rows in a table
- Value: `update`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | The SQL query to execute. You can use n8n expressions and $1, $2, $3, etc to refer to the 'Query Parameters' set in options below. |
| `schema` | resourceLocator | Yes | `{"mode":"list","value":"public"}` | The schema that contains the table you want to work on |
| `table` | resourceLocator | Yes | `{"mode":"list","value":""}` | The table you want to work on |
| `columnToMatchOn` | options | Yes | `""` | The column to compare when finding the rows to update. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/" target="\_blank">expression</a>. |
| `columnToMatchOn` | options | Yes | `""` | The column to compare when finding the rows to update. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/" target="\_blank">expression</a>. |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `resource` | hidden | No | `"database"` | - |
| `operation` | options | No | `"insert"` | - |

### Property Details

#### Resource (`resource`)

Optional values:
- `database`: Database

#### Operation (`operation`)

Optional values:
- `deleteTable`: Delete - Delete an entire table or rows in a table
- `executeQuery`: Execute Query - Execute an SQL query
- `insert`: Insert - Insert rows in a table
- `upsert`: Insert or Update - Insert or update rows in a table
- `select`: Select - Select rows from a table
- `update`: Update - Update rows in a table

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
  "name": "Postgres",
  "type": "nodes-base.postgres",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "schema": {
      "mode": "list",
      "value": "public"
    },
    "table": {
      "mode": "list",
      "value": ""
    },
    "columnToMatchOn": "",
    "columns": {
      "mappingMode": "defineBelow",
      "value": null
    }
  }
}
```

### Delete Example
```json
{
  "name": "Postgres",
  "type": "nodes-base.postgres",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "schema": {
      "mode": "list",
      "value": "public"
    },
    "table": {
      "mode": "list",
      "value": ""
    },
    "columnToMatchOn": "",
    "columns": {
      "mappingMode": "defineBelow",
      "value": null
    },
    "operation": "deleteTable"
  }
}
```

### Execute Query Example
```json
{
  "name": "Postgres",
  "type": "nodes-base.postgres",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "schema": {
      "mode": "list",
      "value": "public"
    },
    "table": {
      "mode": "list",
      "value": ""
    },
    "columnToMatchOn": "",
    "columns": {
      "mappingMode": "defineBelow",
      "value": null
    },
    "operation": "executeQuery"
  }
}
```
