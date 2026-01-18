# APITemplate.io

## Basic Information

- Node Type: `nodes-base.apiTemplateIo`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Consume the APITemplate.io API

## Available Operations

### Create
- Value: `create`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"get"` | - |
| `imageTemplateId` | options | Yes | `""` | ID of the image template to use. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `pdfTemplateId` | options | Yes | `""` | ID of the PDF template to use. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `binaryProperty` | string | Yes | `"data"` | - |
| `resource` | options | No | `"image"` | - |
| `overridesUi` | fixedCollection | No | `{}` | - |
| `propertiesUi` | fixedCollection | No | `{}` | - |
| `options` | collection | No | `{}` | - |

### Property Details

#### Operation (`operation`)

Optional values:
- `create`: Create

#### Operation (`operation`)

Optional values:
- `create`: Create

#### Operation (`operation`)

Optional values:
- `get`: Get

#### Resource (`resource`)

Optional values:
- `account`: Account
- `image`: Image
- `pdf`: PDF

#### Overrides (`overridesUi`)

Optional values:
- `undefined`: overrideValues

#### Properties (`propertiesUi`)

Optional values:
- `undefined`: propertyValues

#### Options (`options`)

Optional values:
- `undefined`: fileName - The name of the downloaded image/pdf. It has to include the extension. For example: report.pdf

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
  "name": "APITemplate.io",
  "type": "nodes-base.apiTemplateIo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "get",
    "imageTemplateId": "",
    "pdfTemplateId": "",
    "binaryProperty": "data"
  }
}
```

### Create Example
```json
{
  "name": "APITemplate.io",
  "type": "nodes-base.apiTemplateIo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "create",
    "imageTemplateId": "",
    "pdfTemplateId": "",
    "binaryProperty": "data"
  }
}
```
