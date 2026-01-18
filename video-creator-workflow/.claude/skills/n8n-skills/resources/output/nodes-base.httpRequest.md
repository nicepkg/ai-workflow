# HTTP Request

## Basic Information

- Node Type: `nodes-base.httpRequest`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Makes an HTTP request and returns the response data

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | The URL to make the request to |
| `nodeCredentialType` | credentialsSelect | Yes | `""` | - |
| `genericAuthType` | credentialsSelect | Yes | `""` | - |
| `method` | options | No | `"GET"` | The request method to use |
| `authentication` | options | No | `"none"` | - |
| `contentType` | options | No | `"json"` | Content-Type to use to send body parameters |
| `specifyBody` | options | No | `"keypair"` | The body can be specified using explicit fields (<code>keypair</code>) or using a JavaScript object (<code>json</code>) |
| `fieldsToInclude` | options | No | `"all"` | What fields response object should include |
| `specifyQuery` | options | No | `"keypair"` | - |
| `queryParameters` | fixedCollection | No | `{"parameters":[{"name":"","value":""}]}` | - |

### Property Details

#### Method (`method`)

The request method to use

Optional values:
- `DELETE`: DELETE
- `GET`: GET
- `HEAD`: HEAD
- `OPTIONS`: OPTIONS
- `PATCH`: PATCH
- `POST`: POST
- `PUT`: PUT

#### Authentication (`authentication`)

Optional values:
- `none`: None
- `predefinedCredentialType`: Predefined Credential Type - We've already implemented auth for many services so that you don't have to set it up manually
- `genericCredentialType`: Generic Credential Type - Fully customizable. Choose between basic, header, OAuth2, etc.

#### Body Content Type (`contentType`)

Content-Type to use to send body parameters

Optional values:
- `form-urlencoded`: Form Urlencoded
- `multipart-form-data`: Form-Data
- `json`: JSON
- `binaryData`: n8n Binary File
- `raw`: Raw

#### Specify Body (`specifyBody`)

The body can be specified using explicit fields (\<code\>keypair\</code\>) or using a JavaScript object (\<code\>json\</code\>)

Optional values:
- `keypair`: Using Fields Below
- `json`: Using JSON

#### Include Fields (`fieldsToInclude`)

What fields response object should include

Optional values:
- `all`: All - Include all fields
- `selected`: Selected - Include only fields specified below
- `except`: Except - Exclude fields specified below

#### Specify Query Parameters (`specifyQuery`)

Optional values:
- `keypair`: Using Fields Below
- `json`: Using JSON

#### Query Parameters (`queryParameters`)

Optional values:
- `undefined`: parameters

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
3. If - via `main` connection
4. Set - via `main` connection
5. Merge - via `main` connection
6. Airtable - via `main` connection
7. Discord - via `main` connection
8. Dropbox - via `main` connection
9. GitHub - via `main` connection
10. Google Drive - via `main` connection
## JSON Configuration Examples

### Basic Configuration
```json
{
  "name": "HTTP Request",
  "type": "nodes-base.httpRequest",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "nodeCredentialType": "",
    "genericAuthType": ""
  }
}
```
