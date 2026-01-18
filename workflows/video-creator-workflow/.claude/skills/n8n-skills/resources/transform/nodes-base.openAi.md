# OpenAI

## Basic Information

- Node Type: `nodes-base.openAi`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Consume Open AI

## Available Operations

### Complete
Create one or more completions for a given text
- Value: `complete`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | No | `"text"` | - |
| `operation` | options | No | `"complete"` | - |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"complete"` | - |
| `options` | collection | No | `{}` | Additional options to add |
| `responseFormat` | options | No | `"binaryData"` | The format in which to return the image(s) |
| `options` | collection | No | `{}` | Additional options to add |
| `model` | options | No | `"text-davinci-edit-001"` | The model which will generate the edited version. <a href="https://beta.openai.com/docs/models/overview">Learn more</a>. |
| `model` | options | No | `"text-moderation-latest"` | The model which will classify the text. <a href="https://beta.openai.com/docs/models/overview">Learn more</a>. |
| `options` | collection | No | `{}` | Additional options to add |

### Property Details

#### Resource (`resource`)

Optional values:
- `chat`: Chat
- `image`: Image
- `text`: Text

#### Operation (`operation`)

Optional values:
- `complete`: Complete - Create one or more completions for a given text

#### Operation (`operation`)

Optional values:
- `create`: Create - Create an image for a given text

#### Operation (`operation`)

Optional values:
- `complete`: Complete - Create one or more completions for a given text
- `edit`: Edit - Create an edited version for a given text
- `moderate`: Moderate - Classify if a text violates OpenAI's content policy

#### Options (`options`)

Additional options to add

Optional values:
- `undefined`: echo - Whether the prompt should be echo back in addition to the completion
- `undefined`: frequency_penalty - Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim
- `undefined`: maxTokens - The maximum number of tokens to generate in the completion. Most models have a context length of 2048 tokens (except for the newest models, which support 32,768).
- `undefined`: n - How many completions to generate for each prompt. Note: Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for max\_tokens and stop.
- `undefined`: presence_penalty - Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: topP - Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both.

#### Response Format (`responseFormat`)

The format in which to return the image(s)

Optional values:
- `binaryData`: Binary File
- `imageUrl`: Image Url

#### Options (`options`)

Additional options to add

Optional values:
- `undefined`: n - Number of images to generate
- `undefined`: quality
- `undefined`: size
- `undefined`: size
- `undefined`: style

#### Model (`model`)

The model which will generate the edited version. \<a href="https://beta.openai.com/docs/models/overview"\>Learn more\</a\>.

Optional values:
- `code-davinci-edit-001`: code-davinci-edit-001
- `text-davinci-edit-001`: text-davinci-edit-001

#### Model (`model`)

The model which will classify the text. \<a href="https://beta.openai.com/docs/models/overview"\>Learn more\</a\>.

Optional values:
- `text-moderation-stable`: text-moderation-stable
- `text-moderation-latest`: text-moderation-latest

#### Options (`options`)

Additional options to add

Optional values:
- `undefined`: echo - Whether the prompt should be echo back in addition to the completion
- `undefined`: frequency_penalty - Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim
- `undefined`: maxTokens - The maximum number of tokens to generate in the completion. Most models have a context length of 2048 tokens (except for the newest models, which support 32,768).
- `undefined`: n - How many completions to generate for each prompt. Note: Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for max\_tokens and stop.
- `undefined`: presence_penalty - Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: topP - Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both.

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
  "name": "OpenAI",
  "type": "nodes-base.openAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

### Complete Example
```json
{
  "name": "OpenAI",
  "type": "nodes-base.openAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "complete"
  }
}
```
