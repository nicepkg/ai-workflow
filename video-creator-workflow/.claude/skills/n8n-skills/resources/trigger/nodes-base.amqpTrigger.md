# AMQP Trigger

## Basic Information

- Node Type: `nodes-base.amqpTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Listens to AMQP 1.0 Messages

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | - |
| `sink` | string | No | `""` | Name of the queue of topic to listen to |
| `clientname` | string | No | `""` | Leave empty for non-durable topic subscriptions or queues |
| `subscription` | string | No | `""` | Leave empty for non-durable topic subscriptions or queues |

### Property Details

#### Options (`options`)

Optional values:
- `undefined`: containerId - Will be used to pass to the RHEA Backend as container\_id
- `undefined`: jsonConvertByteArrayToString - Whether to convert JSON Body content (\["body"\]\["content"\]) from Byte Array to string. Needed for Azure Service Bus.
- `undefined`: jsonParseBody - Whether to parse the body to an object
- `undefined`: pullMessagesNumber - Number of messages to pull from the bus for every cicle
- `undefined`: onlyBody - Whether to return only the body property
- `undefined`: parallelProcessing - Whether to process messages in parallel
- `undefined`: reconnect - Whether to automatically reconnect if disconnected
- `undefined`: reconnectLimit - Maximum number of reconnect attempts
- `undefined`: sleepTime - Milliseconds to sleep after every cicle

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
  "name": "AMQP Trigger",
  "type": "nodes-base.amqpTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```
