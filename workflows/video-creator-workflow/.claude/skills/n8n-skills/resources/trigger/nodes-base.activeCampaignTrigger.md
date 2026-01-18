# ActiveCampaign Trigger

## Basic Information

- Node Type: `nodes-base.activeCampaignTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Handle ActiveCampaign events via webhooks

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `sources` | multiOptions | No | `[]` | - |
| `events` | multiOptions | No | `[]` | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

### Property Details

#### Source (`sources`)

Optional values:
- `public`: Public - Run the hooks when a contact triggers the action
- `admin`: Admin - Run the hooks when an admin user triggers the action
- `api`: Api - Run the hooks when an API call triggers the action
- `system`: System - Run the hooks when automated systems triggers the action

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
  "name": "ActiveCampaign Trigger",
  "type": "nodes-base.activeCampaignTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```
