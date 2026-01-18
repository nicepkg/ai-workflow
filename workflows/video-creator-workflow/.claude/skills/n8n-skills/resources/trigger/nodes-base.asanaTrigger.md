# Asana Trigger

## Basic Information

- Node Type: `nodes-base.asanaTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Starts the workflow when Asana events occur.

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | string | Yes | `""` | The resource ID to subscribe to. The resource can be a task or project. |
| `authentication` | options | No | `"accessToken"` | - |
| `workspace` | options | No | `""` | The workspace ID the resource is registered under. This is only required if you want to allow overriding existing webhooks. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

### Property Details

#### Authentication (`authentication`)

Optional values:
- `accessToken`: Access Token
- `oAuth2`: OAuth2

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
  "name": "Asana Trigger",
  "type": "nodes-base.asanaTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": ""
  }
}
```
