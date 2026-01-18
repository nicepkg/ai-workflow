# Airtable Trigger

## Basic Information

- Node Type: `nodes-base.airtableTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Starts the workflow when Airtable events occur

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `baseId` | resourceLocator | Yes | `{"mode":"url","value":""}` | The Airtable Base in which to operate on |
| `triggerField` | string | Yes | `""` | A Created Time or Last Modified Time field that will be used to sort records. If you do not have a Created Time or Last Modified Time field in your schema, please create one, because without this field trigger will not work correctly. |
| `downloadFieldNames` | string | Yes | `""` | Name of the fields of type 'attachment' that should be downloaded. Multiple ones can be defined separated by comma. Case sensitive. |
| `tableId` | resourceLocator | Yes | `{"mode":"url","value":""}` | - |
| `authentication` | options | No | `"airtableApi"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `downloadAttachments` | boolean | No | `false` | Whether the attachment fields define in 'Download Fields' will be downloaded |

### Property Details

#### Authentication (`authentication`)

Optional values:
- `airtableApi`: API Key
- `airtableTokenApi`: Access Token
- `airtableOAuth2Api`: OAuth2

#### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: fields - Fields to be included in the response. Multiple ones can be set separated by comma. Example: \<code\>name, id\</code\>. By default just the trigger field will be included.
- `undefined`: formula - Formulas may involve functions, numeric operations, logical operations, and text operations that operate on fields. More info \<a href="https://support.airtable.com/hc/en-us/articles/203255215-Formula-Field-Reference"\>here\</a\>.
- `undefined`: viewId - The name or ID of a view in the table. If set, only the records in that view will be returned.

## Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

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
  "name": "Airtable Trigger",
  "type": "nodes-base.airtableTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "baseId": {
      "mode": "url",
      "value": ""
    },
    "triggerField": "",
    "downloadFieldNames": "",
    "tableId": {
      "mode": "url",
      "value": ""
    }
  }
}
```
