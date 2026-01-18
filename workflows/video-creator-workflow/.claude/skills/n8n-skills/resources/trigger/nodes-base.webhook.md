# Webhook

## Basic Information

- Node Type: `nodes-base.webhook`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Starts the workflow when a webhook is called

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `responseBinaryPropertyName` | string | Yes | `"data"` | Name of the binary property to return |
| `authentication` | options | No | `"none"` | The way to authenticate |
| `path` | string | No | `""` | The path to listen to, dynamic values could be specified by using ':', e.g. 'your-path/:dynamic-value'. If dynamic values are set 'webhookId' would be prepended to path. |
| `httpMethod` | options | No | `"GET"` | The HTTP method to listen to |
| `httpMethod` | multiOptions | No | `["GET","POST"]` | The HTTP methods to listen to |
| `responseMode` | options | No | `"onReceived"` | When and how to respond to the webhook |
| `responseMode` | options | No | `"onReceived"` | When and how to respond to the webhook |
| `responseData` | options | No | `"firstEntryJson"` | What data should be returned. If it should return all items as an array or only the first item as object. |
| `options` | collection | No | `{}` | - |
| `multipleMethods` | boolean | No | `false` | Whether to allow the webhook to listen for multiple HTTP methods |

### Property Details

#### Authentication (`authentication`)

The way to authenticate

Optional values:
- `basicAuth`: Basic Auth
- `headerAuth`: Header Auth
- `jwtAuth`: JWT Auth
- `none`: None

#### HTTP Method (`httpMethod`)

The HTTP method to listen to

Optional values:
- `DELETE`: DELETE
- `GET`: GET
- `HEAD`: HEAD
- `PATCH`: PATCH
- `POST`: POST
- `PUT`: PUT

#### HTTP Methods (`httpMethod`)

The HTTP methods to listen to

Optional values:
- `DELETE`: DELETE
- `GET`: GET
- `HEAD`: HEAD
- `PATCH`: PATCH
- `POST`: POST
- `PUT`: PUT

#### Respond (`responseMode`)

When and how to respond to the webhook

Optional values:
- `onReceived`: Immediately - As soon as this node executes
- `lastNode`: When Last Node Finishes - Returns data of the last-executed node
- `responseNode`: Using 'Respond to Webhook' Node - Response defined in that node

#### Respond (`responseMode`)

When and how to respond to the webhook

Optional values:
- `onReceived`: Immediately - As soon as this node executes
- `lastNode`: When Last Node Finishes - Returns data of the last-executed node
- `responseNode`: Using 'Respond to Webhook' Node - Response defined in that node
- `streaming`: Streaming - Returns data in real time from streaming enabled nodes

#### Response Data (`responseData`)

What data should be returned. If it should return all items as an array or only the first item as object.

Optional values:
- `allEntries`: All Entries - Returns all the entries of the last node. Always returns an array.
- `firstEntryJson`: First Entry JSON - Returns the JSON data of the first entry of the last node. Always returns a JSON object.
- `firstEntryBinary`: First Entry Binary - Returns the binary data of the first entry of the last node. Always returns a binary file.
- `noData`: No Response Body - Returns without a body

#### Options (`options`)

Optional values:
- `undefined`: binaryData - Whether the webhook will receive binary data
- `undefined`: binaryPropertyName - The name of the output field to put any binary file data in. Only relevant if binary data is received.
- `undefined`: ignoreBots - Whether to ignore requests from bots like link previewers and web crawlers
- `undefined`: ipWhitelist - Comma-separated list of allowed IP addresses. Leave empty to allow all IPs.
- `undefined`: noResponseBody - Whether to send any body in the response
- `undefined`: responsePropertyName - Name of the property to return the data of instead of the whole JSON
- `undefined`: binaryPropertyName - If the data gets received via "Form-Data Multipart" it will be the prefix and a number starting with 0 will be attached to it
- `undefined`: rawBody - Raw body (binary)
- `undefined`: rawBody - Whether to return the raw body
- `undefined`: responseCode
- `undefined`: responseContentType - Set a custom content-type to return if another one as the "application/json" should be returned
- `undefined`: responseData - Custom response data to send
- `undefined`: responseHeaders - Add headers to the webhook response

## Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

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
  "name": "Webhook",
  "type": "nodes-base.webhook",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "responseBinaryPropertyName": "data"
  }
}
```
