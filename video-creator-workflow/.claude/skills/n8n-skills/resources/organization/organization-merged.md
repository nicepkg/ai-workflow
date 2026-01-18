# Organization Nodes - Node Collection

This file contains complete information for 4 nodes.

## Table of Contents

- [No Operation, do nothing](#no-operation-do-nothing)
- [Simulate](#simulate)
- [Split In Batches](#split-in-batches)
- [Wait](#wait)

---

## No Operation, do nothing

## Basic Information

- Node Type: `nodes-base.noOp`
- Category: organization
- Package: n8n-nodes-base

### Description

No Operation

### Connection Guide

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
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "No Operation, do nothing",
  "type": "nodes-base.noOp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Simulate

## Basic Information

- Node Type: `nodes-base.simulate`
- Category: organization
- Package: n8n-nodes-base

### Description

Simulate a node

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `output` | options | No | `"all"` | - |
| `icon` | options | No | `"n8n-nodes-base.noOp"` | Select a type of node to show corresponding icon |
| `numberOfItems` | number | No | `1` | Number input of items to return, if greater then input length all items will be returned |
| `executionDuration` | number | No | `150` | Execution duration in milliseconds |
| `subtitle` | string | No | `""` | - |
| `jsonOutput` | json | No | `"[\n  {\n  \"my_field_1\": \"value\",\n  \"my_field_2\": 1\n  }\n]"` | - |

#### Property Details

##### Output (`output`)

Optional values:
- `all`: Returns all input items
- `specify`: Specify how many of input items to return
- `custom`: Specify output as JSON

### Connection Guide

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
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Simulate",
  "type": "nodes-base.simulate",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Split In Batches

## Basic Information

- Node Type: `nodes-base.splitInBatches`
- Category: organization
- Package: n8n-nodes-base

### Description

Split data into batches and iterate over each batch

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | - |
| `batchSize` | number | No | `1` | The number of items to return with each call |
| `splitInBatchesNotice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: reset - Whether the node starts again from the beginning of the input items. This will treat incoming data as a new set rather than continuing with the previous items.

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 2

Output Details:
1. `done` - Output when all batches are processed
2. `loop` - Output for each batch iteration (for looping)

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
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Split In Batches",
  "type": "nodes-base.splitInBatches",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Wait

## Basic Information

- Node Type: `nodes-base.wait`
- Category: organization
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Wait before continue with execution

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `dateTime` | dateTime | Yes | `""` | The date and time to wait for before continuing |
| `formTitle` | string | Yes | `""` | Shown at the top of the form |
| `responseBinaryPropertyName` | string | Yes | `"data"` | Name of the binary property to return |
| `resume` | options | No | `"timeInterval"` | Determines the waiting mode to use before the workflow continues |
| `incomingAuthentication` | options | No | `"none"` | If and how incoming resume-webhook-requests to $execution.resumeFormUrl should be authenticated for additional security |
| `incomingAuthentication` | options | No | `"none"` | If and how incoming resume-webhook-requests to $execution.resumeUrl should be authenticated for additional security |
| `unit` | options | No | `"hours"` | The time unit of the Wait Amount value |
| `unit` | options | No | `"seconds"` | The time unit of the Wait Amount value |
| `responseMode` | options | No | `"onReceived"` | When to respond to the form submission |
| `httpMethod` | options | No | `"GET"` | The HTTP method of the Webhook call |

#### Property Details

##### Resume (`resume`)

Determines the waiting mode to use before the workflow continues

Optional values:
- `timeInterval`: After Time Interval - Waits for a certain amount of time
- `specificTime`: At Specified Time - Waits until a specific date and time to continue
- `webhook`: On Webhook Call - Waits for a webhook call before continuing
- `form`: On Form Submitted - Waits for a form submission before continuing

##### Authentication (`incomingAuthentication`)

If and how incoming resume-webhook-requests to $execution.resumeFormUrl should be authenticated for additional security

Optional values:
- `basicAuth`: Basic Auth
- `none`: None

##### Authentication (`incomingAuthentication`)

If and how incoming resume-webhook-requests to $execution.resumeUrl should be authenticated for additional security

Optional values:
- `basicAuth`: Basic Auth
- `headerAuth`: Header Auth
- `jwtAuth`: JWT Auth
- `none`: None

##### Wait Unit (`unit`)

The time unit of the Wait Amount value

Optional values:
- `seconds`: Seconds
- `minutes`: Minutes
- `hours`: Hours
- `days`: Days

##### Wait Unit (`unit`)

The time unit of the Wait Amount value

Optional values:
- `seconds`: Seconds
- `minutes`: Minutes
- `hours`: Hours
- `days`: Days

##### Respond When (`responseMode`)

When to respond to the form submission

Optional values:
- `onReceived`: Form Is Submitted - As soon as this node receives the form submission
- `lastNode`: Workflow Finishes - When the last node of the workflow is executed
- `responseNode`: Using 'Respond to Webhook' Node - When the 'Respond to Webhook' node is executed

##### HTTP Method (`httpMethod`)

The HTTP method of the Webhook call

Optional values:
- `DELETE`: DELETE
- `GET`: GET
- `HEAD`: HEAD
- `PATCH`: PATCH
- `POST`: POST
- `PUT`: PUT

### Connection Guide

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
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Wait",
  "type": "nodes-base.wait",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dateTime": "",
    "formTitle": "",
    "responseBinaryPropertyName": "data"
  }
}
```
