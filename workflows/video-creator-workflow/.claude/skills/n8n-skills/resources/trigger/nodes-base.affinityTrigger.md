# Affinity Trigger

## Basic Information

- Node Type: `nodes-base.affinityTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Handle Affinity events via webhooks

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | Webhook events that will be enabled for that endpoint |

### Property Details

#### Events (`events`)

Webhook events that will be enabled for that endpoint

Optional values:
- `field_value.created`: field_value.created
- `field_value.deleted`: field_value.deleted
- `field_value.updated`: field_value.updated
- `field.created`: field.created
- `field.deleted`: field.deleted
- `field.updated`: field.updated
- `file.created`: file.created
- `file.deleted`: file.deleted
- `list_entry.created`: list_entry.created
- `list_entry.deleted`: list_entry.deleted
- `list.created`: list.created
- `list.deleted`: list.deleted
- `list.updated`: list.updated
- `note.created`: note.created
- `note.deleted`: note.deleted
- `note.updated`: note.updated
- `opportunity.created`: opportunity.created
- `opportunity.deleted`: opportunity.deleted
- `opportunity.updated`: opportunity.updated
- `organization.created`: organization.created
- `organization.deleted`: organization.deleted
- `organization.updated`: organization.updated
- `person.created`: person.created
- `person.deleted`: person.deleted
- `person.updated`: person.updated

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
  "name": "Affinity Trigger",
  "type": "nodes-base.affinityTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```
