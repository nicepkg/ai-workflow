# Output Nodes - Node Collection

This file contains complete information for 84 nodes.

## Table of Contents

- [AWS SES](#aws-ses)
- [AWS SQS](#aws-sqs)
- [AWS Textract](#aws-textract)
- [AWS Transcribe](#aws-transcribe)
- [AwsS3](#awss3)
- [Bannerbear](#bannerbear)
- [Baserow](#baserow)
- [Beeminder](#beeminder)
- [Bitly](#bitly)
- [Brandfetch](#brandfetch)
- [CircleCI](#circleci)
- [Clearbit](#clearbit)
- [ClickUp](#clickup)
- [Cockpit](#cockpit)
- [Coda](#coda)
- [CoinGecko](#coingecko)
- [Customer.io](#customerio)
- [DebugHelper](#debughelper)
- [Demio](#demio)
- [Drift](#drift)
- [E-goi](#e-goi)
- [E2E Test](#e2e-test)
- [ERPNext](#erpnext)
- [Flow](#flow)
- [Freshdesk](#freshdesk)
- [Home Assistant](#home-assistant)
- [HTTP Request Tool](#http-request-tool)
- [HubSpot](#hubspot)
- [Humantic AI](#humantic-ai)
- [Hunter](#hunter)
- [Intercom](#intercom)
- [Invoice Ninja](#invoice-ninja)
- [Jenkins](#jenkins)
- [Jira Software](#jira-software)
- [Linear](#linear)
- [LingvaNex](#lingvanex)
- [Mailchimp](#mailchimp)
- [Mailgun](#mailgun)
- [Mailjet](#mailjet)
- [Mandrill](#mandrill)
- [Markdown](#markdown)
- [Matrix](#matrix)
- [Mattermost](#mattermost)
- [Mautic](#mautic)
- [MCP Client Tool](#mcp-client-tool)
- [Medium](#medium)
- [MessageBird](#messagebird)
- [Monday.com](#mondaycom)
- [Netscaler ADC](#netscaler-adc)
- [OpenThesaurus](#openthesaurus)
- [Orbit](#orbit)
- [Oura](#oura)
- [Paddle](#paddle)
- [PagerDuty](#pagerduty)
- [PayPal](#paypal)
- [Peekalink](#peekalink)
- [ProfitWell](#profitwell)
- [QuickChart](#quickchart)
- [RocketChat](#rocketchat)
- [Salesforce](#salesforce)
- [Salesmate](#salesmate)
- [SeaTable](#seatable)
- [Segment](#segment)
- [Send Email](#send-email)
- [Sentry.io](#sentryio)
- [ServiceNow](#servicenow)
- [Shopify](#shopify)
- [Spontit](#spontit)
- [Storyblok](#storyblok)
- [SyncroMSP](#syncromsp)
- [Todoist](#todoist)
- [TravisCI](#travisci)
- [Uplead](#uplead)
- [uProc](#uproc)
- [UptimeRobot](#uptimerobot)
- [Vero](#vero)
- [WhatsApp Business Cloud](#whatsapp-business-cloud)
- [WooCommerce](#woocommerce)
- [Wordpress](#wordpress)
- [Write Binary File](#write-binary-file)
- [X (Formerly Twitter)](#x-formerly-twitter)
- [Xero](#xero)
- [Zendesk](#zendesk)
- [Zulip](#zulip)

---

## AWS SES

## Basic Information

- Node Type: `nodes-base.awsSes`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Sends data to AWS SES

### Available Operations

### Create
Create a new custom verification email template
- Value: `create`

### Delete
Delete an existing custom verification email template
- Value: `delete`

### Get
Get the custom email verification template
- Value: `get`

### Get Many
Get many of the existing custom verification email templates for your account
- Value: `getAll`

### Send
Add an email address to the list of identities
- Value: `send`

### Update
Update an existing custom verification email template
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `fromEmailAddress` | string | Yes | `""` | The email address that the custom verification email is sent from |
| `templateSubject` | string | Yes | `""` | The subject line of the custom verification email |
| `successRedirectionURL` | string | Yes | `""` | The URL that the recipient of the verification email is sent to if his or her address is successfully verified |
| `failureRedirectionURL` | string | Yes | `""` | The URL that the recipient of the verification email is sent to if his or her address is not successfully verified |
| `email` | string | Yes | `""` | The email address to verify |
| `templateName` | string | Yes | `""` | The name of the custom verification email template to use when sending the verification email |
| `body` | string | Yes | `""` | The message to be sent |
| `fromEmail` | string | Yes | `""` | Email address of the sender |
| `fromEmail` | string | Yes | `""` | Email address of the sender |
| `templateName` | string | Yes | `""` | The name of the template |

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
  "name": "AWS SES",
  "type": "nodes-base.awsSes",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fromEmailAddress": "",
    "templateSubject": "",
    "successRedirectionURL": "",
    "failureRedirectionURL": "",
    "email": "",
    "templateName": "",
    "body": "",
    "fromEmail": ""
  }
}
```

#### Create Example
```json
{
  "name": "AWS SES",
  "type": "nodes-base.awsSes",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fromEmailAddress": "",
    "templateSubject": "",
    "successRedirectionURL": "",
    "failureRedirectionURL": "",
    "email": "",
    "templateName": "",
    "body": "",
    "fromEmail": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "AWS SES",
  "type": "nodes-base.awsSes",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fromEmailAddress": "",
    "templateSubject": "",
    "successRedirectionURL": "",
    "failureRedirectionURL": "",
    "email": "",
    "templateName": "",
    "body": "",
    "fromEmail": "",
    "operation": "delete"
  }
}
```

---

## AWS SQS

## Basic Information

- Node Type: `nodes-base.awsSqs`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Sends messages to AWS SQS

### Available Operations

### Send Message
Send a message to a queue
- Value: `sendMessage`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `queue` | options | Yes | `""` | Queue to send a message to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `message` | string | Yes | `""` | Message to send to the queue |
| `messageGroupId` | string | Yes | `""` | Tag that specifies that a message belongs to a specific message group. Applies only to FIFO (first-in-first-out) queues. |
| `authentication` | options | No | `"iam"` | - |
| `operation` | options | No | `"sendMessage"` | - |
| `queueType` | options | No | `"standard"` | - |
| `options` | collection | No | `{}` | - |
| `sendInputData` | boolean | No | `true` | Whether to send the data the node receives as JSON to SQS |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `iam`: AWS (IAM)
- `assumeRole`: AWS (Assume Role)

##### Operation (`operation`)

Optional values:
- `sendMessage`: Send Message - Send a message to a queue

##### Queue Type (`queueType`)

Optional values:
- `fifo`: FIFO - FIFO SQS queue
- `standard`: Standard - Standard SQS queue

##### Options (`options`)

Optional values:
- `undefined`: delaySeconds - How long, in seconds, to delay a message for
- `undefined`: messageAttributes - Attributes to set
- `undefined`: messageDeduplicationId - Token used for deduplication of sent messages. Applies only to FIFO (first-in-first-out) queues.

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
  "name": "AWS SQS",
  "type": "nodes-base.awsSqs",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "queue": "",
    "message": "",
    "messageGroupId": ""
  }
}
```

#### Send Message Example
```json
{
  "name": "AWS SQS",
  "type": "nodes-base.awsSqs",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "queue": "",
    "message": "",
    "messageGroupId": "",
    "operation": "sendMessage"
  }
}
```

---

## AWS Textract

## Basic Information

- Node Type: `nodes-base.awsTextract`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Sends data to Amazon Textract

### Available Operations

### Analyze Receipt or Invoice
- Value: `analyzeExpense`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `binaryPropertyName` | string | Yes | `"data"` | The name of the input field containing the binary file data to be uploaded. Supported file types: PNG, JPEG. |
| `authentication` | options | No | `"iam"` | - |
| `operation` | options | No | `"analyzeExpense"` | - |
| `simple` | boolean | No | `true` | Whether to return a simplified version of the response instead of the raw data |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `iam`: AWS (IAM)
- `assumeRole`: AWS (Assume Role)

##### Operation (`operation`)

Optional values:
- `analyzeExpense`: Analyze Receipt or Invoice

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
  "name": "AWS Textract",
  "type": "nodes-base.awsTextract",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryPropertyName": "data"
  }
}
```

#### Analyze Receipt or Invoice Example
```json
{
  "name": "AWS Textract",
  "type": "nodes-base.awsTextract",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryPropertyName": "data",
    "operation": "analyzeExpense"
  }
}
```

---

## AWS Transcribe

## Basic Information

- Node Type: `nodes-base.awsTranscribe`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Sends data to AWS Transcribe

### Available Operations

### Create
Create a transcription job
- Value: `create`

### Delete
Delete a transcription job
- Value: `delete`

### Get
Get a transcription job
- Value: `get`

### Get Many
Get many transcription jobs
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | No | `"transcriptionJob"` | - |
| `operation` | options | No | `"create"` | - |
| `languageCode` | options | No | `"en-US"` | Language used in the input media file |
| `options` | collection | No | `{}` | - |
| `filters` | collection | No | `{}` | - |
| `transcriptionJobName` | string | No | `""` | The name of the job |
| `mediaFileUri` | string | No | `""` | The S3 object location of the input media file |
| `detectLanguage` | boolean | No | `false` | Whether to set this field to true to enable automatic language identification |
| `returnTranscript` | boolean | No | `true` | By default, the response only contains metadata about the transcript. Enable this option to retrieve the transcript instead. |
| `simple` | boolean | No | `true` | Whether to return a simplified version of the response instead of the raw data |

#### Property Details

##### Resource (`resource`)

Optional values:
- `transcriptionJob`: Transcription Job

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a transcription job
- `delete`: Delete - Delete a transcription job
- `get`: Get - Get a transcription job
- `getAll`: Get Many - Get many transcription jobs

##### Language (`languageCode`)

Language used in the input media file

Optional values:
- `en-US`: American English
- `en-GB`: British English
- `de-DE`: German
- `en-IN`: Indian English
- `en-IE`: Irish English
- `ru-RU`: Russian
- `es-ES`: Spanish

##### Options (`options`)

Optional values:
- `undefined`: channelIdentification - Instructs Amazon Transcribe to process each audiochannel separately and then merge the transcription output of each channel into a single transcription. You can't set both Max Speaker Labels and Channel Identification in the same request. If you set both, your request returns a BadRequestException.
- `undefined`: maxAlternatives - The number of alternative transcriptions that the service should return
- `undefined`: maxSpeakerLabels - The maximum number of speakers to identify in the input audio. If there are more speakers in the audio than this number, multiple speakers are identified as a single speaker.
- `undefined`: vocabularyName - Name of vocabulary to use when processing the transcription job
- `undefined`: vocabularyFilterName - The name of the vocabulary filter to use when transcribing the audio. The filter that you specify must have the same language code as the transcription job.
- `undefined`: vocabularyFilterMethod - \<p\>Set to mask to remove filtered text from the transcript and replace it with three asterisks ("\*\*\*") as placeholder text.\</p\>\<p\>Set to remove to remove filtered text from the transcript without using placeholder text. Set to tag to mark the word in the transcription output that matches the vocabulary filter. When you set the filter method to tag, the words matching your vocabulary filter are not masked or removed.\</p\>

##### Filters (`filters`)

Optional values:
- `undefined`: jobNameContains - Return only transcription jobs whose name contains the specified string
- `undefined`: status - Return only transcription jobs with the specified status

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
  "name": "AWS Transcribe",
  "type": "nodes-base.awsTranscribe",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Create Example
```json
{
  "name": "AWS Transcribe",
  "type": "nodes-base.awsTranscribe",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "AWS Transcribe",
  "type": "nodes-base.awsTranscribe",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "delete"
  }
}
```

---

## AwsS3

## Basic Information

- Node Type: `nodes-base.awsS3`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Sends data to AWS S3

### Available Operations

### Create
Create a bucket
- Value: `create`

### Delete
Delete a bucket
- Value: `delete`

### Get Many
Get many buckets
- Value: `getAll`

### Search
Search within a bucket
- Value: `search`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `name` | string | Yes | `""` | A succinct description of the nature, symptoms, cause, or effect of the bucket |
| `name` | string | Yes | `""` | Name of the AWS S3 bucket to delete |
| `sourcePath` | string | Yes | `""` | The name of the source bucket should start with (/) and key name of the source object, separated by a slash (/) |
| `destinationPath` | string | Yes | `""` | The name of the destination bucket and key name of the destination object, separated by a slash (/) |
| `bucketName` | string | Yes | `""` | - |
| `bucketName` | string | Yes | `""` | - |
| `folderName` | string | Yes | `""` | - |
| `bucketName` | string | Yes | `""` | - |
| `folderKey` | string | Yes | `""` | - |
| `bucketName` | string | Yes | `""` | - |

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
  "name": "AwsS3",
  "type": "nodes-base.awsS3",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "sourcePath": "",
    "destinationPath": "",
    "bucketName": "",
    "folderName": "",
    "folderKey": ""
  }
}
```

#### Create Example
```json
{
  "name": "AwsS3",
  "type": "nodes-base.awsS3",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "sourcePath": "",
    "destinationPath": "",
    "bucketName": "",
    "folderName": "",
    "folderKey": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "AwsS3",
  "type": "nodes-base.awsS3",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "sourcePath": "",
    "destinationPath": "",
    "bucketName": "",
    "folderName": "",
    "folderKey": "",
    "operation": "delete"
  }
}
```

---

## Bannerbear

## Basic Information

- Node Type: `nodes-base.bannerbear`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Bannerbear API

### Available Operations

### Create
Create an image
- Value: `create`

### Get
Get an image
- Value: `get`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `templateId` | options | Yes | `""` | The template ID you want to use. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `imageId` | string | Yes | `""` | Unique identifier for the image |
| `templateId` | string | Yes | `""` | Unique identifier for the template |
| `resource` | options | No | `"image"` | - |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"get"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `modificationsUi` | fixedCollection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `image`: Image
- `template`: Template

##### Operation (`operation`)

Optional values:
- `create`: Create - Create an image
- `get`: Get - Get an image

##### Operation (`operation`)

Optional values:
- `get`: Get - Get a template
- `getAll`: Get Many - Get many templates

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: metadata - Metadata that you need to store e.g. ID of a record in your DB
- `undefined`: waitForImage - Whether to wait for the image to be proccesed before returning. If after three tries the images is not ready, an error will be thrown. Number of tries can be increased by setting "Wait Max Tries".
- `undefined`: waitForImageMaxTries - How often it should check if the image is available before it fails
- `undefined`: webhookUrl - A URL to POST the Image object to upon rendering completed

##### Modifications (`modificationsUi`)

Optional values:
- `undefined`: modificationsValues

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
  "name": "Bannerbear",
  "type": "nodes-base.bannerbear",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "templateId": "",
    "imageId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Bannerbear",
  "type": "nodes-base.bannerbear",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "templateId": "",
    "imageId": "",
    "operation": "create"
  }
}
```

#### Get Example
```json
{
  "name": "Bannerbear",
  "type": "nodes-base.bannerbear",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "templateId": "",
    "imageId": "",
    "operation": "get"
  }
}
```

---

## Baserow

## Basic Information

- Node Type: `nodes-base.baserow`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Baserow API

### Available Operations

### Create
Create a row
- Value: `create`

### Delete
Delete a row
- Value: `delete`

### Get
Retrieve a row
- Value: `get`

### Get Many
Retrieve many rows
- Value: `getAll`

### Update
Update a row
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `databaseId` | options | Yes | `""` | Database to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `tableId` | options | Yes | `""` | Table to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `rowId` | string | Yes | `""` | ID of the row to return |
| `rowId` | string | Yes | `""` | ID of the row to update |
| `rowId` | string | Yes | `""` | ID of the row to delete |
| `resource` | options | No | `"row"` | - |
| `operation` | options | No | `"getAll"` | - |
| `dataToSend` | options | No | `"defineBelow"` | Whether to insert the input data this node receives in the new row |
| `fieldsUi` | fixedCollection | No | `{}` | - |
| `additionalOptions` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `row`: Row

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a row
- `delete`: Delete - Delete a row
- `get`: Get - Retrieve a row
- `getAll`: Get Many - Retrieve many rows
- `update`: Update - Update a row

##### Data to Send (`dataToSend`)

Whether to insert the input data this node receives in the new row

Optional values:
- `autoMapInputData`: Auto-Map Input Data to Columns - Use when node input properties match destination column names
- `defineBelow`: Define Below for Each Column - Set the value for each destination column

##### Fields to Send (`fieldsUi`)

Optional values:
- `undefined`: fieldValues

##### Options (`additionalOptions`)

Optional values:
- `undefined`: filters - Filter rows based on comparison operators
- `undefined`: filterType - This works only if two or more filters are provided. Defaults to \<code\>AND\</code\>
- `undefined`: search - Text to match (can be in any column)
- `undefined`: order - Set the sort order of the result rows

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
  "name": "Baserow",
  "type": "nodes-base.baserow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "databaseId": "",
    "tableId": "",
    "rowId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Baserow",
  "type": "nodes-base.baserow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "databaseId": "",
    "tableId": "",
    "rowId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Baserow",
  "type": "nodes-base.baserow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "databaseId": "",
    "tableId": "",
    "rowId": "",
    "operation": "delete"
  }
}
```

---

## Beeminder

## Basic Information

- Node Type: `nodes-base.beeminder`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Beeminder API

### Available Operations

### Create
Create a charge
- Value: `create`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"datapoint"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"get"` | - |
| `operation` | options | Yes | `"get"` | - |
| `value` | number | Yes | `1` | Datapoint value to send |
| `goal_type` | options | Yes | `"hustler"` | Type of goal. <a href="https://api.beeminder.com/#attributes-2">More info here.</a>. |
| `goalName` | options | Yes | `""` | The name of the goal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `goalName` | options | Yes | `""` | The name of the goal to derail. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `goalName` | options | Yes | `""` | The name of the goal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

#### Property Details

##### Resource (`resource`)

Optional values:
- `charge`: Charge
- `datapoint`: Datapoint
- `goal`: Goal
- `user`: User

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a charge

##### Operation (`operation`)

Optional values:
- `create`: Create - Create datapoint for goal
- `createAll`: Create All - Create multiple datapoints at once
- `delete`: Delete - Delete a datapoint
- `get`: Get - Get a single datapoint
- `getAll`: Get Many - Get many datapoints for a goal
- `update`: Update - Update a datapoint

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new goal
- `get`: Get - Get a specific goal
- `getAll`: Get Many - Get many goals
- `getArchived`: Get Archived - Get archived goals
- `update`: Update - Update a goal
- `refresh`: Refresh - Refresh goal data
- `shortCircuit`: Short Circuit - Short circuit pledge
- `stepDown`: Step Down - Step down pledge
- `cancelStepDown`: Cancel Step Down
- `uncle`: Uncle - Derail a goal and charge the pledge amount

##### Operation (`operation`)

Optional values:
- `get`: Get - Get user information

##### Goal Type (`goal_type`)

Type of goal. \<a href="https://api.beeminder.com/#attributes-2"\>More info here.\</a\>.

Optional values:
- `hustler`: Hustler
- `biker`: Biker
- `fatloser`: Fatloser
- `gainer`: Gainer
- `inboxer`: Inboxer
- `drinker`: Drinker
- `custom`: Custom

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
  "name": "Beeminder",
  "type": "nodes-base.beeminder",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "datapoint",
    "operation": "get",
    "value": 1,
    "goal_type": "hustler",
    "goalName": ""
  }
}
```

#### Create Example
```json
{
  "name": "Beeminder",
  "type": "nodes-base.beeminder",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "datapoint",
    "operation": "create",
    "value": 1,
    "goal_type": "hustler",
    "goalName": ""
  }
}
```

---

## Bitly

## Basic Information

- Node Type: `nodes-base.bitly`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Bitly API

### Available Operations

### Create
Create a link
- Value: `create`

### Get
Get a link
- Value: `get`

### Update
Update a link
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `longUrl` | string | Yes | `""` | - |
| `id` | string | Yes | `""` | - |
| `id` | string | Yes | `""` | - |
| `authentication` | options | No | `"accessToken"` | - |
| `resource` | options | No | `"link"` | - |
| `operation` | options | No | `"create"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `deeplink` | fixedCollection | No | `{}` | - |
| `updateFields` | collection | No | `{}` | - |
| `deeplink` | fixedCollection | No | `{}` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `accessToken`: Access Token
- `oAuth2`: OAuth2

##### Resource (`resource`)

Optional values:
- `link`: Link

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a link
- `get`: Get - Get a link
- `update`: Update - Update a link

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: domain
- `undefined`: group - Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: tags - Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: title

##### Deeplinks (`deeplink`)

Optional values:
- `undefined`: deeplinkUi

##### Update Fields (`updateFields`)

Optional values:
- `undefined`: archived
- `undefined`: group - Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: longUrl
- `undefined`: tags - Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: title

##### Deeplinks (`deeplink`)

Optional values:
- `undefined`: deeplinkUi

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
  "name": "Bitly",
  "type": "nodes-base.bitly",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "longUrl": "",
    "id": ""
  }
}
```

#### Create Example
```json
{
  "name": "Bitly",
  "type": "nodes-base.bitly",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "longUrl": "",
    "id": "",
    "operation": "create"
  }
}
```

#### Get Example
```json
{
  "name": "Bitly",
  "type": "nodes-base.bitly",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "longUrl": "",
    "id": "",
    "operation": "get"
  }
}
```

---

## Brandfetch

## Basic Information

- Node Type: `nodes-base.Brandfetch`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Brandfetch API

### Available Operations

### Color
Return a company's colors
- Value: `color`

### Company
Return a company's data
- Value: `company`

### Font
Return a company's fonts
- Value: `font`

### Industry
Return a company's industry
- Value: `industry`

### Logo
Return a company's logo & icon
- Value: `logo`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `imageFormats` | multiOptions | Yes | `["png"]` | The image format in which the logo should be returned as |
| `imageTypes` | multiOptions | Yes | `["logo","icon"]` | - |
| `domain` | string | Yes | `""` | The domain name of the company |
| `download` | boolean | Yes | `false` | Name of the binary property to which to write the data of the read file |
| `operation` | options | No | `"logo"` | - |

#### Property Details

##### Image Format (`imageFormats`)

The image format in which the logo should be returned as

Optional values:
- `png`: PNG
- `svg`: SVG

##### Image Type (`imageTypes`)

Optional values:
- `icon`: Icon
- `logo`: Logo

##### Operation (`operation`)

Optional values:
- `color`: Color - Return a company's colors
- `company`: Company - Return a company's data
- `font`: Font - Return a company's fonts
- `industry`: Industry - Return a company's industry
- `logo`: Logo - Return a company's logo & icon

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
  "name": "Brandfetch",
  "type": "nodes-base.Brandfetch",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "imageFormats": [
      "png"
    ],
    "imageTypes": [
      "logo",
      "icon"
    ],
    "domain": "",
    "download": false
  }
}
```

#### Color Example
```json
{
  "name": "Brandfetch",
  "type": "nodes-base.Brandfetch",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "imageFormats": [
      "png"
    ],
    "imageTypes": [
      "logo",
      "icon"
    ],
    "domain": "",
    "download": false,
    "operation": "color"
  }
}
```

#### Company Example
```json
{
  "name": "Brandfetch",
  "type": "nodes-base.Brandfetch",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "imageFormats": [
      "png"
    ],
    "imageTypes": [
      "logo",
      "icon"
    ],
    "domain": "",
    "download": false,
    "operation": "company"
  }
}
```

---

## CircleCI

## Basic Information

- Node Type: `nodes-base.circleCi`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume CircleCI API

### Available Operations

### Get
Get a pipeline
- Value: `get`

### Get Many
Get many pipelines
- Value: `getAll`

### Trigger
Trigger a pipeline
- Value: `trigger`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | No | `"pipeline"` | - |
| `operation` | options | No | `"get"` | - |
| `vcs` | options | No | `""` | Source control system |
| `filters` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |
| `projectSlug` | string | No | `""` | Project slug in the form org-name/repo-name |
| `pipelineNumber` | number | No | `1` | The number of the pipeline |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `100` | Max number of results to return |

#### Property Details

##### Resource (`resource`)

Optional values:
- `pipeline`: Pipeline

##### Operation (`operation`)

Optional values:
- `get`: Get - Get a pipeline
- `getAll`: Get Many - Get many pipelines
- `trigger`: Trigger - Trigger a pipeline

##### Provider (`vcs`)

Source control system

Optional values:
- `bitbucket`: Bitbucket
- `github`: GitHub

##### Filters (`filters`)

Optional values:
- `undefined`: branch - The name of a vcs branch

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: branch - The branch where the pipeline ran. The HEAD commit on this branch was used for the pipeline. Note that branch and tag are mutually exclusive.
- `undefined`: tag - The tag used by the pipeline. The commit that this tag points to was used for the pipeline. Note that branch and tag are mutually exclusive

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
  "name": "CircleCI",
  "type": "nodes-base.circleCi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Get Example
```json
{
  "name": "CircleCI",
  "type": "nodes-base.circleCi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "get"
  }
}
```

#### Get Many Example
```json
{
  "name": "CircleCI",
  "type": "nodes-base.circleCi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "getAll"
  }
}
```

---

## Clearbit

## Basic Information

- Node Type: `nodes-base.clearbit`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Clearbit API

### Available Operations

### Autocomplete
Auto-complete company names and retrieve logo and domain
- Value: `autocomplete`

### Enrich
Look up person and company data based on an email or domain
- Value: `enrich`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `domain` | string | Yes | `""` | The domain to look up |
| `name` | string | Yes | `""` | Name is the partial name of the company |
| `email` | string | Yes | `""` | The email address to look up |
| `resource` | options | No | `"company"` | - |
| `operation` | options | No | `"enrich"` | - |
| `operation` | options | No | `"enrich"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `company`: Company - The Company API allows you to look up a company by their domain
- `person`: Person - The Person API lets you retrieve social information associated with an email address, such as a person’s name, location and Twitter handle

##### Operation (`operation`)

Optional values:
- `autocomplete`: Autocomplete - Auto-complete company names and retrieve logo and domain
- `enrich`: Enrich - Look up person and company data based on an email or domain

##### Operation (`operation`)

Optional values:
- `enrich`: Enrich - Look up a person and company data based on an email or domain

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: companyName - The name of the company
- `undefined`: facebook - The Facebook URL for the company
- `undefined`: linkedin - The LinkedIn URL for the company
- `undefined`: twitter - The Twitter handle for the company

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: company - The name of the person’s employer
- `undefined`: companyDomain - The domain for the person’s employer
- `undefined`: facebook - The Facebook URL for the person
- `undefined`: familyName - Last name of person. If you have this, passing this is strongly recommended to improve match rates.
- `undefined`: givenName - First name of person
- `undefined`: ipAddress - IP address of the person. If you have this, passing this is strongly recommended to improve match rates.
- `undefined`: location - The city or country where the person resides
- `undefined`: linkedIn - The LinkedIn URL for the person
- `undefined`: twitter - The Twitter handle for the person

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
  "name": "Clearbit",
  "type": "nodes-base.clearbit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "domain": "",
    "name": "",
    "email": ""
  }
}
```

#### Autocomplete Example
```json
{
  "name": "Clearbit",
  "type": "nodes-base.clearbit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "domain": "",
    "name": "",
    "email": "",
    "operation": "autocomplete"
  }
}
```

#### Enrich Example
```json
{
  "name": "Clearbit",
  "type": "nodes-base.clearbit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "domain": "",
    "name": "",
    "email": "",
    "operation": "enrich"
  }
}
```

---

## ClickUp

## Basic Information

- Node Type: `nodes-base.clickUp`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume ClickUp API (Beta)

### Available Operations

### Create
Create a checklist
- Value: `create`

### Delete
Delete a checklist
- Value: `delete`

### Update
Update a checklist
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `field` | string | Yes | `""` | The ID of the field to add custom field to |
| `value` | string | Yes | `""` | The value to set on custom field |
| `type` | options | Yes | `""` | - |
| `team` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `space` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `team` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `space` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `folder` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `team` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `space` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

#### Property Details

##### Type (`type`)

Optional values:
- `automatic`: Automatic
- `boolean`: Boolean
- `currency`: Currency
- `number`: Number
- `percentage`: Percentage

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
  "name": "ClickUp",
  "type": "nodes-base.clickUp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "field": "",
    "value": "",
    "type": "",
    "team": "",
    "space": "",
    "folder": ""
  }
}
```

#### Create Example
```json
{
  "name": "ClickUp",
  "type": "nodes-base.clickUp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "field": "",
    "value": "",
    "type": "",
    "team": "",
    "space": "",
    "folder": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "ClickUp",
  "type": "nodes-base.clickUp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "field": "",
    "value": "",
    "type": "",
    "team": "",
    "space": "",
    "folder": "",
    "operation": "delete"
  }
}
```

---

## Cockpit

## Basic Information

- Node Type: `nodes-base.cockpit`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Cockpit API

### Available Operations

### Create an Entry
Create a collection entry
- Value: `create`

### Get Many Entries
Get many collection entries
- Value: `getAll`

### Update an Entry
Update a collection entry
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `collection` | options | Yes | `""` | Name of the collection to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `form` | string | Yes | `""` | Name of the form to operate on |
| `singleton` | options | Yes | `""` | Name of the singleton to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `id` | string | Yes | `""` | - |
| `resource` | options | No | `"collection"` | - |
| `operation` | options | No | `"getAll"` | - |
| `operation` | options | No | `"submit"` | - |
| `operation` | options | No | `"get"` | - |
| `dataFieldsUi` | fixedCollection | No | `{}` | Entry data to send |
| `dataFieldsUi` | fixedCollection | No | `{}` | Form data to send |

#### Property Details

##### Resource (`resource`)

Optional values:
- `collection`: Collection
- `form`: Form
- `singleton`: Singleton

##### Operation (`operation`)

Optional values:
- `create`: Create an Entry - Create a collection entry
- `getAll`: Get Many Entries - Get many collection entries
- `update`: Update an Entry - Update a collection entry

##### Operation (`operation`)

Optional values:
- `submit`: Submit a Form - Store data from a form submission

##### Operation (`operation`)

Optional values:
- `get`: Get - Get a singleton

##### Entry Data (`dataFieldsUi`)

Entry data to send

Optional values:
- `undefined`: field

##### Form Data (`dataFieldsUi`)

Form data to send

Optional values:
- `undefined`: field

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
  "name": "Cockpit",
  "type": "nodes-base.cockpit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "collection": "",
    "form": "",
    "singleton": "",
    "id": ""
  }
}
```

#### Create an Entry Example
```json
{
  "name": "Cockpit",
  "type": "nodes-base.cockpit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "collection": "",
    "form": "",
    "singleton": "",
    "id": "",
    "operation": "create"
  }
}
```

#### Get Many Entries Example
```json
{
  "name": "Cockpit",
  "type": "nodes-base.cockpit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "collection": "",
    "form": "",
    "singleton": "",
    "id": "",
    "operation": "getAll"
  }
}
```

---

## Coda

## Basic Information

- Node Type: `nodes-base.coda`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Coda API

### Available Operations

### Create Row
Create/Insert a row
- Value: `createRow`

### Delete Row
Delete one or multiple rows
- Value: `deleteRow`

### Get All Columns
Get all columns in a table
- Value: `getAllColumns`

### Get All Rows
Get all rows in a table
- Value: `getAllRows`

### Get Column
Get a column
- Value: `getColumn`

### Get Row
Get a row
- Value: `getRow`

### Push Button
Pushes a button
- Value: `pushButton`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `docId` | options | Yes | `""` | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `tableId` | options | Yes | `""` | The table to create the row in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `docId` | options | Yes | `""` | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `tableId` | options | Yes | `""` | The table to get the row from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `rowId` | string | Yes | `""` | ID or name of the row. Names are discouraged because they're easily prone to being changed by users. If you're using a name, be sure to URI-encode it. If there are multiple rows with the same value in the identifying column, an arbitrary one will be selected |
| `docId` | options | Yes | `""` | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `tableId` | options | Yes | `""` | The table to get the rows from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `docId` | options | Yes | `""` | ID of the doc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `tableId` | options | Yes | `""` | The table to delete the row in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `rowId` | string | Yes | `""` | Row IDs to delete |

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
  "name": "Coda",
  "type": "nodes-base.coda",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "docId": "",
    "tableId": "",
    "rowId": ""
  }
}
```

#### Create Row Example
```json
{
  "name": "Coda",
  "type": "nodes-base.coda",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "docId": "",
    "tableId": "",
    "rowId": "",
    "operation": "createRow"
  }
}
```

#### Delete Row Example
```json
{
  "name": "Coda",
  "type": "nodes-base.coda",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "docId": "",
    "tableId": "",
    "rowId": "",
    "operation": "deleteRow"
  }
}
```

---

## CoinGecko

## Basic Information

- Node Type: `nodes-base.coinGecko`
- Category: output
- Package: n8n-nodes-base

### Description

Consume CoinGecko API

### Available Operations

### Candlestick
Get a candlestick open-high-low-close chart for the selected currency
- Value: `candlestick`

### Get
Get current data for a coin
- Value: `get`

### Get Many
Get many coins
- Value: `getAll`

### History
Get historical data (name, price, market, stats) at a given date for a coin
- Value: `history`

### Market
Get prices and market related data for all trading pairs that match the selected currency
- Value: `market`

### Market Chart
Get historical market data include price, market cap, and 24h volume (granularity auto)
- Value: `marketChart`

### Price
Get the current price of any cryptocurrencies in any other supported currencies that you need
- Value: `price`

### Ticker
Get coin tickers
- Value: `ticker`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `searchBy` | options | Yes | `"coinId"` | Search by coin ID or contract address |
| `platformId` | options | Yes | `"ethereum"` | The ID of the platform issuing tokens |
| `days` | options | Yes | `""` | Return data for this many days in the past from now |
| `coinId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `baseCurrency` | options | Yes | `""` | The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `baseCurrency` | options | Yes | `""` | The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `coinId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `baseCurrencies` | multiOptions | Yes | `[]` | The first currency in the pair. For BTC:ETH this is BTC. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `contractAddress` | string | Yes | `""` | Token's contract address |
| `contractAddresses` | string | Yes | `""` | The contract address of tokens, comma-separated |

#### Property Details

##### Search By (`searchBy`)

Search by coin ID or contract address

Optional values:
- `coinId`: Coin ID
- `contractAddress`: Contract Address

##### Platform ID (`platformId`)

The ID of the platform issuing tokens

Optional values:
- `ethereum`: Ethereum

##### Range (Days) (`days`)

Return data for this many days in the past from now

Optional values:
- `1`: 1
- `7`: 7
- `14`: 14
- `30`: 30
- `90`: 90
- `180`: 180
- `365`: 365
- `max`: Max

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
  "name": "CoinGecko",
  "type": "nodes-base.coinGecko",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "searchBy": "coinId",
    "platformId": "ethereum",
    "days": "",
    "coinId": "",
    "baseCurrency": "",
    "baseCurrencies": [],
    "contractAddress": "",
    "contractAddresses": ""
  }
}
```

#### Candlestick Example
```json
{
  "name": "CoinGecko",
  "type": "nodes-base.coinGecko",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "searchBy": "coinId",
    "platformId": "ethereum",
    "days": "",
    "coinId": "",
    "baseCurrency": "",
    "baseCurrencies": [],
    "contractAddress": "",
    "contractAddresses": "",
    "operation": "candlestick"
  }
}
```

#### Get Example
```json
{
  "name": "CoinGecko",
  "type": "nodes-base.coinGecko",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "searchBy": "coinId",
    "platformId": "ethereum",
    "days": "",
    "coinId": "",
    "baseCurrency": "",
    "baseCurrencies": [],
    "contractAddress": "",
    "contractAddresses": "",
    "operation": "get"
  }
}
```

---

## Customer.io

## Basic Information

- Node Type: `nodes-base.customerIo`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Customer.io API

### Available Operations

### Get
- Value: `get`

### Get Many
- Value: `getAll`

### Get Metrics
- Value: `getMetrics`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `campaignId` | number | Yes | `0` | The unique identifier for the campaign |
| `campaignId` | number | Yes | `0` | The unique identifier for the campaign |
| `id` | string | Yes | `""` | The unique identifier for the customer |
| `id` | string | Yes | `""` | The unique identifier for the customer |
| `customerId` | string | Yes | `""` | The unique identifier for the customer |
| `eventName` | string | Yes | `""` | The unique identifier for the customer |
| `segmentId` | number | Yes | `0` | The unique identifier of the segment |
| `customerIds` | string | Yes | `""` | A list of customer IDs to add to the segment |
| `resource` | options | No | `"customer"` | - |
| `operation` | options | No | `"get"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `customer`: Customer
- `event`: Event
- `campaign`: Campaign
- `segment`: Segment

##### Operation (`operation`)

Optional values:
- `get`: Get
- `getAll`: Get Many
- `getMetrics`: Get Metrics

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
  "name": "Customer.io",
  "type": "nodes-base.customerIo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "campaignId": 0,
    "id": "",
    "customerId": "",
    "eventName": "",
    "segmentId": 0,
    "customerIds": ""
  }
}
```

#### Get Example
```json
{
  "name": "Customer.io",
  "type": "nodes-base.customerIo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "campaignId": 0,
    "id": "",
    "customerId": "",
    "eventName": "",
    "segmentId": 0,
    "customerIds": "",
    "operation": "get"
  }
}
```

#### Get Many Example
```json
{
  "name": "Customer.io",
  "type": "nodes-base.customerIo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "campaignId": 0,
    "id": "",
    "customerId": "",
    "eventName": "",
    "segmentId": 0,
    "customerIds": "",
    "operation": "getAll"
  }
}
```

---

## DebugHelper

## Basic Information

- Node Type: `nodes-base.debugHelper`
- Category: output
- Package: n8n-nodes-base

### Description

Causes problems intentionally and generates useful data for debugging

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `category` | options | No | `"throwError"` | - |
| `throwErrorType` | options | No | `"NodeApiError"` | - |
| `randomDataType` | options | No | `"user"` | - |
| `throwErrorMessage` | string | No | `"Node has thrown an error"` | The message to send as part of the error |
| `memorySizeValue` | number | No | `10` | The approximate amount of memory to generate. Be generous... |
| `nanoidAlphabet` | string | No | `"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"` | The alphabet to use for generating the nanoIds |
| `nanoidLength` | string | No | `"16"` | The length of each nanoIds |
| `randomDataSeed` | string | No | `""` | If set, seed to use for generating the data (same seed will generate the same data) |
| `randomDataCount` | number | No | `10` | The number of random data items to generate into an array |
| `randomDataSingleArray` | boolean | No | `false` | Whether to output a single array instead of multiple items |

#### Property Details

##### Category (`category`)

Optional values:
- `doNothing`: Do Nothing - Does nothing
- `throwError`: Throw Error - Throws an error with the specified type and message
- `oom`: Out Of Memory - Generates a large amount of memory to cause an out of memory error
- `randomData`: Generate Random Data - Generates random data sets

##### Error Type (`throwErrorType`)

Optional values:
- `NodeApiError`: NodeApiError
- `NodeOperationError`: NodeOperationError
- `Error`: Error

##### Data Type (`randomDataType`)

Optional values:
- `address`: Address
- `latLong`: Coordinates
- `creditCard`: Credit Card
- `email`: Email
- `ipv4`: IPv4
- `ipv6`: IPv6
- `macAddress`: MAC
- `nanoid`: NanoIds
- `url`: URL
- `user`: User Data
- `uuid`: UUID
- `semver`: Version

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
  "name": "DebugHelper",
  "type": "nodes-base.debugHelper",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Demio

## Basic Information

- Node Type: `nodes-base.demio`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Demio API

### Available Operations

### Get
Get an event
- Value: `get`

### Get Many
Get many events
- Value: `getAll`

### Register
Register someone to an event
- Value: `register`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `firstName` | string | Yes | `""` | The registrant's first name |
| `email` | string | Yes | `""` | The registrant's email address |
| `dateId` | options | Yes | `""` | ID of the session. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `eventId` | string | Yes | `""` | - |
| `resource` | options | No | `"event"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"get"` | - |
| `filters` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `event`: Event
- `report`: Report

##### Operation (`operation`)

Optional values:
- `get`: Get - Get an event
- `getAll`: Get Many - Get many events
- `register`: Register - Register someone to an event

##### Operation (`operation`)

Optional values:
- `get`: Get - Get an event report

##### Filters (`filters`)

Optional values:
- `undefined`: type

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: active - Whether to return only active dates in series
- `undefined`: date_id - Event Date ID

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: company - The value for the predefined Company field
- `undefined`: customFieldsUi
- `undefined`: ref_url - Event Registration page URL. It can be useful when you do not know Event ID, but have Event link.
- `undefined`: gdpr - The value for the predefined GDPR field
- `undefined`: last_name - The value for the predefined Last Name field
- `undefined`: phone_number - The value for the predefined Phone Number field
- `undefined`: date_id - Event Session ID. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: website - The value for the predefined Website field

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
  "name": "Demio",
  "type": "nodes-base.demio",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "firstName": "",
    "email": "",
    "dateId": "",
    "eventId": ""
  }
}
```

#### Get Example
```json
{
  "name": "Demio",
  "type": "nodes-base.demio",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "firstName": "",
    "email": "",
    "dateId": "",
    "eventId": "",
    "operation": "get"
  }
}
```

#### Get Many Example
```json
{
  "name": "Demio",
  "type": "nodes-base.demio",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "firstName": "",
    "email": "",
    "dateId": "",
    "eventId": "",
    "operation": "getAll"
  }
}
```

---

## Drift

## Basic Information

- Node Type: `nodes-base.drift`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Drift API

### Available Operations

### Create
Create a contact
- Value: `create`

### Custom Attributes
Get custom attributes
- Value: `getCustomAttributes`

### Delete
Delete a contact
- Value: `delete`

### Get
Get a contact
- Value: `get`

### Update
Update a contact
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `email` | string | Yes | `""` | The email of the contact |
| `contactId` | string | Yes | `""` | Unique identifier for the contact |
| `contactId` | string | Yes | `""` | Unique identifier for the contact |
| `contactId` | string | Yes | `""` | Unique identifier for the contact |
| `authentication` | options | No | `"accessToken"` | - |
| `resource` | options | No | `"contact"` | - |
| `operation` | options | No | `"create"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `updateFields` | collection | No | `{}` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `accessToken`: Access Token
- `oAuth2`: OAuth2

##### Resource (`resource`)

Optional values:
- `contact`: Contact

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a contact
- `getCustomAttributes`: Custom Attributes - Get custom attributes
- `delete`: Delete - Delete a contact
- `get`: Get - Get a contact
- `update`: Update - Update a contact

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: name - The name of the contact
- `undefined`: phone - The phone number associated with the contact

##### Update Fields (`updateFields`)

Optional values:
- `undefined`: email - The email of the contact
- `undefined`: name - The name of the contact
- `undefined`: phone - The phone number associated with the contact

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
  "name": "Drift",
  "type": "nodes-base.drift",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "contactId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Drift",
  "type": "nodes-base.drift",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "contactId": "",
    "operation": "create"
  }
}
```

#### Custom Attributes Example
```json
{
  "name": "Drift",
  "type": "nodes-base.drift",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "contactId": "",
    "operation": "getCustomAttributes"
  }
}
```

---

## E-goi

## Basic Information

- Node Type: `nodes-base.egoi`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume E-goi API

### Available Operations

### Create
Create a member
- Value: `create`

### Get
Get a member
- Value: `get`

### Get Many
Get many members
- Value: `getAll`

### Update
Update a member
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"contact"` | - |
| `operation` | options | Yes | `"create"` | - |
| `by` | options | No | `"id"` | Search by |
| `additionalFields` | collection | No | `{}` | - |
| `updateFields` | collection | No | `{}` | - |
| `list` | options | No | `""` | ID of list to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `email` | string | No | `""` | Email address for a subscriber |
| `contactId` | string | No | `""` | Contact ID of the subscriber |
| `resolveData` | boolean | No | `true` | By default the response just includes the contact ID. If this option gets activated, it will resolve the data automatically. |
| `contactId` | string | No | `""` | Contact ID of the subscriber |

#### Property Details

##### Resource (`resource`)

Optional values:
- `contact`: Contact

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a member
- `get`: Get - Get a member
- `getAll`: Get Many - Get many members
- `update`: Update - Update a member

##### By (`by`)

Search by

Optional values:
- `id`: Contact ID
- `email`: Email

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: birth_date - Birth date of a subscriber
- `undefined`: cellphone - Cellphone of a subscriber
- `undefined`: extraFieldsUi
- `undefined`: first_name - Name of a subscriber
- `undefined`: last_name - Name of a subscriber
- `undefined`: status - Subscriber's current status
- `undefined`: tagIds - List of tag IDs to be added. Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.

##### Update Fields (`updateFields`)

Optional values:
- `undefined`: birth_date - Birth date of subscriber
- `undefined`: cellphone - Cellphone of subscriber
- `undefined`: email - Email address for subscriber
- `undefined`: extraFieldsUi
- `undefined`: first_name - Name of subscriber
- `undefined`: last_name - Name of subscriber
- `undefined`: status - Subscriber's current status
- `undefined`: tagIds - List of tag IDs to be added. Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.

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
  "name": "E-goi",
  "type": "nodes-base.egoi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "contact",
    "operation": "create"
  }
}
```

#### Create Example
```json
{
  "name": "E-goi",
  "type": "nodes-base.egoi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "contact",
    "operation": "create"
  }
}
```

#### Get Example
```json
{
  "name": "E-goi",
  "type": "nodes-base.egoi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "contact",
    "operation": "get"
  }
}
```

---

## E2E Test

## Basic Information

- Node Type: `nodes-base.e2eTest`
- Category: output
- Package: n8n-nodes-base

### Description

Dummy node used for e2e testing

### Available Operations

### Remote Options
- Value: `remoteOptions`

### Resource Locator
- Value: `resourceLocator`

### Resource Mapping Component
- Value: `resourceMapper`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `remoteOptions` | options | Yes | `[]` | Remote options to load. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `rlc` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `resourceMapper` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `operation` | options | No | `"remoteOptions"` | - |
| `fieldId` | string | No | `""` | - |
| `otherField` | string | No | `""` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `remoteOptions`: Remote Options
- `resourceLocator`: Resource Locator
- `resourceMapper`: Resource Mapping Component

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
  "name": "E2E Test",
  "type": "nodes-base.e2eTest",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "remoteOptions": [],
    "rlc": {
      "mode": "list",
      "value": ""
    },
    "resourceMapper": {
      "mappingMode": "defineBelow",
      "value": null
    }
  }
}
```

#### Remote Options Example
```json
{
  "name": "E2E Test",
  "type": "nodes-base.e2eTest",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "remoteOptions": [],
    "rlc": {
      "mode": "list",
      "value": ""
    },
    "resourceMapper": {
      "mappingMode": "defineBelow",
      "value": null
    },
    "operation": "remoteOptions"
  }
}
```

#### Resource Locator Example
```json
{
  "name": "E2E Test",
  "type": "nodes-base.e2eTest",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "remoteOptions": [],
    "rlc": {
      "mode": "list",
      "value": ""
    },
    "resourceMapper": {
      "mappingMode": "defineBelow",
      "value": null
    },
    "operation": "resourceLocator"
  }
}
```

---

## ERPNext

## Basic Information

- Node Type: `nodes-base.erpNext`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume ERPNext API

### Available Operations

### Create
Create a document
- Value: `create`

### Delete
Delete a document
- Value: `delete`

### Get
Retrieve a document
- Value: `get`

### Get Many
Retrieve many documents
- Value: `getAll`

### Update
Update a document
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `properties` | fixedCollection | Yes | `{}` | - |
| `docType` | options | Yes | `""` | DocType you would like to create. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `docType` | options | Yes | `""` | The type of document you would like to get. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `documentName` | string | Yes | `""` | The name (ID) of document you would like to get |
| `docType` | options | Yes | `""` | The type of document you would like to delete. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `documentName` | string | Yes | `""` | The name (ID) of document you would like to get |
| `docType` | options | Yes | `""` | The type of document you would like to update. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `documentName` | string | Yes | `""` | The name (ID) of document you would like to get |
| `resource` | options | No | `"document"` | - |
| `operation` | options | No | `"create"` | - |

#### Property Details

##### Properties (`properties`)

Optional values:
- `undefined`: customProperty

##### Resource (`resource`)

Optional values:
- `document`: Document

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a document
- `delete`: Delete - Delete a document
- `get`: Get - Retrieve a document
- `getAll`: Get Many - Retrieve many documents
- `update`: Update - Update a document

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
  "name": "ERPNext",
  "type": "nodes-base.erpNext",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "properties": {},
    "docType": "",
    "documentName": ""
  }
}
```

#### Create Example
```json
{
  "name": "ERPNext",
  "type": "nodes-base.erpNext",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "properties": {},
    "docType": "",
    "documentName": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "ERPNext",
  "type": "nodes-base.erpNext",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "properties": {},
    "docType": "",
    "documentName": "",
    "operation": "delete"
  }
}
```

---

## Flow

## Basic Information

- Node Type: `nodes-base.flow`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Flow API

### Available Operations

### Create
Create a new task
- Value: `create`

### Update
Update a task
- Value: `update`

### Get
Get a task
- Value: `get`

### Get Many
Get many tasks
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `workspaceId` | string | Yes | `""` | Create resources under the given workspace |
| `name` | string | Yes | `""` | The title of the task |
| `workspaceId` | string | Yes | `""` | Create resources under the given workspace |
| `taskId` | string | Yes | `""` | - |
| `taskId` | string | Yes | `""` | - |
| `resource` | options | No | `"task"` | - |
| `operation` | options | No | `"create"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `updateFields` | collection | No | `{}` | - |
| `filters` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `task`: Task - Tasks are units of work that can be private or assigned to a list. Through this endpoint, you can manipulate your tasks in Flow, including creating new ones.

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new task
- `update`: Update - Update a task
- `get`: Get - Get a task
- `getAll`: Get Many - Get many tasks

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: ownerid - The ID of the account to whom this task will be assigned
- `undefined`: listID - Put the new task in a list ("project"). Omit this param to have the task be private.
- `undefined`: startsOn - The date on which the task should start
- `undefined`: dueOn - The date on which the task should be due
- `undefined`: mirrorParentSubscribers - Whether this task will be a subtask, and this is true, the parent tasks's subscribers will be mirrored to this one
- `undefined`: mirrorParentTags - Whether this task will be a subtask, and this is true, the parent tasks's tags will be mirrored to this one
- `undefined`: noteContent - Provide the content for the task's note
- `undefined`: noteMimeType - Identify which markup language is used to format the given note
- `undefined`: parentId - If provided, this task will become a subtask of the given task
- `undefined`: positionList - Determines the sort order when showing tasks in, or grouped by, a list
- `undefined`: positionUpcoming - Determines the sort order when showing tasks grouped by their due\_date
- `undefined`: position - Determines the sort order of tasks
- `undefined`: sectionId - Specify which section under which to create this task
- `undefined`: tags - A list of tag names to apply to the new task separated by a comma (,)

##### Update Fields (`updateFields`)

Optional values:
- `undefined`: name - The title of the task
- `undefined`: completed - Whether to complete the task
- `undefined`: ownerid - The ID of the account to whom this task will be assigned
- `undefined`: listID - Put the new task in a list ("project"). Omit this param to have the task be private.
- `undefined`: startsOn - The date on which the task should start
- `undefined`: dueOn - The date on which the task should be due
- `undefined`: mirrorParentSubscribers - Whether this task will be a subtask, and this is true, the parent tasks's subscribers will be mirrored to this one
- `undefined`: mirrorParentTags - Whether this task will be a subtask, and this is true, the parent tasks's tags will be mirrored to this one
- `undefined`: noteContent - Provide the content for the task's note
- `undefined`: noteMimeType - Identify which markup language is used to format the given note
- `undefined`: parentId - If provided, this task will become a subtask of the given task
- `undefined`: positionList - Determines the sort order when showing tasks in, or grouped by, a list
- `undefined`: positionUpcoming - Determines the sort order when showing tasks grouped by their due\_date
- `undefined`: position - Determines the sort order of tasks
- `undefined`: sectionId - Specify which section under which to create this task
- `undefined`: tags - A list of tag names to apply to the new task separated by a comma (,)

##### Filters (`filters`)

Optional values:
- `undefined`: include

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
  "name": "Flow",
  "type": "nodes-base.flow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workspaceId": "",
    "name": "",
    "taskId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Flow",
  "type": "nodes-base.flow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workspaceId": "",
    "name": "",
    "taskId": "",
    "operation": "create"
  }
}
```

#### Update Example
```json
{
  "name": "Flow",
  "type": "nodes-base.flow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workspaceId": "",
    "name": "",
    "taskId": "",
    "operation": "update"
  }
}
```

---

## Freshdesk

## Basic Information

- Node Type: `nodes-base.freshdesk`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Freshdesk API

### Available Operations

### Create
Create a new ticket
- Value: `create`

### Delete
Delete a ticket
- Value: `delete`

### Get
Get a ticket
- Value: `get`

### Get Many
Get many tickets
- Value: `getAll`

### Update
Update a ticket
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"ticket"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"create"` | - |
| `source` | options | Yes | `"portal"` | The channel through which the ticket was created |
| `requester` | options | Yes | `"requesterId"` | - |
| `status` | options | Yes | `"pending"` | - |
| `priority` | options | Yes | `"low"` | - |
| `requesterIdentificationValue` | string | Yes | `""` | Value of the identification selected |
| `name` | string | Yes | `""` | Name of the contact |
| `ticketId` | string | Yes | `""` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `contact`: Contact
- `ticket`: Ticket

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new ticket
- `delete`: Delete - Delete a ticket
- `get`: Get - Get a ticket
- `getAll`: Get Many - Get many tickets
- `update`: Update - Update a ticket

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new contact
- `delete`: Delete - Delete a contact
- `get`: Get - Get a contact
- `getAll`: Get Many - Get many contacts
- `update`: Update - Update a contact

##### Source (`source`)

The channel through which the ticket was created

Optional values:
- `chat`: Chat
- `email`: Email
- `feedbackWidget`: Feedback Widget
- `mobileHelp`: Mobihelp
- `OutboundEmail`: Outbound Email
- `phone`: Phone
- `portal`: Portal

##### Requester Identification (`requester`)

Optional values:
- `email`: Email - Email address of the requester. If no contact exists with this email address in Freshdesk, it will be added as a new contact.
- `facebookId`: Facebook ID - Facebook ID of the requester. If no contact exists with this facebook\_id, then a new contact will be created.
- `phone`: Phone - Phone number of the requester. If no contact exists with this phone number in Freshdesk, it will be added as a new contact. If the phone number is set and the email address is not, then the name attribute is mandatory.
- `requesterId`: Requester ID - User ID of the requester. For existing contacts, the requester\_id can be passed instead of the requester's email.
- `twitterId`: Twitter ID - Twitter handle of the requester. If no contact exists with this handle in Freshdesk, it will be added as a new contact.
- `uniqueExternalId`: Unique External ID - External ID of the requester. If no contact exists with this external ID in Freshdesk, they will be added as a new contact.

##### Status (`status`)

Optional values:
- `closed`: Closed
- `open`: Open
- `pending`: Pending
- `resolved`: Resolved

##### Priority (`priority`)

Optional values:
- `low`: Low
- `medium`: Medium
- `high`: High
- `urgent`: Urgent

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
  "name": "Freshdesk",
  "type": "nodes-base.freshdesk",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "ticket",
    "operation": "create",
    "source": "portal",
    "requester": "requesterId",
    "status": "pending",
    "priority": "low",
    "requesterIdentificationValue": "",
    "name": "",
    "ticketId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Freshdesk",
  "type": "nodes-base.freshdesk",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "ticket",
    "operation": "create",
    "source": "portal",
    "requester": "requesterId",
    "status": "pending",
    "priority": "low",
    "requesterIdentificationValue": "",
    "name": "",
    "ticketId": ""
  }
}
```

#### Delete Example
```json
{
  "name": "Freshdesk",
  "type": "nodes-base.freshdesk",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "ticket",
    "operation": "delete",
    "source": "portal",
    "requester": "requesterId",
    "status": "pending",
    "priority": "low",
    "requesterIdentificationValue": "",
    "name": "",
    "ticketId": ""
  }
}
```

---

## Home Assistant

## Basic Information

- Node Type: `nodes-base.homeAssistant`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Home Assistant API

### Available Operations

### Get Screenshot
Get the camera screenshot
- Value: `getScreenshot`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `cameraEntityId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `eventType` | string | Yes | `""` | The Entity ID for which an event will be created |
| `domain` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `service` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `entityId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `entityId` | options | Yes | `""` | The entity ID for which a state will be created. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `template` | string | Yes | `""` | Render a Home Assistant template. <a href="https://www.home-assistant.io/docs/configuration/templating/">See template docs for more information.</a>. |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `state` | string | Yes | `""` | - |
| `resource` | options | No | `"config"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `cameraProxy`: Camera Proxy
- `config`: Config
- `event`: Event
- `log`: Log
- `service`: Service
- `state`: State
- `template`: Template

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
  "name": "Home Assistant",
  "type": "nodes-base.homeAssistant",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "cameraEntityId": "",
    "eventType": "",
    "domain": "",
    "service": "",
    "entityId": "",
    "template": "",
    "binaryPropertyName": "data",
    "state": ""
  }
}
```

#### Get Screenshot Example
```json
{
  "name": "Home Assistant",
  "type": "nodes-base.homeAssistant",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "cameraEntityId": "",
    "eventType": "",
    "domain": "",
    "service": "",
    "entityId": "",
    "template": "",
    "binaryPropertyName": "data",
    "state": "",
    "operation": "getScreenshot"
  }
}
```

---

## HTTP Request Tool

## Basic Information

- Node Type: `nodes-langchain.toolHttpRequest`
- Category: output
- Package: @n8n/n8n-nodes-langchain

### Description

Makes an HTTP request and returns the response data

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | - |
| `nodeCredentialType` | credentialsSelect | Yes | `""` | - |
| `genericAuthType` | credentialsSelect | Yes | `""` | - |
| `authentication` | options | No | `"none"` | Select the type of authentication to use if needed, authentication would be done by n8n and your credentials will not be shared with the LLM |
| `method` | options | No | `"GET"` | - |
| `fieldsToInclude` | options | No | `"all"` | What fields response object should include |
| `specifyQuery` | options | No | `"keypair"` | - |
| `parametersQuery` | fixedCollection | No | `{"values":[{"name":""}]}` | - |
| `specifyHeaders` | options | No | `"keypair"` | - |
| `parametersHeaders` | fixedCollection | No | `{"values":[{"name":""}]}` | - |

#### Property Details

##### Authentication (`authentication`)

Select the type of authentication to use if needed, authentication would be done by n8n and your credentials will not be shared with the LLM

Optional values:
- `none`: None
- `predefinedCredentialType`: Predefined Credential Type - We've already implemented auth for many services so that you don't have to set it up manually
- `genericCredentialType`: Generic Credential Type - Fully customizable. Choose between basic, header, OAuth2, etc.

##### Method (`method`)

Optional values:
- `DELETE`: DELETE
- `GET`: GET
- `PATCH`: PATCH
- `POST`: POST
- `PUT`: PUT

##### Include Fields (`fieldsToInclude`)

What fields response object should include

Optional values:
- `all`: All - Include all fields
- `selected`: Selected - Include only fields specified below
- `except`: Except - Exclude fields specified below

##### Specify Query Parameters (`specifyQuery`)

Optional values:
- `keypair`: Using Fields Below
- `json`: Using JSON Below
- `model`: Let Model Specify Entire Body

##### Query Parameters (`parametersQuery`)

Optional values:
- `undefined`: values

##### Specify Headers (`specifyHeaders`)

Optional values:
- `keypair`: Using Fields Below
- `json`: Using JSON Below
- `model`: Let Model Specify Entire Body

##### Header Parameters (`parametersHeaders`)

Optional values:
- `undefined`: values

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_tool` (tool)

### Can Connect To

1. AI Agent - via `ai_tool` connection
2. OpenAI Assistant - via `ai_tool` connection
3. MCP Server Trigger - via `ai_tool` connection
4. Tool Executor - via `ai_tool` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "HTTP Request Tool",
  "type": "nodes-langchain.toolHttpRequest",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "nodeCredentialType": "",
    "genericAuthType": ""
  }
}
```

---

## HubSpot

## Basic Information

- Node Type: `nodes-base.hubspot`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume HubSpot API

### Available Operations

### Create or Update
Create a new contact, or update the current one if it already exists (upsert)
- Value: `upsert`

### Delete
Delete a contact
- Value: `delete`

### Get
Get a contact
- Value: `get`

### Get Many
Get many contacts
- Value: `getAll`

### Get Recently Created/Updated
Get recently created/updated contacts
- Value: `getRecentlyCreatedUpdated`

### Search
Search contacts
- Value: `search`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `by` | options | Yes | `"email"` | - |
| `type` | options | Yes | `""` | - |
| `contactId` | resourceLocator | Yes | `{"mode":"list","value":""}` | This is not a contact's email but a number like 1485 |
| `contactId` | resourceLocator | Yes | `{"mode":"list","value":""}` | This is not a contact's email but a number like 1485 |
| `domain` | string | Yes | `""` | The company's website domain to search for, like n8n.io |
| `stage` | options | Yes | `""` | The deal stage is required when creating a deal. See the CRM Pipelines API for details on managing pipelines and stages. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `dueDate` | dateTime | Yes | `""` | The due date for the task |
| `pipelineId` | options | Yes | `""` | The ID of the pipeline the ticket is in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `stageId` | options | Yes | `""` | The stage ID of the pipeline the ticket is in; depends on Pipeline ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `email` | string | Yes | `""` | - |

#### Property Details

##### By (`by`)

Optional values:
- `id`: Contact ID
- `email`: Email

##### Type (`type`)

Optional values:
- `call`: Call
- `email`: Email
- `meeting`: Meeting
- `task`: Task

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
  "name": "HubSpot",
  "type": "nodes-base.hubspot",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "by": "email",
    "type": "",
    "contactId": {
      "mode": "list",
      "value": ""
    },
    "domain": "",
    "stage": "",
    "dueDate": "",
    "pipelineId": "",
    "stageId": "",
    "email": ""
  }
}
```

#### Create or Update Example
```json
{
  "name": "HubSpot",
  "type": "nodes-base.hubspot",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "by": "email",
    "type": "",
    "contactId": {
      "mode": "list",
      "value": ""
    },
    "domain": "",
    "stage": "",
    "dueDate": "",
    "pipelineId": "",
    "stageId": "",
    "email": "",
    "operation": "upsert"
  }
}
```

#### Delete Example
```json
{
  "name": "HubSpot",
  "type": "nodes-base.hubspot",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "by": "email",
    "type": "",
    "contactId": {
      "mode": "list",
      "value": ""
    },
    "domain": "",
    "stage": "",
    "dueDate": "",
    "pipelineId": "",
    "stageId": "",
    "email": "",
    "operation": "delete"
  }
}
```

---

## Humantic AI

## Basic Information

- Node Type: `nodes-base.humanticAi`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Humantic AI API

### Available Operations

### Create
Create a profile
- Value: `create`

### Get
Retrieve a profile
- Value: `get`

### Update
Update a profile
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `userId` | string | Yes | `""` | The LinkedIn profile URL or email ID for creating a Humantic profile. If you are sending the resume, this should be a unique string. |
| `userId` | string | Yes | `""` | This value is the same as the User ID that was provided when the analysis was created. This could be a LinkedIn URL, email ID, or a unique string in case of resume based analysis. |
| `userId` | string | Yes | `""` | This value is the same as the User ID that was provided when the analysis was created. Currently only supported for profiles created using LinkedIn URL. |
| `resource` | options | No | `"profile"` | - |
| `operation` | options | No | `"create"` | - |
| `options` | collection | No | `{}` | - |
| `sendResume` | boolean | No | `false` | Whether to send a resume for a resume based analysis |
| `sendResume` | boolean | No | `false` | Whether to send a resume for a resume of the user |
| `text` | string | No | `""` | Additional text written by the user |
| `binaryPropertyName` | string | No | `"data"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `profile`: Profile

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a profile
- `get`: Get - Retrieve a profile
- `update`: Update - Update a profile

##### Options (`options`)

Optional values:
- `undefined`: persona - Fetch the Humantic profile of the user for a particular persona type. Multiple persona values can be supported using comma as a delimiter.

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
  "name": "Humantic AI",
  "type": "nodes-base.humanticAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "userId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Humantic AI",
  "type": "nodes-base.humanticAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "userId": "",
    "operation": "create"
  }
}
```

#### Get Example
```json
{
  "name": "Humantic AI",
  "type": "nodes-base.humanticAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "userId": "",
    "operation": "get"
  }
}
```

---

## Hunter

## Basic Information

- Node Type: `nodes-base.hunter`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Hunter API

### Available Operations

### Domain Search
Get every email address found on the internet using a given domain name, with sources
- Value: `domainSearch`

### Email Finder
Generate or retrieve the most likely email address from a domain name, a first name and a last name
- Value: `emailFinder`

### Email Verifier
Verify the deliverability of an email address
- Value: `emailVerifier`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `domain` | string | Yes | `""` | Domain name from which you want to find the email addresses. For example, "stripe.com". |
| `domain` | string | Yes | `""` | Domain name from which you want to find the email addresses. For example, "stripe.com". |
| `firstname` | string | Yes | `""` | The person's first name. It doesn't need to be in lowercase. |
| `lastname` | string | Yes | `""` | The person's last name. It doesn't need to be in lowercase. |
| `email` | string | Yes | `""` | The email address you want to verify |
| `operation` | options | No | `"domainSearch"` | Operation to consume |
| `filters` | collection | No | `{}` | - |
| `onlyEmails` | boolean | No | `true` | Whether to return only the found emails |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `100` | Max number of results to return |

#### Property Details

##### Operation (`operation`)

Operation to consume

Optional values:
- `domainSearch`: Domain Search - Get every email address found on the internet using a given domain name, with sources
- `emailFinder`: Email Finder - Generate or retrieve the most likely email address from a domain name, a first name and a last name
- `emailVerifier`: Email Verifier - Verify the deliverability of an email address

##### Filters (`filters`)

Optional values:
- `undefined`: type
- `undefined`: seniority
- `undefined`: department

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
  "name": "Hunter",
  "type": "nodes-base.hunter",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "domain": "",
    "firstname": "",
    "lastname": "",
    "email": ""
  }
}
```

#### Domain Search Example
```json
{
  "name": "Hunter",
  "type": "nodes-base.hunter",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "domain": "",
    "firstname": "",
    "lastname": "",
    "email": "",
    "operation": "domainSearch"
  }
}
```

#### Email Finder Example
```json
{
  "name": "Hunter",
  "type": "nodes-base.hunter",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "domain": "",
    "firstname": "",
    "lastname": "",
    "email": "",
    "operation": "emailFinder"
  }
}
```

---

## Intercom

## Basic Information

- Node Type: `nodes-base.intercom`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Intercom API

### Available Operations

### Create
Create a new lead
- Value: `create`

### Delete
Delete a lead
- Value: `delete`

### Get
Get data of a lead
- Value: `get`

### Get Many
Get data of many leads
- Value: `getAll`

### Update
Update new lead
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `value` | string | Yes | `""` | View by value |
| `value` | string | Yes | `""` | Value of the property to identify the user to update |
| `value` | string | Yes | `""` | Delete by value |
| `value` | string | Yes | `""` | View by value |
| `value` | string | Yes | `""` | Value of the property to identify the lead to update |
| `value` | string | Yes | `""` | View by value |
| `value` | string | Yes | `""` | View by value |
| `id` | string | Yes | `""` | The Intercom defined ID representing the Lead |
| `idValue` | string | Yes | `""` | Unique string identifier value |
| `email` | string | Yes | `""` | The email of the user |

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
  "name": "Intercom",
  "type": "nodes-base.intercom",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "id": "",
    "idValue": "",
    "email": ""
  }
}
```

#### Create Example
```json
{
  "name": "Intercom",
  "type": "nodes-base.intercom",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "id": "",
    "idValue": "",
    "email": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Intercom",
  "type": "nodes-base.intercom",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "id": "",
    "idValue": "",
    "email": "",
    "operation": "delete"
  }
}
```

---

## Invoice Ninja

## Basic Information

- Node Type: `nodes-base.invoiceNinja`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Invoice Ninja API

### Available Operations

### Create
Create a new client
- Value: `create`

### Delete
Delete a client
- Value: `delete`

### Get
Get data of a client
- Value: `get`

### Get Many
Get data of many clients
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `clientId` | string | Yes | `""` | - |
| `clientId` | string | Yes | `""` | - |
| `invoiceId` | string | Yes | `""` | - |
| `invoiceId` | string | Yes | `""` | - |
| `invoiceId` | string | Yes | `""` | - |
| `taskId` | string | Yes | `""` | - |
| `taskId` | string | Yes | `""` | - |
| `paymentId` | string | Yes | `""` | - |
| `paymentId` | string | Yes | `""` | - |
| `expenseId` | string | Yes | `""` | - |

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
  "name": "Invoice Ninja",
  "type": "nodes-base.invoiceNinja",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "clientId": "",
    "invoiceId": "",
    "taskId": "",
    "paymentId": "",
    "expenseId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Invoice Ninja",
  "type": "nodes-base.invoiceNinja",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "clientId": "",
    "invoiceId": "",
    "taskId": "",
    "paymentId": "",
    "expenseId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Invoice Ninja",
  "type": "nodes-base.invoiceNinja",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "clientId": "",
    "invoiceId": "",
    "taskId": "",
    "paymentId": "",
    "expenseId": "",
    "operation": "delete"
  }
}
```

---

## Jenkins

## Basic Information

- Node Type: `nodes-base.jenkins`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Jenkins API

### Available Operations

### Copy
Copy a specific job
- Value: `copy`

### Create
Create a new job
- Value: `create`

### Trigger
Trigger a specific job
- Value: `trigger`

### Trigger with Parameters
Trigger a specific job
- Value: `triggerParams`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `param` | fixedCollection | Yes | `{}` | Parameters for Jenkins job |
| `job` | options | Yes | `""` | Name of the job. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `newJob` | string | Yes | `""` | Name of the new Jenkins job |
| `xml` | string | Yes | `""` | XML of Jenkins config |
| `job` | options | Yes | `""` | Name of the job. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `operation` | options | No | `"trigger"` | Possible operations |
| `operation` | options | No | `"safeRestart"` | Jenkins instance operations |
| `resource` | options | No | `"job"` | - |
| `operation` | options | No | `"getAll"` | - |
| `reason` | string | No | `""` | Freeform reason for quiet down mode |

#### Property Details

##### Parameters (`param`)

Parameters for Jenkins job

Optional values:
- `undefined`: params

##### Operation (`operation`)

Possible operations

Optional values:
- `copy`: Copy - Copy a specific job
- `create`: Create - Create a new job
- `trigger`: Trigger - Trigger a specific job
- `triggerParams`: Trigger with Parameters - Trigger a specific job

##### Operation (`operation`)

Jenkins instance operations

Optional values:
- `cancelQuietDown`: Cancel Quiet Down - Cancel quiet down state
- `quietDown`: Quiet Down - Put Jenkins in quiet mode, no builds can be started, Jenkins is ready for shutdown
- `restart`: Restart - Restart Jenkins immediately on environments where it is possible
- `safeRestart`: Safely Restart - Restart Jenkins once no jobs are running on environments where it is possible
- `safeExit`: Safely Shutdown - Shutdown once no jobs are running
- `exit`: Shutdown - Shutdown Jenkins immediately

##### Resource (`resource`)

Optional values:
- `build`: Build
- `instance`: Instance
- `job`: Job

##### Operation (`operation`)

Optional values:
- `getAll`: Get Many - List Builds

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
  "name": "Jenkins",
  "type": "nodes-base.jenkins",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "param": {},
    "job": "",
    "newJob": "",
    "xml": ""
  }
}
```

#### Copy Example
```json
{
  "name": "Jenkins",
  "type": "nodes-base.jenkins",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "param": {},
    "job": "",
    "newJob": "",
    "xml": "",
    "operation": "copy"
  }
}
```

#### Create Example
```json
{
  "name": "Jenkins",
  "type": "nodes-base.jenkins",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "param": {},
    "job": "",
    "newJob": "",
    "xml": "",
    "operation": "create"
  }
}
```

---

## Jira Software

## Basic Information

- Node Type: `nodes-base.jira`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Jira Software API

### Available Operations

### Changelog
Get issue changelog
- Value: `changelog`

### Create
Create a new issue
- Value: `create`

### Delete
Delete an issue
- Value: `delete`

### Get
Get an issue
- Value: `get`

### Get Many
Get many issues
- Value: `getAll`

### Notify
Create an email notification for an issue and add it to the mail queue
- Value: `notify`

### Status
Return either all transitions or a transition that can be performed by the user on an issue, based on the issue's status
- Value: `transitions`

### Update
Update an issue
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `attachmentId` | string | Yes | `""` | The ID of the attachment |
| `attachmentId` | string | Yes | `""` | The ID of the attachment |
| `issueKey` | string | Yes | `""` | issueComment Key |
| `issueKey` | string | Yes | `""` | The ID or key of the issue |
| `commentId` | string | Yes | `""` | The ID of the comment |
| `issueKey` | string | Yes | `""` | The ID or key of the issue |
| `issueKey` | string | Yes | `""` | The ID or key of the issue |
| `commentId` | string | Yes | `""` | The ID of the comment |
| `issueKey` | string | Yes | `""` | The Issue Comment key |
| `commentId` | string | Yes | `""` | The ID of the comment |

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
  "name": "Jira Software",
  "type": "nodes-base.jira",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "attachmentId": "",
    "issueKey": "",
    "commentId": ""
  }
}
```

#### Changelog Example
```json
{
  "name": "Jira Software",
  "type": "nodes-base.jira",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "attachmentId": "",
    "issueKey": "",
    "commentId": "",
    "operation": "changelog"
  }
}
```

#### Create Example
```json
{
  "name": "Jira Software",
  "type": "nodes-base.jira",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "attachmentId": "",
    "issueKey": "",
    "commentId": "",
    "operation": "create"
  }
}
```

---

## Linear

## Basic Information

- Node Type: `nodes-base.linear`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Linear API

### Available Operations

### Add Comment
Add a comment to an issue
- Value: `addComment`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `teamId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `issueId` | string | Yes | `""` | - |
| `comment` | string | Yes | `""` | - |
| `title` | string | Yes | `""` | - |
| `issueId` | string | Yes | `""` | - |
| `issueId` | string | Yes | `""` | - |
| `link` | string | Yes | `""` | - |
| `authentication` | options | No | `"apiToken"` | - |
| `resource` | options | No | `"issue"` | - |
| `operation` | options | No | `"addComment"` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `apiToken`: API Token
- `oAuth2`: OAuth2

##### Resource (`resource`)

Optional values:
- `comment`: Comment
- `issue`: Issue

##### Operation (`operation`)

Optional values:
- `addComment`: Add Comment - Add a comment to an issue

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
  "name": "Linear",
  "type": "nodes-base.linear",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "teamId": "",
    "issueId": "",
    "comment": "",
    "title": "",
    "link": ""
  }
}
```

#### Add Comment Example
```json
{
  "name": "Linear",
  "type": "nodes-base.linear",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "teamId": "",
    "issueId": "",
    "comment": "",
    "title": "",
    "link": "",
    "operation": "addComment"
  }
}
```

---

## LingvaNex

## Basic Information

- Node Type: `nodes-base.lingvaNex`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume LingvaNex API

### Available Operations

### Translate
Translate data
- Value: `translate`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `text` | string | Yes | `""` | The input text to translate |
| `translateTo` | options | Yes | `""` | The language to use for translation of the input text, set to one of the language codes listed in <a href="https://cloud.google.com/translate/docs/languages">Language Support</a>. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `operation` | options | No | `"translate"` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `translate`: Translate - Translate data

##### Additional Options (`options`)

Optional values:
- `undefined`: from - The language code in the format “language code\_code of the country”. If this parameter is not present, the auto-detect language mode is enabled. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: platform
- `undefined`: translateMode - Describe the input text format. Possible value is "html" for translating and preserving html structure. If value is not specified or is other than "html" than plain text is translating.

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
  "name": "LingvaNex",
  "type": "nodes-base.lingvaNex",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "text": "",
    "translateTo": ""
  }
}
```

#### Translate Example
```json
{
  "name": "LingvaNex",
  "type": "nodes-base.lingvaNex",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "text": "",
    "translateTo": "",
    "operation": "translate"
  }
}
```

---

## Mailchimp

## Basic Information

- Node Type: `nodes-base.mailchimp`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Mailchimp API

### Available Operations

### Create
Create a new member on list
- Value: `create`

### Delete
Delete a member on list
- Value: `delete`

### Get
Get a member on list
- Value: `get`

### Get Many
Get many members on a list
- Value: `getAll`

### Update
Update a new member on list
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"member"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"getAll"` | - |
| `operation` | options | Yes | `"getAll"` | - |
| `status` | options | Yes | `""` | Subscriber's current status |
| `list` | options | Yes | `""` | List of lists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `email` | string | Yes | `""` | Email address for a subscriber |
| `list` | options | Yes | `""` | List of lists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `email` | string | Yes | `""` | Member's email |

#### Property Details

##### Resource (`resource`)

Optional values:
- `campaign`: Campaign
- `listGroup`: List Group
- `member`: Member
- `memberTag`: Member Tag

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new member on list
- `delete`: Delete - Delete a member on list
- `get`: Get - Get a member on list
- `getAll`: Get Many - Get many members on a list
- `update`: Update - Update a new member on list

##### Operation (`operation`)

Optional values:
- `create`: Create - Add tags from a list member
- `delete`: Delete - Remove tags from a list member

##### Operation (`operation`)

Optional values:
- `getAll`: Get Many - Get many groups

##### Operation (`operation`)

Optional values:
- `delete`: Delete - Delete a campaign
- `get`: Get - Get a campaign
- `getAll`: Get Many - Get many campaigns
- `replicate`: Replicate - Replicate a campaign
- `resend`: Resend - Creates a Resend to Non-Openers version of this campaign
- `send`: Send - Send a campaign

##### Status (`status`)

Subscriber's current status

Optional values:
- `cleaned`: Cleaned
- `pending`: Pending
- `subscribed`: Subscribed
- `transactional`: Transactional
- `unsubscribed`: Unsubscribed

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
  "name": "Mailchimp",
  "type": "nodes-base.mailchimp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "member",
    "operation": "getAll",
    "status": "",
    "list": "",
    "email": ""
  }
}
```

#### Create Example
```json
{
  "name": "Mailchimp",
  "type": "nodes-base.mailchimp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "member",
    "operation": "create",
    "status": "",
    "list": "",
    "email": ""
  }
}
```

#### Delete Example
```json
{
  "name": "Mailchimp",
  "type": "nodes-base.mailchimp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "member",
    "operation": "delete",
    "status": "",
    "list": "",
    "email": ""
  }
}
```

---

## Mailgun

## Basic Information

- Node Type: `nodes-base.mailgun`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Sends an email via Mailgun

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `fromEmail` | string | Yes | `""` | Email address of the sender optional with name |
| `toEmail` | string | Yes | `""` | Email address of the recipient. Multiple ones can be separated by comma. |
| `ccEmail` | string | No | `""` | Cc Email address of the recipient. Multiple ones can be separated by comma. |
| `bccEmail` | string | No | `""` | Bcc Email address of the recipient. Multiple ones can be separated by comma. |
| `subject` | string | No | `""` | Subject line of the email |
| `text` | string | No | `""` | Plain text message of email |
| `html` | string | No | `""` | HTML text message of email |
| `attachments` | string | No | `""` | Name of the binary properties which contain data which should be added to email as attachment. Multiple ones can be comma-separated. |

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
  "name": "Mailgun",
  "type": "nodes-base.mailgun",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fromEmail": "",
    "toEmail": ""
  }
}
```

---

## Mailjet

## Basic Information

- Node Type: `nodes-base.mailjet`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Mailjet API

### Available Operations

### Send
Send a email
- Value: `send`

### Send Template
Send a email template
- Value: `sendTemplate`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `fromEmail` | string | Yes | `""` | The title for the email |
| `toEmail` | string | Yes | `""` | Email address of the recipient. Multiple ones can be separated by comma. |
| `fromEmail` | string | Yes | `""` | The title for the email |
| `toEmail` | string | Yes | `""` | Email address of the recipient. Multiple ones can be separated by comma. |
| `templateId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `from` | string | Yes | `""` | Customizable sender name. Should be between 3 and 11 characters in length, only alphanumeric characters are allowed. |
| `to` | string | Yes | `""` | Message recipient. Should be between 3 and 15 characters in length. The number always starts with a plus sign followed by a country code, followed by the number. Phone numbers are expected to comply with the E.164 format. |
| `text` | string | Yes | `""` | - |
| `resource` | options | No | `"email"` | - |
| `operation` | options | No | `"send"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `email`: Email
- `sms`: SMS

##### Operation (`operation`)

Optional values:
- `send`: Send - Send a email
- `sendTemplate`: Send Template - Send a email template

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
  "name": "Mailjet",
  "type": "nodes-base.mailjet",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fromEmail": "",
    "toEmail": "",
    "templateId": "",
    "from": "",
    "to": "",
    "text": ""
  }
}
```

#### Send Example
```json
{
  "name": "Mailjet",
  "type": "nodes-base.mailjet",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fromEmail": "",
    "toEmail": "",
    "templateId": "",
    "from": "",
    "to": "",
    "text": "",
    "operation": "send"
  }
}
```

#### Send Template Example
```json
{
  "name": "Mailjet",
  "type": "nodes-base.mailjet",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fromEmail": "",
    "toEmail": "",
    "templateId": "",
    "from": "",
    "to": "",
    "text": "",
    "operation": "sendTemplate"
  }
}
```

---

## Mandrill

## Basic Information

- Node Type: `nodes-base.mandrill`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Mandrill API

### Available Operations

### Send Template
Send message based on template
- Value: `sendTemplate`

### Send HTML
Send message based on HTML
- Value: `sendHtml`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `template` | options | Yes | `""` | The template you want to send. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `fromEmail` | string | Yes | `""` | Email address of the sender optional with name |
| `toEmail` | string | Yes | `""` | Email address of the recipient. Multiple ones can be separated by comma. |
| `resource` | options | No | `"message"` | - |
| `operation` | options | No | `"sendTemplate"` | - |
| `mergeVarsUi` | fixedCollection | No | `{}` | Per-recipient merge variables |
| `metadataUi` | fixedCollection | No | `{}` | Metadata an associative array of user metadata. Mandrill will store this metadata and make it available for retrieval. In addition, you can select up to 10 metadata fields to index and make searchable using the Mandrill search api. |
| `attachmentsUi` | fixedCollection | No | `{}` | Array of supported attachments to add to the message |
| `headersUi` | fixedCollection | No | `{}` | Optional extra headers to add to the message (most headers are allowed) |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `message`: Message - Send a message

##### Operation (`operation`)

Optional values:
- `sendTemplate`: Send Template - Send message based on template
- `sendHtml`: Send HTML - Send message based on HTML

##### Merge Vars (`mergeVarsUi`)

Per-recipient merge variables

Optional values:
- `undefined`: mergeVarsValues

##### Metadata (`metadataUi`)

Metadata an associative array of user metadata. Mandrill will store this metadata and make it available for retrieval. In addition, you can select up to 10 metadata fields to index and make searchable using the Mandrill search api.

Optional values:
- `undefined`: metadataValues

##### Attachments (`attachmentsUi`)

Array of supported attachments to add to the message

Optional values:
- `undefined`: attachmentsValues
- `undefined`: attachmentsBinary

##### Headers (`headersUi`)

Optional extra headers to add to the message (most headers are allowed)

Optional values:
- `undefined`: headersValues

##### Options (`options`)

Optional values:
- `undefined`: async - Whether to enable a background sending mode that is optimized for bulk sending. In async mode, messages/send will immediately return a status of "queued" for every recipient. To handle rejections when sending in async mode, set up a webhook for the 'reject' event. Defaults to false for messages with no more than 10 recipients; messages with more than 10 recipients are always sent asynchronously, regardless of the value of async.
- `undefined`: autoText - Whether or not to automatically generate a text part for messages that are not given text
- `undefined`: autoHtml - Whether or not to automatically generate an HTML part for messages that are not given HTML
- `undefined`: bccAddress - An optional address to receive an exact copy of each recipient's email
- `undefined`: fromName - Optional from name to be used
- `undefined`: googleAnalyticsCampaign - Optional string indicating the value to set for the utm\_campaign tracking parameter. If this isn't provided the email's from address will be used instead.
- `undefined`: googleAnalyticsDomains - An array of strings separated by a comma (,) indicating for which any matching URLs will automatically have Google Analytics parameters appended to their query string automatically
- `undefined`: html - The html you want to send
- `undefined`: important - Whether or not this message is important, and should be delivered ahead of non-important messages
- `undefined`: inlineCss - Whether or not to automatically inline all CSS styles provided in the message HTML - only for HTML documents less than 256KB in size
- `undefined`: ipPool - The name of the dedicated ip pool that should be used to send the message. If you do not have any dedicated IPs, this parameter has no effect. If you specify a pool that does not exist, your default pool will be used instead.
- `undefined`: preserveRecipients - Whether or not to expose all recipients in to "To" header for each email
- `undefined`: returnPathDomain - A custom domain to use for the messages's return-path
- `undefined`: sendAt - When this message should be sent as a UTC timestamp in YYYY-MM-DD HH:MM:SS format. If you specify a time in the past, the message will be sent immediately. An additional fee applies for scheduled email, and this feature is only available to accounts with a positive balance.
- `undefined`: signingDomain - A custom domain to use for SPF/DKIM signing instead of mandrill(for "via" or "on behalf of" in email clients)
- `undefined`: subAccount - The unique ID of a subaccount for this message - must already exist or will fail with an error
- `undefined`: subject - Subject line of the email
- `undefined`: tags - An array of string separated by a comma (,) to tag the message with. Stats are accumulated using tags, though we only store the first 100 we see, so this should not be unique or change frequently. Tags should be 50 characters or less. Any tags starting with an underscore are reserved for internal use and will cause errors.
- `undefined`: text - Example text content
- `undefined`: trackClicks - Whether or not to turn on click tracking for the message
- `undefined`: trackOpens - Whether or not to turn on open tracking for the message
- `undefined`: trackingDomain - A custom domain to use for tracking opens and clicks instead of mandrillapp.com
- `undefined`: urlStripQs - Whether or not to strip the query string from URLs when aggregating tracked URL data
- `undefined`: viewContentLink - Whether to remove content logging for sensitive emails

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
  "name": "Mandrill",
  "type": "nodes-base.mandrill",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "template": "",
    "fromEmail": "",
    "toEmail": ""
  }
}
```

#### Send Template Example
```json
{
  "name": "Mandrill",
  "type": "nodes-base.mandrill",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "template": "",
    "fromEmail": "",
    "toEmail": "",
    "operation": "sendTemplate"
  }
}
```

#### Send HTML Example
```json
{
  "name": "Mandrill",
  "type": "nodes-base.mandrill",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "template": "",
    "fromEmail": "",
    "toEmail": "",
    "operation": "sendHtml"
  }
}
```

---

## Markdown

## Basic Information

- Node Type: `nodes-base.markdown`
- Category: output
- Package: n8n-nodes-base

### Description

Convert data between Markdown and HTML

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `html` | string | Yes | `""` | The HTML to be converted to markdown |
| `markdown` | string | Yes | `""` | The Markdown to be converted to html |
| `destinationKey` | string | Yes | `"data"` | The field to put the output in. Specify nested fields using dots, e.g."level1.level2.newKey". |
| `mode` | options | No | `"htmlToMarkdown"` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Mode (`mode`)

Optional values:
- `markdownToHtml`: Markdown to HTML - Convert data from Markdown to HTML
- `htmlToMarkdown`: HTML to Markdown - Convert data from HTML to Markdown

##### Options (`options`)

Optional values:
- `undefined`: bulletMarker - Specify bullet marker, default \*
- `undefined`: codeFence - Specify code block fence, default \`\`\`
- `undefined`: emDelimiter - Specify emphasis delimiter, default \_
- `undefined`: globalEscape - Setting this will override the default escape settings, you might want to use textReplace option instead
- `undefined`: ignore - Supplied elements will be ignored (ignores inner text does not parse children)
- `undefined`: keepDataImages - Whether to keep images with data: URI (Note: These can be up to 1MB each), e.g. &lt;img src="data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSK......0o/"&gt;
- `undefined`: lineStartEscape - Setting this will override the default escape settings, you might want to use textReplace option instead
- `undefined`: maxConsecutiveNewlines - Specify max consecutive new lines allowed
- `undefined`: useLinkReferenceDefinitions - Whether to Place URLS at the bottom and format links using link reference definitions
- `undefined`: strongDelimiter - Specify strong delimiter, default \*\*
- `undefined`: codeBlockStyle - Specify style for code block, default "fence"
- `undefined`: textReplace - User-defined text replacement pattern (Replaces matching text retrieved from nodes)
- `undefined`: blockElements - Supplied elements will be treated as blocks (surrounded with blank lines)

##### Options (`options`)

Optional values:
- `undefined`: openLinksInNewWindow - Whether to open all links in new windows (by adding the attribute target="\_blank" to \<a\> tags)
- `undefined`: simplifiedAutoLink - Whether to enable automatic linking to URLs
- `undefined`: backslashEscapesHTMLTags - Whether to support for HTML Tag escaping ex: &lt;div&gt;foo&lt;/div&gt;
- `undefined`: completeHTMLDocument - Whether to output a complete html document, including &lt;html&gt;, &lt;head&gt; and &lt;body&gt; tags instead of an HTML fragment
- `undefined`: customizedHeaderId - Whether to use text in curly braces as header ID
- `undefined`: emoji - Whether to enable emoji support. Ex: this is a :smile: emoji For more info on available emojis, see https://github.com/showdownjs/showdown/wiki/Emojis.
- `undefined`: encodeEmails - Whether to enable e-mail addresses encoding through the use of Character Entities, transforming ASCII e-mail addresses into its equivalent decimal entities
- `undefined`: excludeTrailingPunctuationFromURLs - Whether to exclude trailing punctuation from autolinking URLs. Punctuation excluded: . ! ? ( ). Only applies if simplifiedAutoLink option is set to true.
- `undefined`: ghCodeBlocks - Whether to enable support for GFM code block style
- `undefined`: ghCompatibleHeaderId - Whether to generate header IDs compatible with github style (spaces are replaced with dashes and a bunch of non alphanumeric chars are removed)
- `undefined`: ghMentionsLink - Whether to change the link generated by @mentions. Showdown will replace {u} with the username. Only applies if ghMentions option is enabled.
- `undefined`: ghMentions - Whether to enable github @mentions, which link to the username mentioned
- `undefined`: tasklists - Whether to enable support for GFM tasklists
- `undefined`: headerLevelStart - Whether to set the header starting level
- `undefined`: requireSpaceBeforeHeadingText - Whether to make adding a space between # and the header text mandatory
- `undefined`: literalMidWordAsterisks - Whether to stop showdown from interpreting asterisks in the middle of words as \<em\> and \<strong\> and instead treat them as literal asterisks
- `undefined`: literalMidWordUnderscores - Whether to stop showdown from interpreting underscores in the middle of words as \<em\> and \<strong\> and instead treat them as literal underscores
- `undefined`: noHeaderId - Whether to disable the automatic generation of header IDs
- `undefined`: parseImgDimensions - Whether to enable support for setting image dimensions from within markdown syntax
- `undefined`: prefixHeaderId - Add a prefix to the generated header IDs
- `undefined`: rawHeaderId - Whether to remove only spaces, ' and " from generated header IDs (including prefixes), replacing them with dashes (-)
- `undefined`: rawPrefixHeaderId - Whether to prevent showdown from modifying the prefix
- `undefined`: simpleLineBreaks - Whether to parse line breaks as &lt;br&gt;, like GitHub does, without needing 2 spaces at the end of the line
- `undefined`: smartIndentationFix - Whether to try to smartly fix indentation problems related to es6 template strings in the midst of indented code
- `undefined`: disableForced4SpacesIndentedSublists - Whether to disable the requirement of indenting sublists by 4 spaces for them to be nested, effectively reverting to the old behavior where 2 or 3 spaces were enough
- `undefined`: splitAdjacentBlockquotes - Whether to split adjacent blockquote blocks
- `undefined`: strikethrough - Whether to enable support for strikethrough syntax
- `undefined`: tablesHeaderId - Whether to add an ID property to table headers tags
- `undefined`: tables - Whether to enable support for tables syntax

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
  "name": "Markdown",
  "type": "nodes-base.markdown",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "html": "",
    "markdown": "",
    "destinationKey": "data"
  }
}
```

---

## Matrix

## Basic Information

- Node Type: `nodes-base.matrix`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Matrix API

### Available Operations

### Me
Get current user's account information
- Value: `me`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `mediaType` | options | Yes | `"image"` | Type of file being uploaded |
| `preset` | options | Yes | `"public_chat"` | - |
| `roomId` | string | Yes | `""` | The room related to the event |
| `eventId` | string | Yes | `""` | The room related to the event |
| `roomId` | options | Yes | `""` | Room ID to post. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `roomId` | options | Yes | `""` | The channel to send the message to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `roomId` | options | Yes | `""` | The token to start returning events from. This token can be obtained from a prev\_batch token returned for each room by the sync API. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `returnAll` | boolean | Yes | `false` | Whether to return all results or only up to a given limit |
| `roomId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `roomId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

#### Property Details

##### Media Type (`mediaType`)

Type of file being uploaded

Optional values:
- `file`: File - General file
- `image`: Image - Image media type
- `audio`: Audio - Audio media type
- `video`: Video - Video media type

##### Preset (`preset`)

Optional values:
- `private_chat`: Private Chat
- `public_chat`: Public Chat - Open and public chat

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
  "name": "Matrix",
  "type": "nodes-base.matrix",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "mediaType": "image",
    "preset": "public_chat",
    "roomId": "",
    "eventId": "",
    "returnAll": false
  }
}
```

#### Me Example
```json
{
  "name": "Matrix",
  "type": "nodes-base.matrix",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "mediaType": "image",
    "preset": "public_chat",
    "roomId": "",
    "eventId": "",
    "returnAll": false,
    "operation": "me"
  }
}
```

---

## Mattermost

## Basic Information

- Node Type: `nodes-base.mattermost`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Sends data to Mattermost

### Available Operations

### Add User
Add a user to a channel
- Value: `addUser`

### Create
Create a new channel
- Value: `create`

### Delete
Soft delete a channel
- Value: `delete`

### Member
Get a page of members for a channel
- Value: `members`

### Restore
Restores a soft deleted channel
- Value: `restore`

### Search
Search for a channel
- Value: `search`

### Statistics
Get statistics for a channel
- Value: `statistics`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `teamId` | options | Yes | `""` | The Mattermost Team. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `displayName` | string | Yes | `""` | The non-unique UI name for the channel |
| `channel` | string | Yes | `""` | The unique handle for the channel, will be present in the channel URL |
| `channelId` | options | Yes | `""` | The ID of the channel to soft delete. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `teamId` | options | Yes | `""` | The Mattermost Team. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `channelId` | options | Yes | `""` | The Mattermost Team. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `channelId` | string | Yes | `""` | The ID of the channel to restore |
| `channelId` | options | Yes | `""` | The ID of the channel to invite user to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `userId` | options | Yes | `""` | The ID of the user to invite into channel. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `channelId` | options | Yes | `""` | The ID of the channel to get the statistics from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

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
  "name": "Mattermost",
  "type": "nodes-base.mattermost",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "teamId": "",
    "displayName": "",
    "channel": "",
    "channelId": "",
    "userId": ""
  }
}
```

#### Add User Example
```json
{
  "name": "Mattermost",
  "type": "nodes-base.mattermost",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "teamId": "",
    "displayName": "",
    "channel": "",
    "channelId": "",
    "userId": "",
    "operation": "addUser"
  }
}
```

#### Create Example
```json
{
  "name": "Mattermost",
  "type": "nodes-base.mattermost",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "teamId": "",
    "displayName": "",
    "channel": "",
    "channelId": "",
    "userId": "",
    "operation": "create"
  }
}
```

---

## Mautic

## Basic Information

- Node Type: `nodes-base.mautic`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Mautic API

### Available Operations

### Create
Create a new company
- Value: `create`

### Delete
Delete a company
- Value: `delete`

### Get
Get data of a company
- Value: `get`

### Get Many
Get data of many companies
- Value: `getAll`

### Update
Update a company
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `channel` | options | Yes | `"email"` | - |
| `campaignEmailId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `segmentId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `campaignId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `segmentEmailId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `contactId` | string | Yes | `""` | - |
| `contactId` | string | Yes | `""` | - |
| `contactId` | string | Yes | `""` | - |
| `authentication` | options | No | `"credentials"` | - |
| `resource` | options | No | `"contact"` | - |

#### Property Details

##### Channel (`channel`)

Optional values:
- `email`: Email
- `sms`: SMS

##### Authentication (`authentication`)

Optional values:
- `credentials`: Credentials
- `oAuth2`: OAuth2

##### Resource (`resource`)

Optional values:
- `campaignContact`: Campaign Contact - Add/remove contacts to/from a campaign
- `company`: Company - Create or modify a company
- `companyContact`: Company Contact - Add/remove contacts to/from a company
- `contact`: Contact - Create & modify contacts
- `contactSegment`: Contact Segment - Add/remove contacts to/from a segment
- `segmentEmail`: Segment Email - Send an email

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
  "name": "Mautic",
  "type": "nodes-base.mautic",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "channel": "email",
    "campaignEmailId": "",
    "segmentId": "",
    "campaignId": "",
    "segmentEmailId": "",
    "contactId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Mautic",
  "type": "nodes-base.mautic",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "channel": "email",
    "campaignEmailId": "",
    "segmentId": "",
    "campaignId": "",
    "segmentEmailId": "",
    "contactId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Mautic",
  "type": "nodes-base.mautic",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "channel": "email",
    "campaignEmailId": "",
    "segmentId": "",
    "campaignId": "",
    "segmentEmailId": "",
    "contactId": "",
    "operation": "delete"
  }
}
```

---

## MCP Client Tool

## Basic Information

- Node Type: `nodes-langchain.mcpClientTool`
- Category: output
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Connect tools from an MCP Server

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `sseEndpoint` | string | Yes | `""` | SSE Endpoint of your MCP server |
| `endpointUrl` | string | Yes | `""` | Endpoint of your MCP server |
| `authentication` | options | No | `"none"` | The way to authenticate with your endpoint |
| `authentication` | options | No | `"none"` | The way to authenticate with your endpoint |
| `credentials` | credentials | No | `""` | - |
| `serverTransport` | options | No | `"sse"` | The transport used by your endpoint |
| `serverTransport` | options | No | `"httpStreamable"` | The transport used by your endpoint |
| `include` | options | No | `"all"` | How to select the tools you want to be exposed to the AI Agent |
| `options` | collection | No | `{}` | Additional options to add |
| `includeTools` | multiOptions | No | `[]` | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

#### Property Details

##### Authentication (`authentication`)

The way to authenticate with your endpoint

Optional values:
- `bearerAuth`: Bearer Auth
- `headerAuth`: Header Auth
- `none`: None

##### Authentication (`authentication`)

The way to authenticate with your endpoint

Optional values:
- `bearerAuth`: Bearer Auth
- `headerAuth`: Header Auth
- `mcpOAuth2Api`: MCP OAuth2
- `multipleHeadersAuth`: Multiple Headers Auth
- `none`: None

##### Server Transport (`serverTransport`)

The transport used by your endpoint

Optional values:
- `httpStreamable`: HTTP Streamable
- `sse`: Server Sent Events (Deprecated)

##### Server Transport (`serverTransport`)

The transport used by your endpoint

Optional values:
- `httpStreamable`: HTTP Streamable
- `sse`: Server Sent Events (Deprecated)

##### Tools to Include (`include`)

How to select the tools you want to be exposed to the AI Agent

Optional values:
- `all`: All - Also include all unchanged fields from the input
- `selected`: Selected - Also include the tools listed in the parameter "Tools to Include"
- `except`: All Except - Exclude the tools listed in the parameter "Tools to Exclude"

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: timeout - Time in ms to wait for tool calls to finish

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_tool` (tool)

### Can Connect To

1. AI Agent - via `ai_tool` connection
2. OpenAI Assistant - via `ai_tool` connection
3. MCP Server Trigger - via `ai_tool` connection
4. Tool Executor - via `ai_tool` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "MCP Client Tool",
  "type": "nodes-langchain.mcpClientTool",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "sseEndpoint": "",
    "endpointUrl": ""
  }
}
```

---

## Medium

## Basic Information

- Node Type: `nodes-base.medium`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Medium API

### Available Operations

### Create
Create a post
- Value: `create`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `contentFormat` | options | Yes | `""` | The format of the content to be posted |
| `title` | string | Yes | `""` | Title of the post. Max Length : 100 characters. |
| `content` | string | Yes | `""` | The body of the post, in a valid semantic HTML fragment, or Markdown |
| `authentication` | options | No | `"accessToken"` | - |
| `resource` | options | No | `"post"` | - |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"publication"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `publication` | boolean | No | `false` | Whether you are posting for a publication |
| `publicationId` | options | No | `""` | Publication IDs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

#### Property Details

##### Content Format (`contentFormat`)

The format of the content to be posted

Optional values:
- `html`: HTML
- `markdown`: Markdown

##### Authentication (`authentication`)

Optional values:
- `accessToken`: Access Token
- `oAuth2`: OAuth2

##### Resource (`resource`)

Optional values:
- `post`: Post
- `publication`: Publication

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a post

##### Operation (`operation`)

Optional values:
- `getAll`: Get Many - Get many publications

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: canonicalUrl - The original home of this content, if it was originally published elsewhere
- `undefined`: license - License of the post
- `undefined`: notifyFollowers - Whether to notify followers that the user has published
- `undefined`: publishStatus - The status of the post
- `undefined`: tags - Comma-separated strings to be used as tags for post classification. Max allowed tags: 5. Max tag length: 25 characters.

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
  "name": "Medium",
  "type": "nodes-base.medium",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contentFormat": "",
    "title": "",
    "content": ""
  }
}
```

#### Create Example
```json
{
  "name": "Medium",
  "type": "nodes-base.medium",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contentFormat": "",
    "title": "",
    "content": "",
    "operation": "create"
  }
}
```

---

## MessageBird

## Basic Information

- Node Type: `nodes-base.messageBird`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Sends SMS via MessageBird

### Available Operations

### Send
Send text messages (SMS)
- Value: `send`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `originator` | string | Yes | `""` | The number from which to send the message |
| `recipients` | string | Yes | `""` | All recipients separated by commas |
| `message` | string | Yes | `""` | The message to be send |
| `resource` | options | No | `"sms"` | - |
| `operation` | options | No | `"send"` | - |
| `operation` | options | No | `"get"` | - |
| `additionalFields` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `sms`: SMS
- `balance`: Balance

##### Operation (`operation`)

Optional values:
- `send`: Send - Send text messages (SMS)

##### Operation (`operation`)

Optional values:
- `get`: Get - Get the balance

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: createdDatetime - The date and time of the creation of the message in RFC3339 format (Y-m-dTH:i:sP)
- `undefined`: datacoding - Using unicode will limit the maximum number of characters to 70 instead of 160
- `undefined`: gateway - The SMS route that is used to send the message
- `undefined`: groupIds - Group IDs separated by commas, If provided recipients can be omitted
- `undefined`: mclass - Indicated the message type. 1 is a normal message, 0 is a flash message.
- `undefined`: reference - A client reference
- `undefined`: reportUrl - The status report URL to be used on a per-message basis. Reference is required for a status report webhook to be sent.
- `undefined`: scheduledDatetime - The scheduled date and time of the message in RFC3339 format (Y-m-dTH:i:sP)
- `undefined`: type - The type of message. Values can be: sms, binary, or flash.
- `undefined`: typeDetails - A hash with extra information. Is only used when a binary message is sent.
- `undefined`: validity - The amount of seconds that the message is valid

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
  "name": "MessageBird",
  "type": "nodes-base.messageBird",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "originator": "",
    "recipients": "",
    "message": ""
  }
}
```

#### Send Example
```json
{
  "name": "MessageBird",
  "type": "nodes-base.messageBird",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "originator": "",
    "recipients": "",
    "message": "",
    "operation": "send"
  }
}
```

---

## Monday.com

## Basic Information

- Node Type: `nodes-base.mondayCom`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Monday.com API

### Available Operations

### Archive
Archive a board
- Value: `archive`

### Create
Create a new board
- Value: `create`

### Get
Get a board
- Value: `get`

### Get Many
Get many boards
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `value` | string | Yes | `""` | The update text to add |
| `value` | json | Yes | `""` | The column value in JSON format. Documentation can be found <a href="https://monday.com/developers/v2#mutations-section-columns-change-column-value">here</a>. |
| `kind` | options | Yes | `""` | The board's kind (public / private / share) |
| `columnType` | options | Yes | `""` | - |
| `boardId` | options | Yes | `""` | Board unique identifiers. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `name` | string | Yes | `""` | The board's name |
| `boardId` | options | Yes | `""` | Board unique identifiers. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `boardId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `boardId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `boardId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

#### Property Details

##### Kind (`kind`)

The board's kind (public / private / share)

Optional values:
- `share`: Share
- `public`: Public
- `private`: Private

##### Column Type (`columnType`)

Optional values:
- `checkbox`: Checkbox
- `country`: Country
- `date`: Date
- `dropdown`: Dropdown
- `email`: Email
- `hour`: Hour
- `Link`: Link
- `longText`: Long Text
- `numbers`: Numbers
- `people`: People
- `person`: Person
- `phone`: Phone
- `rating`: Rating
- `status`: Status
- `tags`: Tags
- `team`: Team
- `text`: Text
- `timeline`: Timeline
- `timezone`: Timezone
- `week`: Week
- `worldClock`: World Clock

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
  "name": "Monday.com",
  "type": "nodes-base.mondayCom",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "kind": "",
    "columnType": "",
    "boardId": "",
    "name": ""
  }
}
```

#### Archive Example
```json
{
  "name": "Monday.com",
  "type": "nodes-base.mondayCom",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "kind": "",
    "columnType": "",
    "boardId": "",
    "name": "",
    "operation": "archive"
  }
}
```

#### Create Example
```json
{
  "name": "Monday.com",
  "type": "nodes-base.mondayCom",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "kind": "",
    "columnType": "",
    "boardId": "",
    "name": "",
    "operation": "create"
  }
}
```

---

## Netscaler ADC

## Basic Information

- Node Type: `nodes-base.citrixAdc`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Netscaler ADC API

### Available Operations

### Create
- Value: `create`

### Install
- Value: `install`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `certificateFormat` | options | Yes | `"PEM"` | Format in which the certificate is stored on the appliance |
| `caCertificateFileFormat` | options | Yes | `"PEM"` | Format of the CA certificate |
| `caPrivateKeyFileFormat` | options | Yes | `"PEM"` | Format of the CA certificate |
| `privateKeyFormat` | options | Yes | `"PEM"` | Format in which the key is stored on the appliance |
| `certificateFormat` | options | Yes | `"PEM"` | Input format of the certificate and the private-key files. The three formats supported by the appliance are: PEM - Privacy Enhanced Mail DER - Distinguished Encoding Rule PFX - Personal Information Exchange. |
| `certificateType` | options | Yes | `"ROOT_CERT"` | - |
| `certificateFileName` | string | Yes | `""` | Name for and, optionally, path to the generated certificate file. /nsconfig/ssl/ is the default path. |
| `certificateRequestFileName` | string | Yes | `""` | Name for and, optionally, path to the certificate-signing request (CSR). /nsconfig/ssl/ is the default path. |
| `caCertificateFileName` | string | Yes | `""` | Name of the CA certificate file that issues and signs the Intermediate-CA certificate or the end-user client and server certificates |
| `caPrivateKeyFileName` | string | Yes | `""` | Private key, associated with the CA certificate that is used to sign the Intermediate-CA certificate or the end-user client and server certificate. If the CA key file is password protected, the user is prompted to enter the pass phrase that was used to encrypt the key. |

#### Property Details

##### Certificate Format (`certificateFormat`)

Format in which the certificate is stored on the appliance

Optional values:
- `PEM`: PEM
- `DER`: DER

##### CA Certificate File Format (`caCertificateFileFormat`)

Format of the CA certificate

Optional values:
- `PEM`: PEM
- `DER`: DER

##### CA Private Key File Format (`caPrivateKeyFileFormat`)

Format of the CA certificate

Optional values:
- `PEM`: PEM
- `DER`: DER

##### Private Key Format (`privateKeyFormat`)

Format in which the key is stored on the appliance

Optional values:
- `PEM`: PEM
- `DER`: DER

##### Certificate Format (`certificateFormat`)

Input format of the certificate and the private-key files. The three formats supported by the appliance are: PEM - Privacy Enhanced Mail DER - Distinguished Encoding Rule PFX - Personal Information Exchange.

Optional values:
- `PEM`: PEM
- `DER`: DER

##### Certificate Type (`certificateType`)

Optional values:
- `ROOT_CERT`: Root-CA - You must specify the key file name. The generated Root-CA certificate can be used for signing end-user client or server certificates or to create Intermediate-CA certificates.
- `INTM_CERT`: Intermediate-CA - Intermediate-CA certificate
- `SRVR_CERT`: Server - SSL server certificate used on SSL servers for end-to-end encryption
- `CLNT_CERT`: Client - End-user client certificate used for client authentication

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
  "name": "Netscaler ADC",
  "type": "nodes-base.citrixAdc",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "certificateFormat": "PEM",
    "caCertificateFileFormat": "PEM",
    "caPrivateKeyFileFormat": "PEM",
    "privateKeyFormat": "PEM",
    "certificateType": "ROOT_CERT",
    "certificateFileName": "",
    "certificateRequestFileName": "",
    "caCertificateFileName": "",
    "caPrivateKeyFileName": ""
  }
}
```

#### Create Example
```json
{
  "name": "Netscaler ADC",
  "type": "nodes-base.citrixAdc",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "certificateFormat": "PEM",
    "caCertificateFileFormat": "PEM",
    "caPrivateKeyFileFormat": "PEM",
    "privateKeyFormat": "PEM",
    "certificateType": "ROOT_CERT",
    "certificateFileName": "",
    "certificateRequestFileName": "",
    "caCertificateFileName": "",
    "caPrivateKeyFileName": "",
    "operation": "create"
  }
}
```

#### Install Example
```json
{
  "name": "Netscaler ADC",
  "type": "nodes-base.citrixAdc",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "certificateFormat": "PEM",
    "caCertificateFileFormat": "PEM",
    "caPrivateKeyFileFormat": "PEM",
    "privateKeyFormat": "PEM",
    "certificateType": "ROOT_CERT",
    "certificateFileName": "",
    "certificateRequestFileName": "",
    "caCertificateFileName": "",
    "caPrivateKeyFileName": "",
    "operation": "install"
  }
}
```

---

## OpenThesaurus

## Basic Information

- Node Type: `nodes-base.openThesaurus`
- Category: output
- Package: n8n-nodes-base

### Description

Get synonmns for German words using the OpenThesaurus API

### Available Operations

### Get Synonyms
Get synonyms for a German word in German
- Value: `getSynonyms`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `text` | string | Yes | `""` | The word to get synonyms for |
| `operation` | options | No | `"getSynonyms"` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `getSynonyms`: Get Synonyms - Get synonyms for a German word in German

##### Options (`options`)

Optional values:
- `undefined`: baseform - Specifies the basic form for the search term if it is not already a basic form
- `undefined`: similar - This also returns up to five similarly written words for each answer. This is useful to be able to make a suggestion to the user in the event of a possible typing error.
- `undefined`: startswith - Like substring = true, but only finds words that begin with the specified search term
- `undefined`: substring - Whether up to ten words are returned for each answer that only contain the search term as a partial word
- `undefined`: substringFromResults - Specifies from which entry the partial word hits are to be returned. Only works together with substring = true.
- `undefined`: substringMaxResults - Specifies how many partial word hits should be returned in total. Only works together with substring = true.
- `undefined`: subsynsets - Whether each synonym group has its (optional) sub-terms supplied
- `undefined`: supersynsets - Whether each synonym group is supplied with its (optional) generic terms

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
  "name": "OpenThesaurus",
  "type": "nodes-base.openThesaurus",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "text": ""
  }
}
```

#### Get Synonyms Example
```json
{
  "name": "OpenThesaurus",
  "type": "nodes-base.openThesaurus",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "text": "",
    "operation": "getSynonyms"
  }
}
```

---

## Orbit

## Basic Information

- Node Type: `nodes-base.orbit`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Orbit API

### Available Operations

### Create
Create an activity for a member
- Value: `create`

### Get Many
Get many activities
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | Supply any URL and Orbit will do its best job to parse out a title, description, and image |
| `source` | options | Yes | `""` | Set to github, twitter, email, discourse or the source of any identities you've manually created |
| `searchBy` | options | Yes | `""` | - |
| `workspaceId` | options | Yes | `"Deprecated"` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `workspaceId` | options | Yes | `"Deprecated"` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `workspaceId` | options | Yes | `"Deprecated"` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `workspaceId` | options | Yes | `"Deprecated"` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `workspaceId` | options | Yes | `"Deprecated"` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `workspaceId` | options | Yes | `"Deprecated"` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `id` | string | Yes | `""` | The username at the source |

#### Property Details

##### Source (`source`)

Set to github, twitter, email, discourse or the source of any identities you've manually created

Optional values:
- `discourse`: Discourse
- `email`: Email
- `github`: GitHub
- `twitter`: Twitter

##### Search By (`searchBy`)

Optional values:
- `username`: Username
- `id`: ID

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
  "name": "Orbit",
  "type": "nodes-base.orbit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "source": "",
    "searchBy": "",
    "workspaceId": "Deprecated",
    "id": ""
  }
}
```

#### Create Example
```json
{
  "name": "Orbit",
  "type": "nodes-base.orbit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "source": "",
    "searchBy": "",
    "workspaceId": "Deprecated",
    "id": "",
    "operation": "create"
  }
}
```

#### Get Many Example
```json
{
  "name": "Orbit",
  "type": "nodes-base.orbit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "source": "",
    "searchBy": "",
    "workspaceId": "Deprecated",
    "id": "",
    "operation": "getAll"
  }
}
```

---

## Oura

## Basic Information

- Node Type: `nodes-base.oura`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Oura API

### Available Operations

### Get
Get the user's personal information
- Value: `get`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | No | `"summary"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"getSleep"` | - |
| `filters` | collection | No | `{}` | - |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `5` | Max number of results to return |

#### Property Details

##### Resource (`resource`)

Optional values:
- `profile`: Profile
- `summary`: Summary

##### Operation (`operation`)

Optional values:
- `get`: Get - Get the user's personal information

##### Operation (`operation`)

Optional values:
- `getActivity`: Get Activity Summary - Get the user's activity summary
- `getReadiness`: Get Readiness Summary - Get the user's readiness summary
- `getSleep`: Get Sleep Periods - Get the user's sleep summary

##### Filters (`filters`)

Optional values:
- `undefined`: end - End date for the summary retrieval. If omitted, it defaults to the current day.
- `undefined`: start - Start date for the summary retrieval. If omitted, it defaults to a week ago.

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
  "name": "Oura",
  "type": "nodes-base.oura",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Get Example
```json
{
  "name": "Oura",
  "type": "nodes-base.oura",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "get"
  }
}
```

---

## Paddle

## Basic Information

- Node Type: `nodes-base.paddle`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Paddle API

### Available Operations

### Create
Create a coupon
- Value: `create`

### Get Many
Get many coupons
- Value: `getAll`

### Update
Update a coupon
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `productIds` | multiOptions | Yes | `[]` | Comma-separated list of product IDs. Required if coupon\_type is product. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `productId` | string | Yes | `""` | The specific product/subscription ID |
| `paymentId` | options | Yes | `""` | The upcoming subscription payment ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `planId` | string | Yes | `""` | Filter: The subscription plan ID |
| `limit` | number | Yes | `100` | Max number of results to return |
| `resource` | options | No | `"coupon"` | - |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"getAll"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"getAll"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `coupon`: Coupon
- `payment`: Payment
- `plan`: Plan
- `product`: Product
- `user`: User

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a coupon
- `getAll`: Get Many - Get many coupons
- `update`: Update - Update a coupon

##### Operation (`operation`)

Optional values:
- `getAll`: Get Many - Get many payments
- `reschedule`: Reschedule - Reschedule payment

##### Operation (`operation`)

Optional values:
- `get`: Get - Get a plan
- `getAll`: Get Many - Get many plans

##### Operation (`operation`)

Optional values:
- `getAll`: Get Many - Get many products

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
  "name": "Paddle",
  "type": "nodes-base.paddle",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "productIds": [],
    "productId": "",
    "paymentId": "",
    "planId": "",
    "limit": 100
  }
}
```

#### Create Example
```json
{
  "name": "Paddle",
  "type": "nodes-base.paddle",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "productIds": [],
    "productId": "",
    "paymentId": "",
    "planId": "",
    "limit": 100,
    "operation": "create"
  }
}
```

#### Get Many Example
```json
{
  "name": "Paddle",
  "type": "nodes-base.paddle",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "productIds": [],
    "productId": "",
    "paymentId": "",
    "planId": "",
    "limit": 100,
    "operation": "getAll"
  }
}
```

---

## PagerDuty

## Basic Information

- Node Type: `nodes-base.pagerDuty`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume PagerDuty API

### Available Operations

### Create
Create an incident
- Value: `create`

### Get
Get an incident
- Value: `get`

### Get Many
Get many incidents
- Value: `getAll`

### Update
Update an incident
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `title` | string | Yes | `""` | A succinct description of the nature, symptoms, cause, or effect of the incident |
| `serviceId` | options | Yes | `""` | The incident will be created on this service. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `email` | string | Yes | `""` | The email address of a valid user associated with the account making the request |
| `incidentId` | string | Yes | `""` | Unique identifier for the incident |
| `incidentId` | string | Yes | `""` | Unique identifier for the incident |
| `email` | string | Yes | `""` | The email address of a valid user associated with the account making the request |
| `incidentId` | string | Yes | `""` | Unique identifier for the incident |
| `content` | string | Yes | `""` | The note content |
| `email` | string | Yes | `""` | The email address of a valid user associated with the account making the request |
| `incidentId` | string | Yes | `""` | Unique identifier for the incident |

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
  "name": "PagerDuty",
  "type": "nodes-base.pagerDuty",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "serviceId": "",
    "email": "",
    "incidentId": "",
    "content": ""
  }
}
```

#### Create Example
```json
{
  "name": "PagerDuty",
  "type": "nodes-base.pagerDuty",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "serviceId": "",
    "email": "",
    "incidentId": "",
    "content": "",
    "operation": "create"
  }
}
```

#### Get Example
```json
{
  "name": "PagerDuty",
  "type": "nodes-base.pagerDuty",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "serviceId": "",
    "email": "",
    "incidentId": "",
    "content": "",
    "operation": "get"
  }
}
```

---

## PayPal

## Basic Information

- Node Type: `nodes-base.payPal`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume PayPal API

### Available Operations

### Create
Create a batch payout
- Value: `create`

### Get
Show batch payout details
- Value: `get`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `senderBatchId` | string | Yes | `""` | A sender-specified ID number. Tracks the payout in an accounting system. |
| `payoutBatchId` | string | Yes | `""` | The ID of the payout for which to show details |
| `payoutItemId` | string | Yes | `""` | The ID of the payout item for which to show details |
| `payoutItemId` | string | Yes | `""` | The ID of the payout item to cancel |
| `resource` | options | No | `"payout"` | - |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"get"` | - |
| `itemsUi` | fixedCollection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |
| `itemsJson` | json | No | `""` | An array of individual payout items |

#### Property Details

##### Resource (`resource`)

Optional values:
- `payout`: Payout
- `payoutItem`: Payout Item

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a batch payout
- `get`: Get - Show batch payout details

##### Operation (`operation`)

Optional values:
- `cancel`: Cancel - Cancels an unclaimed payout item
- `get`: Get - Show payout item details

##### Items (`itemsUi`)

Optional values:
- `undefined`: itemsValues

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: emailSubject - The subject line for the email that PayPal sends when payment for a payout item completes. The subject line is the same for all recipients. Max length: 255 characters.
- `undefined`: emailMessage - The email message that PayPal sends when the payout item completes. The message is the same for all recipients.
- `undefined`: note - The payouts and item-level notes are concatenated in the email. Max length: 1000 characters.

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
  "name": "PayPal",
  "type": "nodes-base.payPal",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "senderBatchId": "",
    "payoutBatchId": "",
    "payoutItemId": ""
  }
}
```

#### Create Example
```json
{
  "name": "PayPal",
  "type": "nodes-base.payPal",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "senderBatchId": "",
    "payoutBatchId": "",
    "payoutItemId": "",
    "operation": "create"
  }
}
```

#### Get Example
```json
{
  "name": "PayPal",
  "type": "nodes-base.payPal",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "senderBatchId": "",
    "payoutBatchId": "",
    "payoutItemId": "",
    "operation": "get"
  }
}
```

---

## Peekalink

## Basic Information

- Node Type: `nodes-base.peekalink`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Peekalink API

### Available Operations

### Is Available
Check whether preview for a given link is available
- Value: `isAvailable`

### Preview
Return the preview for a link
- Value: `preview`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | - |
| `operation` | options | No | `"preview"` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `isAvailable`: Is Available - Check whether preview for a given link is available
- `preview`: Preview - Return the preview for a link

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
  "name": "Peekalink",
  "type": "nodes-base.peekalink",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": ""
  }
}
```

#### Is Available Example
```json
{
  "name": "Peekalink",
  "type": "nodes-base.peekalink",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "operation": "isAvailable"
  }
}
```

#### Preview Example
```json
{
  "name": "Peekalink",
  "type": "nodes-base.peekalink",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "operation": "preview"
  }
}
```

---

## ProfitWell

## Basic Information

- Node Type: `nodes-base.profitWell`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume ProfitWell API

### Available Operations

### Get Settings
Get your company's ProfitWell account settings
- Value: `getSetting`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `type` | options | Yes | `""` | - |
| `month` | string | Yes | `""` | Can only be the current or previous month. Format should be YYYY-MM. |
| `resource` | options | No | `"metric"` | - |
| `operation` | options | No | `"getSetting"` | - |
| `operation` | options | No | `"get"` | - |
| `options` | collection | No | `{}` | - |
| `simple` | boolean | No | `true` | Whether to return a simplified version of the response instead of the raw data |

#### Property Details

##### Type (`type`)

Optional values:
- `daily`: Daily - Retrieve financial metric broken down by day for either the current month or the last
- `monthly`: Monthly - Retrieve all monthly financial metric for your company

##### Resource (`resource`)

Optional values:
- `company`: Company
- `metric`: Metric

##### Operation (`operation`)

Optional values:
- `getSetting`: Get Settings - Get your company's ProfitWell account settings

##### Operation (`operation`)

Optional values:
- `get`: Get - Retrieve financial metric broken down by day for either the current month or the last

##### Options (`options`)

Optional values:
- `undefined`: plan_id - Only return the metric for this Plan ID. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: dailyMetrics - Comma-separated list of metric trends to return (the default is to return all metric)
- `undefined`: monthlyMetrics - Comma-separated list of metric trends to return (the default is to return all metric)

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
  "name": "ProfitWell",
  "type": "nodes-base.profitWell",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "type": "",
    "month": ""
  }
}
```

