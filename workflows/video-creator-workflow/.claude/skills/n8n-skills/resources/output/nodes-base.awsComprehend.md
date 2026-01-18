# AWS Comprehend

## Basic Information

- Node Type: `nodes-base.awsComprehend`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Sends data to Amazon Comprehend

## Available Operations

### Detect Dominant Language
Identify the dominant language
- Value: `detectDominantLanguage`

### Detect Entities
Inspects text for named entities, and returns information about them
- Value: `detectEntities`

### Detect Sentiment
Analyse the sentiment of the text
- Value: `detectSentiment`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | No | `"text"` | The resource to perform |
| `authentication` | options | No | `"iam"` | - |
| `operation` | options | No | `"detectDominantLanguage"` | - |
| `languageCode` | options | No | `"en"` | The language code for text |
| `additionalFields` | collection | No | `{}` | - |
| `text` | string | No | `""` | The text to send |
| `simple` | boolean | No | `true` | Whether to return a simplified version of the response instead of the raw data |

### Property Details

#### Resource (`resource`)

The resource to perform

Optional values:
- `text`: Text

#### Authentication (`authentication`)

Optional values:
- `iam`: AWS (IAM)
- `assumeRole`: AWS (Assume Role)

#### Operation (`operation`)

Optional values:
- `detectDominantLanguage`: Detect Dominant Language - Identify the dominant language
- `detectEntities`: Detect Entities - Inspects text for named entities, and returns information about them
- `detectSentiment`: Detect Sentiment - Analyse the sentiment of the text

#### Language Code (`languageCode`)

The language code for text

Optional values:
- `ar`: Arabic
- `zh`: Chinese
- `zh-TW`: Chinese (T)
- `en`: English
- `fr`: French
- `de`: German
- `hi`: Hindi
- `it`: Italian
- `ja`: Japanese
- `ko`: Korean
- `pt`: Portuguese
- `es`: Spanish

#### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: endpointArn - The Amazon Resource Name of an endpoint that is associated with a custom entity recognition model

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
  "name": "AWS Comprehend",
  "type": "nodes-base.awsComprehend",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

### Detect Dominant Language Example
```json
{
  "name": "AWS Comprehend",
  "type": "nodes-base.awsComprehend",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "detectDominantLanguage"
  }
}
```

### Detect Entities Example
```json
{
  "name": "AWS Comprehend",
  "type": "nodes-base.awsComprehend",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "detectEntities"
  }
}
```
