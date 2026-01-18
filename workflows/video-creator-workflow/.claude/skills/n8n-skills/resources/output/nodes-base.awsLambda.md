# AWS Lambda

## Basic Information

- Node Type: `nodes-base.awsLambda`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Invoke functions on AWS Lambda

## Available Operations

### Invoke
Invoke a function
- Value: `invoke`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `function` | options | Yes | `""` | The function you want to invoke. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `qualifier` | string | Yes | `"$LATEST"` | Specify a version or alias to invoke a published version of the function |
| `authentication` | options | No | `"iam"` | - |
| `operation` | options | No | `"invoke"` | - |
| `invocationType` | options | No | `"RequestResponse"` | Specify if the workflow should wait for the function to return the results |
| `payload` | string | No | `""` | The JSON that you want to provide to your Lambda function as input |

### Property Details

#### Authentication (`authentication`)

Optional values:
- `iam`: AWS (IAM)
- `assumeRole`: AWS (Assume Role)

#### Operation (`operation`)

Optional values:
- `invoke`: Invoke - Invoke a function

#### Invocation Type (`invocationType`)

Specify if the workflow should wait for the function to return the results

Optional values:
- `RequestResponse`: Wait for Results - Invoke the function synchronously and wait for the response
- `Event`: Continue Workflow - Invoke the function and immediately continue the workflow

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
  "name": "AWS Lambda",
  "type": "nodes-base.awsLambda",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "function": "",
    "qualifier": "$LATEST"
  }
}
```

### Invoke Example
```json
{
  "name": "AWS Lambda",
  "type": "nodes-base.awsLambda",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "function": "",
    "qualifier": "$LATEST",
    "operation": "invoke"
  }
}
```