#### Get Settings Example
```json
{
  "name": "ProfitWell",
  "type": "nodes-base.profitWell",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "type": "",
    "month": "",
    "operation": "getSetting"
  }
}
```

---

## QuickChart

## Basic Information

- Node Type: `nodes-base.quickChart`
- Category: output
- Package: n8n-nodes-base

### Description

Create a chart via QuickChart

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `labelsUi` | fixedCollection | Yes | `{}` | Labels to use in the chart |
| `labelsArray` | string | Yes | `""` | The array of labels to be used in the chart |
| `data` | json | Yes | `""` | Data to use for the dataset, documentation and examples <a href="https://quickchart.io/documentation/chart-types/" target="\_blank">here</a> |
| `output` | string | Yes | `"data"` | The binary data will be displayed in the Output panel on the right, under the Binary tab |
| `chartType` | options | No | `"bar"` | The type of chart to create |
| `labelsMode` | options | No | `"manually"` | - |
| `chartOptions` | collection | No | `{}` | - |
| `datasetOptions` | collection | No | `{}` | - |

#### Property Details

##### Labels (`labelsUi`)

Labels to use in the chart

Optional values:
- `undefined`: labelsValues

##### Chart Type (`chartType`)

The type of chart to create

Optional values:
- `bar`: Bar Chart
- `doughnut`: Doughnut Chart
- `line`: Line Chart
- `pie`: Pie Chart
- `polarArea`: Polar Chart

