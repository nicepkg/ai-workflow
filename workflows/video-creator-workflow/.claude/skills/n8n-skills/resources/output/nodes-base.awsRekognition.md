# AWS Rekognition

## Basic Information

- Node Type: `nodes-base.awsRekognition`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Sends data to AWS Rekognition

## Available Operations

### Analyze
- Value: `analyze`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `binaryData` | boolean | Yes | `false` | Whether the image to analyze should be taken from binary field |
| `bucket` | string | Yes | `""` | Name of the S3 bucket |
| `name` | string | Yes | `""` | S3 object key name |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `authentication` | options | No | `"iam"` | - |
| `resource` | options | No | `"image"` | - |
| `operation` | options | No | `"analyze"` | - |
| `type` | options | No | `"detectFaces"` | - |
| `additionalFields` | collection | No | `{}` | - |

### Property Details

#### Authentication (`authentication`)

Optional values:
- `iam`: AWS (IAM)
- `assumeRole`: AWS (Assume Role)

#### Resource (`resource`)

Optional values:
- `image`: Image

#### Operation (`operation`)

Optional values:
- `analyze`: Analyze

#### Type (`type`)

Optional values:
- `detectFaces`: Detect Faces
- `detectLabels`: Detect Labels
- `detectModerationLabels`: Detect Moderation Labels
- `detectText`: Detect Text
- `recognizeCelebrity`: Recognize Celebrity

#### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: regionsOfInterestUi
- `undefined`: version - If the bucket is versioning enabled, you can specify the object version
- `undefined`: wordFilterUi
- `undefined`: maxLabels - Maximum number of labels you want the service to return in the response. The service returns the specified number of highest confidence labels.
- `undefined`: minConfidence - Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn't return any labels with a confidence level lower than this specified value.
- `undefined`: attributes - An array of facial attributes you want to be returned

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
  "name": "AWS Rekognition",
  "type": "nodes-base.awsRekognition",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryData": false,
    "bucket": "",
    "name": "",
    "binaryPropertyName": "data"
  }
}
```

### Analyze Example
```json
{
  "name": "AWS Rekognition",
  "type": "nodes-base.awsRekognition",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryData": false,
    "bucket": "",
    "name": "",
    "binaryPropertyName": "data",
    "operation": "analyze"
  }
}
```