##### Add Labels (`labelsMode`)

Optional values:
- `manually`: Manually
- `array`: From Array

##### Chart Options (`chartOptions`)

Optional values:
- `undefined`: backgroundColor - Background color of the chart
- `undefined`: devicePixelRatio - Pixel ratio of the chart
- `undefined`: format - File format of the resulting chart
- `undefined`: height - Height of the chart
- `undefined`: horizontal - Whether the chart should use its Y axis horizontal
- `undefined`: width - Width of the chart

##### Dataset Options (`datasetOptions`)

Optional values:
- `undefined`: backgroundColor - Color used for the background the dataset (area of a line graph, fill of a bar chart, etc.)
- `undefined`: borderColor - Color used for lines of the dataset
- `undefined`: fill - Whether to fill area of the dataset
- `undefined`: label - The label of the dataset
- `undefined`: pointStyle - Style to use for points of the dataset

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
  "name": "QuickChart",
  "type": "nodes-base.quickChart",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "labelsUi": {},
    "labelsArray": "",
    "data": "",
    "output": "data"
  }
}
```

---

## RocketChat

## Basic Information

- Node Type: `nodes-base.rocketchat`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume RocketChat API

### Available Operations

### Post Message
Post a message to a channel or a direct message
- Value: `postMessage`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `channel` | string | Yes | `""` | The channel name with the prefix in front of it |
| `resource` | options | No | `"chat"` | - |
| `operation` | options | No | `"postMessage"` | - |
| `options` | collection | No | `{}` | - |
| `attachments` | collection | No | `{}` | - |
| `text` | string | No | `""` | The text of the message to send, is optional because of attachments |
| `jsonParameters` | boolean | No | `false` | - |
| `attachmentsJson` | json | No | `""` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `chat`: Chat

##### Operation (`operation`)

Optional values:
- `postMessage`: Post Message - Post a message to a channel or a direct message

##### Options (`options`)

Optional values:
- `undefined`: alias - This will cause the message’s name to appear as the given alias, but your username will still display
- `undefined`: avatar - If provided, this will make the avatar use the provided image URL
- `undefined`: emoji - This will cause the message’s name to appear as the given alias, but your username will still display

##### Attachments (`attachments`)

Optional values:
- `undefined`: color - The color you want the order on the left side to be, any value background-css supports
- `undefined`: text - The text to display for this attachment, it is different than the message’s text
- `undefined`: ts - Displays the time next to the text portion
- `undefined`: thumbUrl - An image that displays to the left of the text, looks better when this is relatively small
- `undefined`: messageLink - Only applicable if the timestamp is provided, as it makes the time clickable to this link
- `undefined`: collapsed - Causes the image, audio, and video sections to be hiding when collapsed is true
- `undefined`: authorName - Name of the author
- `undefined`: authorLink - Providing this makes the author name clickable and points to this link
- `undefined`: authorIcon - Displays a tiny icon to the left of the Author’s name
- `undefined`: title - Title to display for this attachment, displays under the author
- `undefined`: titleLink - Providing this makes the title clickable, pointing to this link
- `undefined`: titleLinkDownload - When this is true, a download icon appears and clicking this saves the link to file
- `undefined`: imageUrl - The image to display, will be “big” and easy to see
- `undefined`: audioUrl - Audio file to play, only supports what html audio does
- `undefined`: videoUrl - Video file to play, only supports what html video does
- `undefined`: fields

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
  "name": "RocketChat",
  "type": "nodes-base.rocketchat",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "channel": ""
  }
}
```

#### Post Message Example
```json
{
  "name": "RocketChat",
  "type": "nodes-base.rocketchat",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "channel": "",
    "operation": "postMessage"
  }
}
```

---

## Salesforce

## Basic Information

- Node Type: `nodes-base.salesforce`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Salesforce API

### Available Operations

### Add Lead To Campaign
Add lead to a campaign
- Value: `addToCampaign`

### Add Note
Add note to a lead
- Value: `addNote`

### Create
Create a lead
- Value: `create`

### Create or Update
Create a new lead, or update the current one if it already exists (upsert)
- Value: `upsert`

### Delete
Delete a lead
- Value: `delete`

### Get
Get a lead
- Value: `get`

### Get Many
Get many leads
- Value: `getAll`

### Get Summary
Returns an overview of Lead's metadata
- Value: `getSummary`

### Update
Update a lead
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | A SOQL query. An example query parameter string might look like: “SELECT+Name+FROM+MyObject”. If the SOQL query string is invalid, a MALFORMED\_QUERY response is returned. |
| `externalId` | options | Yes | `""` | The field to check to see if the lead already exists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `externalIdValue` | string | Yes | `""` | If this value exists in the 'match against' field, update the lead. Otherwise create a new one. |
| `company` | string | Yes | `""` | Company of the lead. If person account record types have been enabled, and if the value of Company is null, the lead converts to a person account. |
| `lastname` | string | Yes | `""` | Required. Last name of the lead. Limited to 80 characters. |
| `leadId` | string | Yes | `""` | ID of Lead that needs to be fetched |
| `leadId` | string | Yes | `""` | ID of Lead that needs to be fetched |
| `leadId` | string | Yes | `""` | ID of Lead that needs to be fetched |
| `leadId` | string | Yes | `""` | ID of contact that needs to be fetched |
| `campaignId` | options | Yes | `""` | ID of the campaign that needs to be fetched. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

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
  "name": "Salesforce",
  "type": "nodes-base.salesforce",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "externalId": "",
    "externalIdValue": "",
    "company": "",
    "lastname": "",
    "leadId": "",
    "campaignId": ""
  }
}
```

#### Add Lead To Campaign Example
```json
{
  "name": "Salesforce",
  "type": "nodes-base.salesforce",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "externalId": "",
    "externalIdValue": "",
    "company": "",
    "lastname": "",
    "leadId": "",
    "campaignId": "",
    "operation": "addToCampaign"
  }
}
```

#### Add Note Example
```json
{
  "name": "Salesforce",
  "type": "nodes-base.salesforce",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "externalId": "",
    "externalIdValue": "",
    "company": "",
    "lastname": "",
    "leadId": "",
    "campaignId": "",
    "operation": "addNote"
  }
}
```

---

## Salesmate

## Basic Information

- Node Type: `nodes-base.salesmate`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Salesmate API

### Available Operations

### Create
Create a company
- Value: `create`

### Delete
Delete a company
- Value: `delete`

### Get
Get a company
- Value: `get`

### Get Many
Get many companies
- Value: `getAll`

### Update
Update a company
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `pipeline` | options | Yes | `""` | - |
| `status` | options | Yes | `"Open"` | - |
| `stage` | options | Yes | `""` | - |
| `owner` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `id` | string | Yes | `""` | If more than one company add them separated by , |
| `owner` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `type` | string | Yes | `""` | This field displays activity type such as call, meeting etc |
| `id` | string | Yes | `""` | If more than one activity add them separated by , |
| `owner` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `primaryContact` | options | Yes | `""` | Primary contact for the deal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

#### Property Details

##### Pipeline (`pipeline`)

Optional values:
- `Sales`: Sales

##### Status (`status`)

Optional values:
- `Open`: Open
- `Close`: Close
- `Lost`: Lost

##### Stage (`stage`)

Optional values:
- `New (Untouched)`: New (Untouched)
- `Contacted`: Contacted
- `Qualified`: Qualified
- `In Negotiation`: In Negotiation
- `Proposal Presented`: Proposal Presented

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
  "name": "Salesmate",
  "type": "nodes-base.salesmate",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "pipeline": "",
    "status": "Open",
    "stage": "",
    "owner": "",
    "id": "",
    "type": "",
    "primaryContact": ""
  }
}
```

#### Create Example
```json
{
  "name": "Salesmate",
  "type": "nodes-base.salesmate",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "pipeline": "",
    "status": "Open",
    "stage": "",
    "owner": "",
    "id": "",
    "type": "",
    "primaryContact": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Salesmate",
  "type": "nodes-base.salesmate",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "pipeline": "",
    "status": "Open",
    "stage": "",
    "owner": "",
    "id": "",
    "type": "",
    "primaryContact": "",
    "operation": "delete"
  }
}
```

---

## SeaTable

## Basic Information

- Node Type: `nodes-base.seaTable`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Read, update, write and delete data from SeaTable

### Available Operations

### Create
Create a new row
- Value: `create`

### Delete
Delete a row
- Value: `remove`

### Get
Get the content of a row
- Value: `get`

### Get Many
Get many rows from a table or a table view
- Value: `list`

### Lock
Lock a row to prevent further changes
- Value: `lock`

### Search
Search one or multiple rows
- Value: `search`

### Unlock
Remove the lock from a row
- Value: `unlock`

### Update
Update the content of a row
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `tableName` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `rowId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `searchColumn` | options | Yes | `""` | Select the column to be searched. Not all column types are supported for search. Choose from the list, or specify a name using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a>. |
| `searchTerm` | string | Yes | `""` | What to look for? |
| `searchString` | string | Yes | `""` | SeaTable identifies users with a unique username like 244b43hr6fy54bb4afa2c2cb7369d244@auth.local. Get this username from an email or the name of a collaborator. |
| `tableName` | options | Yes | `""` | Choose from the list, of specify by using an expression. Provide it in the way "table\_name:::table\_id". |
| `linkColumn` | options | Yes | `""` | Choose from the list of specify the Link Column by using an expression. You have to provide it in the way "column\_name:::link\_id:::other\_table\_id". |
| `linkColumnSourceId` | string | Yes | `""` | Provide the row ID of table you selected |
| `linkColumnTargetId` | string | Yes | `""` | Provide the row ID of table you want to link |
| `tableName` | options | Yes | `""` | Choose from the list, of specify by using an expression. Provide it in the way "table\_name:::table\_id". |

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
  "name": "SeaTable",
  "type": "nodes-base.seaTable",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "tableName": "",
    "rowId": "",
    "searchColumn": "",
    "searchTerm": "",
    "searchString": "",
    "linkColumn": "",
    "linkColumnSourceId": "",
    "linkColumnTargetId": ""
  }
}
```

#### Create Example
```json
{
  "name": "SeaTable",
  "type": "nodes-base.seaTable",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "tableName": "",
    "rowId": "",
    "searchColumn": "",
    "searchTerm": "",
    "searchString": "",
    "linkColumn": "",
    "linkColumnSourceId": "",
    "linkColumnTargetId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "SeaTable",
  "type": "nodes-base.seaTable",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "tableName": "",
    "rowId": "",
    "searchColumn": "",
    "searchTerm": "",
    "searchString": "",
    "linkColumn": "",
    "linkColumnSourceId": "",
    "linkColumnTargetId": "",
    "operation": "remove"
  }
}
```

---

## Segment

## Basic Information

- Node Type: `nodes-base.segment`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Segment API

### Available Operations

### Add
Add a user to a group
- Value: `add`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `groupId` | string | Yes | `""` | A Group ID is the unique identifier which you recognize a group by in your own database |
| `event` | string | Yes | `""` | Name of the action that a user has performed |
| `resource` | options | No | `"identify"` | - |
| `operation` | options | No | `"add"` | - |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"event"` | - |
| `traits` | fixedCollection | No | `{}` | - |
| `context` | fixedCollection | No | `{}` | - |
| `integrations` | fixedCollection | No | `{}` | - |
| `traits` | fixedCollection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `group`: Group - Group lets you associate an identified user with a group
- `identify`: Identify - Identify lets you tie a user to their actions
- `track`: Track - Track lets you record events

##### Operation (`operation`)

Optional values:
- `add`: Add - Add a user to a group

##### Operation (`operation`)

Optional values:
- `create`: Create - Create an identity

##### Operation (`operation`)

Optional values:
- `event`: Event - Record the actions your users perform. Every action triggers an event, which can also have associated properties.
- `page`: Page - Record page views on your website, along with optional extra information about the page being viewed

##### Traits (`traits`)

Optional values:
- `undefined`: traitsUi

##### Context (`context`)

Optional values:
- `undefined`: contextUi

##### Integration (`integrations`)

Optional values:
- `undefined`: integrationsUi

##### Traits (`traits`)

Optional values:
- `undefined`: traitsUi

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
  "name": "Segment",
  "type": "nodes-base.segment",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "groupId": "",
    "event": ""
  }
}
```

#### Add Example
```json
{
  "name": "Segment",
  "type": "nodes-base.segment",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "groupId": "",
    "event": "",
    "operation": "add"
  }
}
```

---

## Send Email

## Basic Information

- Node Type: `nodes-base.emailSend`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Sends an email using SMTP protocol

### Available Operations

### Send
- Value: `send`

### Send and Wait for Response
- Value: `sendAndWait`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `fromEmail` | string | Yes | `""` | Email address of the sender. You can also specify a name: Nathan Doe &lt;nate@n8n.io&gt;. |
| `toEmail` | string | Yes | `""` | Email address of the recipient. You can also specify a name: Nathan Doe &lt;nate@n8n.io&gt;. |
| `fromEmail` | string | Yes | `""` | Email address of the sender. You can also specify a name: Nathan Doe &lt;nate@n8n.io&gt;. |
| `toEmail` | string | Yes | `""` | Email address of the recipient. You can also specify a name: Nathan Doe &lt;nate@n8n.io&gt;. |
| `subject` | string | Yes | `""` | - |
| `message` | string | Yes | `""` | - |
| `resource` | hidden | No | `"email"` | - |
| `operation` | options | No | `"send"` | - |
| `emailFormat` | options | No | `"html"` | - |
| `emailFormat` | options | No | `"text"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `email`: Email

##### Operation (`operation`)

Optional values:
- `send`: Send
- `sendAndWait`: Send and Wait for Response

##### Email Format (`emailFormat`)

Optional values:
- `text`: Text - Send email as plain text
- `html`: HTML - Send email as HTML
- `both`: Both - Send both formats, recipient's client selects version to display

##### Email Format (`emailFormat`)

Optional values:
- `text`: Text
- `html`: HTML
- `both`: Both

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
  "name": "Send Email",
  "type": "nodes-base.emailSend",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fromEmail": "",
    "toEmail": "",
    "subject": "",
    "message": ""
  }
}
```

#### Send Example
```json
{
  "name": "Send Email",
  "type": "nodes-base.emailSend",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fromEmail": "",
    "toEmail": "",
    "subject": "",
    "message": "",
    "operation": "send"
  }
}
```

#### Send and Wait for Response Example
```json
{
  "name": "Send Email",
  "type": "nodes-base.emailSend",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fromEmail": "",
    "toEmail": "",
    "subject": "",
    "message": "",
    "operation": "sendAndWait"
  }
}
```

---

## Sentry.io

## Basic Information

- Node Type: `nodes-base.sentryIo`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Sentry.io API

### Available Operations

### Get
Get event by ID
- Value: `get`

### Get Many
Get many events
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | A URL that points to the release. This can be the path to an online interface to the sourcecode for instance. |
| `organizationSlug` | options | Yes | `""` | The slug of the organization the events belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `projectSlug` | options | Yes | `""` | The slug of the project the events belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `organizationSlug` | options | Yes | `""` | The slug of the organization the events belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `projectSlug` | options | Yes | `""` | The slug of the project the events belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `eventId` | string | Yes | `""` | The ID of the event to retrieve (either the numeric primary-key or the hexadecimal ID as reported by the raven client) |
| `issueId` | string | Yes | `""` | ID of issue to get |
| `organizationSlug` | options | Yes | `""` | The slug of the organization the issues belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `projectSlug` | options | Yes | `""` | The slug of the project the issues belong to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `issueId` | string | Yes | `""` | ID of issue to get |

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
  "name": "Sentry.io",
  "type": "nodes-base.sentryIo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "organizationSlug": "",
    "projectSlug": "",
    "eventId": "",
    "issueId": ""
  }
}
```

#### Get Example
```json
{
  "name": "Sentry.io",
  "type": "nodes-base.sentryIo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "organizationSlug": "",
    "projectSlug": "",
    "eventId": "",
    "issueId": "",
    "operation": "get"
  }
}
```

#### Get Many Example
```json
{
  "name": "Sentry.io",
  "type": "nodes-base.sentryIo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "organizationSlug": "",
    "projectSlug": "",
    "eventId": "",
    "issueId": "",
    "operation": "getAll"
  }
}
```

---

## ServiceNow

## Basic Information

- Node Type: `nodes-base.serviceNow`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume ServiceNow API

### Available Operations

### Upload
Upload an attachment to a specific table record
- Value: `upload`

### Delete
Delete an attachment
- Value: `delete`

### Get
Get an attachment
- Value: `get`

### Get Many
Get many attachments on a table
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `getOption` | options | Yes | `"id"` | Unique identifier of the user |
| `tableName` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `id` | string | Yes | `""` | Sys\_id of the record in the table specified in Table Name that you want to attach the file to |
| `inputDataFieldName` | string | Yes | `"data"` | Name of the binary property that contains the data to upload |
| `attachmentId` | string | Yes | `""` | Sys\_id value of the attachment to delete |
| `attachmentId` | string | Yes | `""` | Sys\_id value of the attachment to delete |
| `short_description` | string | Yes | `""` | Short description of the incident |
| `id` | string | Yes | `""` | Unique identifier of the incident |
| `id` | string | Yes | `""` | Unique identifier of the incident |
| `tableName` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

#### Property Details

##### Retrieve Identifier (`getOption`)

Unique identifier of the user

Optional values:
- `id`: ID
- `user_name`: Username

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
  "name": "ServiceNow",
  "type": "nodes-base.serviceNow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "getOption": "id",
    "tableName": "",
    "id": "",
    "inputDataFieldName": "data",
    "attachmentId": "",
    "short_description": ""
  }
}
```

#### Upload Example
```json
{
  "name": "ServiceNow",
  "type": "nodes-base.serviceNow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "getOption": "id",
    "tableName": "",
    "id": "",
    "inputDataFieldName": "data",
    "attachmentId": "",
    "short_description": "",
    "operation": "upload"
  }
}
```

#### Delete Example
```json
{
  "name": "ServiceNow",
  "type": "nodes-base.serviceNow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "getOption": "id",
    "tableName": "",
    "id": "",
    "inputDataFieldName": "data",
    "attachmentId": "",
    "short_description": "",
    "operation": "delete"
  }
}
```

---

## Shopify

## Basic Information

- Node Type: `nodes-base.shopify`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Shopify API

### Available Operations

### Create
Create an order
- Value: `create`

### Delete
Delete an order
- Value: `delete`

### Get
Get an order
- Value: `get`

### Get Many
Get many orders
- Value: `getAll`

### Update
Update an order
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `title` | string | Yes | `""` | The name of the product |
| `orderId` | string | Yes | `""` | - |
| `orderId` | string | Yes | `""` | - |
| `orderId` | string | Yes | `""` | - |
| `productId` | string | Yes | `""` | - |
| `productId` | string | Yes | `""` | - |
| `productId` | string | Yes | `""` | - |
| `authentication` | options | No | `"apiKey"` | - |
| `resource` | options | No | `"order"` | - |
| `operation` | options | No | `"create"` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `accessToken`: Access Token
- `oAuth2`: OAuth2
- `apiKey`: API Key

##### Resource (`resource`)

Optional values:
- `order`: Order
- `product`: Product

##### Operation (`operation`)

Optional values:
- `create`: Create - Create an order
- `delete`: Delete - Delete an order
- `get`: Get - Get an order
- `getAll`: Get Many - Get many orders
- `update`: Update - Update an order

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
  "name": "Shopify",
  "type": "nodes-base.shopify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "orderId": "",
    "productId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Shopify",
  "type": "nodes-base.shopify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "orderId": "",
    "productId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Shopify",
  "type": "nodes-base.shopify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "orderId": "",
    "productId": "",
    "operation": "delete"
  }
}
```

---

## Spontit

## Basic Information

- Node Type: `nodes-base.spontit`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Spontit API

### Available Operations

### Create
Create a push notification
- Value: `create`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | No | `"push"` | - |
| `operation` | options | No | `"create"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `content` | string | No | `""` | To provide text in a push, supply one of either "content" or "pushContent" (or both). Limited to 2500 characters. (Required if a value for "pushContent" is not provided). |

#### Property Details

##### Resource (`resource`)

Optional values:
- `push`: Push

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a push notification

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: channelName - The name of a channel you created. If you have not yet created a channel, simply don't provide this value and the push will be sent to your main account.
- `undefined`: expirationStamp - A Unix timestamp. When to automatically expire your push notification. The default is 10 days after pushing. The push will become unaccessible within 15-30 minutes of the selected time, but will remain on all device screens until dismissed or clicked.
- `undefined`: iOSDeepLink - An iOS deep link. Use this to deep link into other apps. Alternatively, you can provide a universal link in the link attribute and set openLinkInApp to false.
- `undefined`: link - A link that can be attached to your push. Must be a valid URL.
- `undefined`: openInHomeFeed - Whether the notification opens to the home feed or to a standalone page with the notification. The default (openInHomeFeed=False) is to open the notification on a standalone page.
- `undefined`: openLinkInApp - Whether to open the provided link within the iOS app or in Safari. Android PWA opens all links in the default web browser.
- `undefined`: pushToEmails - \<p\>Emails (strings) to whom to send the notification. If all three attributes 'pushToFollowers', 'pushToPhoneNumbers' and 'pushToEmails' are not supplied, then everyone who follows the channel will receive the push notification.\</p\>\<p\>If 'pushToFollowers' is supplied, only those listed in the array will receive the push notification.\</p\>\<p\>If one of the userIds supplied does not follow the specified channel, then that userId value will be ignored.\</p\>\<p\>See the "Followers" section to learn how to list the userIds of those who follow one of your channels.\</p\>.
- `undefined`: pushToFollowers - \<p\>User IDs (strings) to whom to send the notification. If all three attributes 'pushToFollowers', 'pushToPhoneNumbers' and 'pushToEmails' are not supplied, then everyone who follows the channel will receive the push notification.\</p\>\<p\>If 'pushToFollowers' is supplied, only those listed in the array will receive the push notification.\</p\>\<p\>If one of the userIds supplied does not follow the specified channel, then that userId value will be ignored.\</p\>\<p\>See the "Followers" section to learn how to list the userIds of those who follow one of your channels.\</p\>.
- `undefined`: pushToPhoneNumbers - \<p\>Phone numbers (strings) to whom to send the notification. If all three attributes 'pushToFollowers', 'pushToPhoneNumbers' and 'pushToEmails' are not supplied, then everyone who follows the channel will receive the push notification.\</p\>\<p\>If 'pushToFollowers' is supplied, only those listed in the array will receive the push notification.\</p\>\<p\>If one of the userIds supplied does not follow the specified channel, then that userId value will be ignored.\</p\>\<p\>See the "Followers" section to learn how to list the userIds of those who follow one of your channels.\</p\>.
- `undefined`: schedule - A Unix timestamp. Schedule a push to be sent at a later date and time.
- `undefined`: subtitle - The subtitle of your push. Limited to 20 characters. Only appears on iOS devices.
- `undefined`: pushTitle - The title of push. Appears in bold at the top. Limited to 100 characters.

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
  "name": "Spontit",
  "type": "nodes-base.spontit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Create Example
```json
{
  "name": "Spontit",
  "type": "nodes-base.spontit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "create"
  }
}
```

---

## Storyblok

## Basic Information

- Node Type: `nodes-base.storyblok`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Storyblok API

### Available Operations

### Get
Get a story
- Value: `get`

### Get Many
Get many stories
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `identifier` | string | Yes | `""` | The ID or slug of the story to get |
| `space` | options | Yes | `""` | The name of the space. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `storyId` | string | Yes | `""` | Numeric ID of the story |
| `space` | options | Yes | `""` | The name of the space. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `storyId` | string | Yes | `""` | Numeric ID of the story |
| `space` | options | Yes | `""` | The name of the space. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `space` | options | Yes | `""` | The name of the space. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `storyId` | string | Yes | `""` | Numeric ID of the story |
| `space` | options | Yes | `""` | The name of the space. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `storyId` | string | Yes | `""` | Numeric ID of the story |

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
  "name": "Storyblok",
  "type": "nodes-base.storyblok",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "identifier": "",
    "space": "",
    "storyId": ""
  }
}
```

#### Get Example
```json
{
  "name": "Storyblok",
  "type": "nodes-base.storyblok",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "identifier": "",
    "space": "",
    "storyId": "",
    "operation": "get"
  }
}
```

#### Get Many Example
```json
{
  "name": "Storyblok",
  "type": "nodes-base.storyblok",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "identifier": "",
    "space": "",
    "storyId": "",
    "operation": "getAll"
  }
}
```

---

## SyncroMSP

## Basic Information

- Node Type: `nodes-base.syncroMsp`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Manage contacts, tickets and more from Syncro MSP

### Available Operations

### Create
Create new customer
- Value: `create`

### Delete
Delete customer
- Value: `delete`

### Get
Retrieve customer
- Value: `get`

### Get Many
Retrieve many customers
- Value: `getAll`

### Update
Update customer
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `customerId` | string | Yes | `""` | Get specific customer by ID |
| `customerId` | string | Yes | `""` | Delete a specific customer by ID |
| `ticketId` | string | Yes | `""` | Delete a specific customer by ID |
| `contactId` | string | Yes | `""` | Get specific contact by ID |
| `contactId` | string | Yes | `""` | Delete a specific contact by ID |
| `alertId` | string | Yes | `""` | Get specific RMM alert by ID |
| `alertId` | string | Yes | `""` | Delete the RMM alert by ID |
| `alertId` | string | Yes | `""` | Mute the RMM alert by ID |
| `customerId` | string | Yes | `""` | - |
| `subject` | string | Yes | `""` | - |

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
  "name": "SyncroMSP",
  "type": "nodes-base.syncroMsp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "customerId": "",
    "ticketId": "",
    "contactId": "",
    "alertId": "",
    "subject": ""
  }
}
```

#### Create Example
```json
{
  "name": "SyncroMSP",
  "type": "nodes-base.syncroMsp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "customerId": "",
    "ticketId": "",
    "contactId": "",
    "alertId": "",
    "subject": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "SyncroMSP",
  "type": "nodes-base.syncroMsp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "customerId": "",
    "ticketId": "",
    "contactId": "",
    "alertId": "",
    "subject": "",
    "operation": "delete"
  }
}
```

---

## Todoist

## Basic Information

- Node Type: `nodes-base.todoist`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Todoist API

### Available Operations

### Close
Close a task
- Value: `close`

### Create
Create a new task
- Value: `create`

### Delete
Delete a task
- Value: `delete`

### Get
Get a task
- Value: `get`

### Get Many
Get many tasks
- Value: `getAll`

### Move
Move a task
- Value: `move`

### Quick Add
Quick add a task using natural language
- Value: `quickAdd`

### Reopen
Reopen a task
- Value: `reopen`

### Update
Update a task
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"task"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"create"` | - |
| `dueDateType` | options | Yes | `"natural_language"` | How to specify when the reminder should trigger |
| `project` | resourceLocator | Yes | `{"mode":"list","value":""}` | The destination project. Choose from the list, or specify an ID. |
| `content` | string | Yes | `""` | Task content |

#### Property Details

##### Resource (`resource`)

Optional values:
- `task`: Task - Task resource
- `project`: Project - Project resource
- `section`: Section - Section resource
- `comment`: Comment - Comment resource
- `label`: Label - Label resource
- `reminder`: Reminder - Reminder resource

##### Operation (`operation`)

Optional values:
- `close`: Close - Close a task
- `create`: Create - Create a new task
- `delete`: Delete - Delete a task
- `get`: Get - Get a task
- `getAll`: Get Many - Get many tasks
- `move`: Move - Move a task
- `quickAdd`: Quick Add - Quick add a task using natural language
- `reopen`: Reopen - Reopen a task
- `update`: Update - Update a task

##### Operation (`operation`)

Optional values:
- `archive`: Archive - Archive a project
- `create`: Create - Create a new project
- `delete`: Delete - Delete a project
- `get`: Get - Get a project
- `getCollaborators`: Get Collaborators - Get project collaborators
- `getAll`: Get Many - Get many projects
- `unarchive`: Unarchive - Unarchive a project
- `update`: Update - Update a project

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new section
- `delete`: Delete - Delete a section
- `get`: Get - Get a section
- `getAll`: Get Many - Get many sections
- `update`: Update - Update a section

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new comment
- `delete`: Delete - Delete a comment
- `get`: Get - Get a comment
- `getAll`: Get Many - Get many comments
- `update`: Update - Update a comment

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new label
- `delete`: Delete - Delete a label
- `get`: Get - Get a label
- `getAll`: Get Many - Get many labels
- `update`: Update - Update a label

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new reminder
- `delete`: Delete - Delete a reminder
- `getAll`: Get Many - Get many reminders
- `update`: Update - Update a reminder

##### Due Date Type (`dueDateType`)

How to specify when the reminder should trigger

Optional values:
- `natural_language`: Natural Language - Human-readable date and time (e.g., "tomorrow 2pm")
- `full_day`: Full-Day Date - Date without specific time (floating)
- `floating_time`: Floating Date with Time - Date and time without timezone
- `fixed_timezone`: Fixed Timezone Date with Time - Date and time with specific timezone

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
  "name": "Todoist",
  "type": "nodes-base.todoist",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "task",
    "operation": "create",
    "dueDateType": "natural_language",
    "project": {
      "mode": "list",
      "value": ""
    },
    "content": ""
  }
}
```

#### Close Example
```json
{
  "name": "Todoist",
  "type": "nodes-base.todoist",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "task",
    "operation": "close",
    "dueDateType": "natural_language",
    "project": {
      "mode": "list",
      "value": ""
    },
    "content": ""
  }
}
```

#### Create Example
```json
{
  "name": "Todoist",
  "type": "nodes-base.todoist",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "task",
    "operation": "create",
    "dueDateType": "natural_language",
    "project": {
      "mode": "list",
      "value": ""
    },
    "content": ""
  }
}
```

---

## TravisCI

## Basic Information

- Node Type: `nodes-base.travisCi`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume TravisCI API

### Available Operations

### Cancel
Cancel a build
- Value: `cancel`

### Get
Get a build
- Value: `get`

### Get Many
Get many builds
- Value: `getAll`

### Restart
Restart a build
- Value: `restart`

### Trigger
Trigger a build
- Value: `trigger`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | No | `"build"` | - |
| `operation` | options | No | `"cancel"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |
| `buildId` | string | No | `""` | Value uniquely identifying the build |
| `buildId` | string | No | `""` | Value uniquely identifying the build |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `100` | Max number of results to return |
| `buildId` | string | No | `""` | Value uniquely identifying the build |

#### Property Details

##### Resource (`resource`)

Optional values:
- `build`: Build

##### Operation (`operation`)

Optional values:
- `cancel`: Cancel - Cancel a build
- `get`: Get - Get a build
- `getAll`: Get Many - Get many builds
- `restart`: Restart - Restart a build
- `trigger`: Trigger - Trigger a build

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: include - List of attributes to eager load

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: include - List of attributes to eager load
- `undefined`: order - You may specify order to sort your response
- `undefined`: sortBy

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: message - Travis-ci status message attached to the request
- `undefined`: mergeMode

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
  "name": "TravisCI",
  "type": "nodes-base.travisCi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Cancel Example
```json
{
  "name": "TravisCI",
  "type": "nodes-base.travisCi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "cancel"
  }
}
```

#### Get Example
```json
{
  "name": "TravisCI",
  "type": "nodes-base.travisCi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "get"
  }
}
```

---

## Uplead

## Basic Information

- Node Type: `nodes-base.uplead`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Uplead API

### Available Operations

### Enrich
- Value: `enrich`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | No | `"company"` | - |
| `operation` | options | No | `"enrich"` | - |
| `operation` | options | No | `"enrich"` | - |
| `company` | string | No | `""` | The name of the company (e.g – amazon) |
| `domain` | string | No | `""` | The domain name (e.g – amazon.com) |
| `email` | string | No | `""` | Email address (e.g – mbenioff@salesforce.com) |
| `firstname` | string | No | `""` | First name of the person (e.g – Marc) |
| `lastname` | string | No | `""` | Last name of the person (e.g – Benioff) |
| `domain` | string | No | `""` | The domain name (e.g – salesforce.com) |

#### Property Details

##### Resource (`resource`)

Optional values:
- `company`: Company - Company API lets you lookup company data via a domain name or company name
- `person`: Person - Person API lets you lookup a person based on an email address OR based on a domain name + first name + last name

##### Operation (`operation`)

Optional values:
- `enrich`: Enrich

##### Operation (`operation`)

Optional values:
- `enrich`: Enrich

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
  "name": "Uplead",
  "type": "nodes-base.uplead",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Enrich Example
```json
{
  "name": "Uplead",
  "type": "nodes-base.uplead",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "enrich"
  }
}
```

---

## uProc

## Basic Information

- Node Type: `nodes-base.uproc`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume uProc API

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `field` | options | Yes | `""` | The "Field" value to use as a parameter for this Operation |
| `url` | string | Yes | `""` | The "Url" value to use as a parameter for this Operation |
| `gender` | options | Yes | `""` | The "Gender" value to use as a parameter for this Operation |
| `language` | options | Yes | `""` | The "Language" value to use as a parameter for this Operation |
| `bcid` | options | Yes | `""` | The "Bcid" value to use as a parameter for this Operation |
| `coin` | options | Yes | `""` | The "Coin" value to use as a parameter for this Operation |
| `isocode1` | options | Yes | `""` | The "Isocode1" value to use as a parameter for this Operation |
| `isocode2` | options | Yes | `""` | The "Isocode2" value to use as a parameter for this Operation |
| `period` | options | Yes | `""` | The "Period" value to use as a parameter for this Operation |
| `mode` | options | Yes | `""` | The "Mode" value to use as a parameter for this Operation |

#### Property Details

##### Field (`field`)

The "Field" value to use as a parameter for this Operation

Optional values:
- `alphabetic`: Alphabetic
- `alphanumeric`: Alphanumeric
- `cif`: Cif
- `city`: City
- `country`: Country
- `date`: Date
- `decimal`: Decimal
- `dni`: Dni
- `domain`: Domain
- `email`: Email
- `gender`: Gender
- `integer`: Integer
- `ip`: Ip
- `mobile`: Mobile
- `name`: Name
- `nie`: Nie
- `nif`: Nif
- `phone`: Phone
- `province`: Province
- `zipcode`: Zipcode

##### Gender (`gender`)

The "Gender" value to use as a parameter for this Operation

Optional values:
- `female`: Female
- `male`: Male

##### Language (`language`)

The "Language" value to use as a parameter for this Operation

Optional values:
- `american`: American
- `arabic`: Arabic
- `bengali`: Bengali
- `british`: British
- `czech`: Czech
- `danish`: Danish
- `dutch`: Dutch
- `filipino`: Filipino
- `finnish`: Finnish
- `french`: French
- `german`: German
- `greek`: Greek
- `gujurati`: Gujurati
- `hindi`: Hindi
- `hungarian`: Hungarian
- `indonesian`: Indonesian
- `italian`: Italian
- `japanese`: Japanese
- `kannada`: Kannada
- `korean`: Korean
- `malayalam`: Malayalam
- `mandarin`: Mandarin
- `norwegian`: Norwegian
- `polish`: Polish
- `portuguese`: Portuguese
- `russian`: Russian
- `slovak`: Slovak
- `spanish`: Spanish
- `tamil`: Tamil
- `telugu`: Telugu
- `thai`: Thai
- `turkish`: Turkish
- `ukranian`: Ukranian
- `vietnamese`: Vietnamese

##### Bcid (`bcid`)

The "Bcid" value to use as a parameter for this Operation

Optional values:
- `auspost`: Auspost
- `azteccode`: Azteccode
- `azteccodecompact`: Azteccodecompact
- `aztecrune`: Aztecrune
- `bc412`: Bc412
- `channelcode`: Channelcode
- `codablockf`: Codablockf
- `code11`: Code11
- `code128`: Code128
- `code16k`: Code16k
- `code2of5`: Code2of5
- `code32`: Code32
- `code39`: Code39
- `code39ext`: Code39ext
- `code49`: Code49
- `code93`: Code93
- `code93ext`: Code93ext
- `codeone`: Codeone
- `coop2of5`: Coop2of5
- `daft`: Daft
- `databarexpanded`: Databarexpanded
- `databarexpandedcomposite`: Databarexpandedcomposite
- `databarexpandedstacked`: Databarexpandedstacked
- `databarexpandedstackedcomposite`: Databarexpandedstackedcomposite
- `databarlimited`: Databarlimited
- `databarlimitedcomposite`: Databarlimitedcomposite
- `databaromni`: Databaromni
- `databaromnicomposite`: Databaromnicomposite
- `databarstacked`: Databarstacked
- `databarstackedcomposite`: Databarstackedcomposite
- `databarstackedomni`: Databarstackedomni
- `databarstackedomnicomposite`: Databarstackedomnicomposite
- `databartruncated`: Databartruncated
- `databartruncatedcomposite`: Databartruncatedcomposite
- `datalogic2of5`: Datalogic2of5
- `datamatrix`: Datamatrix
- `datamatrixrectangular`: Datamatrixrectangular
- `dotcode`: Dotcode
- `ean13`: Ean13
- `ean13composite`: Ean13composite
- `ean14`: Ean14
- `ean2`: Ean2
- `ean5`: Ean5
- `ean8`: Ean8
- `ean8composite`: Ean8composite
- `flattermarken`: Flattermarken
- `gs1-128`: Gs1-128
- `gs1-128composite`: Gs1-128composite
- `gs1-cc`: Gs1-cc
- `gs1datamatrix`: Gs1datamatrix
- `gs1datamatrixrectangular`: Gs1datamatrixrectangular
- `gs1northamericancoupon`: Gs1northamericancoupon
- `hanxin`: Hanxin
- `hibcazteccode`: Hibcazteccode
- `hibccodablockf`: Hibccodablockf
- `hibccode128`: Hibccode128
- `hibccode39`: Hibccode39
- `hibcdatamatrix`: Hibcdatamatrix
- `hibcdatamatrixrectangular`: Hibcdatamatrixrectangular
- `hibcmicropdf417`: Hibcmicropdf417
- `hibcpdf417`: Hibcpdf417
- `iata2of5`: Iata2of5
- `identcode`: Identcode
- `industrial2of5`: Industrial2of5
- `interleaved2of5`: Interleaved2of5
- `isbn`: Isbn
- `ismn`: Ismn
- `issn`: Issn
- `itf14`: Itf14
- `japanpost`: Japanpost
- `kix`: Kix
- `leitcode`: Leitcode
- `matrix2of5`: Matrix2of5
- `maxicode`: Maxicode
- `micropdf417`: Micropdf417
- `msi`: Msi
- `onecode`: Onecode
- `pdf417`: Pdf417
- `pdf417compact`: Pdf417compact
- `pharmacode`: Pharmacode
- `pharmacode2`: Pharmacode2
- `planet`: Planet
- `plessey`: Plessey
- `posicode`: Posicode
- `postnet`: Postnet
- `pzn`: Pzn
- `rationalizedCodabar`: RationalizedCodabar
- `raw`: Raw
- `royalmail`: Royalmail
- `sscc18`: Sscc18
- `symbol`: Symbol
- `telepen`: Telepen
- `telepennumeric`: Telepennumeric
- `ultracode`: Ultracode
- `upca`: Upca
- `upcacomposite`: Upcacomposite
- `upce`: Upce
- `upcecomposite`: Upcecomposite

##### Coin (`coin`)

The "Coin" value to use as a parameter for this Operation

Optional values:
- `0x`: 0x
- `Aave Coin`: Aave Coin
- `Algorand`: Algorand
- `Aragon`: Aragon
- `Augur`: Augur
- `AugurV2`: AugurV2
- `AuroraCoin`: AuroraCoin
- `BTU Protocol`: BTU Protocol
- `Bancor`: Bancor
- `Bankex`: Bankex
- `Basic Attention Token`: Basic Attention Token
- `BeaverCoin`: BeaverCoin
- `BioCoin`: BioCoin
- `Bitcoin`: Bitcoin
- `Bitcoin SV`: Bitcoin SV
- `BitcoinCash`: BitcoinCash
- `BitcoinGold`: BitcoinGold
- `BitcoinPrivate`: BitcoinPrivate
- `BitcoinZ`: BitcoinZ
- `BlockTrade`: BlockTrade
- `CUSD`: CUSD
- `Callisto`: Callisto
- `Cardano`: Cardano
- `Chainlink`: Chainlink
- `Civic`: Civic
- `Compound`: Compound
- `Cred`: Cred
- `Crypto.com Coin`: Crypto.com Coin
- `Dash`: Dash
- `Decentraland`: Decentraland
- `Decred`: Decred
- `DigiByte`: DigiByte
- `District0x`: District0x
- `DogeCoin`: DogeCoin
- `EOS`: EOS
- `Enjin Coin`: Enjin Coin
- `EtherZero`: EtherZero
- `Ethereum`: Ethereum
- `EthereumClassic`: EthereumClassic
- `Expanse`: Expanse
- `FirmaChain`: FirmaChain
- `FreiCoin`: FreiCoin
- `GameCredits`: GameCredits
- `GarliCoin`: GarliCoin
- `Gnosis`: Gnosis
- `Golem`: Golem
- `Golem (GNT)`: Golem (GNT)
- `HedgeTrade`: HedgeTrade
- `Hush`: Hush
- `HyperSpace`: HyperSpace
- `Komodo`: Komodo
- `LBRY Credits`: LBRY Credits
- `Lisk`: Lisk
- `LiteCoin`: LiteCoin
- `Loom Network`: Loom Network
- `Maker`: Maker
- `Matchpool`: Matchpool
- `Matic`: Matic
- `MegaCoin`: MegaCoin
- `Melon`: Melon
- `Metal`: Metal
- `MonaCoin`: MonaCoin
- `Monero`: Monero
- `Multi-collateral DAI`: Multi-collateral DAI
- `NameCoin`: NameCoin
- `Nano`: Nano
- `Nem`: Nem
- `Neo`: Neo
- `NeoGas`: NeoGas
- `Numeraire`: Numeraire
- `Ocean Protocol`: Ocean Protocol
- `Odyssey`: Odyssey
- `OmiseGO`: OmiseGO
- `PIVX`: PIVX
- `Paxos`: Paxos
- `PeerCoin`: PeerCoin
- `Polkadot`: Polkadot
- `Polymath`: Polymath
- `PrimeCoin`: PrimeCoin
- `ProtoShares`: ProtoShares
- `Qtum`: Qtum
- `Quant`: Quant
- `Quantum Resistant Ledger`: Quantum Resistant Ledger
- `RaiBlocks`: RaiBlocks
- `Ripio Credit Network`: Ripio Credit Network
- `Ripple`: Ripple
- `SOLVE`: SOLVE
- `Salt`: Salt
- `Serve`: Serve
- `Siacoin`: Siacoin
- `SnowGem`: SnowGem
- `SolarCoin`: SolarCoin
- `Spendcoin`: Spendcoin
- `Status`: Status
- `Stellar`: Stellar
- `Storj`: Storj
- `Storm`: Storm
- `StormX`: StormX
- `Swarm City`: Swarm City
- `Synthetix Network`: Synthetix Network
- `TEMCO`: TEMCO
- `Tap`: Tap
- `TenX`: TenX
- `Tether`: Tether
- `Tezos`: Tezos
- `Tron`: Tron
- `TrueUSD`: TrueUSD
- `USD Coin`: USD Coin
- `Uniswap Coin`: Uniswap Coin
- `VeChain`: VeChain
- `VertCoin`: VertCoin
- `Viberate`: Viberate
- `VoteCoin`: VoteCoin
- `Waves`: Waves
- `Wings`: Wings
- `ZCash`: ZCash
- `ZClassic`: ZClassic
- `ZenCash`: ZenCash
- `iExec RLC`: IExec RLC
- `loki`: Loki

##### Isocode1 (`isocode1`)

The "Isocode1" value to use as a parameter for this Operation

Optional values:
- `AUD`: AUD
- `BGN`: BGN
- `BRL`: BRL
- `CAD`: CAD
- `CHF`: CHF
- `CNY`: CNY
- `CZK`: CZK
- `DKK`: DKK
- `EUR`: EUR
- `GBP`: GBP
- `HKD`: HKD
- `HRK`: HRK
- `HUF`: HUF
- `IDR`: IDR
- `ILS`: ILS
- `INR`: INR
- `ISK`: ISK
- `JPY`: JPY
- `KRW`: KRW
- `MXN`: MXN
- `MYR`: MYR
- `NOK`: NOK
- `NZD`: NZD
- `PHP`: PHP
- `PLN`: PLN
- `RON`: RON
- `RUB`: RUB
- `SEK`: SEK
- `SGD`: SGD
- `THB`: THB
- `TRY`: TRY
- `USD`: USD
- `ZAR`: ZAR

##### Isocode2 (`isocode2`)

The "Isocode2" value to use as a parameter for this Operation

Optional values:
- `AUD`: AUD
- `BGN`: BGN
- `BRL`: BRL
- `CAD`: CAD
- `CHF`: CHF
- `CNY`: CNY
- `CZK`: CZK
- `DKK`: DKK
- `EUR`: EUR
- `GBP`: GBP
- `HKD`: HKD
- `HRK`: HRK
- `HUF`: HUF
- `IDR`: IDR
- `ILS`: ILS
- `INR`: INR
- `ISK`: ISK
- `JPY`: JPY
- `KRW`: KRW
- `MXN`: MXN
- `MYR`: MYR
- `NOK`: NOK
- `NZD`: NZD
- `PHP`: PHP
- `PLN`: PLN
- `RON`: RON
- `RUB`: RUB
- `SEK`: SEK
- `SGD`: SGD
- `THB`: THB
- `TRY`: TRY
- `USD`: USD
- `ZAR`: ZAR

##### Period (`period`)

The "Period" value to use as a parameter for this Operation

Optional values:
- `days`: Days
- `hours`: Hours
- `minutes`: Minutes
- `seconds`: Seconds

##### Mode (`mode`)

The "Mode" value to use as a parameter for this Operation

Optional values:
- `guess`: Guess
- `only_verify`: Only_verify
- `verify`: Verify

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
  "name": "uProc",
  "type": "nodes-base.uproc",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "field": "",
    "url": "",
    "gender": "",
    "language": "",
    "bcid": "",
    "coin": "",
    "isocode1": "",
    "isocode2": "",
    "period": "",
    "mode": ""
  }
}
```

---

## UptimeRobot

## Basic Information

- Node Type: `nodes-base.uptimeRobot`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume UptimeRobot API

### Available Operations

### Get
Get account details
- Value: `get`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | The URL/IP of the monitor |
| `value` | string | Yes | `""` | The correspondent value for the alert contact type |
| `type` | options | Yes | `""` | The type of the monitor |
| `type` | options | Yes | `""` | The type of the alert contact |
| `type` | options | Yes | `""` | The type of the maintenance window |
| `friendlyName` | string | Yes | `""` | The friendly name of the monitor |
| `id` | string | Yes | `""` | The ID of the monitor |
| `id` | string | Yes | `""` | The ID of the monitor |
| `friendlyName` | string | Yes | `""` | The friendly name of the alert contact |
| `id` | string | Yes | `""` | The ID of the alert contact |

#### Property Details

##### Type (`type`)

The type of the monitor

Optional values:
- `5`: Heartbeat
- `1`: HTTP(S)
- `2`: Keyword
- `3`: Ping
- `4`: Port

##### Type (`type`)

The type of the alert contact

Optional values:
- `4`: Boxcar
- `2`: E-Mail
- `6`: Pushbullet
- `9`: Pushover
- `1`: SMS
- `3`: Twitter DM
- `5`: Webhook

##### Type (`type`)

The type of the maintenance window

Optional values:
- `1`: Once
- `2`: Daily
- `3`: Weekly
- `4`: Monthly

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
  "name": "UptimeRobot",
  "type": "nodes-base.uptimeRobot",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "value": "",
    "type": "",
    "friendlyName": "",
    "id": ""
  }
}
```

#### Get Example
```json
{
  "name": "UptimeRobot",
  "type": "nodes-base.uptimeRobot",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "value": "",
    "type": "",
    "friendlyName": "",
    "id": "",
    "operation": "get"
  }
}
```

---

## Vero

## Basic Information

- Node Type: `nodes-base.vero`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Vero API

### Available Operations

### Add Tags
Adds a tag to a users profile
- Value: `addTags`

### Alias
Change a users identifier
- Value: `alias`

### Create or Update
Create or update a user profile
- Value: `create`

### Delete
Delete a user
- Value: `delete`

### Re-Subscribe
Resubscribe a user
- Value: `resubscribe`

### Remove Tags
Removes a tag from a users profile
- Value: `removeTags`

### Unsubscribe
Unsubscribe a user
- Value: `unsubscribe`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `id` | string | Yes | `""` | The unique identifier of the customer |
| `id` | string | Yes | `""` | The old unique identifier of the user |
| `newId` | string | Yes | `""` | The new unique identifier of the user |
| `id` | string | Yes | `""` | The unique identifier of the user |
| `id` | string | Yes | `""` | The unique identifier of the user |
| `id` | string | Yes | `""` | The unique identifier of the user |
| `id` | string | Yes | `""` | The unique identifier of the user |
| `tags` | string | Yes | `""` | Tags to add separated by "," |
| `id` | string | Yes | `""` | The unique identifier of the user |
| `tags` | string | Yes | `""` | Tags to remove separated by "," |

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
  "name": "Vero",
  "type": "nodes-base.vero",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "id": "",
    "newId": "",
    "tags": ""
  }
}
```

#### Add Tags Example
```json
{
  "name": "Vero",
  "type": "nodes-base.vero",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "id": "",
    "newId": "",
    "tags": "",
    "operation": "addTags"
  }
}
```

#### Alias Example
```json
{
  "name": "Vero",
  "type": "nodes-base.vero",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "id": "",
    "newId": "",
    "tags": "",
    "operation": "alias"
  }
}
```

---

## WhatsApp Business Cloud

## Basic Information

- Node Type: `nodes-base.whatsApp`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Access WhatsApp API

### Available Operations

### Send
- Value: `send`

### Send and Wait for Response
- Value: `sendAndWait`

### Send Template
- Value: `sendTemplate`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `phoneNumberId` | options | Yes | `""` | The ID of the business account's phone number from which the message will be sent from |
| `recipientPhoneNumber` | string | Yes | `""` | Phone number of the recipient of the message |
| `textBody` | string | Yes | `""` | The body of the message (max 4096 characters) |
| `mediaPropertyName` | string | Yes | `"data"` | The name of the input field containing the binary file data to be uploaded |
| `mediaFilename` | string | Yes | `""` | The name of the file (required when using a file ID) |
| `template` | options | Yes | `""` | Name of the template |
| `phoneNumberId` | options | Yes | `""` | The ID of the business account's phone number to store the media |
| `mediaPropertyName` | string | Yes | `"data"` | Name of the binary property which contains the data for the file to be uploaded |
| `mediaGetId` | string | Yes | `""` | The ID of the media |
| `mediaDeleteId` | string | Yes | `""` | The ID of the media |

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
  "name": "WhatsApp Business Cloud",
  "type": "nodes-base.whatsApp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "phoneNumberId": "",
    "recipientPhoneNumber": "",
    "textBody": "",
    "mediaPropertyName": "data",
    "mediaFilename": "",
    "template": "",
    "mediaGetId": "",
    "mediaDeleteId": ""
  }
}
```

#### Send Example
```json
{
  "name": "WhatsApp Business Cloud",
  "type": "nodes-base.whatsApp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "phoneNumberId": "",
    "recipientPhoneNumber": "",
    "textBody": "",
    "mediaPropertyName": "data",
    "mediaFilename": "",
    "template": "",
    "mediaGetId": "",
    "mediaDeleteId": "",
    "operation": "send"
  }
}
```

#### Send and Wait for Response Example
```json
{
  "name": "WhatsApp Business Cloud",
  "type": "nodes-base.whatsApp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "phoneNumberId": "",
    "recipientPhoneNumber": "",
    "textBody": "",
    "mediaPropertyName": "data",
    "mediaFilename": "",
    "template": "",
    "mediaGetId": "",
    "mediaDeleteId": "",
    "operation": "sendAndWait"
  }
}
```

---

## WooCommerce

## Basic Information

- Node Type: `nodes-base.wooCommerce`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume WooCommerce API

### Available Operations

### Create
Create a customer
- Value: `create`

### Delete
Delete a customer
- Value: `delete`

### Get
Retrieve a customer
- Value: `get`

### Get Many
Retrieve many customers
- Value: `getAll`

### Update
Update a customer
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `customerId` | string | Yes | `""` | ID of the customer to delete |
| `customerId` | string | Yes | `""` | ID of the customer to retrieve |
| `customerId` | string | Yes | `""` | ID of the customer to update |
| `name` | string | Yes | `""` | Product name |
| `email` | string | Yes | `""` | - |
| `resource` | options | No | `"product"` | - |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"create"` | - |
| `dimensionsUi` | fixedCollection | No | `{}` | Product dimensions |

#### Property Details

##### Resource (`resource`)

Optional values:
- `customer`: Customer
- `order`: Order
- `product`: Product

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a customer
- `delete`: Delete - Delete a customer
- `get`: Get - Retrieve a customer
- `getAll`: Get Many - Retrieve many customers
- `update`: Update - Update a customer

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a product
- `delete`: Delete - Delete a product
- `get`: Get - Get a product
- `getAll`: Get Many - Get many products
- `update`: Update - Update a product

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a order
- `delete`: Delete - Delete a order
- `get`: Get - Get a order
- `getAll`: Get Many - Get many orders
- `update`: Update - Update a order

##### Dimensions (`dimensionsUi`)

Product dimensions

Optional values:
- `undefined`: dimensionsValues

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
  "name": "WooCommerce",
  "type": "nodes-base.wooCommerce",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "customerId": "",
    "name": "",
    "email": ""
  }
}
```

#### Create Example
```json
{
  "name": "WooCommerce",
  "type": "nodes-base.wooCommerce",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "customerId": "",
    "name": "",
    "email": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "WooCommerce",
  "type": "nodes-base.wooCommerce",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "customerId": "",
    "name": "",
    "email": "",
    "operation": "delete"
  }
}
```

---

## Wordpress

## Basic Information

- Node Type: `nodes-base.wordpress`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Wordpress API

### Available Operations

### Create
Create a post
- Value: `create`

### Get
Get a post
- Value: `get`

### Get Many
Get many posts
- Value: `getAll`

### Update
Update a post
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `title` | string | Yes | `""` | The title for the post |
| `postId` | string | Yes | `""` | Unique identifier for the object |
| `postId` | string | Yes | `""` | Unique identifier for the object |
| `postId` | string | Yes | `""` | Unique identifier for the object |
| `title` | string | Yes | `""` | The title for the page |
| `pageId` | string | Yes | `""` | Unique identifier for the object |
| `pageId` | string | Yes | `""` | Unique identifier for the object |
| `pageId` | string | Yes | `""` | Unique identifier for the object |
| `username` | string | Yes | `""` | Login name for the user |
| `name` | string | Yes | `""` | Display name for the user |

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
  "name": "Wordpress",
  "type": "nodes-base.wordpress",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "postId": "",
    "pageId": "",
    "username": "",
    "name": ""
  }
}
```

#### Create Example
```json
{
  "name": "Wordpress",
  "type": "nodes-base.wordpress",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "postId": "",
    "pageId": "",
    "username": "",
    "name": "",
    "operation": "create"
  }
}
```

#### Get Example
```json
{
  "name": "Wordpress",
  "type": "nodes-base.wordpress",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "postId": "",
    "pageId": "",
    "username": "",
    "name": "",
    "operation": "get"
  }
}
```

---

## Write Binary File

## Basic Information

- Node Type: `nodes-base.writeBinaryFile`
- Category: output
- Package: n8n-nodes-base

### Description

Writes a binary file to disk

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `fileName` | string | Yes | `""` | Path to which the file should be written |
| `dataPropertyName` | string | Yes | `"data"` | Name of the binary property which contains the data for the file to be written |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: append - Whether to append to an existing file

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
  "name": "Write Binary File",
  "type": "nodes-base.writeBinaryFile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fileName": "",
    "dataPropertyName": "data"
  }
}
```

---

## X (Formerly Twitter)

## Basic Information

- Node Type: `nodes-base.twitter`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the X API

### Available Operations

### Create
Send a direct message to a user
- Value: `create`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `user` | resourceLocator | Yes | `{"mode":"username","value":""}` | The user you want to send the message to |
| `text` | string | Yes | `""` | The text of the direct message. URL encoding is required. Max length of 10,000 characters. |
| `list` | resourceLocator | Yes | `{"mode":"id","value":""}` | The list you want to add the user to |
| `user` | resourceLocator | Yes | `{"mode":"username","value":""}` | The user you want to add to the list |
| `text` | string | Yes | `""` | The text of the status update. URLs must be encoded. Links wrapped with the t.co shortener will affect character count |
| `tweetDeleteId` | resourceLocator | Yes | `{"mode":"id","value":""}` | The tweet to delete |
| `tweetId` | resourceLocator | Yes | `{"mode":"id","value":""}` | The tweet to like |
| `searchText` | string | Yes | `""` | A UTF-8, URL-encoded search query of 500 characters maximum, including operators. Queries may additionally be limited by complexity. Check the searching examples <a href="https://developer.twitter.com/en/docs/tweets/search/guides/standard-operators">here</a>. |
| `tweetId` | resourceLocator | Yes | `{"mode":"id","value":""}` | The tweet to retweet |
| `user` | resourceLocator | Yes | `{"mode":"username","value":""}` | The user you want to search |

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
  "name": "X (Formerly Twitter)",
  "type": "nodes-base.twitter",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "user": {
      "mode": "username",
      "value": ""
    },
    "text": "",
    "list": {
      "mode": "id",
      "value": ""
    },
    "tweetDeleteId": {
      "mode": "id",
      "value": ""
    },
    "tweetId": {
      "mode": "id",
      "value": ""
    },
    "searchText": ""
  }
}
```

#### Create Example
```json
{
  "name": "X (Formerly Twitter)",
  "type": "nodes-base.twitter",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "user": {
      "mode": "username",
      "value": ""
    },
    "text": "",
    "list": {
      "mode": "id",
      "value": ""
    },
    "tweetDeleteId": {
      "mode": "id",
      "value": ""
    },
    "tweetId": {
      "mode": "id",
      "value": ""
    },
    "searchText": "",
    "operation": "create"
  }
}
```

---

## Xero

## Basic Information

- Node Type: `nodes-base.xero`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Xero API

### Available Operations

### Create
Create a contact
- Value: `create`

### Get
Get a contact
- Value: `get`

### Get Many
Get many contacts
- Value: `getAll`

### Update
Update a contact
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `type` | options | Yes | `""` | Invoice Type |
| `organizationId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `name` | string | Yes | `""` | Full name of contact/organisation |
| `organizationId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `organizationId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `organizationId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `organizationId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `organizationId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `organizationId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `organizationId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

#### Property Details

##### Type (`type`)

Invoice Type

Optional values:
- `ACCPAY`: Bill - Accounts Payable or supplier invoice
- `ACCREC`: Sales Invoice - Accounts Receivable or customer invoice

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
  "name": "Xero",
  "type": "nodes-base.xero",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "type": "",
    "organizationId": "",
    "name": ""
  }
}
```

#### Create Example
```json
{
  "name": "Xero",
  "type": "nodes-base.xero",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "type": "",
    "organizationId": "",
    "name": "",
    "operation": "create"
  }
}
```

#### Get Example
```json
{
  "name": "Xero",
  "type": "nodes-base.xero",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "type": "",
    "organizationId": "",
    "name": "",
    "operation": "get"
  }
}
```

---

## Zendesk

## Basic Information

- Node Type: `nodes-base.zendesk`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Zendesk API

### Available Operations

### Create
Create a ticket
- Value: `create`

### Delete
Delete a ticket
- Value: `delete`

### Get
Get a ticket
- Value: `get`

### Get Many
Get many tickets
- Value: `getAll`

### Recover
Recover a suspended ticket
- Value: `recover`

### Update
Update a ticket
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `ticketType` | options | Yes | `"regular"` | - |
| `description` | string | Yes | `""` | The first comment on the ticket |
| `id` | string | Yes | `""` | Ticket ID |
| `id` | string | Yes | `""` | Ticket ID |
| `name` | string | Yes | `""` | The user's name |
| `id` | string | Yes | `""` | - |
| `id` | string | Yes | `""` | - |
| `id` | string | Yes | `""` | - |
| `id` | string | Yes | `""` | - |
| `ticketFieldId` | string | Yes | `""` | - |

#### Property Details

##### Ticket Type (`ticketType`)

Optional values:
- `regular`: Regular
- `suspended`: Suspended

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
  "name": "Zendesk",
  "type": "nodes-base.zendesk",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "ticketType": "regular",
    "description": "",
    "id": "",
    "name": "",
    "ticketFieldId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Zendesk",
  "type": "nodes-base.zendesk",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "ticketType": "regular",
    "description": "",
    "id": "",
    "name": "",
    "ticketFieldId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Zendesk",
  "type": "nodes-base.zendesk",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "ticketType": "regular",
    "description": "",
    "id": "",
    "name": "",
    "ticketFieldId": "",
    "operation": "delete"
  }
}
```

---

## Zulip

## Basic Information

- Node Type: `nodes-base.zulip`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Zulip API

### Available Operations

### Delete
Delete a message
- Value: `delete`

### Get
Get a message
- Value: `get`

### Send Private
Send a private message
- Value: `sendPrivate`

### Send to Stream
Send a message to stream
- Value: `sendStream`

### Update
Update a message
- Value: `update`

### Upload a File
- Value: `updateFile`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `subscriptions` | fixedCollection | Yes | `{}` | A list of dictionaries containing the the key name and value specifying the name of the stream to subscribe. If the stream does not exist a new stream is created. |
| `to` | multiOptions | Yes | `[]` | The destination stream, or a comma-separated list containing the usernames (emails) of the recipients. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `content` | string | Yes | `""` | The content of the message |
| `stream` | options | Yes | `""` | The destination stream, or a comma-separated list containing the usernames (emails) of the recipients. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `topic` | options | Yes | `""` | The topic of the message. Only required if type is stream, ignored otherwise. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `content` | string | Yes | `""` | The content of the message |
| `messageId` | string | Yes | `""` | Unique identifier for the message |
| `messageId` | string | Yes | `""` | Unique identifier for the message |
| `messageId` | string | Yes | `""` | Unique identifier for the message |
| `streamId` | string | Yes | `""` | ID of stream to update |

#### Property Details

##### Subscriptions (`subscriptions`)

A list of dictionaries containing the the key name and value specifying the name of the stream to subscribe. If the stream does not exist a new stream is created.

Optional values:
- `undefined`: properties

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
  "name": "Zulip",
  "type": "nodes-base.zulip",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "subscriptions": {},
    "to": [],
    "content": "",
    "stream": "",
    "topic": "",
    "messageId": "",
    "streamId": ""
  }
}
```

#### Delete Example
```json
{
  "name": "Zulip",
  "type": "nodes-base.zulip",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "subscriptions": {},
    "to": [],
    "content": "",
    "stream": "",
    "topic": "",
    "messageId": "",
    "streamId": "",
    "operation": "delete"
  }
}
```

#### Get Example
```json
{
  "name": "Zulip",
  "type": "nodes-base.zulip",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "subscriptions": {},
    "to": [],
    "content": "",
    "stream": "",
    "topic": "",
    "messageId": "",
    "streamId": "",
    "operation": "get"
  }
}
```
