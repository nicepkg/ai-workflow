# Data Transformation Nodes - Node Collection (Part 1)

This file contains complete information for 100 nodes.

## Table of Contents

- [Azure Cosmos DB](#azure-cosmos-db)
- [Azure Storage](#azure-storage)
- [BambooHR](#bamboohr)
- [Bitwarden](#bitwarden)
- [Brevo](#brevo)
- [Bubble](#bubble)
- [Clockify](#clockify)
- [Compare Datasets](#compare-datasets)
- [Compression](#compression)
- [Convert to/from binary data](#convert-tofrom-binary-data)
- [Copper](#copper)
- [Cortex](#cortex)
- [crowd.dev](#crowddev)
- [Crypto](#crypto)
- [Customer Datastore (n8n training)](#customer-datastore-n8n-training)
- [Customer Messenger (n8n training)](#customer-messenger-n8n-training)
- [Date & Time](#date--time)
- [Dropcontact](#dropcontact)
- [Edit Image](#edit-image)
- [Elastic Security](#elastic-security)
- [Elasticsearch](#elasticsearch)
- [Evaluation](#evaluation)
- [Execute Command](#execute-command)
- [Execute Sub-workflow](#execute-sub-workflow)
- [Facebook Graph API](#facebook-graph-api)
- [Filter](#filter)
- [Freshservice](#freshservice)
- [Freshworks CRM](#freshworks-crm)
- [Function Item](#function-item)
- [Git](#git)
- [Gong](#gong)
- [Google Ads](#google-ads)
- [Google Analytics](#google-analytics)
- [Google Cloud Storage](#google-cloud-storage)
- [Google Perspective](#google-perspective)
- [GoToWebinar](#gotowebinar)
- [Grafana](#grafana)
- [Hacker News](#hacker-news)
- [HighLevel](#highlevel)
- [HTML](#html)
- [HTML Extract](#html-extract)
- [Jina AI](#jina-ai)
- [JWT](#jwt)
- [Kafka](#kafka)
- [KoBoToolbox](#kobotoolbox)
- [Ldap](#ldap)
- [Lemlist](#lemlist)
- [LoneScale](#lonescale)
- [Mailcheck](#mailcheck)
- [Marketstack](#marketstack)
- [Metabase](#metabase)
- [Microsoft Entra ID](#microsoft-entra-id)
- [Microsoft Graph Security](#microsoft-graph-security)
- [Microsoft Outlook](#microsoft-outlook)
- [Microsoft SharePoint](#microsoft-sharepoint)
- [MISP](#misp)
- [Mistral AI](#mistral-ai)
- [Mocean](#mocean)
- [Monica CRM](#monica-crm)
- [MSG91](#msg91)
- [n8n](#n8n)
- [NASA](#nasa)
- [Netlify](#netlify)
- [Odoo](#odoo)
- [Okta](#okta)
- [One Simple API](#one-simple-api)
- [Perplexity](#perplexity)
- [Pipedrive](#pipedrive)
- [Plivo](#plivo)
- [PostBin](#postbin)
- [QuickBooks Online](#quickbooks-online)
- [RabbitMQ](#rabbitmq)
- [Raindrop](#raindrop)
- [Reddit](#reddit)
- [Rename Keys](#rename-keys)
- [Respond to Webhook](#respond-to-webhook)
- [Rundeck](#rundeck)
- [SecurityScorecard](#securityscorecard)
- [SendGrid](#sendgrid)
- [seven](#seven)
- [SIGNL4](#signl4)
- [Splunk](#splunk)
- [Spreadsheet File](#spreadsheet-file)
- [Stackby](#stackby)
- [Stripe](#stripe)
- [Switch](#switch)
- [Taiga](#taiga)
- [Tapfiliate](#tapfiliate)
- [TheHive](#thehive)
- [TheHive 5](#thehive-5)
- [TOTP](#totp)
- [Trello](#trello)
- [Twake](#twake)
- [Twilio](#twilio)
- [Unleashed Software](#unleashed-software)
- [urlscan.io](#urlscanio)
- [Webex by Cisco](#webex-by-cisco)
- [Webflow](#webflow)
- [Wekan](#wekan)
- [Wise](#wise)

---

## Azure Cosmos DB

## Basic Information

- Node Type: `nodes-base.azureCosmosDb`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Interact with Azure Cosmos DB API

### Available Operations

### Create
Create a container
- Value: `create`

### Delete
Delete a container
- Value: `delete`

### Get
Retrieve a container
- Value: `get`

### Get Many
Retrieve a list of containers
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | The SQL query to execute. Use $1, $2, $3, etc., to reference the 'Query Parameters' set in the options below. |
| `containerCreate` | string | Yes | `""` | Unique identifier for the new container |
| `partitionKey` | json | Yes | `"{\n\t\"paths\": [\n\t\t\"/id\"\n\t],\n\t\"kind\": \"Hash\",\n\t\"version\": 2\n}"` | The partition key is used to automatically distribute data across partitions for scalability. Choose a property in your JSON document that has a wide range of values and evenly distributes request volume. |
| `container` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the container you want to delete |
| `container` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the container you want to retrieve |
| `container` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the container you want to use |
| `customProperties` | json | Yes | `"{\n\t\"id\": \"replace_with_new_document_id\"\n}"` | The item contents as a JSON object |
| `container` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the container you want to use |
| `item` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the item to be deleted |
| `container` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the container you want to use |

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
  "name": "Azure Cosmos DB",
  "type": "nodes-base.azureCosmosDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "containerCreate": "",
    "partitionKey": "{\n\t\"paths\": [\n\t\t\"/id\"\n\t],\n\t\"kind\": \"Hash\",\n\t\"version\": 2\n}",
    "container": {
      "mode": "list",
      "value": ""
    },
    "customProperties": "{\n\t\"id\": \"replace_with_new_document_id\"\n}",
    "item": {
      "mode": "list",
      "value": ""
    }
  }
}
```

#### Create Example
```json
{
  "name": "Azure Cosmos DB",
  "type": "nodes-base.azureCosmosDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "containerCreate": "",
    "partitionKey": "{\n\t\"paths\": [\n\t\t\"/id\"\n\t],\n\t\"kind\": \"Hash\",\n\t\"version\": 2\n}",
    "container": {
      "mode": "list",
      "value": ""
    },
    "customProperties": "{\n\t\"id\": \"replace_with_new_document_id\"\n}",
    "item": {
      "mode": "list",
      "value": ""
    },
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Azure Cosmos DB",
  "type": "nodes-base.azureCosmosDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "containerCreate": "",
    "partitionKey": "{\n\t\"paths\": [\n\t\t\"/id\"\n\t],\n\t\"kind\": \"Hash\",\n\t\"version\": 2\n}",
    "container": {
      "mode": "list",
      "value": ""
    },
    "customProperties": "{\n\t\"id\": \"replace_with_new_document_id\"\n}",
    "item": {
      "mode": "list",
      "value": ""
    },
    "operation": "delete"
  }
}
```

---

## Azure Storage

## Basic Information

- Node Type: `nodes-base.azureStorage`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Interact with Azure Storage API

### Available Operations

### Create
Create a new blob or replace an existing one
- Value: `create`

### Delete
Delete a blob
- Value: `delete`

### Get
Retrieve data for a specific blob
- Value: `get`

### Get Many
Retrieve a list of blobs
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | URL where to read of the blob contents from |
| `from` | options | Yes | `"binary"` | - |
| `container` | resourceLocator | Yes | `{"mode":"list","value":""}` | Container to create or replace a blob in |
| `blobCreate` | string | Yes | `""` | The name of the new or existing blob |
| `binaryPropertyName` | string | Yes | `"data"` | The name of the input binary field containing the file to be written |
| `container` | resourceLocator | Yes | `{"mode":"list","value":""}` | Container to delete a blob from |
| `blob` | resourceLocator | Yes | `{"mode":"list","value":""}` | Blob to be deleted |
| `container` | resourceLocator | Yes | `{"mode":"list","value":""}` | Container to get a blob from |
| `blob` | resourceLocator | Yes | `{"mode":"list","value":""}` | Blob to get |
| `container` | resourceLocator | Yes | `{"mode":"list","value":""}` | Container to get blobs from |

#### Property Details

##### From (`from`)

Optional values:
- `binary`: Binary
- `url`: URL

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
  "name": "Azure Storage",
  "type": "nodes-base.azureStorage",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "from": "binary",
    "container": {
      "mode": "list",
      "value": ""
    },
    "blobCreate": "",
    "binaryPropertyName": "data",
    "blob": {
      "mode": "list",
      "value": ""
    }
  }
}
```

#### Create Example
```json
{
  "name": "Azure Storage",
  "type": "nodes-base.azureStorage",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "from": "binary",
    "container": {
      "mode": "list",
      "value": ""
    },
    "blobCreate": "",
    "binaryPropertyName": "data",
    "blob": {
      "mode": "list",
      "value": ""
    },
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Azure Storage",
  "type": "nodes-base.azureStorage",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "from": "binary",
    "container": {
      "mode": "list",
      "value": ""
    },
    "blobCreate": "",
    "binaryPropertyName": "data",
    "blob": {
      "mode": "list",
      "value": ""
    },
    "operation": "delete"
  }
}
```

---

## BambooHR

## Basic Information

- Node Type: `nodes-base.bambooHr`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume BambooHR API

### Available Operations

### Create
Create an employee
- Value: `create`

### Get
Get an employee
- Value: `get`

### Get Many
Get many employees
- Value: `getAll`

### Update
Update an employee
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `format` | options | Yes | `"JSON"` | The output format for the report |
| `address` | fixedCollection | Yes | `{}` | - |
| `exempt` | options | Yes | `""` | - |
| `gender` | options | Yes | `""` | - |
| `maritalStatus` | options | Yes | `""` | - |
| `paidPer` | options | Yes | `""` | - |
| `payRate` | fixedCollection | Yes | `{}` | - |
| `payType` | options | Yes | `""` | - |
| `addasasress` | fixedCollection | Yes | `{}` | - |
| `exempt` | options | Yes | `""` | - |

#### Property Details

##### Format (`format`)

The output format for the report

Optional values:
- `CSV`: CSV
- `JSON`: JSON
- `PDF`: PDF
- `XLS`: XLS
- `XML`: XML

##### Address (`address`)

Optional values:
- `undefined`: value

##### FLSA Overtime Status (`exempt`)

Optional values:
- `exempt`: Exempt
- `non-exempt`: Non-Exempt

##### Gender (`gender`)

Optional values:
- `female`: Female
- `male`: Male

##### Marital Status (`maritalStatus`)

Optional values:
- `single`: Single
- `married`: Married
- `domesticPartnership`: Domestic Partnership

##### Pay Per (`paidPer`)

Optional values:
- `hour`: Hour
- `day`: Day
- `week`: Week
- `month`: Month
- `quater`: Quater
- `year`: Year

##### Pay Rate (`payRate`)

Optional values:
- `undefined`: value

##### Pay Type (`payType`)

Optional values:
- `commission`: Commission
- `contract`: Contract
- `daily`: Daily
- `exceptionHourly`: Exception Hourly
- `hourly`: Hourly
- `monthly`: Monthly
- `pieceRate`: Piece Rate
- `proRata`: Pro Rata
- `salary`: Salary
- `weekly`: Weekly

##### Address (`addasasress`)

Optional values:
- `undefined`: value

##### FLSA Overtime Status (`exempt`)

Optional values:
- `exempt`: Exempt
- `non-exempt`: Non-Exempt

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
  "name": "BambooHR",
  "type": "nodes-base.bambooHr",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "format": "JSON",
    "address": {},
    "exempt": "",
    "gender": "",
    "maritalStatus": "",
    "paidPer": "",
    "payRate": {},
    "payType": "",
    "addasasress": {}
  }
}
```

#### Create Example
```json
{
  "name": "BambooHR",
  "type": "nodes-base.bambooHr",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "format": "JSON",
    "address": {},
    "exempt": "",
    "gender": "",
    "maritalStatus": "",
    "paidPer": "",
    "payRate": {},
    "payType": "",
    "addasasress": {},
    "operation": "create"
  }
}
```

#### Get Example
```json
{
  "name": "BambooHR",
  "type": "nodes-base.bambooHr",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "format": "JSON",
    "address": {},
    "exempt": "",
    "gender": "",
    "maritalStatus": "",
    "paidPer": "",
    "payRate": {},
    "payType": "",
    "addasasress": {},
    "operation": "get"
  }
}
```

---

## Bitwarden

## Basic Information

- Node Type: `nodes-base.bitwarden`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Bitwarden API

### Available Operations

### Delete
- Value: `delete`

### Get
- Value: `get`

### Get Many
- Value: `getAll`

### Update
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `updateFields` | collection | Yes | `{}` | - |
| `type` | options | Yes | `2` | - |
| `collectionId` | string | Yes | `""` | The identifier of the collection |
| `groupId` | string | Yes | `""` | The identifier of the group |
| `name` | string | Yes | `""` | The name of the group to create |
| `memberId` | string | Yes | `""` | The identifier of the member |
| `resource` | options | No | `"collection"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"get"` | - |

#### Property Details

##### Update Fields (`updateFields`)

Optional values:
- `undefined`: groups - The group to assign this collection to. Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: externalId - The external identifier to set to this collection

##### Type (`type`)

Optional values:
- `0`: Owner
- `1`: Admin
- `2`: User
- `3`: Manager

##### Resource (`resource`)

Optional values:
- `collection`: Collection
- `event`: Event
- `group`: Group
- `member`: Member

##### Operation (`operation`)

Optional values:
- `delete`: Delete
- `get`: Get
- `getAll`: Get Many
- `update`: Update

##### Operation (`operation`)

Optional values:
- `getAll`: Get Many

##### Operation (`operation`)

Optional values:
- `create`: Create
- `delete`: Delete
- `get`: Get
- `getAll`: Get Many
- `getMembers`: Get Members
- `update`: Update
- `updateMembers`: Update Members

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
  "name": "Bitwarden",
  "type": "nodes-base.bitwarden",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "updateFields": {},
    "type": 2,
    "collectionId": "",
    "groupId": "",
    "name": "",
    "memberId": ""
  }
}
```

#### Delete Example
```json
{
  "name": "Bitwarden",
  "type": "nodes-base.bitwarden",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "updateFields": {},
    "type": 2,
    "collectionId": "",
    "groupId": "",
    "name": "",
    "memberId": "",
    "operation": "delete"
  }
}
```

#### Get Example
```json
{
  "name": "Bitwarden",
  "type": "nodes-base.bitwarden",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "updateFields": {},
    "type": 2,
    "collectionId": "",
    "groupId": "",
    "name": "",
    "memberId": "",
    "operation": "get"
  }
}
```

---

## Brevo

## Basic Information

- Node Type: `nodes-base.sendInBlue`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Brevo API

### Available Operations

### Create
- Value: `create`

### Update
- Value: `update`

### Delete
- Value: `delete`

### Get Many
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `attributeCategory` | options | Yes | `"normal"` | Category of the attribute |
| `attributeType` | options | Yes | `""` | Attribute Type |
| `attributeName` | string | Yes | `""` | Name of the attribute |
| `attributeValue` | string | Yes | `""` | Value of the attribute |
| `name` | string | Yes | `""` | Name of the sender |
| `email` | string | Yes | `""` | Email of the sender |
| `identifier` | string | Yes | `""` | Email (urlencoded) OR ID of the contact OR its SMS attribute value |
| `identifier` | string | Yes | `""` | Email (urlencoded) OR ID of the contact OR its SMS attribute value |
| `email` | string | Yes | `""` | Email of the contact |
| `sender` | string | Yes | `""` | - |

#### Property Details

##### Category (`attributeCategory`)

Category of the attribute

Optional values:
- `calculated`: Calculated
- `category`: Category
- `global`: Global
- `normal`: Normal
- `transactional`: Transactional

##### Type (`attributeType`)

Attribute Type

Optional values:
- `boolean`: Boolean
- `date`: Date
- `float`: Float
- `text`: Text

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
  "name": "Brevo",
  "type": "nodes-base.sendInBlue",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "attributeCategory": "normal",
    "attributeType": "",
    "attributeName": "",
    "attributeValue": "",
    "name": "",
    "email": "",
    "identifier": "",
    "sender": ""
  }
}
```

#### Create Example
```json
{
  "name": "Brevo",
  "type": "nodes-base.sendInBlue",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "attributeCategory": "normal",
    "attributeType": "",
    "attributeName": "",
    "attributeValue": "",
    "name": "",
    "email": "",
    "identifier": "",
    "sender": "",
    "operation": "create"
  }
}
```

#### Update Example
```json
{
  "name": "Brevo",
  "type": "nodes-base.sendInBlue",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "attributeCategory": "normal",
    "attributeType": "",
    "attributeName": "",
    "attributeValue": "",
    "name": "",
    "email": "",
    "identifier": "",
    "sender": "",
    "operation": "update"
  }
}
```

---

## Bubble

## Basic Information

- Node Type: `nodes-base.bubble`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Bubble Data API

### Available Operations

### Create
- Value: `create`

### Delete
- Value: `delete`

### Get
- Value: `get`

### Get Many
- Value: `getAll`

### Update
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `typeName` | string | Yes | `""` | Name of data type of the object to create |
| `typeName` | string | Yes | `""` | Name of data type of the object to retrieve |
| `objectId` | string | Yes | `""` | ID of the object to retrieve |
| `typeName` | string | Yes | `""` | Name of data type of the object to update |
| `objectId` | string | Yes | `""` | ID of the object to update |
| `typeName` | string | Yes | `""` | Name of data type of the object to create |
| `resource` | options | No | `"object"` | - |
| `operation` | options | No | `"get"` | - |
| `properties` | fixedCollection | No | `{}` | - |
| `properties` | fixedCollection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `object`: Object

##### Operation (`operation`)

Optional values:
- `create`: Create
- `delete`: Delete
- `get`: Get
- `getAll`: Get Many
- `update`: Update

##### Properties (`properties`)

Optional values:
- `undefined`: property

##### Properties (`properties`)

Optional values:
- `undefined`: property

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
  "name": "Bubble",
  "type": "nodes-base.bubble",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "typeName": "",
    "objectId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Bubble",
  "type": "nodes-base.bubble",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "typeName": "",
    "objectId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Bubble",
  "type": "nodes-base.bubble",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "typeName": "",
    "objectId": "",
    "operation": "delete"
  }
}
```

---

## Clockify

## Basic Information

- Node Type: `nodes-base.clockify`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Clockify REST API

### Available Operations

### Create
Create a client
- Value: `create`

### Delete
Delete a client
- Value: `delete`

### Get
Get a client
- Value: `get`

### Get Many
Get many clients
- Value: `getAll`

### Update
Update a client
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `workspaceId` | options | Yes | `[]` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `name` | string | Yes | `""` | Name of client being created |
| `name` | string | Yes | `""` | Name of project being created |
| `name` | string | Yes | `""` | Name of tag being created |
| `projectId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `name` | string | Yes | `""` | Name of task to create |
| `taskId` | string | Yes | `""` | ID of task to delete |
| `taskId` | string | Yes | `""` | ID of task to get |
| `taskId` | string | Yes | `""` | ID of task to update |
| `name` | string | Yes | `""` | - |

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
  "name": "Clockify",
  "type": "nodes-base.clockify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workspaceId": [],
    "name": "",
    "projectId": "",
    "taskId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Clockify",
  "type": "nodes-base.clockify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workspaceId": [],
    "name": "",
    "projectId": "",
    "taskId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Clockify",
  "type": "nodes-base.clockify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workspaceId": [],
    "name": "",
    "projectId": "",
    "taskId": "",
    "operation": "delete"
  }
}
```

---

## Compare Datasets

## Basic Information

- Node Type: `nodes-base.compareDatasets`
- Category: transform
- Package: n8n-nodes-base

### Description

Compare two inputs for changes

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `mergeByFields` | fixedCollection | No | `{"values":[{"field1":"","field2":""}]}` | - |
| `resolve` | options | No | `"preferInput2"` | - |
| `resolve` | options | No | `"includeBoth"` | - |
| `preferWhenMix` | options | No | `"input1"` | - |
| `options` | collection | No | `{}` | - |
| `fuzzyCompare` | boolean | No | `false` | Whether to tolerate small type differences when comparing fields. E.g. the number 3 and the string '3' are treated as the same. |
| `infoBox` | notice | No | `""` | - |
| `exceptWhenMix` | string | No | `""` | - |

#### Property Details

##### Fields to Match (`mergeByFields`)

Optional values:
- `undefined`: values

##### When There Are Differences (`resolve`)

Optional values:
- `preferInput1`: Use Input A Version
- `preferInput2`: Use Input B Version
- `mix`: Use a Mix of Versions - Output uses different inputs for different fields
- `includeBoth`: Include Both Versions - Output contains all data (but structure more complex)

##### When There Are Differences (`resolve`)

Optional values:
- `preferInput1`: Use Input A Version
- `preferInput2`: Use Input B Version
- `mix`: Use a Mix of Versions - Output uses different inputs for different fields
- `includeBoth`: Include Both Versions - Output contains all data (but structure more complex)

##### Prefer (`preferWhenMix`)

Optional values:
- `input1`: Input A Version
- `input2`: Input B Version

##### Options (`options`)

Optional values:
- `undefined`: skipFields - Fields that shouldn't be included when checking whether two items are the same
- `undefined`: fuzzyCompare - Whether to tolerate small type differences when comparing fields. E.g. the number 3 and the string '3' are treated as the same.
- `undefined`: disableDotNotation - Whether to disallow referencing child fields using \`parent.child\` in the field name
- `undefined`: multipleMatches

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 4

Output Details:
1. `In A only` - Items only in dataset A
2. `Same` - Items that are the same in both datasets
3. `Different` - Items that are different between datasets
4. `In B only` - Items only in dataset B

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
  "name": "Compare Datasets",
  "type": "nodes-base.compareDatasets",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Compression

## Basic Information

- Node Type: `nodes-base.compression`
- Category: transform
- Package: n8n-nodes-base

### Description

Compress and decompress files

### Available Operations

### Compress
Compress files into a zip or gzip archive
- Value: `compress`

### Decompress
Decompress zip or gzip archives
- Value: `decompress`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `binaryPropertyName` | string | Yes | `"data"` | To process more than one file, use a comma-separated list of the binary fields names |
| `binaryPropertyName` | string | Yes | `"data"` | To process more than one file, use a comma-separated list of the binary fields names |
| `fileName` | string | Yes | `""` | Name of the output file |
| `outputPrefix` | string | Yes | `"data"` | Prefix to add to the gzip file |
| `outputPrefix` | string | Yes | `"file_"` | Prefix to add to the decompressed files |
| `operation` | options | No | `"decompress"` | - |
| `outputFormat` | options | No | `""` | Format of the output |
| `outputFormat` | options | No | `"zip"` | Format of the output |
| `fileName` | string | No | `""` | Name of the output file |
| `binaryPropertyOutput` | string | No | `"data"` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `compress`: Compress - Compress files into a zip or gzip archive
- `decompress`: Decompress - Decompress zip or gzip archives

##### Output Format (`outputFormat`)

Format of the output

Optional values:
- `gzip`: Gzip
- `zip`: Zip

##### Output Format (`outputFormat`)

Format of the output

Optional values:
- `gzip`: Gzip
- `zip`: Zip

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
  "name": "Compression",
  "type": "nodes-base.compression",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryPropertyName": "data",
    "fileName": "",
    "outputPrefix": "file_"
  }
}
```

#### Compress Example
```json
{
  "name": "Compression",
  "type": "nodes-base.compression",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryPropertyName": "data",
    "fileName": "",
    "outputPrefix": "file_",
    "operation": "compress"
  }
}
```

#### Decompress Example
```json
{
  "name": "Compression",
  "type": "nodes-base.compression",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryPropertyName": "data",
    "fileName": "",
    "outputPrefix": "file_",
    "operation": "decompress"
  }
}
```

---

## Convert to/from binary data

## Basic Information

- Node Type: `nodes-base.moveBinaryData`
- Category: transform
- Package: n8n-nodes-base

### Description

Move data between binary and JSON properties

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `sourceKey` | string | Yes | `"data"` | The name of the binary key to get data from. It is also possible to define deep keys by using dot-notation like for example: "level1.level2.currentKey". |
| `destinationKey` | string | Yes | `"data"` | The name the JSON key to copy data to. It is also possible to define deep keys by using dot-notation like for example: "level1.level2.newKey". |
| `sourceKey` | string | Yes | `"data"` | The name of the JSON key to get data from. It is also possible to define deep keys by using dot-notation like for example: "level1.level2.currentKey". |
| `destinationKey` | string | Yes | `"data"` | The name the binary key to copy data to. It is also possible to define deep keys by using dot-notation like for example: "level1.level2.newKey". |
| `mode` | options | No | `"binaryToJson"` | From and to where data should be moved |
| `options` | collection | No | `{}` | - |
| `setAllData` | boolean | No | `true` | Whether all JSON data should be replaced with the data retrieved from binary key. Else the data will be written to a single key. |
| `convertAllData` | boolean | No | `true` | Whether all JSON data should be converted to binary. Else only the data of one key will be converted. |

#### Property Details

##### Mode (`mode`)

From and to where data should be moved

Optional values:
- `binaryToJson`: Binary to JSON - Move data from Binary to JSON
- `jsonToBinary`: JSON to Binary - Move data from JSON to Binary

##### Options (`options`)

Optional values:
- `undefined`: addBOM - Whether to add special marker at the start of your text file. This marker helps some programs understand how to read the file correctly.
- `undefined`: dataIsBase64 - Whether to keep the binary data as base64 string
- `undefined`: encoding - Choose the character set to use to encode the data
- `undefined`: stripBOM
- `undefined`: fileName - The file name to set
- `undefined`: jsonParse - Whether to run JSON parse on the data to get proper object data
- `undefined`: keepSource - Whether the source key should be kept. By default it will be deleted.
- `undefined`: keepAsBase64 - Whether to keep the binary data as base64 string
- `undefined`: mimeType - The mime-type to set. By default will the mime-type for JSON be set.
- `undefined`: useRawData - Whether to use data as is and do not JSON.stringify it

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
  "name": "Convert to/from binary data",
  "type": "nodes-base.moveBinaryData",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "sourceKey": "data",
    "destinationKey": "data"
  }
}
```

---

## Copper

## Basic Information

- Node Type: `nodes-base.copper`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Copper API

### Available Operations

### Create
- Value: `create`

### Delete
- Value: `delete`

### Get
- Value: `get`

### Get Many
- Value: `getAll`

### Update
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `name` | string | Yes | `""` | Name of the company to create |
| `companyId` | string | Yes | `""` | ID of the company to delete |
| `companyId` | string | Yes | `""` | ID of the company to retrieve |
| `companyId` | string | Yes | `""` | ID of the company to update |
| `name` | string | Yes | `""` | Name of the lead to create |
| `leadId` | string | Yes | `""` | ID of the lead to delete |
| `leadId` | string | Yes | `""` | ID of the lead to retrieve |
| `leadId` | string | Yes | `""` | ID of the lead to update |
| `name` | string | Yes | `""` | Name of the opportunity to create |
| `opportunityId` | string | Yes | `""` | ID of the opportunity to delete |

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
  "name": "Copper",
  "type": "nodes-base.copper",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "companyId": "",
    "leadId": "",
    "opportunityId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Copper",
  "type": "nodes-base.copper",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "companyId": "",
    "leadId": "",
    "opportunityId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Copper",
  "type": "nodes-base.copper",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "companyId": "",
    "leadId": "",
    "opportunityId": "",
    "operation": "delete"
  }
}
```

---

## Cortex

## Basic Information

- Node Type: `nodes-base.cortex`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Apply the Cortex analyzer/responder on the given entity

### Available Operations

### Execute
Execute Analyzer
- Value: `execute`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"analyzer"` | Choose a resource |
| `operation` | options | Yes | `"execute"` | Choose an operation |
| `operation` | options | Yes | `"execute"` | Choose an operation |
| `operation` | options | Yes | `"get"` | Choose an operation |
| `analyzer` | options | Yes | `""` | Choose the analyzer. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `observableType` | options | Yes | `""` | Choose the observable type. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `observableValue` | string | Yes | `""` | Enter the observable value |
| `responder` | options | Yes | `""` | Choose the responder. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `entityType` | options | Yes | `""` | Choose the Data type. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `jobId` | string | Yes | `""` | ID of the job |

#### Property Details

##### Resource (`resource`)

Choose a resource

Optional values:
- `analyzer`: Analyzer
- `job`: Job
- `responder`: Responder

##### Operation (`operation`)

Choose an operation

Optional values:
- `execute`: Execute - Execute Analyzer

##### Operation (`operation`)

Choose an operation

Optional values:
- `execute`: Execute - Execute Responder

##### Operation (`operation`)

Choose an operation

Optional values:
- `get`: Get - Get job details
- `report`: Report - Get job report

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
  "name": "Cortex",
  "type": "nodes-base.cortex",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "analyzer",
    "operation": "get",
    "analyzer": "",
    "observableType": "",
    "observableValue": "",
    "responder": "",
    "entityType": "",
    "jobId": ""
  }
}
```

#### Execute Example
```json
{
  "name": "Cortex",
  "type": "nodes-base.cortex",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "analyzer",
    "operation": "execute",
    "analyzer": "",
    "observableType": "",
    "observableValue": "",
    "responder": "",
    "entityType": "",
    "jobId": ""
  }
}
```

---

## crowd.dev

## Basic Information

- Node Type: `nodes-base.crowdDev`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

crowd.dev is an open-source suite of community and data tools built to unlock community-led growth for your organization.

### Available Operations

### Create or Update with a Member
Create or update an activity with a member
- Value: `createWithMember`

### Create
Create an activity for a member
- Value: `createForMember`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | URL to POST webhook data to |
| `trigger` | options | Yes | `"new_activity"` | What will trigger an automation |
| `username` | fixedCollection | Yes | `{}` | - |
| `member` | string | Yes | `""` | The ID of the member that performed the activity |
| `type` | string | Yes | `""` | Type of activity |
| `timestamp` | dateTime | Yes | `""` | Date and time when the activity took place |
| `platform` | string | Yes | `""` | Platform on which the activity took place |
| `sourceId` | string | Yes | `""` | The ID of the activity in the platform (e.g. the ID of the message in Discord) |
| `id` | string | Yes | `""` | The ID of the member |
| `platform` | string | Yes | `""` | Platform for which to check member existence |

#### Property Details

##### Trigger (`trigger`)

What will trigger an automation

Optional values:
- `new_activity`: New Activity
- `new_member`: New Member

##### Username (`username`)

Optional values:
- `undefined`: itemChoice

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
  "name": "crowd.dev",
  "type": "nodes-base.crowdDev",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "trigger": "new_activity",
    "username": {},
    "member": "",
    "type": "",
    "timestamp": "",
    "platform": "",
    "sourceId": "",
    "id": ""
  }
}
```

#### Create or Update with a Member Example
```json
{
  "name": "crowd.dev",
  "type": "nodes-base.crowdDev",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "trigger": "new_activity",
    "username": {},
    "member": "",
    "type": "",
    "timestamp": "",
    "platform": "",
    "sourceId": "",
    "id": "",
    "operation": "createWithMember"
  }
}
```

#### Create Example
```json
{
  "name": "crowd.dev",
  "type": "nodes-base.crowdDev",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "trigger": "new_activity",
    "username": {},
    "member": "",
    "type": "",
    "timestamp": "",
    "platform": "",
    "sourceId": "",
    "id": "",
    "operation": "createForMember"
  }
}
```

---

## Crypto

## Basic Information

- Node Type: `nodes-base.crypto`
- Category: transform
- Package: n8n-nodes-base

### Description

Provide cryptographic utilities

### Available Operations

### Generate
Generate random string
- Value: `generate`

### Hash
Hash a text or file in a specified format
- Value: `hash`

### Hmac
Hmac a text or file in a specified format
- Value: `hmac`

### Sign
Sign a string using a private key
- Value: `sign`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `value` | string | Yes | `""` | The value that should be hashed |
| `value` | string | Yes | `""` | The value of which the hmac should be created |
| `value` | string | Yes | `""` | The value that should be signed |
| `type` | options | Yes | `"MD5"` | The hash type to use |
| `type` | options | Yes | `"MD5"` | The hash type to use |
| `algorithm` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `encodingType` | options | Yes | `"uuid"` | Encoding that will be used to generate string |
| `encoding` | options | Yes | `"hex"` | - |
| `encoding` | options | Yes | `"hex"` | - |
| `encoding` | options | Yes | `"hex"` | - |

#### Property Details

##### Type (`type`)

The hash type to use

Optional values:
- `MD5`: MD5
- `SHA256`: SHA256
- `SHA3-256`: SHA3-256
- `SHA3-384`: SHA3-384
- `SHA3-512`: SHA3-512
- `SHA384`: SHA384
- `SHA512`: SHA512

##### Type (`type`)

The hash type to use

Optional values:
- `MD5`: MD5
- `SHA256`: SHA256
- `SHA3-256`: SHA3-256
- `SHA3-384`: SHA3-384
- `SHA3-512`: SHA3-512
- `SHA384`: SHA384
- `SHA512`: SHA512

##### Algorithm Name or ID (`algorithm`)

Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>

Optional values:
- `RSA-MD5`: RSA-MD5
- `RSA-RIPEMD160`: RSA-RIPEMD160
- `RSA-SHA1`: RSA-SHA1
- `RSA-SHA1-2`: RSA-SHA1-2
- `RSA-SHA224`: RSA-SHA224
- `RSA-SHA256`: RSA-SHA256
- `RSA-SHA3-224`: RSA-SHA3-224
- `RSA-SHA3-256`: RSA-SHA3-256
- `RSA-SHA3-384`: RSA-SHA3-384
- `RSA-SHA3-512`: RSA-SHA3-512
- `RSA-SHA384`: RSA-SHA384
- `RSA-SHA512`: RSA-SHA512
- `RSA-SHA512/224`: RSA-SHA512/224
- `RSA-SHA512/256`: RSA-SHA512/256
- `RSA-SM3`: RSA-SM3
- `blake2b512`: blake2b512
- `blake2s256`: blake2s256
- `id-rsassa-pkcs1-v1_5-with-sha3-224`: id-rsassa-pkcs1-v1_5-with-sha3-224
- `id-rsassa-pkcs1-v1_5-with-sha3-256`: id-rsassa-pkcs1-v1_5-with-sha3-256
- `id-rsassa-pkcs1-v1_5-with-sha3-384`: id-rsassa-pkcs1-v1_5-with-sha3-384
- `id-rsassa-pkcs1-v1_5-with-sha3-512`: id-rsassa-pkcs1-v1_5-with-sha3-512
- `md5`: md5
- `md5-sha1`: md5-sha1
- `md5WithRSAEncryption`: md5WithRSAEncryption
- `ripemd`: ripemd
- `ripemd160`: ripemd160
- `ripemd160WithRSA`: ripemd160WithRSA
- `rmd160`: rmd160
- `sha1`: sha1
- `sha1WithRSAEncryption`: sha1WithRSAEncryption
- `sha224`: sha224
- `sha224WithRSAEncryption`: sha224WithRSAEncryption
- `sha256`: sha256
- `sha256WithRSAEncryption`: sha256WithRSAEncryption
- `sha3-224`: sha3-224
- `sha3-256`: sha3-256
- `sha3-384`: sha3-384
- `sha3-512`: sha3-512
- `sha384`: sha384
- `sha384WithRSAEncryption`: sha384WithRSAEncryption
- `sha512`: sha512
- `sha512-224`: sha512-224
- `sha512-224WithRSAEncryption`: sha512-224WithRSAEncryption
- `sha512-256`: sha512-256
- `sha512-256WithRSAEncryption`: sha512-256WithRSAEncryption
- `sha512WithRSAEncryption`: sha512WithRSAEncryption
- `shake128`: shake128
- `shake256`: shake256
- `sm3`: sm3
- `sm3WithRSAEncryption`: sm3WithRSAEncryption
- `ssl3-md5`: ssl3-md5
- `ssl3-sha1`: ssl3-sha1

##### Type (`encodingType`)

Encoding that will be used to generate string

Optional values:
- `ascii`: ASCII
- `base64`: BASE64
- `hex`: HEX
- `uuid`: UUID

##### Encoding (`encoding`)

Optional values:
- `base64`: BASE64
- `hex`: HEX

##### Encoding (`encoding`)

Optional values:
- `base64`: BASE64
- `hex`: HEX

##### Encoding (`encoding`)

Optional values:
- `base64`: BASE64
- `hex`: HEX

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
  "name": "Crypto",
  "type": "nodes-base.crypto",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "type": "MD5",
    "algorithm": "",
    "encodingType": "uuid",
    "encoding": "hex"
  }
}
```

#### Generate Example
```json
{
  "name": "Crypto",
  "type": "nodes-base.crypto",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "type": "MD5",
    "algorithm": "",
    "encodingType": "uuid",
    "encoding": "hex",
    "operation": "generate"
  }
}
```

#### Hash Example
```json
{
  "name": "Crypto",
  "type": "nodes-base.crypto",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "type": "MD5",
    "algorithm": "",
    "encodingType": "uuid",
    "encoding": "hex",
    "operation": "hash"
  }
}
```

---

## Customer Datastore (n8n training)

## Basic Information

- Node Type: `nodes-base.n8nTrainingCustomerDatastore`
- Category: transform
- Package: n8n-nodes-base

### Description

Dummy node used for n8n training

### Available Operations

### Get One Person
- Value: `getOnePerson`

### Get All People
- Value: `getAllPeople`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `operation` | options | No | `"getOnePerson"` | - |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `5` | Max number of results to return |

#### Property Details

##### Operation (`operation`)

Optional values:
- `getOnePerson`: Get One Person
- `getAllPeople`: Get All People

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
  "name": "Customer Datastore (n8n training)",
  "type": "nodes-base.n8nTrainingCustomerDatastore",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Get One Person Example
```json
{
  "name": "Customer Datastore (n8n training)",
  "type": "nodes-base.n8nTrainingCustomerDatastore",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "getOnePerson"
  }
}
```

#### Get All People Example
```json
{
  "name": "Customer Datastore (n8n training)",
  "type": "nodes-base.n8nTrainingCustomerDatastore",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "getAllPeople"
  }
}
```

---

## Customer Messenger (n8n training)

## Basic Information

- Node Type: `nodes-base.n8nTrainingCustomerMessenger`
- Category: transform
- Package: n8n-nodes-base

### Description

Dummy node used for n8n training

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `customerId` | string | Yes | `""` | - |
| `message` | string | Yes | `""` | - |

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
  "name": "Customer Messenger (n8n training)",
  "type": "nodes-base.n8nTrainingCustomerMessenger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "customerId": "",
    "message": ""
  }
}
```

---

## Date & Time

## Basic Information

- Node Type: `nodes-base.dateTime`
- Category: transform
- Package: n8n-nodes-base

### Description

Allows you to manipulate date and time values

### Available Operations

### Add to a Date
- Value: `addToDate`

### Extract Part of a Date
- Value: `extractDate`

### Format a Date
- Value: `formatDate`

### Get Current Date
- Value: `getCurrentDate`

### Get Time Between Dates
- Value: `getTimeBetweenDates`

### Round a Date
- Value: `roundDate`

### Subtract From a Date
- Value: `subtractFromDate`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `timeUnit` | options | Yes | `"days"` | Time unit for Duration parameter below |
| `timeUnit` | options | Yes | `"days"` | Time unit for Duration parameter below |
| `magnitude` | string | Yes | `""` | The date that you want to change |
| `magnitude` | string | Yes | `""` | The date that you want to change |
| `operation` | options | No | `"getCurrentDate"` | - |
| `format` | options | No | `"MM/dd/yyyy"` | The format to convert the date to |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Time Unit to Add (`timeUnit`)

Time unit for Duration parameter below

Optional values:
- `years`: Years
- `quarters`: Quarters
- `months`: Months
- `weeks`: Weeks
- `days`: Days
- `hours`: Hours
- `minutes`: Minutes
- `seconds`: Seconds
- `milliseconds`: Milliseconds

##### Time Unit to Subtract (`timeUnit`)

Time unit for Duration parameter below

Optional values:
- `years`: Years
- `quarters`: Quarters
- `months`: Months
- `weeks`: Weeks
- `days`: Days
- `hours`: Hours
- `minutes`: Minutes
- `seconds`: Seconds
- `milliseconds`: Milliseconds

##### Operation (`operation`)

Optional values:
- `addToDate`: Add to a Date
- `extractDate`: Extract Part of a Date
- `formatDate`: Format a Date
- `getCurrentDate`: Get Current Date
- `getTimeBetweenDates`: Get Time Between Dates
- `roundDate`: Round a Date
- `subtractFromDate`: Subtract From a Date

##### Format (`format`)

The format to convert the date to

Optional values:
- `custom`: Custom Format
- `MM/dd/yyyy`: MM/DD/YYYY - Example: 09/04/1986
- `yyyy/MM/dd`: YYYY/MM/DD - Example: 1986/04/09
- `MMMM dd yyyy`: MMMM DD YYYY - Example: April 09 1986
- `MM-dd-yyyy`: MM-DD-YYYY - Example: 09-04-1986
- `yyyy-MM-dd`: YYYY-MM-DD - Example: 1986-04-09
- `X`: Unix Timestamp - Example: 1672531200
- `x`: Unix Ms Timestamp - Example: 1674691200000

##### Options (`options`)

Optional values:
- `undefined`: includeInputFields - Whether to include all fields of the input item in the output item
- `undefined`: timezone - The timezone to use. If not set, the timezone of the n8n instance will be used. Use ‘GMT’ for +00:00 timezone.

##### Options (`options`)

Optional values:
- `undefined`: includeInputFields - Whether to include all fields of the input item in the output item

##### Options (`options`)

Optional values:
- `undefined`: includeInputFields - Whether to include all fields of the input item in the output item

##### Options (`options`)

Optional values:
- `undefined`: includeInputFields - Whether to include all fields of the input item in the output item
- `undefined`: fromFormat - Format in which the input 'Date' is, it's helpful when the format is not recognized automatically. Use those \<a href="https://moment.github.io/luxon/#/formatting?id=table-of-tokens&id=table-of-tokens" target="\_blank"\>tokens\</a\> to define the format.
- `undefined`: timezone - Whether to use the timezone of the input or the workflow's timezone

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
  "name": "Date & Time",
  "type": "nodes-base.dateTime",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "timeUnit": "days",
    "magnitude": ""
  }
}
```

#### Add to a Date Example
```json
{
  "name": "Date & Time",
  "type": "nodes-base.dateTime",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "timeUnit": "days",
    "magnitude": "",
    "operation": "addToDate"
  }
}
```

#### Extract Part of a Date Example
```json
{
  "name": "Date & Time",
  "type": "nodes-base.dateTime",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "timeUnit": "days",
    "magnitude": "",
    "operation": "extractDate"
  }
}
```

---

## Dropcontact

## Basic Information

- Node Type: `nodes-base.dropcontact`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Find B2B emails and enrich contacts

### Available Operations

### Enrich
Find B2B emails and enrich your contact from his name and his website
- Value: `enrich`

### Fetch Request
- Value: `fetchRequest`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"contact"` | - |
| `operation` | options | Yes | `"enrich"` | - |
| `requestId` | string | Yes | `""` | - |
| `additionalFields` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `simplify` | boolean | No | `false` | When off, waits for the contact data before completing. Waiting time can be adjusted with Extend Wait Time option. When on, returns a request\_id that can be used later in the Fetch Request operation. |
| `email` | string | No | `""` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `contact`: Contact

##### Operation (`operation`)

Optional values:
- `enrich`: Enrich - Find B2B emails and enrich your contact from his name and his website
- `fetchRequest`: Fetch Request

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: num_siren
- `undefined`: siret
- `undefined`: company
- `undefined`: country
- `undefined`: first_name
- `undefined`: full_name
- `undefined`: last_name
- `undefined`: linkedin
- `undefined`: phone
- `undefined`: website

##### Options (`options`)

Optional values:
- `undefined`: waitTime - When not simplifying the response, data will be fetched in two steps. This parameter controls how long to wait (in seconds) before trying the second step.
- `undefined`: siren - Whether you want the \<a href="https://en.wikipedia.org/wiki/SIREN\_code" target="\_blank"\>SIREN number\</a\>, NAF code, TVA number, company address and informations about the company leader. Only applies to french companies.
- `undefined`: language - Whether the response is in English or French

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
  "name": "Dropcontact",
  "type": "nodes-base.dropcontact",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "contact",
    "operation": "enrich",
    "requestId": ""
  }
}
```

#### Enrich Example
```json
{
  "name": "Dropcontact",
  "type": "nodes-base.dropcontact",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "contact",
    "operation": "enrich",
    "requestId": ""
  }
}
```

#### Fetch Request Example
```json
{
  "name": "Dropcontact",
  "type": "nodes-base.dropcontact",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "contact",
    "operation": "fetchRequest",
    "requestId": ""
  }
}
```

---

## Edit Image

## Basic Information

- Node Type: `nodes-base.editImage`
- Category: transform
- Package: n8n-nodes-base

### Description

Edits an image like blur, resize or adding border and text

### Available Operations

### Blur
Adds a blur to the image and so makes it less sharp
- Value: `blur`

### Border
Adds a border to the image
- Value: `border`

### Composite
Composite image on top of another one
- Value: `composite`

### Create
Create a new image
- Value: `create`

### Crop
Crops the image
- Value: `crop`

### Draw
Draw on image
- Value: `draw`

### Get Information
Returns image information like resolution
- Value: `information`

### Multi Step
Perform multiple operations
- Value: `multiStep`

### Resize
Change the size of image
- Value: `resize`

### Rotate
Rotate image
- Value: `rotate`

### Shear
Shear image along the X or Y axis
- Value: `shear`

### Text
Adds text to image
- Value: `text`

### Transparent
Make a color in image transparent
- Value: `transparent`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `operation` | options | No | `"border"` | - |
| `operations` | fixedCollection | No | `{}` | The operations to perform |
| `primitive` | options | No | `"rectangle"` | The primitive to draw |
| `operator` | options | No | `"Over"` | The operator to use to combine the images |
| `resizeOption` | options | No | `"maximumArea"` | How to resize the image |
| `options` | collection | No | `{}` | - |
| `dataPropertyName` | string | No | `"data"` | Name of the binary property in which the image data can be found |
| `backgroundColor` | color | No | `"#ffffff00"` | The background color of the image to create |
| `width` | number | No | `50` | The width of the image to create |
| `height` | number | No | `50` | The height of the image to create |

#### Property Details

##### Operation (`operation`)

Optional values:
- `blur`: Blur - Adds a blur to the image and so makes it less sharp
- `border`: Border - Adds a border to the image
- `composite`: Composite - Composite image on top of another one
- `create`: Create - Create a new image
- `crop`: Crop - Crops the image
- `draw`: Draw - Draw on image
- `information`: Get Information - Returns image information like resolution
- `multiStep`: Multi Step - Perform multiple operations
- `resize`: Resize - Change the size of image
- `rotate`: Rotate - Rotate image
- `shear`: Shear - Shear image along the X or Y axis
- `text`: Text - Adds text to image
- `transparent`: Transparent - Make a color in image transparent

##### Operations (`operations`)

The operations to perform

Optional values:
- `undefined`: operations

##### Primitive (`primitive`)

The primitive to draw

Optional values:
- `circle`: Circle
- `line`: Line
- `rectangle`: Rectangle

##### Operator (`operator`)

The operator to use to combine the images

Optional values:
- `Add`: Add
- `Atop`: Atop
- `Bumpmap`: Bumpmap
- `Copy`: Copy
- `CopyBlack`: Copy Black
- `CopyBlue`: Copy Blue
- `CopyCyan`: Copy Cyan
- `CopyGreen`: Copy Green
- `CopyMagenta`: Copy Magenta
- `CopyOpacity`: Copy Opacity
- `CopyRed`: Copy Red
- `CopyYellow`: Copy Yellow
- `Difference`: Difference
- `Divide`: Divide
- `In`: In
- `Minus`: Minus
- `Multiply`: Multiply
- `Out`: Out
- `Over`: Over
- `Plus`: Plus
- `Subtract`: Subtract
- `Xor`: Xor

##### Option (`resizeOption`)

How to resize the image

Optional values:
- `ignoreAspectRatio`: Ignore Aspect Ratio - Ignore aspect ratio and resize exactly to specified values
- `maximumArea`: Maximum Area - Specified values are maximum area
- `minimumArea`: Minimum Area - Specified values are minimum area
- `onlyIfLarger`: Only if Larger - Resize only if image is larger than width or height
- `onlyIfSmaller`: Only if Smaller - Resize only if image is smaller than width or height
- `percent`: Percent - Width and height are specified in percents

##### Options (`options`)

Optional values:
- `undefined`: fileName - File name to set in binary data
- `undefined`: font - The font to use. Defaults to Arial. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: format - Set the output image format
- `undefined`: quality - Sets the jpeg\|png\|tiff compression level from 0 to 100 (best)

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
  "name": "Edit Image",
  "type": "nodes-base.editImage",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Blur Example
```json
{
  "name": "Edit Image",
  "type": "nodes-base.editImage",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "blur"
  }
}
```

#### Border Example
```json
{
  "name": "Edit Image",
  "type": "nodes-base.editImage",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "border"
  }
}
```

---

## Elastic Security

## Basic Information

- Node Type: `nodes-base.elasticSecurity`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Elastic Security API

### Available Operations

### Create
Create a case
- Value: `create`

### Delete
Delete a case
- Value: `delete`

### Get
Get a case
- Value: `get`

### Get Many
Retrieve many cases
- Value: `getAll`

### Get Status
Retrieve a summary of all case activity
- Value: `getStatus`

### Update
Update a case
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `urgency` | options | Yes | `1` | Urgency of the ServiceNow ITSM issue to create for this case |
| `severity` | options | Yes | `1` | Severity of the ServiceNow ITSM issue to create for this case |
| `impact` | options | Yes | `1` | Impact of the ServiceNow ITSM issue to create for this case |
| `connectorType` | options | Yes | `".jira"` | - |
| `connectorType` | options | Yes | `".jira"` | - |
| `connectorId` | options | Yes | `""` | Connectors allow you to send Elastic Security cases into other systems (only ServiceNow, Jira, or IBM Resilient). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `issueType` | string | Yes | `""` | Type of the Jira issue to create for this case |
| `priority` | string | Yes | `""` | Priority of the Jira issue to create for this case |
| `category` | string | Yes | `""` | Category of the ServiceNow ITSM issue to create for this case |
| `issueTypes` | string | Yes | `""` | Comma-separated list of numerical types of the IBM Resilient issue to create for this case |

#### Property Details

##### Urgency (`urgency`)

Urgency of the ServiceNow ITSM issue to create for this case

Optional values:
- `1`: Low
- `2`: Medium
- `3`: High

##### Severity (`severity`)

Severity of the ServiceNow ITSM issue to create for this case

Optional values:
- `1`: Low
- `2`: Medium
- `3`: High

##### Impact (`impact`)

Impact of the ServiceNow ITSM issue to create for this case

Optional values:
- `1`: Low
- `2`: Medium
- `3`: High

##### Connector Type (`connectorType`)

Optional values:
- `.resilient`: IBM Resilient
- `.jira`: Jira
- `.servicenow`: ServiceNow ITSM

##### Connector Type (`connectorType`)

Optional values:
- `.resilient`: IBM Resilient
- `.jira`: Jira
- `.servicenow`: ServiceNow ITSM

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
  "name": "Elastic Security",
  "type": "nodes-base.elasticSecurity",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "urgency": 1,
    "severity": 1,
    "impact": 1,
    "connectorType": ".jira",
    "connectorId": "",
    "issueType": "",
    "priority": "",
    "category": "",
    "issueTypes": ""
  }
}
```

#### Create Example
```json
{
  "name": "Elastic Security",
  "type": "nodes-base.elasticSecurity",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "urgency": 1,
    "severity": 1,
    "impact": 1,
    "connectorType": ".jira",
    "connectorId": "",
    "issueType": "",
    "priority": "",
    "category": "",
    "issueTypes": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Elastic Security",
  "type": "nodes-base.elasticSecurity",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "urgency": 1,
    "severity": 1,
    "impact": 1,
    "connectorType": ".jira",
    "connectorId": "",
    "issueType": "",
    "priority": "",
    "category": "",
    "issueTypes": "",
    "operation": "delete"
  }
}
```

---

## Elasticsearch

## Basic Information

- Node Type: `nodes-base.elasticsearch`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Elasticsearch API

### Available Operations

### Create
Create a document
- Value: `create`

### Delete
Delete a document
- Value: `delete`

### Get
Get a document
- Value: `get`

### Get Many
Get many documents
- Value: `getAll`

### Update
Update a document
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `indexId` | string | Yes | `""` | ID of the index containing the document to delete |
| `documentId` | string | Yes | `""` | ID of the document to delete |
| `indexId` | string | Yes | `""` | ID of the index containing the document to retrieve |
| `documentId` | string | Yes | `""` | ID of the document to retrieve |
| `indexId` | string | Yes | `""` | ID of the index containing the documents to retrieve |
| `indexId` | string | Yes | `""` | ID of the index to add the document to |
| `indexId` | string | Yes | `""` | ID of the document to update |
| `documentId` | string | Yes | `""` | ID of the document to update |
| `indexId` | string | Yes | `""` | ID of the index to create |
| `indexId` | string | Yes | `""` | ID of the index to delete |

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
  "name": "Elasticsearch",
  "type": "nodes-base.elasticsearch",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "indexId": "",
    "documentId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Elasticsearch",
  "type": "nodes-base.elasticsearch",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "indexId": "",
    "documentId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Elasticsearch",
  "type": "nodes-base.elasticsearch",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "indexId": "",
    "documentId": "",
    "operation": "delete"
  }
}
```

---

## Evaluation

## Basic Information

- Node Type: `nodes-base.evaluation`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Runs an evaluation

### Available Operations

### Set Inputs
- Value: `setInputs`

### Set Outputs
- Value: `setOutputs`

### Set Metrics
- Value: `setMetrics`

### Check If Evaluating
- Value: `checkIfEvaluating`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `documentId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `sheetName` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `dataTableId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `operation` | options | No | `"setOutputs"` | - |
| `authentication` | options | No | `"oAuth2"` | - |
| `credentials` | credentials | No | `""` | - |
| `source` | options | No | `"dataTable"` | Where to get the test dataset from |
| `source` | options | No | `"googleSheets"` | Where to get the test dataset from |
| `inputs` | fixedCollection | No | `{}` | - |
| `outputs` | fixedCollection | No | `{}` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `setInputs`: Set Inputs
- `setOutputs`: Set Outputs
- `setMetrics`: Set Metrics
- `checkIfEvaluating`: Check If Evaluating

##### Authentication (`authentication`)

Optional values:
- `serviceAccount`: Service Account
- `oAuth2`: OAuth2 (recommended)

##### Source (`source`)

Where to get the test dataset from

Optional values:
- `dataTable`: Data table - Load the test dataset from a local Data table
- `googleSheets`: Google Sheets - Load the test dataset from a Google Sheets document

##### Source (`source`)

Where to get the test dataset from

Optional values:
- `dataTable`: Data table - Load the test dataset from a local Data table
- `googleSheets`: Google Sheets - Load the test dataset from a Google Sheets document

##### Inputs (`inputs`)

Optional values:
- `undefined`: values

##### Outputs (`outputs`)

Optional values:
- `undefined`: values

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

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
  "name": "Evaluation",
  "type": "nodes-base.evaluation",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "documentId": {
      "mode": "list",
      "value": ""
    },
    "sheetName": {
      "mode": "list",
      "value": ""
    },
    "dataTableId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

#### Set Inputs Example
```json
{
  "name": "Evaluation",
  "type": "nodes-base.evaluation",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "documentId": {
      "mode": "list",
      "value": ""
    },
    "sheetName": {
      "mode": "list",
      "value": ""
    },
    "dataTableId": {
      "mode": "list",
      "value": ""
    },
    "operation": "setInputs"
  }
}
```

#### Set Outputs Example
```json
{
  "name": "Evaluation",
  "type": "nodes-base.evaluation",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "documentId": {
      "mode": "list",
      "value": ""
    },
    "sheetName": {
      "mode": "list",
      "value": ""
    },
    "dataTableId": {
      "mode": "list",
      "value": ""
    },
    "operation": "setOutputs"
  }
}
```

---

## Execute Command

## Basic Information

- Node Type: `nodes-base.executeCommand`
- Category: transform
- Package: n8n-nodes-base

### Description

Executes a command on the host

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `command` | string | Yes | `""` | The command to execute |
| `executeOnce` | boolean | No | `true` | Whether to execute only once instead of once for each entry |

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
  "name": "Execute Command",
  "type": "nodes-base.executeCommand",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "command": ""
  }
}
```

---

## Execute Sub-workflow

## Basic Information

- Node Type: `nodes-base.executeWorkflow`
- Category: transform
- Package: n8n-nodes-base

### Description

Execute another workflow

### Available Operations

### Execute a Sub-Workflow
- Value: `call_workflow`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `workflowId` | string | Yes | `""` | Note on using an expression here: if this node is set to run once with all items, they will all be sent to the <em>same</em> workflow. That workflow's ID will be calculated by evaluating the expression for the <strong>first input item</strong>. |
| `workflowPath` | string | Yes | `""` | The path to local JSON workflow file to execute |
| `workflowJson` | json | Yes | `"\n\n\n"` | The workflow JSON code to execute |
| `workflowUrl` | string | Yes | `""` | The URL from which to load the workflow from |
| `workflowId` | workflowSelector | Yes | `""` | - |
| `workflowInputs` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `operation` | hidden | No | `"call_workflow"` | - |
| `source` | options | No | `"database"` | Where to get the workflow to execute from |
| `source` | options | No | `"database"` | Where to get the workflow to execute from |
| `mode` | options | No | `"once"` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `call_workflow`: Execute a Sub-Workflow

##### Source (`source`)

Where to get the workflow to execute from

Optional values:
- `database`: Database - Load the workflow from the database by ID
- `localFile`: Local File - Load the workflow from a locally saved file
- `parameter`: Parameter - Load the workflow from a parameter
- `url`: URL - Load the workflow from an URL

##### Source (`source`)

Where to get the workflow to execute from

Optional values:
- `database`: Database - Load the workflow from the database by ID
- `parameter`: Define Below - Pass the JSON code of a workflow

##### Mode (`mode`)

Optional values:
- `once`: Run once with all items - Pass all items into a single execution of the sub-workflow
- `each`: Run once for each item - Call the sub-workflow individually for each item

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
  "name": "Execute Sub-workflow",
  "type": "nodes-base.executeWorkflow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workflowId": "",
    "workflowPath": "",
    "workflowJson": "\n\n\n",
    "workflowUrl": "",
    "workflowInputs": {
      "mappingMode": "defineBelow",
      "value": null
    }
  }
}
```

#### Execute a Sub-Workflow Example
```json
{
  "name": "Execute Sub-workflow",
  "type": "nodes-base.executeWorkflow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workflowId": "",
    "workflowPath": "",
    "workflowJson": "\n\n\n",
    "workflowUrl": "",
    "workflowInputs": {
      "mappingMode": "defineBelow",
      "value": null
    },
    "operation": "call_workflow"
  }
}
```

---

## Facebook Graph API

## Basic Information

- Node Type: `nodes-base.facebookGraphApi`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Interacts with Facebook using the Graph API

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `hostUrl` | options | Yes | `"graph.facebook.com"` | The Host URL of the request. Almost all requests are passed to the graph.facebook.com host URL. The single exception is video uploads, which use graph-video.facebook.com. |
| `httpRequestMethod` | options | Yes | `"GET"` | The HTTP Method to be used for the request |
| `graphApiVersion` | options | Yes | `""` | The version of the Graph API to be used in the request |
| `node` | string | Yes | `""` | The node on which to operate. A node is an individual object with a unique ID. For example, there are many User node objects, each with a unique ID representing a person on Facebook. |
| `sendBinaryData` | boolean | Yes | `false` | Whether binary data should be sent as body |
| `options` | collection | No | `{}` | - |
| `edge` | string | No | `""` | Edge of the node on which to operate. Edges represent collections of objects which are attached to the node. |
| `allowUnauthorizedCerts` | boolean | No | `false` | Whether to connect even if SSL certificate validation is not possible |
| `binaryPropertyName` | string | No | `""` | For Form-Data Multipart, they can be provided in the format: <code>"sendKey1:binaryProperty1,sendKey2:binaryProperty2</code> |

#### Property Details

##### Host URL (`hostUrl`)

The Host URL of the request. Almost all requests are passed to the graph.facebook.com host URL. The single exception is video uploads, which use graph-video.facebook.com.

Optional values:
- `graph.facebook.com`: Default
- `graph-video.facebook.com`: Video Uploads

##### HTTP Request Method (`httpRequestMethod`)

The HTTP Method to be used for the request

Optional values:
- `GET`: GET
- `POST`: POST
- `DELETE`: DELETE

##### Graph API Version (`graphApiVersion`)

The version of the Graph API to be used in the request

Optional values:
- ``: Default
- `v23.0`: v23.0
- `v22.0`: v22.0
- `v21.0`: v21.0
- `v20.0`: v20.0
- `v19.0`: v19.0
- `v18.0`: v18.0
- `v17.0`: v17.0
- `v16.0`: v16.0
- `v15.0`: v15.0
- `v14.0`: v14.0
- `v13.0`: v13.0
- `v12.0`: v12.0
- `v11.0`: v11.0
- `v10.0`: v10.0
- `v9.0`: v9.0
- `v8.0`: v8.0
- `v7.0`: v7.0
- `v6.0`: v6.0
- `v5.0`: v5.0
- `v4.0`: v4.0
- `v3.3`: v3.3
- `v3.2`: v3.2
- `v3.1`: v3.1
- `v3.0`: v3.0

##### Options (`options`)

Optional values:
- `undefined`: fields - The list of fields to request in the GET request
- `undefined`: queryParameters - The query parameters to send
- `undefined`: queryParametersJson - The query parameters to send, defined as a JSON object

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
  "name": "Facebook Graph API",
  "type": "nodes-base.facebookGraphApi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "hostUrl": "graph.facebook.com",
    "httpRequestMethod": "GET",
    "graphApiVersion": "",
    "node": "",
    "sendBinaryData": false
  }
}
```

---

## Filter

## Basic Information

- Node Type: `nodes-base.filter`
- Category: transform
- Package: n8n-nodes-base

### Description

Remove items matching a condition

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | - |
| `looseTypeValidation` | boolean | No | `false` | If the type of an expression doesn't match the type of the comparison, n8n will try to cast the expression to the required type. E.g. for booleans <code>"false"</code> or <code>0</code> will be cast to <code>false</code> |
| `conditions` | filter | No | `{}` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: ignoreCase - Whether to ignore letter case when evaluating conditions
- `undefined`: looseTypeValidation - If the type of an expression doesn't match the type of the comparison, n8n will try to cast the expression to the required type. E.g. for booleans \<code\>"false"\</code\> or \<code\>0\</code\> will be cast to \<code\>false\</code\>

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
  "name": "Filter",
  "type": "nodes-base.filter",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Freshservice

## Basic Information

- Node Type: `nodes-base.freshservice`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Freshservice API

### Available Operations

### Create
Create an agent
- Value: `create`

### Delete
Delete an agent
- Value: `delete`

### Get
Retrieve an agent
- Value: `get`

### Get Many
Retrieve many agents
- Value: `getAll`

### Update
Update an agent
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `roles` | fixedCollection | Yes | `{}` | Role to assign to the agent |
| `visibility` | options | Yes | `"everyone"` | - |
| `applicationType` | options | Yes | `"desktop"` | - |
| `agentId` | string | Yes | `""` | ID of the agent to delete |
| `agentId` | string | Yes | `""` | ID of the agent to retrieve |
| `agentId` | string | Yes | `""` | ID of the agent to update |
| `agentGroupId` | string | Yes | `""` | ID of the agent group to delete |
| `agentGroupId` | string | Yes | `""` | ID of the agent group to retrieve |
| `agentGroupId` | string | Yes | `""` | ID of the agent group to update |
| `agentRoleId` | string | Yes | `""` | ID of the agent role to retrieve |

#### Property Details

##### Roles (`roles`)

Role to assign to the agent

Optional values:
- `undefined`: roleProperties

##### Visibility (`visibility`)

Optional values:
- `agents_only`: Agents Only
- `grouped_visibility`: Agents and Groups
- `everyone`: Everyone

##### Application Type (`applicationType`)

Optional values:
- `desktop`: Desktop
- `mobile`: Mobile
- `saas`: SaaS

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
  "name": "Freshservice",
  "type": "nodes-base.freshservice",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "roles": {},
    "visibility": "everyone",
    "applicationType": "desktop",
    "agentId": "",
    "agentGroupId": "",
    "agentRoleId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Freshservice",
  "type": "nodes-base.freshservice",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "roles": {},
    "visibility": "everyone",
    "applicationType": "desktop",
    "agentId": "",
    "agentGroupId": "",
    "agentRoleId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Freshservice",
  "type": "nodes-base.freshservice",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "roles": {},
    "visibility": "everyone",
    "applicationType": "desktop",
    "agentId": "",
    "agentGroupId": "",
    "agentRoleId": "",
    "operation": "delete"
  }
}
```

---

## Freshworks CRM

## Basic Information

- Node Type: `nodes-base.freshworksCrm`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Freshworks CRM API

### Available Operations

### Create
Create an account
- Value: `create`

### Delete
Delete an account
- Value: `delete`

### Get
Retrieve an account
- Value: `get`

### Get Many
Retrieve many accounts
- Value: `getAll`

### Update
Update an account
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | Enter a term that will be used for searching entities |
| `targetableType` | options | Yes | `"Contact"` | Type of the entity for which the note is created |
| `targetableType` | options | Yes | `"Contact"` | Type of the entity for which the sales activity is created |
| `entities` | multiOptions | Yes | `[]` | Enter a term that will be used for searching entities |
| `searchField` | options | Yes | `""` | Field against which the entities have to be searched |
| `targetableType` | options | Yes | `"Contact"` | Type of the entity for which the task is updated |
| `name` | string | Yes | `""` | Name of the account |
| `accountId` | string | Yes | `""` | ID of the account to delete |
| `accountId` | string | Yes | `""` | ID of the account to retrieve |
| `view` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

#### Property Details

##### Target Type (`targetableType`)

Type of the entity for which the note is created

Optional values:
- `Contact`: Contact
- `Deal`: Deal
- `SalesAccount`: Sales Account

##### Target Type (`targetableType`)

Type of the entity for which the sales activity is created

Optional values:
- `Contact`: Contact
- `Deal`: Deal
- `SalesAccount`: Sales Account

##### Search on Entities (`entities`)

Enter a term that will be used for searching entities

Optional values:
- `contact`: Contact
- `deal`: Deal
- `sales_account`: Sales Account
- `user`: User

##### Search Field (`searchField`)

Field against which the entities have to be searched

Optional values:
- `email`: Email
- `name`: Name
- `customField`: Custom Field - Only allowed custom fields of type "Text field", "Number", "Dropdown" or "Radio button"

##### Target Type (`targetableType`)

Type of the entity for which the task is updated

Optional values:
- `Contact`: Contact
- `Deal`: Deal
- `SalesAccount`: SalesAccount

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
  "name": "Freshworks CRM",
  "type": "nodes-base.freshworksCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "targetableType": "Contact",
    "entities": [],
    "searchField": "",
    "name": "",
    "accountId": "",
    "view": ""
  }
}
```

#### Create Example
```json
{
  "name": "Freshworks CRM",
  "type": "nodes-base.freshworksCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "targetableType": "Contact",
    "entities": [],
    "searchField": "",
    "name": "",
    "accountId": "",
    "view": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Freshworks CRM",
  "type": "nodes-base.freshworksCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "targetableType": "Contact",
    "entities": [],
    "searchField": "",
    "name": "",
    "accountId": "",
    "view": "",
    "operation": "delete"
  }
}
```

---

## Function Item

## Basic Information

- Node Type: `nodes-base.functionItem`
- Category: transform
- Package: n8n-nodes-base

### Description

Run custom function code which gets executed once per item

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `functionCode` | string | No | `"// Code here will run once per input item.\n// More info and help: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.functionitem/\n// Tip: You can use luxon for dates and $jmespath for querying JSON structures\n\n// Add a new field called 'myNewField' to the JSON of the item\nitem.myNewField = 1;\n\n// You can write logs to the browser console\nconsole.log('Done!');\n\nreturn item;"` | The JavaScript code to execute for each item |
| `notice` | notice | No | `""` | - |

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
  "name": "Function Item",
  "type": "nodes-base.functionItem",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Git

## Basic Information

- Node Type: `nodes-base.git`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Control git.

### Available Operations

### Add
Add a file or folder to commit
- Value: `add`

### Add Config
Add configuration property
- Value: `addConfig`

### Clone
Clone a repository
- Value: `clone`

### Commit
Commit files or folders to git
- Value: `commit`

### Fetch
Fetch from remote repository
- Value: `fetch`

### List Config
Return current configuration
- Value: `listConfig`

### Log
Return git commit history
- Value: `log`

### Pull
Pull from remote repository
- Value: `pull`

### Push
Push to remote repository
- Value: `push`

### Push Tags
Push Tags to remote repository
- Value: `pushTags`

### Status
Return status of current repository
- Value: `status`

### Switch Branch
Switch to a different branch
- Value: `switchBranch`

### Tag
Create a new tag
- Value: `tag`

### User Setup
Set the user
- Value: `userSetup`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `value` | string | Yes | `""` | Value of the key to set |
| `repositoryPath` | string | Yes | `""` | Local path of the git repository to operate on |
| `repositoryPath` | string | Yes | `""` | Local path to which the git repository should be cloned into |
| `pathsToAdd` | string | Yes | `""` | Comma-separated list of paths (absolute or relative to Repository Path) of files or folders to add |
| `key` | string | Yes | `""` | Name of the key to set |
| `sourceRepository` | string | Yes | `""` | The URL or path of the repository to clone |
| `branchName` | string | Yes | `""` | The name of the branch to switch to |
| `name` | string | Yes | `""` | The name of the tag to create |
| `authentication` | options | No | `"none"` | The way to authenticate |
| `operation` | options | No | `"log"` | - |

#### Property Details

##### Authentication (`authentication`)

The way to authenticate

Optional values:
- `gitPassword`: Authenticate
- `none`: None

##### Operation (`operation`)

Optional values:
- `add`: Add - Add a file or folder to commit
- `addConfig`: Add Config - Add configuration property
- `clone`: Clone - Clone a repository
- `commit`: Commit - Commit files or folders to git
- `fetch`: Fetch - Fetch from remote repository
- `listConfig`: List Config - Return current configuration
- `log`: Log - Return git commit history
- `pull`: Pull - Pull from remote repository
- `push`: Push - Push to remote repository
- `pushTags`: Push Tags - Push Tags to remote repository
- `status`: Status - Return status of current repository
- `switchBranch`: Switch Branch - Switch to a different branch
- `tag`: Tag - Create a new tag
- `userSetup`: User Setup - Set the user

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
  "name": "Git",
  "type": "nodes-base.git",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "repositoryPath": "",
    "pathsToAdd": "",
    "key": "",
    "sourceRepository": "",
    "branchName": "",
    "name": ""
  }
}
```

#### Add Example
```json
{
  "name": "Git",
  "type": "nodes-base.git",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "repositoryPath": "",
    "pathsToAdd": "",
    "key": "",
    "sourceRepository": "",
    "branchName": "",
    "name": "",
    "operation": "add"
  }
}
```

#### Add Config Example
```json
{
  "name": "Git",
  "type": "nodes-base.git",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "repositoryPath": "",
    "pathsToAdd": "",
    "key": "",
    "sourceRepository": "",
    "branchName": "",
    "name": "",
    "operation": "addConfig"
  }
}
```

---

## Gong

## Basic Information

- Node Type: `nodes-base.gong`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Interact with Gong API

### Available Operations

### Get
Retrieve data for a specific call
- Value: `get`

### Get Many
Retrieve a list of calls
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `call` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `user` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `authentication` | options | No | `"accessToken"` | - |
| `resource` | options | No | `"call"` | - |
| `operation` | options | No | `"getAll"` | - |
| `operation` | options | No | `"get"` | - |
| `options` | collection | No | `{}` | - |
| `filters` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `filters` | collection | No | `{}` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `accessToken`: Access Token
- `oAuth2`: OAuth2

##### Resource (`resource`)

Optional values:
- `call`: Call
- `user`: User

##### Operation (`operation`)

Optional values:
- `get`: Get - Retrieve data for a specific call
- `getAll`: Get Many - Retrieve a list of calls

##### Operation (`operation`)

Optional values:
- `get`: Get - Retrieve data for a specific user
- `getAll`: Get Many - Retrieve a list of users

##### Options (`options`)

Optional values:
- `undefined`: properties - The Call properties to include in the returned results. Choose from a list, or specify IDs using an \<a href="https://docs.n8n.io/code-examples/expressions/"\>expression\</a\>.

##### Filters (`filters`)

Optional values:
- `undefined`: fromDateTime - Returns calls that started on or after the specified date and time. If not provided, list starts with earliest call. For web-conference calls recorded by Gong, the date denotes its scheduled time, otherwise, it denotes its actual start time.
- `undefined`: toDateTime - Returns calls that started up to but excluding specified date and time. If not provided, list ends with most recent call. For web-conference calls recorded by Gong, the date denotes its scheduled time, otherwise, it denotes its actual start time.
- `undefined`: workspaceId - Return only the calls belonging to this workspace
- `undefined`: callIds - List of calls IDs to be filtered
- `undefined`: primaryUserIds - Return only the calls hosted by the specified user

##### Options (`options`)

Optional values:
- `undefined`: properties - The Call properties to include in the returned results. Choose from a list, or specify IDs using an \<a href="https://docs.n8n.io/code-examples/expressions/"\>expression\</a\>.

##### Filters (`filters`)

Optional values:
- `undefined`: createdFromDateTime - An optional user creation time lower limit, if supplied the API will return only the users created at or after this time
- `undefined`: createdToDateTime - An optional user creation time upper limit, if supplied the API will return only the users created before this time
- `undefined`: userIds - Set of Gong's unique numeric identifiers for the users (up to 20 digits)

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
  "name": "Gong",
  "type": "nodes-base.gong",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "call": {
      "mode": "list",
      "value": ""
    },
    "user": {
      "mode": "list",
      "value": ""
    }
  }
}
```

#### Get Example
```json
{
  "name": "Gong",
  "type": "nodes-base.gong",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "call": {
      "mode": "list",
      "value": ""
    },
    "user": {
      "mode": "list",
      "value": ""
    },
    "operation": "get"
  }
}
```

#### Get Many Example
```json
{
  "name": "Gong",
  "type": "nodes-base.gong",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "call": {
      "mode": "list",
      "value": ""
    },
    "user": {
      "mode": "list",
      "value": ""
    },
    "operation": "getAll"
  }
}
```

---

## Google Ads

## Basic Information

- Node Type: `nodes-base.googleAds`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Use the Google Ads API

### Available Operations

### Get Many
Get many campaigns linked to the specified account
- Value: `getAll`

### Get
Get a specific campaign
- Value: `get`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `campaignId` | string | Yes | `""` | ID of the campaign |
| `managerCustomerId` | string | Yes | `""` | - |
| `clientCustomerId` | string | Yes | `""` | - |
| `resource` | options | No | `"campaign"` | - |
| `operation` | options | No | `"getAll"` | - |
| `additionalOptions` | collection | No | `{}` | Additional options for fetching campaigns |
| `campaigsNotice` | notice | No | `""` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `campaign`: Campaign

##### Operation (`operation`)

Optional values:
- `getAll`: Get Many - Get many campaigns linked to the specified account
- `get`: Get - Get a specific campaign

##### Additional Options (`additionalOptions`)

Additional options for fetching campaigns

Optional values:
- `undefined`: dateRange - Filters statistics by period
- `undefined`: campaignStatus - Filters campaigns by status

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
  "name": "Google Ads",
  "type": "nodes-base.googleAds",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "campaignId": "",
    "managerCustomerId": "",
    "clientCustomerId": ""
  }
}
```

#### Get Many Example
```json
{
  "name": "Google Ads",
  "type": "nodes-base.googleAds",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "campaignId": "",
    "managerCustomerId": "",
    "clientCustomerId": "",
    "operation": "getAll"
  }
}
```

#### Get Example
```json
{
  "name": "Google Ads",
  "type": "nodes-base.googleAds",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "campaignId": "",
    "managerCustomerId": "",
    "clientCustomerId": "",
    "operation": "get"
  }
}
```

---

## Google Analytics

## Basic Information

- Node Type: `nodes-base.googleAnalytics`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Use the Google Analytics API

### Available Operations

### Get
Return the analytics data
- Value: `get`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `dateRange` | options | Yes | `"last7days"` | - |
| `dateRange` | options | Yes | `"last7days"` | - |
| `propertyId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The Property of Google Analytics |
| `viewId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The View of Google Analytics |
| `viewId` | options | Yes | `""` | The view from Google Analytics. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `userId` | string | Yes | `""` | ID of a user |
| `startDate` | dateTime | Yes | `"2025-12-13T00:00:00.000+08:00"` | - |
| `endDate` | dateTime | Yes | `"2025-12-20T00:00:00.000+08:00"` | - |
| `startDate` | dateTime | Yes | `"2025-12-13T00:00:00.000+08:00"` | - |
| `endDate` | dateTime | Yes | `"2025-12-20T00:00:00.000+08:00"` | - |

#### Property Details

##### Date Range (`dateRange`)

Optional values:
- `last7days`: Last 7 Days
- `last30days`: Last 30 Days
- `today`: Today
- `yesterday`: Yesterday
- `lastCalendarWeek`: Last Complete Calendar Week
- `lastCalendarMonth`: Last Complete Calendar Month
- `custom`: Custom

##### Date Range (`dateRange`)

Optional values:
- `last7days`: Last 7 Days
- `last30days`: Last 30 Days
- `today`: Today
- `yesterday`: Yesterday
- `lastCalendarWeek`: Last Complete Calendar Week
- `lastCalendarMonth`: Last Complete Calendar Month
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
  "name": "Google Analytics",
  "type": "nodes-base.googleAnalytics",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dateRange": "last7days",
    "propertyId": {
      "mode": "list",
      "value": ""
    },
    "viewId": "",
    "userId": "",
    "startDate": "2025-12-13T00:00:00.000+08:00",
    "endDate": "2025-12-20T00:00:00.000+08:00"
  }
}
```

#### Get Example
```json
{
  "name": "Google Analytics",
  "type": "nodes-base.googleAnalytics",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dateRange": "last7days",
    "propertyId": {
      "mode": "list",
      "value": ""
    },
    "viewId": "",
    "userId": "",
    "startDate": "2025-12-13T00:00:00.000+08:00",
    "endDate": "2025-12-20T00:00:00.000+08:00",
    "operation": "get"
  }
}
```

---

## Google Cloud Storage

## Basic Information

- Node Type: `nodes-base.googleCloudStorage`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Use the Google Cloud Storage API

### Available Operations

### Create
Create a new Bucket
- Value: `create`

### Delete
Delete an empty Bucket
- Value: `delete`

### Get
Get metadata for a specific Bucket
- Value: `get`

### Get Many
Get list of Buckets
- Value: `getAll`

### Update
Update the metadata of a bucket
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `projectId` | string | Yes | `""` | - |
| `bucketName` | string | Yes | `""` | - |
| `bucketName` | string | Yes | `""` | - |
| `objectName` | string | Yes | `""` | - |
| `resource` | options | No | `"bucket"` | - |
| `operation` | options | No | `"getAll"` | - |
| `operation` | options | No | `"getAll"` | - |
| `projection` | options | No | `"noAcl"` | - |
| `getFilters` | collection | No | `{}` | - |
| `createAcl` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `bucket`: Bucket
- `object`: Object

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new Bucket
- `delete`: Delete - Delete an empty Bucket
- `get`: Get - Get metadata for a specific Bucket
- `getAll`: Get Many - Get list of Buckets
- `update`: Update - Update the metadata of a bucket

##### Operation (`operation`)

Optional values:
- `create`: Create - Create an object
- `delete`: Delete - Delete an object
- `get`: Get - Get object data or metadata
- `getAll`: Get Many - Retrieve a list of objects
- `update`: Update - Update an object's metadata

##### Projection (`projection`)

Optional values:
- `full`: All Properties
- `noAcl`: No ACL

##### Filters (`getFilters`)

Optional values:
- `undefined`: ifMetagenerationMatch - Only return data if the metageneration value of the Bucket matches the sent value
- `undefined`: ifMetagenerationNotMatch - Only return data if the metageneration value of the Bucket does not match the sent value

##### Predefined Access Control (`createAcl`)

Optional values:
- `undefined`: predefinedAcl
- `undefined`: predefinedDefaultObjectAcl

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
  "name": "Google Cloud Storage",
  "type": "nodes-base.googleCloudStorage",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "projectId": "",
    "bucketName": "",
    "objectName": ""
  }
}
```

#### Create Example
```json
{
  "name": "Google Cloud Storage",
  "type": "nodes-base.googleCloudStorage",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "projectId": "",
    "bucketName": "",
    "objectName": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Google Cloud Storage",
  "type": "nodes-base.googleCloudStorage",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "projectId": "",
    "bucketName": "",
    "objectName": "",
    "operation": "delete"
  }
}
```

---

## Google Perspective

## Basic Information

- Node Type: `nodes-base.googlePerspective`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Google Perspective API

### Available Operations

### Analyze Comment
- Value: `analyzeComment`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `requestedAttributesUi` | fixedCollection | Yes | `{}` | - |
| `text` | string | Yes | `""` | - |
| `operation` | options | No | `"analyzeComment"` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Attributes to Analyze (`requestedAttributesUi`)

Optional values:
- `undefined`: requestedAttributesValues

##### Operation (`operation`)

Optional values:
- `analyzeComment`: Analyze Comment

##### Options (`options`)

Optional values:
- `undefined`: languages - Languages of the text input. If unspecified, the API will auto-detect the comment language. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.

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
  "name": "Google Perspective",
  "type": "nodes-base.googlePerspective",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "requestedAttributesUi": {},
    "text": ""
  }
}
```

#### Analyze Comment Example
```json
{
  "name": "Google Perspective",
  "type": "nodes-base.googlePerspective",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "requestedAttributesUi": {},
    "text": "",
    "operation": "analyzeComment"
  }
}
```

---

## GoToWebinar

## Basic Information

- Node Type: `nodes-base.goToWebinar`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the GoToWebinar API

### Available Operations

### Get
- Value: `get`

### Get Many
- Value: `getAll`

### Get Details
- Value: `getDetails`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `details` | options | Yes | `""` | The details to retrieve for the attendee |
| `times` | fixedCollection | Yes | `{}` | - |
| `webinarKey` | options | Yes | `""` | Key of the webinar that the attendee attended. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `sessionKey` | options | Yes | `""` | Key of the session that the attendee attended. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `registrantKey` | string | Yes | `""` | Registrant key of the attendee at the webinar session |
| `registrantKey` | string | Yes | `""` | Registrant key of the attendee at the webinar session |
| `webinarKey` | options | Yes | `[]` | Key of the webinar that the co-organizer is hosting. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `isExternal` | boolean | Yes | `false` | Whether the co-organizer has no GoToWebinar account |
| `webinarKey` | options | Yes | `[]` | Key of the webinar to delete. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `isExternal` | boolean | Yes | `false` | By default only internal co-organizers (with a GoToWebinar account) can be deleted. If you want to use this call for external co-organizers you have to set this parameter to 'true'. |

#### Property Details

##### Details (`details`)

The details to retrieve for the attendee

Optional values:
- `polls`: Polls - Poll answers from the attendee in a webinar session
- `questions`: Questions - Questions asked by the attendee in a webinar session
- `surveyAnswers`: Survey Answers - Survey answers from the attendee in a webinar session

##### Time Range (`times`)

Optional values:
- `undefined`: timesProperties

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
  "name": "GoToWebinar",
  "type": "nodes-base.goToWebinar",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "details": "",
    "times": {},
    "webinarKey": [],
    "sessionKey": "",
    "registrantKey": "",
    "isExternal": false
  }
}
```

#### Get Example
```json
{
  "name": "GoToWebinar",
  "type": "nodes-base.goToWebinar",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "details": "",
    "times": {},
    "webinarKey": [],
    "sessionKey": "",
    "registrantKey": "",
    "isExternal": false,
    "operation": "get"
  }
}
```

#### Get Many Example
```json
{
  "name": "GoToWebinar",
  "type": "nodes-base.goToWebinar",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "details": "",
    "times": {},
    "webinarKey": [],
    "sessionKey": "",
    "registrantKey": "",
    "isExternal": false,
    "operation": "getAll"
  }
}
```

---

## Grafana

## Basic Information

- Node Type: `nodes-base.grafana`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Grafana API

### Available Operations

### Create
Create a dashboard
- Value: `create`

### Delete
Delete a dashboard
- Value: `delete`

### Get
Get a dashboard
- Value: `get`

### Get Many
Get many dashboards
- Value: `getAll`

### Update
Update a dashboard
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `title` | string | Yes | `""` | Title of the dashboard to create |
| `dashboardUidOrUrl` | string | Yes | `""` | Unique alphabetic identifier or URL of the dashboard to delete |
| `dashboardUidOrUrl` | string | Yes | `""` | Unique alphabetic identifier or URL of the dashboard to retrieve |
| `dashboardUidOrUrl` | string | Yes | `""` | Unique alphabetic identifier or URL of the dashboard to update |
| `name` | string | Yes | `""` | Name of the team to create |
| `teamId` | string | Yes | `""` | ID of the team to delete |
| `teamId` | string | Yes | `""` | ID of the team to retrieve |
| `teamId` | string | Yes | `""` | ID of the team to update |
| `userId` | options | Yes | `""` | User to add to a team. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `teamId` | options | Yes | `""` | Team to add the user to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

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
  "name": "Grafana",
  "type": "nodes-base.grafana",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "dashboardUidOrUrl": "",
    "name": "",
    "teamId": "",
    "userId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Grafana",
  "type": "nodes-base.grafana",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "dashboardUidOrUrl": "",
    "name": "",
    "teamId": "",
    "userId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Grafana",
  "type": "nodes-base.grafana",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "dashboardUidOrUrl": "",
    "name": "",
    "teamId": "",
    "userId": "",
    "operation": "delete"
  }
}
```

---

## Hacker News

## Basic Information

- Node Type: `nodes-base.hackerNews`
- Category: transform
- Package: n8n-nodes-base

### Description

Consume Hacker News API

### Available Operations

### Get Many
Get many items
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `articleId` | string | Yes | `""` | The ID of the Hacker News article to be returned |
| `username` | string | Yes | `""` | The Hacker News user to be returned |
| `resource` | options | No | `"article"` | - |
| `operation` | options | No | `"getAll"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"get"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `100` | Max number of results to return |

#### Property Details

##### Resource (`resource`)

Optional values:
- `all`: All
- `article`: Article
- `user`: User

##### Operation (`operation`)

Optional values:
- `getAll`: Get Many - Get many items

##### Operation (`operation`)

Optional values:
- `get`: Get - Get a Hacker News article

##### Operation (`operation`)

Optional values:
- `get`: Get - Get a Hacker News user

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: includeComments - Whether to include all the comments in a Hacker News article

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: keyword - The keyword for filtering the results of the query
- `undefined`: tags - Tags for filtering the results of the query

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
  "name": "Hacker News",
  "type": "nodes-base.hackerNews",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "articleId": "",
    "username": ""
  }
}
```

#### Get Many Example
```json
{
  "name": "Hacker News",
  "type": "nodes-base.hackerNews",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "articleId": "",
    "username": "",
    "operation": "getAll"
  }
}
```

---

## HighLevel

## Basic Information

- Node Type: `nodes-base.highLevel`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume HighLevel API

### Available Operations

### Create or Update
- Value: `create`

### Delete
- Value: `delete`

### Get
- Value: `get`

### Get Many
- Value: `getAll`

### Update
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"contact"` | - |
| `status` | options | Yes | `"open"` | - |
| `contactId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `contactId` | options | Yes | `""` | Contact the task belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `contactId` | options | Yes | `""` | Contact the task belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `contactId` | options | Yes | `""` | Contact the task belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `contactId` | options | Yes | `""` | Contact the task belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `contactId` | options | Yes | `""` | Contact the task belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `startTime` | string | Yes | `""` | Example: 2021-06-23T03:30:00+05:30 |
| `startDate` | number | Yes | `""` | The start date for fetching free calendar slots. Example: 1548898600000. |

#### Property Details

##### Resource (`resource`)

Optional values:
- `contact`: Contact
- `opportunity`: Opportunity
- `task`: Task
- `calendar`: Calendar

##### Status (`status`)

Optional values:
- `open`: Open
- `won`: Won
- `lost`: Lost
- `abandoned`: Abandoned

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
  "name": "HighLevel",
  "type": "nodes-base.highLevel",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "contact",
    "status": "open",
    "contactId": "",
    "startTime": "",
    "startDate": ""
  }
}
```

#### Create or Update Example
```json
{
  "name": "HighLevel",
  "type": "nodes-base.highLevel",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "contact",
    "status": "open",
    "contactId": "",
    "startTime": "",
    "startDate": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "HighLevel",
  "type": "nodes-base.highLevel",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "contact",
    "status": "open",
    "contactId": "",
    "startTime": "",
    "startDate": "",
    "operation": "delete"
  }
}
```

---

## HTML

## Basic Information

- Node Type: `nodes-base.html`
- Category: transform
- Package: n8n-nodes-base

### Description

Work with HTML

### Available Operations

### Generate HTML Template
- Value: `generateHtmlTemplate`

### Extract HTML Content
- Value: `extractHtmlContent`

### Convert to HTML Table
- Value: `convertToHtmlTable`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `dataPropertyName` | string | Yes | `"data"` | Name of the JSON property in which the HTML to extract the data from can be found. The property can either contain a string or an array of strings. |
| `dataPropertyName` | string | Yes | `"data"` | - |
| `operation` | options | No | `"generateHtmlTemplate"` | - |
| `sourceData` | options | No | `"json"` | If HTML should be read from binary or JSON data |
| `extractionValues` | fixedCollection | No | `{}` | - |
| `extractionValues` | fixedCollection | No | `{"values":[{"key":"","cssSelector":"","returnValue":"text","returnArray":false}]}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `html` | string | No | `"<!DOCTYPE html>\n\n<html>\n<head>\n  <meta charset=\"UTF-8\" />\n  <title>My HTML document</title>\n</head>\n<body>\n  <div class=\"container\">\n    <h1>This is an H1 heading</h1>\n    <h2>This is an H2 heading</h2>\n    <p>This is a paragraph</p>\n  </div>\n</body>\n</html>\n\n<style>\n.container {\n  background-color: #ffffff;\n  text-align: center;\n  padding: 16px;\n  border-radius: 8px;\n}\n\nh1 {\n  color: #ff6d5a;\n  font-size: 24px;\n  font-weight: bold;\n  padding: 8px;\n}\n\nh2 {\n  color: #909399;\n  font-size: 18px;\n  font-weight: bold;\n  padding: 8px;\n}\n</style>\n\n<script>\nconsole.log(\"Hello World!\");\n</script>"` | HTML template to render |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `generateHtmlTemplate`: Generate HTML Template
- `extractHtmlContent`: Extract HTML Content
- `convertToHtmlTable`: Convert to HTML Table

##### Source Data (`sourceData`)

If HTML should be read from binary or JSON data

Optional values:
- `binary`: Binary
- `json`: JSON

##### Extraction Values (`extractionValues`)

Optional values:
- `undefined`: values

##### Extraction Values (`extractionValues`)

Optional values:
- `undefined`: values

##### Options (`options`)

Optional values:
- `undefined`: trimValues - Whether to remove automatically all spaces and newlines from the beginning and end of the values
- `undefined`: cleanUpText - Whether to remove leading and trailing whitespaces, line breaks (newlines) and condense multiple consecutive whitespaces into a single space

##### Options (`options`)

Optional values:
- `undefined`: capitalize - Whether to capitalize the headers
- `undefined`: customStyling - Whether to use custom styling
- `undefined`: caption - Caption to add to the table
- `undefined`: tableAttributes - Attributes to attach to the table
- `undefined`: headerAttributes - Attributes to attach to the table header
- `undefined`: rowAttributes - Attributes to attach to the table row
- `undefined`: cellAttributes - Attributes to attach to the table cell

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
  "name": "HTML",
  "type": "nodes-base.html",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dataPropertyName": "data"
  }
}
```

#### Generate HTML Template Example
```json
{
  "name": "HTML",
  "type": "nodes-base.html",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dataPropertyName": "data",
    "operation": "generateHtmlTemplate"
  }
}
```

#### Extract HTML Content Example
```json
{
  "name": "HTML",
  "type": "nodes-base.html",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dataPropertyName": "data",
    "operation": "extractHtmlContent"
  }
}
```

---

## HTML Extract

## Basic Information

- Node Type: `nodes-base.htmlExtract`
- Category: transform
- Package: n8n-nodes-base

### Description

Extracts data from HTML

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `dataPropertyName` | string | Yes | `"data"` | Name of the JSON property in which the HTML to extract the data from can be found. The property can either contain a string or an array of strings. |
| `dataPropertyName` | string | Yes | `"data"` | - |
| `sourceData` | options | No | `"json"` | If HTML should be read from binary or JSON data |
| `extractionValues` | fixedCollection | No | `{}` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Source Data (`sourceData`)

If HTML should be read from binary or JSON data

Optional values:
- `binary`: Binary
- `json`: JSON

##### Extraction Values (`extractionValues`)

Optional values:
- `undefined`: values

##### Options (`options`)

Optional values:
- `undefined`: trimValues - Whether to remove automatically all spaces and newlines from the beginning and end of the values

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
  "name": "HTML Extract",
  "type": "nodes-base.htmlExtract",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dataPropertyName": "data"
  }
}
```

---

## Jina AI

## Basic Information

- Node Type: `nodes-base.jinaAi`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Interact with Jina AI API

### Available Operations

### Read
Fetches content from a URL and converts it to clean, LLM-friendly formats
- Value: `read`

### Search
Performs a web search via Jina AI and returns top results as clean, LLM-friendly formats
- Value: `search`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | The URL to fetch content from |
| `researchQuery` | string | Yes | `""` | The topic or question for the AI to research |
| `searchQuery` | string | Yes | `""` | - |
| `resource` | options | No | `"reader"` | - |
| `operation` | options | No | `"read"` | - |
| `operation` | options | No | `"deepResearch"` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `simplify` | boolean | No | `true` | Whether to return a simplified version of the response instead of the raw data |

#### Property Details

##### Resource (`resource`)

Optional values:
- `reader`: Reader
- `research`: Research

##### Operation (`operation`)

Optional values:
- `read`: Read - Fetches content from a URL and converts it to clean, LLM-friendly formats
- `search`: Search - Performs a web search via Jina AI and returns top results as clean, LLM-friendly formats

##### Operation (`operation`)

Optional values:
- `deepResearch`: Deep Research - Research a topic and generate a structured research report

##### Options (`options`)

Optional values:
- `undefined`: outputFormat - Specify desired output format
- `undefined`: targetSelector - CSS selector to focus on specific page elements
- `undefined`: excludeSelector - CSS selector for elements to exclude
- `undefined`: enableImageCaptioning - Whether to generate captions for images within the content
- `undefined`: waitForSelector - Wait for a specific element to appear before extracting content (for dynamic pages)

##### Options (`options`)

Optional values:
- `undefined`: outputFormat - Specify desired output format
- `undefined`: siteFilter - Restrict search to specific websites
- `undefined`: pageNumber - The page number of the search results to retrieve

##### Options (`options`)

Optional values:
- `undefined`: maxReturnedSources - The maximum number of URLs to include in the final answer
- `undefined`: prioritizeSources - A list of domains that are given a higher priority for content retrieval
- `undefined`: excludeSources - A list of domains to be strictly excluded from content retrieval
- `undefined`: siteFilter - Restrict search to specific websites

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
  "name": "Jina AI",
  "type": "nodes-base.jinaAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "researchQuery": "",
    "searchQuery": ""
  }
}
```

#### Read Example
```json
{
  "name": "Jina AI",
  "type": "nodes-base.jinaAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "researchQuery": "",
    "searchQuery": "",
    "operation": "read"
  }
}
```

#### Search Example
```json
{
  "name": "Jina AI",
  "type": "nodes-base.jinaAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "researchQuery": "",
    "searchQuery": "",
    "operation": "search"
  }
}
```

---

## JWT

## Basic Information

- Node Type: `nodes-base.jwt`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

JWT

### Available Operations

### Decode
- Value: `decode`

### Sign
- Value: `sign`

### Verify
- Value: `verify`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `token` | string | Yes | `""` | The token to verify or decode |
| `operation` | options | No | `"sign"` | - |
| `claims` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `useJson` | boolean | No | `false` | Whether to use JSON to build the claims |
| `claimsJson` | json | No | `"{\n  \"my_field_1\": \"value 1\",\n  \"my_field_2\": \"value 2\"\n}\n"` | Claims to add to the token in JSON format |

#### Property Details

##### Operation (`operation`)

Optional values:
- `decode`: Decode
- `sign`: Sign
- `verify`: Verify

##### Payload Claims (`claims`)

Optional values:
- `undefined`: audience - Identifies the recipients that the JWT is intended for
- `undefined`: expiresIn - The lifetime of the token in seconds
- `undefined`: issuer - Identifies the principal that issued the JWT
- `undefined`: jwtid - Unique identifier for the JWT
- `undefined`: notBefore - The time before which the JWT must not be accepted for processing
- `undefined`: subject - Identifies the principal that is the subject of the JWT

##### Options (`options`)

Optional values:
- `undefined`: complete - Whether to return the complete decoded token with information about the header and signature or just the payload
- `undefined`: ignoreExpiration - Whether to ignore the expiration of the token
- `undefined`: ignoreNotBefore - Whether to ignore the not before claim of the token
- `undefined`: clockTolerance - Number of seconds to tolerate when checking the nbf and exp claims, to deal with small clock differences among different servers
- `undefined`: kid - The kid (key ID) claim is an optional header claim, used to specify the key for validating the signature
- `undefined`: algorithm - The algorithm to use for signing or verifying the token, overrides algorithm in credentials

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
  "name": "JWT",
  "type": "nodes-base.jwt",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "token": ""
  }
}
```

#### Decode Example
```json
{
  "name": "JWT",
  "type": "nodes-base.jwt",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "token": "",
    "operation": "decode"
  }
}
```

#### Sign Example
```json
{
  "name": "JWT",
  "type": "nodes-base.jwt",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "token": "",
    "operation": "sign"
  }
}
```

---

## Kafka

## Basic Information

- Node Type: `nodes-base.kafka`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Sends messages to a Kafka topic

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `schemaRegistryUrl` | string | Yes | `""` | URL of the schema registry |
| `key` | string | Yes | `""` | The message key |
| `eventName` | string | Yes | `""` | Namespace and Name of Schema in Schema Registry (namespace.name) |
| `headersUi` | fixedCollection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `topic` | string | No | `""` | Name of the queue of topic to publish to |
| `sendInputData` | boolean | No | `true` | Whether to send the data the node receives as JSON to Kafka |
| `message` | string | No | `""` | The message to be sent |
| `useSchemaRegistry` | boolean | No | `false` | Whether to use Confluent Schema Registry |
| `useKey` | boolean | No | `false` | Whether to use a message key |

#### Property Details

##### Headers (`headersUi`)

Optional values:
- `undefined`: headerValues

##### Options (`options`)

Optional values:
- `undefined`: acks - Whether or not producer must wait for acknowledgement from all replicas
- `undefined`: compression - Whether to send the data in a compressed format using the GZIP codec
- `undefined`: timeout - The time to await a response in ms

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
  "name": "Kafka",
  "type": "nodes-base.kafka",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "schemaRegistryUrl": "",
    "key": "",
    "eventName": ""
  }
}
```

---

## KoBoToolbox

## Basic Information

- Node Type: `nodes-base.koBoToolbox`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Work with KoBoToolbox forms and submissions

### Available Operations

### Get
Get a form
- Value: `get`

### Get Many
Get many forms
- Value: `getAll`

### Redeploy
Redeploy Current Form Version
- Value: `redeploy`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"submission"` | - |
| `validationStatus` | options | Yes | `""` | Desired Validation Status |
| `fileMode` | options | Yes | `"binary"` | - |
| `formId` | options | Yes | `""` | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `returnAll` | boolean | Yes | `false` | Whether to return all results or only up to a given limit |
| `formId` | options | Yes | `""` | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `hookId` | string | Yes | `""` | Hook ID (starts with h, e.g. hVehywQ2oXPYGHJHKtqth4) |
| `logId` | string | Yes | `""` | Hook log ID (starts with hl, e.g. hlSbGKaUKzTVNoWEVMYbLHe) |
| `returnAll` | boolean | Yes | `false` | Whether to return all results or only up to a given limit |
| `formId` | options | Yes | `""` | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

#### Property Details

##### Resource (`resource`)

Optional values:
- `file`: File
- `form`: Form
- `hook`: Hook
- `submission`: Submission

##### Validation Status (`validationStatus`)

Desired Validation Status

Optional values:
- `validation_status_approved`: Approved
- `validation_status_not_approved`: Not Approved
- `validation_status_on_hold`: On Hold

##### File Upload Mode (`fileMode`)

Optional values:
- `binary`: Binary File
- `url`: URL

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
  "name": "KoBoToolbox",
  "type": "nodes-base.koBoToolbox",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "submission",
    "validationStatus": "",
    "fileMode": "binary",
    "formId": "",
    "returnAll": false,
    "hookId": "",
    "logId": ""
  }
}
```

#### Get Example
```json
{
  "name": "KoBoToolbox",
  "type": "nodes-base.koBoToolbox",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "submission",
    "validationStatus": "",
    "fileMode": "binary",
    "formId": "",
    "returnAll": false,
    "hookId": "",
    "logId": "",
    "operation": "get"
  }
}
```

#### Get Many Example
```json
{
  "name": "KoBoToolbox",
  "type": "nodes-base.koBoToolbox",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "submission",
    "validationStatus": "",
    "fileMode": "binary",
    "formId": "",
    "returnAll": false,
    "hookId": "",
    "logId": "",
    "operation": "getAll"
  }
}
```

---

## Ldap

## Basic Information

- Node Type: `nodes-base.ldap`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Interact with LDAP servers

### Available Operations

### Compare
Compare an attribute
- Value: `compare`

### Create
Create a new entry
- Value: `create`

### Delete
Delete an entry
- Value: `delete`

### Rename
Rename the DN of an existing entry
- Value: `rename`

### Search
Search LDAP
- Value: `search`

### Update
Update attributes
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `dn` | string | Yes | `""` | The distinguished name of the entry to compare |
| `dn` | string | Yes | `""` | The distinguished name of the entry to create |
| `dn` | string | Yes | `""` | The distinguished name of the entry to delete |
| `dn` | string | Yes | `""` | The distinguished name of the entry to rename |
| `dn` | string | Yes | `""` | The distinguished name of the entry to modify |
| `dn` | string | Yes | `""` | The distinguished name of the entry to update |
| `id` | options | Yes | `[]` | The ID of the attribute to compare |
| `targetDn` | string | Yes | `""` | The new distinguished name for the entry |
| `baseDN` | string | Yes | `""` | The distinguished name of the subtree to search in |
| `attribute` | options | Yes | `[]` | Attribute to search for |

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
  "name": "Ldap",
  "type": "nodes-base.ldap",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dn": "",
    "id": [],
    "targetDn": "",
    "baseDN": "",
    "attribute": []
  }
}
```

#### Compare Example
```json
{
  "name": "Ldap",
  "type": "nodes-base.ldap",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dn": "",
    "id": [],
    "targetDn": "",
    "baseDN": "",
    "attribute": [],
    "operation": "compare"
  }
}
```

#### Create Example
```json
{
  "name": "Ldap",
  "type": "nodes-base.ldap",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dn": "",
    "id": [],
    "targetDn": "",
    "baseDN": "",
    "attribute": [],
    "operation": "create"
  }
}
```

---

## Lemlist

## Basic Information

- Node Type: `nodes-base.lemlist`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Lemlist API

### Available Operations

### Get Many
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `campaignId` | options | Yes | `[]` | ID of the campaign to get stats for. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `enrichId` | string | Yes | `""` | ID of the enrichment to retrieve |
| `campaignId` | options | Yes | `[]` | ID of the campaign to create the lead under. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `campaignId` | options | Yes | `[]` | ID of the campaign to remove the lead from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `campaignId` | options | Yes | `[]` | ID of the campaign to unsubscribe the lead from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `startDate` | dateTime | Yes | `""` | - |
| `endDate` | dateTime | Yes | `""` | - |
| `timezone` | string | Yes | `""` | - |
| `leadId` | string | Yes | `""` | - |
| `resource` | options | No | `"activity"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `activity`: Activity
- `campaign`: Campaign
- `enrich`: Enrichment
- `lead`: Lead
- `team`: Team
- `unsubscribe`: Unsubscribe

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
  "name": "Lemlist",
  "type": "nodes-base.lemlist",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "campaignId": [],
    "enrichId": "",
    "startDate": "",
    "endDate": "",
    "timezone": "",
    "leadId": ""
  }
}
```

#### Get Many Example
```json
{
  "name": "Lemlist",
  "type": "nodes-base.lemlist",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "campaignId": [],
    "enrichId": "",
    "startDate": "",
    "endDate": "",
    "timezone": "",
    "leadId": "",
    "operation": "getAll"
  }
}
```

---

## LoneScale

## Basic Information

- Node Type: `nodes-base.loneScale`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Create List, add / delete items

### Available Operations

### Create
Create a list
- Value: `create`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"list"` | Create a new list |
| `type` | options | Yes | `"PEOPLE"` | Type of your list |
| `type` | options | Yes | `"COMPANY"` | Type of your list |
| `list` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `first_name` | string | Yes | `""` | Contact first name |
| `last_name` | string | Yes | `""` | Contact last name |
| `name` | string | Yes | `""` | Name of your list |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"add"` | - |
| `peopleAdditionalFields` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Create a new list

Optional values:
- `list`: List - Manipulate list
- `item`: Item - Manipulate item

##### Type (`type`)

Type of your list

Optional values:
- `COMPANY`: Company - List of company
- `PEOPLE`: Contact - List of contact

##### Type (`type`)

Type of your list

Optional values:
- `COMPANY`: Company - Create a list of companies
- `PEOPLE`: Contact - Create a list of contacts

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a list

##### Operation (`operation`)

Optional values:
- `add`: Create - Create an item

##### Additional Fields (`peopleAdditionalFields`)

Optional values:
- `undefined`: full_name - Contact full name
- `undefined`: email
- `undefined`: company_name - Contact company name
- `undefined`: current_position - Contact current position
- `undefined`: domain - Contact company domain
- `undefined`: linkedin_url - Contact Linkedin URL
- `undefined`: location
- `undefined`: contact_id - Contact ID from your source

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
  "name": "LoneScale",
  "type": "nodes-base.loneScale",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "list",
    "type": "COMPANY",
    "list": "",
    "first_name": "",
    "last_name": "",
    "name": ""
  }
}
```

#### Create Example
```json
{
  "name": "LoneScale",
  "type": "nodes-base.loneScale",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "list",
    "type": "COMPANY",
    "list": "",
    "first_name": "",
    "last_name": "",
    "name": "",
    "operation": "create"
  }
}
```

---

## Mailcheck

## Basic Information

- Node Type: `nodes-base.mailcheck`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Mailcheck API

### Available Operations

### Check
- Value: `check`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | No | `"email"` | - |
| `operation` | options | No | `"check"` | - |
| `email` | string | No | `""` | Email address to check |

#### Property Details

##### Resource (`resource`)

Optional values:
- `email`: Email

##### Operation (`operation`)

Optional values:
- `check`: Check

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
  "name": "Mailcheck",
  "type": "nodes-base.mailcheck",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Check Example
```json
{
  "name": "Mailcheck",
  "type": "nodes-base.mailcheck",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "check"
  }
}
```

---

## Marketstack

## Basic Information

- Node Type: `nodes-base.marketstack`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Marketstack API

### Available Operations

### Get Many
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"endOfDayData"` | - |
| `symbols` | string | Yes | `""` | One or multiple comma-separated stock symbols (tickers) to retrieve, e.g. <code>AAPL</code> or <code>AAPL,MSFT</code> |
| `exchange` | string | Yes | `""` | Stock exchange to retrieve, specified by <a href="https://en.wikipedia.org/wiki/Market\_Identifier\_Code">Market Identifier Code</a>, e.g. <code>XNAS</code> |
| `symbol` | string | Yes | `""` | Stock symbol (ticker) to retrieve, e.g. <code>AAPL</code> |
| `operation` | options | No | `"getAll"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"get"` | - |
| `filters` | collection | No | `{}` | - |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `50` | Max number of results to return |

#### Property Details

##### Resource (`resource`)

Optional values:
- `endOfDayData`: End-of-Day Data - Stock market closing data
- `exchange`: Exchange - Stock market exchange
- `ticker`: Ticker - Stock market symbol

##### Operation (`operation`)

Optional values:
- `getAll`: Get Many

##### Operation (`operation`)

Optional values:
- `get`: Get

##### Operation (`operation`)

Optional values:
- `get`: Get

##### Filters (`filters`)

Optional values:
- `undefined`: exchange - Stock exchange to filter results by, specified by \<a href="https://en.wikipedia.org/wiki/Market\_Identifier\_Code"\>Market Identifier Code\</a\>, e.g. \<code\>XNAS\</code\>
- `undefined`: latest - Whether to fetch the most recent stock market data
- `undefined`: sort - Order to sort results in
- `undefined`: specificDate - Date in YYYY-MM-DD format, e.g. \<code\>2020-01-01\</code\>, or in ISO-8601 date format, e.g. \<code\>2020-05-21T00:00:00+0000\</code\>
- `undefined`: dateFrom - Timeframe start date in YYYY-MM-DD format, e.g. \<code\>2020-01-01\</code\>, or in ISO-8601 date format, e.g. \<code\>2020-05-21T00:00:00+0000\</code\>
- `undefined`: dateTo - Timeframe end date in YYYY-MM-DD format, e.g. \<code\>2020-01-01\</code\>, or in ISO-8601 date format, e.g. \<code\>2020-05-21T00:00:00+0000\</code\>

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
  "name": "Marketstack",
  "type": "nodes-base.marketstack",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "endOfDayData",
    "symbols": "",
    "exchange": "",
    "symbol": ""
  }
}
```

#### Get Many Example
```json
{
  "name": "Marketstack",
  "type": "nodes-base.marketstack",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "endOfDayData",
    "symbols": "",
    "exchange": "",
    "symbol": "",
    "operation": "getAll"
  }
}
```

---

## Metabase

## Basic Information

- Node Type: `nodes-base.metabase`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Use the Metabase API

### Available Operations

### Get
Get a specific question
- Value: `get`

### Get Many
Get many questions
- Value: `getAll`

### Result Data
Return the result of the question to a specific file format
- Value: `resultData`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `format` | options | Yes | `"csv"` | - |
| `engine` | options | Yes | `"postgres"` | - |
| `questionId` | string | Yes | `""` | - |
| `metricId` | string | Yes | `""` | - |
| `databaseId` | string | Yes | `""` | - |
| `host` | string | Yes | `""` | - |
| `name` | string | Yes | `""` | - |
| `port` | number | Yes | `5432` | - |
| `user` | string | Yes | `""` | - |
| `password` | string | Yes | `""` | - |

#### Property Details

##### Format (`format`)

Optional values:
- `csv`: CSV
- `json`: JSON
- `xlsx`: XLSX

##### Engine (`engine`)

Optional values:
- `h2`: H2
- `mongo`: MongoDB
- `mysql`: Mysql
- `postgres`: PostgreSQL
- `redshift`: Redshift
- `sqlite`: Sqlite

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
  "name": "Metabase",
  "type": "nodes-base.metabase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "format": "csv",
    "engine": "postgres",
    "questionId": "",
    "metricId": "",
    "databaseId": "",
    "host": "",
    "name": "",
    "port": 5432,
    "user": "",
    "password": ""
  }
}
```

#### Get Example
```json
{
  "name": "Metabase",
  "type": "nodes-base.metabase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "format": "csv",
    "engine": "postgres",
    "questionId": "",
    "metricId": "",
    "databaseId": "",
    "host": "",
    "name": "",
    "port": 5432,
    "user": "",
    "password": "",
    "operation": "get"
  }
}
```

#### Get Many Example
```json
{
  "name": "Metabase",
  "type": "nodes-base.metabase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "format": "csv",
    "engine": "postgres",
    "questionId": "",
    "metricId": "",
    "databaseId": "",
    "host": "",
    "name": "",
    "port": 5432,
    "user": "",
    "password": "",
    "operation": "getAll"
  }
}
```

---

## Microsoft Entra ID

## Basic Information

- Node Type: `nodes-base.microsoftEntra`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Interact with Microsoft Entra ID API

### Available Operations

### Create
Create a group
- Value: `create`

### Delete
Delete a group
- Value: `delete`

### Get
Retrieve data for a specific group
- Value: `get`

### Get Many
Retrieve a list of groups
- Value: `getAll`

### Update
Update a group
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `displayName` | string | Yes | `""` | The name to display in the address book for the group |
| `mailNickname` | string | Yes | `""` | The mail alias for the group. Only enter the local-part without the domain. |
| `mailEnabled` | boolean | Yes | `false` | Whether the group is mail-enabled |
| `accountEnabled` | boolean | Yes | `true` | Whether the account is enabled |
| `displayName` | string | Yes | `""` | The name to display in the address book for the user |
| `userPrincipalName` | string | Yes | `""` | The user principal name (UPN) |
| `mailNickname` | string | Yes | `""` | The mail alias for the user |
| `password` | string | Yes | `""` | The password for the user |
| `group` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `group` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |

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
  "name": "Microsoft Entra ID",
  "type": "nodes-base.microsoftEntra",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "displayName": "",
    "mailNickname": "",
    "mailEnabled": false,
    "accountEnabled": true,
    "userPrincipalName": "",
    "password": "",
    "group": {
      "mode": "list",
      "value": ""
    }
  }
}
```

#### Create Example
```json
{
  "name": "Microsoft Entra ID",
  "type": "nodes-base.microsoftEntra",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "displayName": "",
    "mailNickname": "",
    "mailEnabled": false,
    "accountEnabled": true,
    "userPrincipalName": "",
    "password": "",
    "group": {
      "mode": "list",
      "value": ""
    },
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Microsoft Entra ID",
  "type": "nodes-base.microsoftEntra",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "displayName": "",
    "mailNickname": "",
    "mailEnabled": false,
    "accountEnabled": true,
    "userPrincipalName": "",
    "password": "",
    "group": {
      "mode": "list",
      "value": ""
    },
    "operation": "delete"
  }
}
```

---

## Microsoft Graph Security

## Basic Information

- Node Type: `nodes-base.microsoftGraphSecurity`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Microsoft Graph Security API

### Available Operations

### Get
- Value: `get`

### Get Many
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `secureScoreId` | string | Yes | `""` | ID of the secure score to retrieve |
| `secureScoreControlProfileId` | string | Yes | `""` | ID of the secure score control profile to retrieve |
| `secureScoreControlProfileId` | string | Yes | `""` | ID of the secure score control profile to update |
| `provider` | string | Yes | `""` | Name of the provider of the security product or service |
| `vendor` | string | Yes | `""` | Name of the vendor of the security product or service |
| `resource` | options | No | `"secureScore"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"get"` | - |
| `filters` | collection | No | `{}` | - |
| `filters` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `secureScore`: Secure Score
- `secureScoreControlProfile`: Secure Score Control Profile

##### Operation (`operation`)

Optional values:
- `get`: Get
- `getAll`: Get Many

##### Operation (`operation`)

Optional values:
- `get`: Get
- `getAll`: Get Many
- `update`: Update

##### Filters (`filters`)

Optional values:
- `undefined`: filter - \<a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter"\>Query parameter\</a\> to filter results by
- `undefined`: includeControlScores

##### Filters (`filters`)

Optional values:
- `undefined`: filter - \<a href="https://docs.microsoft.com/en-us/graph/query-parameters#filter-parameter"\>Query parameter\</a\> to filter results by

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
  "name": "Microsoft Graph Security",
  "type": "nodes-base.microsoftGraphSecurity",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "secureScoreId": "",
    "secureScoreControlProfileId": "",
    "provider": "",
    "vendor": ""
  }
}
```

#### Get Example
```json
{
  "name": "Microsoft Graph Security",
  "type": "nodes-base.microsoftGraphSecurity",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "secureScoreId": "",
    "secureScoreControlProfileId": "",
    "provider": "",
    "vendor": "",
    "operation": "get"
  }
}
```

#### Get Many Example
```json
{
  "name": "Microsoft Graph Security",
  "type": "nodes-base.microsoftGraphSecurity",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "secureScoreId": "",
    "secureScoreControlProfileId": "",
    "provider": "",
    "vendor": "",
    "operation": "getAll"
  }
}
```

---

## Microsoft Outlook

## Basic Information

- Node Type: `nodes-base.microsoftOutlook`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Microsoft Outlook API

### Available Operations

### Create
Create a new calendar
- Value: `create`

### Delete
Delete a calendar
- Value: `delete`

### Get
Retrieve a calendar
- Value: `get`

### Get Many
List and search calendars
- Value: `getAll`

### Update
Update a calendar
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `name` | string | Yes | `""` | The name of the calendar to create |
| `displayName` | string | Yes | `""` | Name of the folder |
| `displayName` | string | Yes | `""` | Name of the folder |
| `toRecipients` | string | Yes | `""` | Comma-separated list of email addresses of recipients |
| `toRecipients` | string | Yes | `""` | Comma-separated list of email addresses of recipients |
| `calendarId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `calendarId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `calendarId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `givenName` | string | Yes | `""` | - |
| `contactId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |

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
  "name": "Microsoft Outlook",
  "type": "nodes-base.microsoftOutlook",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "displayName": "",
    "toRecipients": "",
    "calendarId": {
      "mode": "list",
      "value": ""
    },
    "givenName": "",
    "contactId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

#### Create Example
```json
{
  "name": "Microsoft Outlook",
  "type": "nodes-base.microsoftOutlook",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "displayName": "",
    "toRecipients": "",
    "calendarId": {
      "mode": "list",
      "value": ""
    },
    "givenName": "",
    "contactId": {
      "mode": "list",
      "value": ""
    },
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Microsoft Outlook",
  "type": "nodes-base.microsoftOutlook",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "displayName": "",
    "toRecipients": "",
    "calendarId": {
      "mode": "list",
      "value": ""
    },
    "givenName": "",
    "contactId": {
      "mode": "list",
      "value": ""
    },
    "operation": "delete"
  }
}
```

---

## Microsoft SharePoint

## Basic Information

- Node Type: `nodes-base.microsoftSharePoint`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Interact with Microsoft SharePoint API

### Available Operations

### Download
Download a file
- Value: `download`

### Update
Update a file
- Value: `update`

### Upload
Upload an existing file
- Value: `upload`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `site` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the site to retrieve folders from |
| `folder` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the folder to download the file from |
| `file` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the file to download |
| `site` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the site to retrieve folders from |
| `folder` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the folder to update the file in |
| `file` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the file to update |
| `changeFileContent` | boolean | Yes | `false` | Whether to update the file contents |
| `fileContents` | string | Yes | `""` | Find the name of input field containing the binary data to update the file with in the Input panel on the left, in the Binary tab |
| `site` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the site to retrieve folders from |
| `folder` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the folder to upload the file to |

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
  "name": "Microsoft SharePoint",
  "type": "nodes-base.microsoftSharePoint",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "site": {
      "mode": "list",
      "value": ""
    },
    "folder": {
      "mode": "list",
      "value": ""
    },
    "file": {
      "mode": "list",
      "value": ""
    },
    "changeFileContent": false,
    "fileContents": ""
  }
}
```

#### Download Example
```json
{
  "name": "Microsoft SharePoint",
  "type": "nodes-base.microsoftSharePoint",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "site": {
      "mode": "list",
      "value": ""
    },
    "folder": {
      "mode": "list",
      "value": ""
    },
    "file": {
      "mode": "list",
      "value": ""
    },
    "changeFileContent": false,
    "fileContents": "",
    "operation": "download"
  }
}
```

#### Update Example
```json
{
  "name": "Microsoft SharePoint",
  "type": "nodes-base.microsoftSharePoint",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "site": {
      "mode": "list",
      "value": ""
    },
    "folder": {
      "mode": "list",
      "value": ""
    },
    "file": {
      "mode": "list",
      "value": ""
    },
    "changeFileContent": false,
    "fileContents": "",
    "operation": "update"
  }
}
```

---

## MISP

## Basic Information

- Node Type: `nodes-base.misp`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the MISP API

### Available Operations

### Create
- Value: `create`

### Delete
- Value: `delete`

### Get
- Value: `get`

### Get Many
- Value: `getAll`

### Search
- Value: `search`

### Update
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `value` | string | Yes | `""` | - |
| `value` | string | Yes | `""` | - |
| `value` | string | Yes | `""` | - |
| `url` | string | Yes | `""` | - |
| `value` | string | Yes | `""` | - |
| `type` | options | Yes | `"text"` | - |
| `eventId` | string | Yes | `""` | UUID of the event to attach the attribute to |
| `attributeId` | string | Yes | `""` | UUID or numeric ID of the attribute |
| `attributeId` | string | Yes | `""` | UUID or numeric ID of the attribute |
| `attributeId` | string | Yes | `""` | ID of the attribute to update |

#### Property Details

##### Type (`type`)

Optional values:
- `text`: Text
- `url`: URL
- `comment`: Comment

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
  "name": "MISP",
  "type": "nodes-base.misp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "url": "",
    "type": "text",
    "eventId": "",
    "attributeId": ""
  }
}
```

#### Create Example
```json
{
  "name": "MISP",
  "type": "nodes-base.misp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "url": "",
    "type": "text",
    "eventId": "",
    "attributeId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "MISP",
  "type": "nodes-base.misp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "url": "",
    "type": "text",
    "eventId": "",
    "attributeId": "",
    "operation": "delete"
  }
}
```

---

## Mistral AI

## Basic Information

- Node Type: `nodes-base.mistralAi`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Mistral AI API

### Available Operations

### Extract Text
Extract text from document using OCR
- Value: `extractText`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | URL of the document or image to process |
| `model` | options | Yes | `"mistral-ocr-latest"` | The OCR model to use |
| `documentType` | options | Yes | `"document_url"` | The type of document to process |
| `inputType` | options | Yes | `"binary"` | How the document will be provided |
| `binaryProperty` | string | Yes | `"data"` | Name of the input binary field that contains the file to process |
| `resource` | options | No | `"document"` | - |
| `operation` | options | No | `"extractText"` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Model (`model`)

The OCR model to use

Optional values:
- `mistral-ocr-latest`: mistral-ocr-latest

##### Document Type (`documentType`)

The type of document to process

Optional values:
- `document_url`: Document
- `image_url`: Image

##### Input Type (`inputType`)

How the document will be provided

Optional values:
- `binary`: Binary Data
- `url`: URL

##### Resource (`resource`)

Optional values:
- `document`: Document

##### Operation (`operation`)

Optional values:
- `extractText`: Extract Text - Extract text from document using OCR

##### Options (`options`)

Optional values:
- `undefined`: batch - Whether to process multiple documents in a single API call (more cost-efficient)
- `undefined`: batchSize - Maximum number of documents to process in a single batch
- `undefined`: deleteFiles - Whether to delete the files on Mistral Cloud after processing

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
  "name": "Mistral AI",
  "type": "nodes-base.mistralAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "model": "mistral-ocr-latest",
    "documentType": "document_url",
    "inputType": "binary",
    "binaryProperty": "data"
  }
}
```

#### Extract Text Example
```json
{
  "name": "Mistral AI",
  "type": "nodes-base.mistralAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "model": "mistral-ocr-latest",
    "documentType": "document_url",
    "inputType": "binary",
    "binaryProperty": "data",
    "operation": "extractText"
  }
}
```

---

## Mocean

## Basic Information

- Node Type: `nodes-base.mocean`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Send SMS and voice messages via Mocean

### Available Operations

### Send
Send SMS/Voice message
- Value: `send`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `from` | string | Yes | `""` | Number to which to send the message |
| `to` | string | Yes | `""` | Number from which to send the message |
| `message` | string | Yes | `""` | Message to send |
| `resource` | options | No | `"sms"` | - |
| `operation` | options | No | `"send"` | - |
| `language` | options | No | `"en-US"` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `sms`: SMS
- `voice`: Voice

##### Operation (`operation`)

Optional values:
- `send`: Send - Send SMS/Voice message

##### Language (`language`)

Optional values:
- `cmn-CN`: Chinese Mandarin (China)
- `en-GB`: English (United Kingdom)
- `en-US`: English (United States)
- `ja-JP`: Japanese (Japan)
- `ko-KR`: Korean (Korea)

##### Options (`options`)

Optional values:
- `undefined`: dlrUrl

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
  "name": "Mocean",
  "type": "nodes-base.mocean",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "from": "",
    "to": "",
    "message": ""
  }
}
```

#### Send Example
```json
{
  "name": "Mocean",
  "type": "nodes-base.mocean",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "from": "",
    "to": "",
    "message": "",
    "operation": "send"
  }
}
```

---

## Monica CRM

## Basic Information

- Node Type: `nodes-base.monicaCrm`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Monica CRM API

### Available Operations

### Create
Create an activity
- Value: `create`

### Delete
Delete an activity
- Value: `delete`

### Get
Retrieve an activity
- Value: `get`

### Get Many
Retrieve many activities
- Value: `getAll`

### Update
Update an activity
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `writtenByMe` | options | Yes | `true` | Author of the message |
| `frequencyType` | options | Yes | `"one_time"` | Type of frequency of the reminder |
| `activityTypeId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `contacts` | string | Yes | `""` | Comma-separated list of IDs of the contacts to associate the activity with |
| `happenedAt` | dateTime | Yes | `""` | Date when the activity happened |
| `summary` | string | Yes | `""` | Brief description of the activity - max 255 characters |
| `activityId` | string | Yes | `""` | ID of the activity to delete |
| `activityId` | string | Yes | `""` | ID of the activity to retrieve |
| `activityId` | string | Yes | `""` | ID of the activity to update |
| `contactId` | string | Yes | `""` | ID of the contact to associate the call with |

#### Property Details

##### Written By (`writtenByMe`)

Author of the message

Optional values:
- `true`: User
- `false`: Contact

##### Frequency Type (`frequencyType`)

Type of frequency of the reminder

Optional values:
- `one_time`: Once
- `week`: Weekly
- `month`: Monthly
- `year`: Yearly

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
  "name": "Monica CRM",
  "type": "nodes-base.monicaCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "writtenByMe": true,
    "frequencyType": "one_time",
    "activityTypeId": "",
    "contacts": "",
    "happenedAt": "",
    "summary": "",
    "activityId": "",
    "contactId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Monica CRM",
  "type": "nodes-base.monicaCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "writtenByMe": true,
    "frequencyType": "one_time",
    "activityTypeId": "",
    "contacts": "",
    "happenedAt": "",
    "summary": "",
    "activityId": "",
    "contactId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Monica CRM",
  "type": "nodes-base.monicaCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "writtenByMe": true,
    "frequencyType": "one_time",
    "activityTypeId": "",
    "contacts": "",
    "happenedAt": "",
    "summary": "",
    "activityId": "",
    "contactId": "",
    "operation": "delete"
  }
}
```

---

## MSG91

## Basic Information

- Node Type: `nodes-base.msg91`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Sends transactional SMS via MSG91

### Available Operations

### Send
Send SMS
- Value: `send`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `from` | string | Yes | `""` | The number from which to send the message |
| `to` | string | Yes | `""` | The number, with coutry code, to which to send the message |
| `message` | string | Yes | `""` | The message to send |
| `resource` | options | No | `"sms"` | - |
| `operation` | options | No | `"send"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `sms`: SMS

##### Operation (`operation`)

Optional values:
- `send`: Send - Send SMS

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
  "name": "MSG91",
  "type": "nodes-base.msg91",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "from": "",
    "to": "",
    "message": ""
  }
}
```

#### Send Example
```json
{
  "name": "MSG91",
  "type": "nodes-base.msg91",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "from": "",
    "to": "",
    "message": "",
    "operation": "send"
  }
}
```

---

## n8n

## Basic Information

- Node Type: `nodes-base.n8n`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle events and perform actions on your n8n instance

### Available Operations

### Generate
Generate a security audit for this n8n instance
- Value: `generate`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `name` | string | Yes | `""` | Name of the new credential |
| `credentialTypeName` | string | Yes | `""` | The available types depend on nodes installed on the n8n instance. Some built-in types include e.g. 'githubApi', 'notionApi', and 'slackApi'. |
| `data` | json | Yes | `""` | A valid JSON object with properties required for this Credential Type. To see the expected format, you can use 'Get Schema' operation. |
| `credentialTypeName` | string | Yes | `""` | The available types depend on nodes installed on the n8n instance. Some built-in types include e.g. 'githubApi', 'notionApi', and 'slackApi'. |
| `workflowId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Workflow to filter the executions by |
| `workflowObject` | json | Yes | `"{ \"name\": \"My workflow\", \"nodes\": [], \"connections\": {}, \"settings\": {} }"` | A valid JSON object with required fields: 'name', 'nodes', 'connections' and 'settings'. More information can be found in the <a href="https://docs.n8n.io/api/api-reference/#tag/workflow/paths/~1workflows/post">documentation</a>. |
| `workflowId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Workflow to filter the executions by |
| `workflowId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Workflow to filter the executions by |
| `workflowId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Workflow to filter the executions by |
| `workflowId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Workflow to filter the executions by |

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
  "name": "n8n",
  "type": "nodes-base.n8n",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "credentialTypeName": "",
    "data": "",
    "workflowId": {
      "mode": "list",
      "value": ""
    },
    "workflowObject": "{ \"name\": \"My workflow\", \"nodes\": [], \"connections\": {}, \"settings\": {} }"
  }
}
```

#### Generate Example
```json
{
  "name": "n8n",
  "type": "nodes-base.n8n",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "credentialTypeName": "",
    "data": "",
    "workflowId": {
      "mode": "list",
      "value": ""
    },
    "workflowObject": "{ \"name\": \"My workflow\", \"nodes\": [], \"connections\": {}, \"settings\": {} }",
    "operation": "generate"
  }
}
```

---

## NASA

## Basic Information

- Node Type: `nodes-base.nasa`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Retrieve data from the NASA API

### Available Operations

### Get
Get the Astronomy Picture of the Day
- Value: `get`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `asteroidId` | string | Yes | `""` | The ID of the asteroid to be returned |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `resource` | options | No | `"astronomyPictureOfTheDay"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"getAll"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"get"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `asteroidNeoBrowse`: Asteroid Neo-Browse
- `asteroidNeoFeed`: Asteroid Neo-Feed
- `asteroidNeoLookup`: Asteroid Neo-Lookup
- `astronomyPictureOfTheDay`: Astronomy Picture of the Day
- `donkiCoronalMassEjection`: DONKI Coronal Mass Ejection
- `donkiHighSpeedStream`: DONKI High Speed Stream
- `donkiInterplanetaryShock`: DONKI Interplanetary Shock
- `donkiMagnetopauseCrossing`: DONKI Magnetopause Crossing
- `donkiNotifications`: DONKI Notification
- `donkiRadiationBeltEnhancement`: DONKI Radiation Belt Enhancement
- `donkiSolarEnergeticParticle`: DONKI Solar Energetic Particle
- `donkiSolarFlare`: DONKI Solar Flare
- `donkiWsaEnlilSimulation`: DONKI WSA+EnlilSimulation
- `earthAssets`: Earth Asset
- `earthImagery`: Earth Imagery

##### Operation (`operation`)

Optional values:
- `get`: Get - Get the Astronomy Picture of the Day

##### Operation (`operation`)

Optional values:
- `get`: Get - Retrieve a list of asteroids based on their closest approach date to Earth

##### Operation (`operation`)

Optional values:
- `get`: Get - Look up an asteroid based on its NASA SPK-ID

##### Operation (`operation`)

Optional values:
- `getAll`: Get Many - Browse the overall asteroid dataset

##### Operation (`operation`)

Optional values:
- `get`: Get - Retrieve DONKI coronal mass ejection data

##### Operation (`operation`)

Optional values:
- `get`: Get - Retrieve DONKI geomagnetic storm data

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
  "name": "NASA",
  "type": "nodes-base.nasa",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "asteroidId": "",
    "binaryPropertyName": "data"
  }
}
```

#### Get Example
```json
{
  "name": "NASA",
  "type": "nodes-base.nasa",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "asteroidId": "",
    "binaryPropertyName": "data",
    "operation": "get"
  }
}
```

---

## Netlify

## Basic Information

- Node Type: `nodes-base.netlify`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Netlify API

### Available Operations

### Cancel
Cancel a deployment
- Value: `cancel`

### Create
Create a new deployment
- Value: `create`

### Get
Get a deployment
- Value: `get`

### Get Many
Get many deployments
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"deploy"` | - |
| `siteId` | options | Yes | `""` | Enter the Site ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `deployId` | string | Yes | `""` | - |
| `siteId` | string | Yes | `""` | - |
| `operation` | options | No | `"getAll"` | - |
| `operation` | options | No | `"delete"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `50` | Max number of results to return |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |

#### Property Details

##### Resource (`resource`)

Optional values:
- `deploy`: Deploy
- `site`: Site

##### Operation (`operation`)

Optional values:
- `cancel`: Cancel - Cancel a deployment
- `create`: Create - Create a new deployment
- `get`: Get - Get a deployment
- `getAll`: Get Many - Get many deployments

##### Operation (`operation`)

Optional values:
- `delete`: Delete - Delete a site
- `get`: Get - Get a site
- `getAll`: Get Many - Returns many sites

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: branch
- `undefined`: title

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
  "name": "Netlify",
  "type": "nodes-base.netlify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "deploy",
    "siteId": "",
    "deployId": ""
  }
}
```

#### Cancel Example
```json
{
  "name": "Netlify",
  "type": "nodes-base.netlify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "deploy",
    "siteId": "",
    "deployId": "",
    "operation": "cancel"
  }
}
```

#### Create Example
```json
{
  "name": "Netlify",
  "type": "nodes-base.netlify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "deploy",
    "siteId": "",
    "deployId": "",
    "operation": "create"
  }
}
```

---

## Odoo

## Basic Information

- Node Type: `nodes-base.odoo`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Odoo API

### Available Operations

### Create
Create a new item
- Value: `create`

### Delete
Delete an item
- Value: `delete`

### Get
Get an item
- Value: `get`

### Get Many
Get many items
- Value: `getAll`

### Update
Update an item
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `customResourceId` | string | Yes | `""` | - |
| `customResourceId` | string | Yes | `""` | - |
| `opportunityName` | string | Yes | `""` | - |
| `opportunityId` | string | Yes | `""` | - |
| `opportunityId` | string | Yes | `""` | - |
| `contactName` | string | Yes | `""` | - |
| `contactId` | string | Yes | `""` | - |
| `contactId` | string | Yes | `""` | - |
| `memo` | string | Yes | `""` | - |
| `noteId` | string | Yes | `""` | - |

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
  "name": "Odoo",
  "type": "nodes-base.odoo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "customResourceId": "",
    "opportunityName": "",
    "opportunityId": "",
    "contactName": "",
    "contactId": "",
    "memo": "",
    "noteId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Odoo",
  "type": "nodes-base.odoo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "customResourceId": "",
    "opportunityName": "",
    "opportunityId": "",
    "contactName": "",
    "contactId": "",
    "memo": "",
    "noteId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Odoo",
  "type": "nodes-base.odoo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "customResourceId": "",
    "opportunityName": "",
    "opportunityId": "",
    "contactName": "",
    "contactId": "",
    "memo": "",
    "noteId": "",
    "operation": "delete"
  }
}
```

---

## Okta

## Basic Information

- Node Type: `nodes-base.okta`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Use the Okta API

### Available Operations

### Create
Create a new user
- Value: `create`

### Delete
Delete an existing user
- Value: `delete`

### Get
Get details of a user
- Value: `get`

### Get Many
Get many users
- Value: `getAll`

### Update
Update an existing user
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `userId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The user you want to operate on. Choose from the list, or specify an ID. |
| `firstName` | string | Yes | `""` | - |
| `lastName` | string | Yes | `""` | - |
| `login` | string | Yes | `""` | - |
| `email` | string | Yes | `""` | - |
| `resource` | options | No | `"user"` | - |
| `operation` | options | No | `"getAll"` | - |
| `getCreateFields` | collection | No | `{}` | - |
| `getUpdateFields` | collection | No | `{}` | - |
| `activate` | boolean | No | `true` | Whether to activate the user and allow access to all assigned applications |

#### Property Details

##### Resource (`resource`)

Optional values:
- `user`: User

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new user
- `delete`: Delete - Delete an existing user
- `get`: Get - Get details of a user
- `getAll`: Get Many - Get many users
- `update`: Update - Update an existing user

##### Fields (`getCreateFields`)

Optional values:
- `undefined`: city
- `undefined`: costCenter
- `undefined`: countryCode
- `undefined`: department
- `undefined`: displayName
- `undefined`: division
- `undefined`: employeeNumber
- `undefined`: honorificPrefix
- `undefined`: honorificSuffix
- `undefined`: locale
- `undefined`: manager
- `undefined`: managerId
- `undefined`: middleName
- `undefined`: mobilePhone
- `undefined`: nickName
- `undefined`: password
- `undefined`: organization
- `undefined`: postalAddress
- `undefined`: preferredLanguage
- `undefined`: primaryPhone
- `undefined`: profileUrl
- `undefined`: recoveryQuestionAnswer
- `undefined`: recoveryQuestionQuestion
- `undefined`: secondEmail
- `undefined`: state
- `undefined`: streetAddress
- `undefined`: timezone
- `undefined`: title
- `undefined`: userType
- `undefined`: zipCode

##### Fields (`getUpdateFields`)

Optional values:
- `undefined`: city
- `undefined`: costCenter
- `undefined`: countryCode
- `undefined`: department
- `undefined`: displayName
- `undefined`: division
- `undefined`: email
- `undefined`: employeeNumber
- `undefined`: firstName
- `undefined`: honorificPrefix
- `undefined`: honorificSuffix
- `undefined`: lastName
- `undefined`: locale
- `undefined`: manager
- `undefined`: managerId
- `undefined`: middleName
- `undefined`: mobilePhone
- `undefined`: nickName
- `undefined`: organization
- `undefined`: password
- `undefined`: postalAddress
- `undefined`: preferredLanguage
- `undefined`: primaryPhone
- `undefined`: profileUrl
- `undefined`: recoveryQuestionAnswer
- `undefined`: recoveryQuestionQuestion
- `undefined`: secondEmail
- `undefined`: state
- `undefined`: streetAddress
- `undefined`: timezone
- `undefined`: title
- `undefined`: userType
- `undefined`: login
- `undefined`: zipCode

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
  "name": "Okta",
  "type": "nodes-base.okta",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "userId": {
      "mode": "list",
      "value": ""
    },
    "firstName": "",
    "lastName": "",
    "login": "",
    "email": ""
  }
}
```

#### Create Example
```json
{
  "name": "Okta",
  "type": "nodes-base.okta",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "userId": {
      "mode": "list",
      "value": ""
    },
    "firstName": "",
    "lastName": "",
    "login": "",
    "email": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Okta",
  "type": "nodes-base.okta",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "userId": {
      "mode": "list",
      "value": ""
    },
    "firstName": "",
    "lastName": "",
    "login": "",
    "email": "",
    "operation": "delete"
  }
}
```

---

## One Simple API

## Basic Information

- Node Type: `nodes-base.oneSimpleApi`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

A toolbox of no-code utilities

### Available Operations

### Generate PDF
Generate a PDF from a webpage
- Value: `pdf`

### Get SEO Data
Get SEO information from website
- Value: `seo`

### Take Screenshot
Create a screenshot from a webpage
- Value: `screenshot`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"website"` | - |
| `value` | string | Yes | `""` | Value to convert |
| `link` | string | Yes | `""` | Link to webpage to convert |
| `download` | boolean | Yes | `false` | Whether to download the PDF or return a link to it |
| `output` | string | Yes | `"data"` | The name of the output field to put the binary file data in |
| `message` | string | Yes | `""` | The text that should be turned into a QR code - like a website URL |
| `download` | boolean | Yes | `false` | Whether to download the QR code or return a link to it |
| `output` | string | Yes | `"data"` | The name of the output field to put the binary file data in |
| `link` | string | Yes | `""` | Link to webpage to convert |
| `download` | boolean | Yes | `false` | Whether to download the screenshot or return a link to it |

#### Property Details

##### Resource (`resource`)

Optional values:
- `information`: Information
- `socialProfile`: Social Profile
- `utility`: Utility
- `website`: Website

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
  "name": "One Simple API",
  "type": "nodes-base.oneSimpleApi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "website",
    "value": "",
    "link": "",
    "download": false,
    "output": "data",
    "message": ""
  }
}
```

#### Generate PDF Example
```json
{
  "name": "One Simple API",
  "type": "nodes-base.oneSimpleApi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "website",
    "value": "",
    "link": "",
    "download": false,
    "output": "data",
    "message": "",
    "operation": "pdf"
  }
}
```

#### Get SEO Data Example
```json
{
  "name": "One Simple API",
  "type": "nodes-base.oneSimpleApi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "website",
    "value": "",
    "link": "",
    "download": false,
    "output": "data",
    "message": "",
    "operation": "seo"
  }
}
```

---

## Perplexity

## Basic Information

- Node Type: `nodes-base.perplexity`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Interact with the Perplexity API to generate AI responses with citations

### Available Operations

### Message a Model
Create one or more completions for a given text
- Value: `complete`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `model` | options | Yes | `"sonar"` | The model which will generate the completion |
| `messages` | fixedCollection | Yes | `{"message":[{"role":"user","content":""}]}` | Any optional system messages must be sent first, followed by alternating user and assistant messages |
| `resource` | hidden | No | `"chat"` | - |
| `operation` | options | No | `"complete"` | - |
| `options` | collection | No | `{}` | - |
| `simplify` | boolean | No | `false` | Whether to return only essential fields (ID, citations, message) |

#### Property Details

##### Model (`model`)

The model which will generate the completion

Optional values:
- `sonar`: Sonar
- `sonar-deep-research`: Sonar Deep Research
- `sonar-pro`: Sonar Pro
- `sonar-reasoning`: Sonar Reasoning
- `sonar-reasoning-pro`: Sonar Reasoning Pro

##### Messages (`messages`)

Any optional system messages must be sent first, followed by alternating user and assistant messages

Optional values:
- `undefined`: message

##### Resource (`resource`)

Optional values:
- `chat`: Chat

##### Operation (`operation`)

Optional values:
- `complete`: Message a Model - Create one or more completions for a given text

##### Options (`options`)

Optional values:
- `undefined`: frequencyPenalty - Values greater than 1.0 penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim
- `undefined`: maxTokens - The maximum number of tokens to generate in the completion. The number of tokens requested plus the number of prompt tokens sent in messages must not exceed the context window token limit of model requested.
- `undefined`: temperature - The amount of randomness in the response, valued between 0 inclusive and 2 exclusive. Higher values are more random, and lower values are more deterministic.
- `undefined`: topK - The number of tokens to keep for highest Top K filtering, specified as an integer between 0 and 2048 inclusive. If set to 0, Top K filtering is disabled. We recommend either altering Top K or Top P, but not both.
- `undefined`: topP - The nucleus sampling threshold, valued between 0 and 1 inclusive. For each subsequent token, the model considers the results of the tokens with Top P probability mass. We recommend either altering Top K or Top P, but not both.
- `undefined`: presencePenalty - A value between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
- `undefined`: returnImages - Whether or not a request to an online model should return images. Requires Perplexity API usage Tier-2.
- `undefined`: returnRelatedQuestions - Whether or not a request to an online model should return related questions. Requires Perplexity API usage Tier-2.
- `undefined`: searchDomainFilter - Limit the citations used by the online model to URLs from the specified domains. For blacklisting, add a \<code\>-\</code\> to the beginning of the domain string (e.g., \<code\>-domain1\</code\>). Currently limited to 3 domains. Requires Perplexity API usage Tier-3.
- `undefined`: searchRecency - Returns search results within the specified time interval

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
  "name": "Perplexity",
  "type": "nodes-base.perplexity",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "model": "sonar",
    "messages": {
      "message": [
        {
          "role": "user",
          "content": ""
        }
      ]
    }
  }
}
```

#### Message a Model Example
```json
{
  "name": "Perplexity",
  "type": "nodes-base.perplexity",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "model": "sonar",
    "messages": {
      "message": [
        {
          "role": "user",
          "content": ""
        }
      ]
    },
    "operation": "complete"
  }
}
```

---

## Pipedrive

## Basic Information

- Node Type: `nodes-base.pipedrive`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Create and edit data in Pipedrive

### Available Operations

### Create
Create an activity
- Value: `create`

### Delete
Delete an activity
- Value: `delete`

### Get
Get data of an activity
- Value: `get`

### Get Many
Get data of many activities
- Value: `getAll`

### Update
Update an activity
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `associateWith` | options | Yes | `"organization"` | Type of entity to link to this deal |
| `associateWith` | options | Yes | `"organization"` | Type of entity to link to this lead |
| `subject` | string | Yes | `""` | The subject of the activity to create |
| `type` | string | Yes | `""` | Type of the activity like "call", "meeting", etc |
| `activityId` | number | Yes | `0` | ID of the activity to delete |
| `activityId` | number | Yes | `0` | ID of the activity to get |
| `activityId` | number | Yes | `0` | ID of the activity to update |
| `title` | string | Yes | `""` | The title of the deal to create |
| `org_id` | number | Yes | `0` | ID of the organization this deal will be associated with |
| `dealId` | number | Yes | `0` | ID of the deal to delete |

#### Property Details

##### Associate With (`associateWith`)

Type of entity to link to this deal

Optional values:
- `organization`: Organization
- `person`: Person

##### Associate With (`associateWith`)

Type of entity to link to this lead

Optional values:
- `organization`: Organization
- `person`: Person

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
  "name": "Pipedrive",
  "type": "nodes-base.pipedrive",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "associateWith": "organization",
    "subject": "",
    "type": "",
    "activityId": 0,
    "title": "",
    "org_id": 0,
    "dealId": 0
  }
}
```

#### Create Example
```json
{
  "name": "Pipedrive",
  "type": "nodes-base.pipedrive",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "associateWith": "organization",
    "subject": "",
    "type": "",
    "activityId": 0,
    "title": "",
    "org_id": 0,
    "dealId": 0,
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Pipedrive",
  "type": "nodes-base.pipedrive",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "associateWith": "organization",
    "subject": "",
    "type": "",
    "activityId": 0,
    "title": "",
    "org_id": 0,
    "dealId": 0,
    "operation": "delete"
  }
}
```

---

## Plivo

## Basic Information

- Node Type: `nodes-base.plivo`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Send SMS/MMS messages or make phone calls

### Available Operations

### Send
Send an SMS message
- Value: `send`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"sms"` | - |
| `answer_method` | options | Yes | `"POST"` | HTTP verb to be used when invoking the Answer URL |
| `from` | string | Yes | `""` | Plivo Number to send the SMS from |
| `to` | string | Yes | `""` | Phone number to send the message to |
| `message` | string | Yes | `""` | Message to send |
| `from` | string | Yes | `""` | Plivo Number to send the MMS from |
| `to` | string | Yes | `""` | Phone number to send the MMS to |
| `from` | string | Yes | `""` | Caller ID for the call to make |
| `to` | string | Yes | `""` | Phone number to make the call to |
| `answer_url` | string | Yes | `""` | URL to be invoked by Plivo once the call is answered. It should return the XML to handle the call once answered. |

#### Property Details

##### Resource (`resource`)

Optional values:
- `call`: Call
- `mms`: MMS
- `sms`: SMS

##### Answer Method (`answer_method`)

HTTP verb to be used when invoking the Answer URL

Optional values:
- `GET`: GET
- `POST`: POST

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
  "name": "Plivo",
  "type": "nodes-base.plivo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "sms",
    "answer_method": "POST",
    "from": "",
    "to": "",
    "message": "",
    "answer_url": ""
  }
}
```

#### Send Example
```json
{
  "name": "Plivo",
  "type": "nodes-base.plivo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "sms",
    "answer_method": "POST",
    "from": "",
    "to": "",
    "message": "",
    "answer_url": "",
    "operation": "send"
  }
}
```

---

## PostBin

## Basic Information

- Node Type: `nodes-base.postBin`
- Category: transform
- Package: n8n-nodes-base

### Description

Consume PostBin API

### Available Operations

### Create
Create bin
- Value: `create`

### Get
Get a bin
- Value: `get`

### Delete
Delete a bin
- Value: `delete`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"bin"` | - |
| `binId` | string | Yes | `""` | Unique identifier for each bin |
| `binId` | string | Yes | `""` | Unique identifier for each bin |
| `requestId` | string | Yes | `""` | Unique identifier for each request |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"get"` | - |
| `binContent` | string | No | `""` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `bin`: Bin
- `request`: Request

##### Operation (`operation`)

Optional values:
- `create`: Create - Create bin
- `get`: Get - Get a bin
- `delete`: Delete - Delete a bin

##### Operation (`operation`)

Optional values:
- `get`: Get - Get a request
- `removeFirst`: Remove First - Remove the first request from bin
- `send`: Send - Send a test request to the bin

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
  "name": "PostBin",
  "type": "nodes-base.postBin",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "bin",
    "binId": "",
    "requestId": ""
  }
}
```

#### Create Example
```json
{
  "name": "PostBin",
  "type": "nodes-base.postBin",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "bin",
    "binId": "",
    "requestId": "",
    "operation": "create"
  }
}
```

#### Get Example
```json
{
  "name": "PostBin",
  "type": "nodes-base.postBin",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "bin",
    "binId": "",
    "requestId": "",
    "operation": "get"
  }
}
```

---

## QuickBooks Online

## Basic Information

- Node Type: `nodes-base.quickbooks`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the QuickBooks Online API

### Available Operations

### Create
- Value: `create`

### Delete
- Value: `delete`

### Get
- Value: `get`

### Get Many
- Value: `getAll`

### Update
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `updateFields` | collection | Yes | `{}` | - |
| `updateFields` | collection | Yes | `{}` | - |
| `updateFields` | collection | Yes | `{}` | - |
| `updateFields` | collection | Yes | `{}` | - |
| `updateFields` | collection | Yes | `{}` | - |
| `updateFields` | collection | Yes | `{}` | - |
| `updateFields` | collection | Yes | `{}` | - |
| `VendorRef` | options | Yes | `[]` | The ID of the vendor who the bill is for. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `billId` | string | Yes | `""` | The ID of the bill to delete |
| `billId` | string | Yes | `""` | The ID of the bill to retrieve |

#### Property Details

##### Update Fields (`updateFields`)

Optional values:
- `undefined`: APAccountRef - Accounts Payable account to which the bill will be credited
- `undefined`: DueDate - Date when the payment of the transaction is due
- `undefined`: SalesTermRef - Sales term associated with the transaction
- `undefined`: TxnDate - Date when the transaction occurred

##### Update Fields (`updateFields`)

Optional values:
- `undefined`: Active - Whether the customer is currently enabled for use by QuickBooks
- `undefined`: Balance - Open balance amount or amount unpaid by the customer
- `undefined`: BalanceWithJobs - Cumulative open balance amount for the customer (or job) and all its sub-jobs
- `undefined`: BillAddr
- `undefined`: BillWithParent - Whether to bill this customer together with its parent
- `undefined`: CompanyName
- `undefined`: FamilyName
- `undefined`: FullyQualifiedName
- `undefined`: GivenName
- `undefined`: PreferredDeliveryMethod
- `undefined`: PrimaryEmailAddr
- `undefined`: PrimaryPhone
- `undefined`: PrintOnCheckName - Name of the customer as printed on a check
- `undefined`: Taxable - Whether transactions for this customer are taxable

##### Update Fields (`updateFields`)

Optional values:
- `undefined`: Active - Whether the employee is currently enabled for use by QuickBooks
- `undefined`: BillableTime
- `undefined`: DisplayName
- `undefined`: BillAddr
- `undefined`: PrimaryPhone
- `undefined`: PrintOnCheckName - Name of the employee as printed on a check
- `undefined`: SSN

##### Update Fields (`updateFields`)

Optional values:
- `undefined`: ApplyTaxAfterDiscount
- `undefined`: BillAddr
- `undefined`: BillEmail - E-mail address to which the estimate will be sent
- `undefined`: CustomFields
- `undefined`: CustomerMemo - User-entered message to the customer. This message is visible to end user on their transactions.
- `undefined`: DocNumber - Reference number for the transaction
- `undefined`: EmailStatus
- `undefined`: PrintStatus
- `undefined`: ShipAddr
- `undefined`: TxnDate - Date when the transaction occurred

##### Update Fields (`updateFields`)

Optional values:
- `undefined`: BillAddr
- `undefined`: BillEmail - E-mail address to which the invoice will be sent
- `undefined`: CustomerMemo - User-entered message to the customer. This message is visible to end user on their transactions.
- `undefined`: CustomFields
- `undefined`: DocNumber - Reference number for the transaction
- `undefined`: DueDate - Date when the payment of the transaction is due
- `undefined`: EmailStatus
- `undefined`: PrintStatus
- `undefined`: ShipAddr
- `undefined`: TxnDate - Date when the transaction occurred

##### Update Fields (`updateFields`)

Optional values:
- `undefined`: TxnDate - Date when the transaction occurred

##### Update Fields (`updateFields`)

Optional values:
- `undefined`: AcctNum
- `undefined`: Active - Whether the employee is currently enabled for use by QuickBooks
- `undefined`: Balance - The balance reflecting any payments made against the transaction
- `undefined`: BillAddr
- `undefined`: CompanyName
- `undefined`: FamilyName
- `undefined`: GivenName
- `undefined`: PrimaryEmailAddr
- `undefined`: PrimaryPhone
- `undefined`: PrintOnCheckName - Name of the vendor as printed on a check
- `undefined`: Vendor1099 - Whether the vendor is an independent contractor, given a 1099-MISC form at the end of the year

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
  "name": "QuickBooks Online",
  "type": "nodes-base.quickbooks",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "updateFields": {},
    "VendorRef": [],
    "billId": ""
  }
}
```

#### Create Example
```json
{
  "name": "QuickBooks Online",
  "type": "nodes-base.quickbooks",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "updateFields": {},
    "VendorRef": [],
    "billId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "QuickBooks Online",
  "type": "nodes-base.quickbooks",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "updateFields": {},
    "VendorRef": [],
    "billId": "",
    "operation": "delete"
  }
}
```

---

## RabbitMQ

## Basic Information

- Node Type: `nodes-base.rabbitmq`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Sends messages to a RabbitMQ topic

### Available Operations

### Send a Message to RabbitMQ
- Value: `sendMessage`

### Delete From Queue
- Value: `deleteMessage`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `operation` | hidden | No | `"sendMessage"` | - |
| `operation` | options | No | `"sendMessage"` | - |
| `mode` | options | No | `"queue"` | To where data should be moved |
| `exchangeType` | options | No | `"fanout"` | Type of exchange |
| `options` | collection | No | `{}` | - |
| `queue` | string | No | `""` | Name of the queue to publish to |
| `exchange` | string | No | `""` | Name of the exchange to publish to |
| `routingKey` | string | No | `""` | The routing key for the message |
| `sendInputData` | boolean | No | `true` | Whether to send the data the node receives as JSON |
| `message` | string | No | `""` | The message to be sent |

#### Property Details

##### Operation (`operation`)

Optional values:
- `sendMessage`: Send a Message to RabbitMQ
- `deleteMessage`: Delete From Queue

##### Operation (`operation`)

Optional values:
- `sendMessage`: Send a Message to RabbitMQ
- `deleteMessage`: Delete From Queue

##### Mode (`mode`)

To where data should be moved

Optional values:
- `queue`: Queue - Publish data to queue
- `exchange`: Exchange - Publish data to exchange

##### Type (`exchangeType`)

Type of exchange

Optional values:
- `direct`: Direct - Direct exchange type
- `topic`: Topic - Topic exchange type
- `headers`: Headers - Headers exchange type
- `fanout`: Fanout - Fanout exchange type

##### Options (`options`)

Optional values:
- `undefined`: alternateExchange - An exchange to send messages to if this exchange can’t route them to any queues
- `undefined`: arguments - Arguments to add, See \<a href="https://amqp-node.github.io/amqplib/channel\_api.html#channel\_publish" target="\_blank"\>here\</a\> for valid options
- `undefined`: autoDelete - Whether the queue will be deleted when the number of consumers drops to zero
- `undefined`: durable - Whether the queue will survive broker restarts
- `undefined`: exclusive - Whether to scope the queue to the connection
- `undefined`: headers - Headers to add

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
  "name": "RabbitMQ",
  "type": "nodes-base.rabbitmq",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Send a Message to RabbitMQ Example
```json
{
  "name": "RabbitMQ",
  "type": "nodes-base.rabbitmq",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "sendMessage"
  }
}
```

#### Delete From Queue Example
```json
{
  "name": "RabbitMQ",
  "type": "nodes-base.rabbitmq",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "deleteMessage"
  }
}
```

---

## Raindrop

## Basic Information

- Node Type: `nodes-base.raindrop`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Raindrop API

### Available Operations

### Create
- Value: `create`

### Delete
- Value: `delete`

### Get
- Value: `get`

### Get Many
- Value: `getAll`

### Update
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `type` | options | Yes | `"parent"` | - |
| `link` | string | Yes | `""` | Link of the bookmark to be created |
| `bookmarkId` | string | Yes | `""` | The ID of the bookmark to delete |
| `bookmarkId` | string | Yes | `""` | The ID of the bookmark to retrieve |
| `collectionId` | options | Yes | `[]` | The ID of the collection from which to retrieve all bookmarks. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `bookmarkId` | string | Yes | `""` | The ID of the bookmark to update |
| `title` | string | Yes | `""` | Title of the collection to create |
| `collectionId` | string | Yes | `""` | The ID of the collection to delete |
| `collectionId` | string | Yes | `""` | The ID of the collection to retrieve |
| `collectionId` | string | Yes | `""` | The ID of the collection to update |

#### Property Details

##### Type (`type`)

Optional values:
- `parent`: Parent - Root-level collections
- `children`: Children - Nested collections

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
  "name": "Raindrop",
  "type": "nodes-base.raindrop",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "type": "parent",
    "link": "",
    "bookmarkId": "",
    "collectionId": "",
    "title": ""
  }
}
```

#### Create Example
```json
{
  "name": "Raindrop",
  "type": "nodes-base.raindrop",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "type": "parent",
    "link": "",
    "bookmarkId": "",
    "collectionId": "",
    "title": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Raindrop",
  "type": "nodes-base.raindrop",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "type": "parent",
    "link": "",
    "bookmarkId": "",
    "collectionId": "",
    "title": "",
    "operation": "delete"
  }
}
```

---

## Reddit

## Basic Information

- Node Type: `nodes-base.reddit`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Reddit API

### Available Operations

### Create
Create a top-level comment in a post
- Value: `create`

### Get Many
Retrieve many comments in a post
- Value: `getAll`

### Delete
Remove a comment from a post
- Value: `delete`

### Reply
Write a reply to a comment in a post
- Value: `reply`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | URL of the post |
| `details` | options | Yes | `"identity"` | Details of my account to retrieve |
| `content` | options | Yes | `"about"` | Subreddit content to retrieve |
| `details` | options | Yes | `"about"` | Details of the user to retrieve |
| `postId` | string | Yes | `""` | ID of the post to write the comment to. Found in the post URL: <code>/r/[subreddit\_name]/comments/[post\_id]/[post\_title]</code> |
| `commentText` | string | Yes | `""` | Text of the comment. Markdown supported. |
| `subreddit` | string | Yes | `""` | The name of subreddit where the post is |
| `postId` | string | Yes | `""` | ID of the post to get all comments from. Found in the post URL: <code>/r/[subreddit\_name]/comments/[post\_id]/[post\_title]</code> |
| `commentId` | string | Yes | `""` | ID of the comment to remove. Found in the comment URL:<code>/r/[subreddit\_name]/comments/[post\_id]/[post\_title]/[comment\_id]</code> |
| `commentId` | string | Yes | `""` | ID of the comment to reply to. To be found in the comment URL: <code>www.reddit.com/r/[subreddit\_name]/comments/[post\_id]/[post\_title]/[comment\_id]</code> |

#### Property Details

##### Details (`details`)

Details of my account to retrieve

Optional values:
- `blockedUsers`: Blocked Users - Return the blocked users of the logged-in user
- `friends`: Friends - Return the friends of the logged-in user
- `identity`: Identity - Return the identity of the logged-in user
- `karma`: Karma - Return the subreddit karma for the logged-in user
- `prefs`: Preferences - Return the settings preferences of the logged-in user
- `saved`: Saved - Return the saved posts for the user
- `trophies`: Trophies - Return the trophies of the logged-in user

##### Content (`content`)

Subreddit content to retrieve

Optional values:
- `about`: About
- `rules`: Rules

##### Details (`details`)

Details of the user to retrieve

Optional values:
- `about`: About
- `comments`: Comments
- `gilded`: Gilded
- `overview`: Overview
- `submitted`: Submitted

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
  "name": "Reddit",
  "type": "nodes-base.reddit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "details": "about",
    "content": "about",
    "postId": "",
    "commentText": "",
    "subreddit": "",
    "commentId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Reddit",
  "type": "nodes-base.reddit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "details": "about",
    "content": "about",
    "postId": "",
    "commentText": "",
    "subreddit": "",
    "commentId": "",
    "operation": "create"
  }
}
```

#### Get Many Example
```json
{
  "name": "Reddit",
  "type": "nodes-base.reddit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "details": "about",
    "content": "about",
    "postId": "",
    "commentText": "",
    "subreddit": "",
    "commentId": "",
    "operation": "getAll"
  }
}
```

---

## Rename Keys

## Basic Information

- Node Type: `nodes-base.renameKeys`
- Category: transform
- Package: n8n-nodes-base

### Description

Update item field names

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `keys` | fixedCollection | No | `{}` | Adds a key which should be renamed |
| `additionalOptions` | collection | No | `{}` | - |

#### Property Details

##### Keys (`keys`)

Adds a key which should be renamed

Optional values:
- `undefined`: key

##### Additional Options (`additionalOptions`)

Optional values:
- `undefined`: regexReplacement - Adds a regular expression

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
  "name": "Rename Keys",
  "type": "nodes-base.renameKeys",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Respond to Webhook

## Basic Information

- Node Type: `nodes-base.respondToWebhook`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Returns data for Webhook

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `redirectURL` | string | Yes | `""` | The URL to redirect to |
| `inputFieldName` | string | Yes | `"data"` | The name of the node input field with the binary data |
| `credentials` | credentials | No | `""` | - |
| `respondWith` | options | No | `"firstIncomingItem"` | The data that should be returned |
| `respondWith` | options | No | `"firstIncomingItem"` | The data that should be returned |
| `responseDataSource` | options | No | `"automatically"` | - |
| `options` | collection | No | `{}` | - |
| `enableResponseOutput` | boolean | No | `false` | Whether to provide an additional output branch with the response sent to the webhook |
| `responseBody` | json | No | `"{\n  \"myField\": \"value\"\n}"` | The HTTP response JSON data |
| `payload` | json | No | `"{\n  \"myField\": \"value\"\n}"` | The payload to include in the JWT token |

#### Property Details

##### Respond With (`respondWith`)

The data that should be returned

Optional values:
- `allIncomingItems`: All Incoming Items - Respond with all input JSON items
- `binary`: Binary File - Respond with incoming file binary data
- `firstIncomingItem`: First Incoming Item - Respond with the first input JSON item
- `json`: JSON - Respond with a custom JSON body
- `jwt`: JWT Token - Respond with a JWT token
- `noData`: No Data - Respond with an empty body
- `redirect`: Redirect - Respond with a redirect to a given URL
- `text`: Text - Respond with a simple text message body

##### Respond With (`respondWith`)

The data that should be returned

Optional values:
- `allIncomingItems`: All Incoming Items - Respond with all input JSON items
- `binary`: Binary File - Respond with incoming file binary data
- `firstIncomingItem`: First Incoming Item - Respond with the first input JSON item
- `json`: JSON - Respond with a custom JSON body
- `jwt`: JWT Token - Respond with a JWT token
- `noData`: No Data - Respond with an empty body
- `redirect`: Redirect - Respond with a redirect to a given URL
- `text`: Text - Respond with a simple text message body

##### Response Data Source (`responseDataSource`)

Optional values:
- `automatically`: Choose Automatically From Input - Use if input data will contain a single piece of binary data
- `set`: Specify Myself - Enter the name of the input field the binary data will be in

##### Options (`options`)

Optional values:
- `undefined`: responseCode - The HTTP response code to return. Defaults to 200.
- `undefined`: responseHeaders - Add headers to the webhook response
- `undefined`: responseKey - The name of the response field to put all items in
- `undefined`: enableStreaming - Whether to enable streaming to the response

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

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
  "name": "Respond to Webhook",
  "type": "nodes-base.respondToWebhook",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "redirectURL": "",
    "inputFieldName": "data"
  }
}
```

---

## Rundeck

## Basic Information

- Node Type: `nodes-base.rundeck`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Manage Rundeck API

### Available Operations

### Execute
Execute a job
- Value: `execute`

### Get Metadata
Get metadata of a job
- Value: `getMetadata`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `jobid` | string | Yes | `""` | The job ID to execute |
| `jobid` | string | Yes | `""` | The job ID to get metadata off |
| `resource` | options | No | `"job"` | - |
| `operation` | options | No | `"execute"` | - |
| `arguments` | fixedCollection | No | `{}` | - |
| `filter` | string | No | `""` | Filter Rundeck nodes by name |

#### Property Details

##### Resource (`resource`)

Optional values:
- `job`: Job

##### Operation (`operation`)

Optional values:
- `execute`: Execute - Execute a job
- `getMetadata`: Get Metadata - Get metadata of a job

##### Arguments (`arguments`)

Optional values:
- `undefined`: arguments

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
  "name": "Rundeck",
  "type": "nodes-base.rundeck",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "jobid": ""
  }
}
```

#### Execute Example
```json
{
  "name": "Rundeck",
  "type": "nodes-base.rundeck",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "jobid": "",
    "operation": "execute"
  }
}
```

#### Get Metadata Example
```json
{
  "name": "Rundeck",
  "type": "nodes-base.rundeck",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "jobid": "",
    "operation": "getMetadata"
  }
}
```

---

## SecurityScorecard

## Basic Information

- Node Type: `nodes-base.securityScorecard`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume SecurityScorecard API

### Available Operations

### Get Factor Scores
Get company factor scores and issue counts
- Value: `getFactor`

### Get Historical Factor Scores
Get company's historical factor scores
- Value: `getFactorHistorical`

### Get Historical Scores
Get company's historical scores
- Value: `getHistoricalScore`

### Get Information and Scorecard
Get company information and summary of their scorecard
- Value: `getScorecard`

### Get Score Plan
Get company's score improvement plan
- Value: `getScorePlan`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"company"` | - |
| `operation` | options | Yes | `"getFactor"` | - |
| `operation` | options | Yes | `"getFactor"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"add"` | - |
| `operation` | options | Yes | `"getAll"` | - |
| `url` | string | Yes | `""` | URL to a generated report |
| `industry` | options | Yes | `"food"` | - |
| `report` | options | Yes | `"detailed"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `company`: Company
- `industry`: Industry
- `invite`: Invite
- `portfolio`: Portfolio
- `portfolioCompany`: Portfolio Company
- `report`: Report

##### Operation (`operation`)

Optional values:
- `getFactor`: Get Factor Scores - Get company factor scores and issue counts
- `getFactorHistorical`: Get Historical Factor Scores - Get company's historical factor scores
- `getHistoricalScore`: Get Historical Scores - Get company's historical scores
- `getScorecard`: Get Information and Scorecard - Get company information and summary of their scorecard
- `getScorePlan`: Get Score Plan - Get company's score improvement plan

##### Operation (`operation`)

Optional values:
- `getFactor`: Get Factor Scores
- `getFactorHistorical`: Get Historical Factor Scores
- `getScore`: Get Score

##### Operation (`operation`)

Optional values:
- `create`: Create - Create an invite for a company/user

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a portfolio
- `delete`: Delete - Delete a portfolio
- `getAll`: Get Many - Get many portfolios
- `update`: Update - Update a portfolio

##### Operation (`operation`)

Optional values:
- `add`: Add - Add a company to portfolio
- `getAll`: Get Many - Get many companies in a portfolio
- `remove`: Remove - Remove a company from portfolio

##### Operation (`operation`)

Optional values:
- `download`: Download - Download a generated report
- `generate`: Generate - Generate a report
- `getAll`: Get Many - Get list of recently generated report

##### Industry (`industry`)

Optional values:
- `food`: Food
- `healthcare`: Healthcare
- `manofacturing`: Manofacturing
- `retail`: Retail
- `technology`: Technology

##### Report (`report`)

Optional values:
- `detailed`: Company Detailed
- `events-json`: Company Events
- `issues`: Company Issues
- `partnership`: Company Partnership
- `summary`: Company Summary
- `full-scorecard-json`: Full Scorecard
- `portfolio`: Portfolio
- `scorecard-footprint`: Scorecard Footprint

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
  "name": "SecurityScorecard",
  "type": "nodes-base.securityScorecard",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "company",
    "operation": "getAll",
    "url": "",
    "industry": "food",
    "report": "detailed"
  }
}
```

#### Get Factor Scores Example
```json
{
  "name": "SecurityScorecard",
  "type": "nodes-base.securityScorecard",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "company",
    "operation": "getFactor",
    "url": "",
    "industry": "food",
    "report": "detailed"
  }
}
```

#### Get Historical Factor Scores Example
```json
{
  "name": "SecurityScorecard",
  "type": "nodes-base.securityScorecard",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "company",
    "operation": "getFactorHistorical",
    "url": "",
    "industry": "food",
    "report": "detailed"
  }
}
```

---

## SendGrid

## Basic Information

- Node Type: `nodes-base.sendGrid`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume SendGrid API

### Available Operations

### Create
Create a list
- Value: `create`

### Delete
Delete a list
- Value: `delete`

### Get
Get a list
- Value: `get`

### Get Many
Get many lists
- Value: `getAll`

### Update
Update a list
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"list"` | - |
| `by` | options | Yes | `"id"` | Search the user by ID or email |
| `name` | string | Yes | `""` | Name of the list |
| `listId` | string | Yes | `""` | ID of the list |
| `listId` | string | Yes | `""` | ID of the list |
| `listId` | string | Yes | `""` | ID of the list |
| `name` | string | Yes | `""` | Name of the list |
| `email` | string | Yes | `""` | Primary email for the contact |
| `contactId` | string | Yes | `""` | ID of the contact |
| `email` | string | Yes | `""` | Email of the contact |

#### Property Details

##### Resource (`resource`)

Optional values:
- `contact`: Contact
- `list`: List
- `mail`: Mail

##### By (`by`)

Search the user by ID or email

Optional values:
- `id`: ID
- `email`: Email

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
  "name": "SendGrid",
  "type": "nodes-base.sendGrid",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "list",
    "by": "id",
    "name": "",
    "listId": "",
    "email": "",
    "contactId": ""
  }
}
```

#### Create Example
```json
{
  "name": "SendGrid",
  "type": "nodes-base.sendGrid",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "list",
    "by": "id",
    "name": "",
    "listId": "",
    "email": "",
    "contactId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "SendGrid",
  "type": "nodes-base.sendGrid",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "list",
    "by": "id",
    "name": "",
    "listId": "",
    "email": "",
    "contactId": "",
    "operation": "delete"
  }
}
```

---

## seven

## Basic Information

- Node Type: `nodes-base.sms77`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Send SMS and make text-to-speech calls

### Available Operations

### Send
Send SMS
- Value: `send`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `to` | string | Yes | `""` | The number of your recipient(s) separated by comma. Can be regular numbers or contact/groups from seven. |
| `message` | string | Yes | `""` | The message to send. Max. 1520 characters |
| `resource` | options | No | `"sms"` | - |
| `operation` | options | No | `"send"` | - |
| `operation` | options | No | `"send"` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `from` | string | No | `""` | The caller ID displayed in the receivers display. Max 16 numeric or 11 alphanumeric characters. |

#### Property Details

##### Resource (`resource`)

Optional values:
- `sms`: SMS
- `voice`: Voice Call

##### Operation (`operation`)

Optional values:
- `send`: Send - Send SMS

##### Operation (`operation`)

Optional values:
- `send`: Send - Converts text to voice and calls a given number

##### Options (`options`)

Optional values:
- `undefined`: delay - Pick a date for time delayed dispatch
- `undefined`: foreign_id - Custom foreign ID returned in DLR callbacks
- `undefined`: flash - Send as flash message being displayed directly the receiver's display
- `undefined`: label - Custom label used to group analytics
- `undefined`: performance_tracking - Whether to enable performance tracking for URLs found in the message text
- `undefined`: ttl - Custom time to live specifying the validity period of a message in minutes

##### Options (`options`)

Optional values:
- `undefined`: from - The caller ID. Please use only verified sender IDs, one of your virtual inbound numbers or one of our shared virtual numbers.

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
  "name": "seven",
  "type": "nodes-base.sms77",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "to": "",
    "message": ""
  }
}
```

#### Send Example
```json
{
  "name": "seven",
  "type": "nodes-base.sms77",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "to": "",
    "message": "",
    "operation": "send"
  }
}
```

---

## SIGNL4

## Basic Information

- Node Type: `nodes-base.signl4`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume SIGNL4 API

### Available Operations

### Send
Send an alert
- Value: `send`

### Resolve
Resolve an alert
- Value: `resolve`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | No | `"alert"` | - |
| `operation` | options | No | `"send"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `message` | string | No | `""` | A more detailed description for the alert |
| `externalId` | string | No | `""` | If the event originates from a record in a 3rd party system, use this parameter to pass the unique ID of that record. That ID will be communicated in outbound webhook notifications from SIGNL4, which is great for correlation/synchronization of that record with the alert. If you resolve / close an alert you must use the same External ID as in the original alert. |

#### Property Details

##### Resource (`resource`)

Optional values:
- `alert`: Alert

##### Operation (`operation`)

Optional values:
- `send`: Send - Send an alert
- `resolve`: Resolve - Resolve an alert

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: alertingScenario
- `undefined`: attachmentsUi
- `undefined`: externalId - If the event originates from a record in a 3rd party system, use this parameter to pass the unique ID of that record. That ID will be communicated in outbound webhook notifications from SIGNL4, which is great for correlation/synchronization of that record with the alert. If you resolve / close an alert you must use the same External ID as in the original alert.
- `undefined`: filtering - Whether to apply event filtering for this event, or not. If set to true, the event will only trigger a notification to the team, if it contains at least one keyword from one of your services and system categories (i.e. it is whitelisted)
- `undefined`: locationFieldsUi - Transmit location information ('latitude, longitude') with your event and display a map in the mobile app
- `undefined`: service - Assigns the alert to the service/system category with the specified name
- `undefined`: title - The title or subject of this alert

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
  "name": "SIGNL4",
  "type": "nodes-base.signl4",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Send Example
```json
{
  "name": "SIGNL4",
  "type": "nodes-base.signl4",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "send"
  }
}
```

#### Resolve Example
```json
{
  "name": "SIGNL4",
  "type": "nodes-base.signl4",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "resolve"
  }
}
```

---

## Splunk

## Basic Information

- Node Type: `nodes-base.splunk`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Splunk Enterprise API

### Available Operations

### Get Fired Alerts
Retrieve a fired alerts report
- Value: `getReport`

### Get Metrics
Retrieve metrics
- Value: `getMetrics`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `search` | string | Yes | `""` | Search language string to execute, in Splunk's <a href="https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/WhatsInThisManual">Search Processing Language</a> |
| `name` | string | Yes | `""` | Login name of the user |
| `roles` | multiOptions | Yes | `["user"]` | Comma-separated list of roles to assign to the user. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `searchJobId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `reportId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `reportId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `searchJobId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `searchJobId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `searchJobId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `password` | string | Yes | `""` | - |

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
  "name": "Splunk",
  "type": "nodes-base.splunk",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "search": "",
    "name": "",
    "roles": [
      "user"
    ],
    "searchJobId": {
      "mode": "list",
      "value": ""
    },
    "reportId": {
      "mode": "list",
      "value": ""
    },
    "password": ""
  }
}
```

#### Get Fired Alerts Example
```json
{
  "name": "Splunk",
  "type": "nodes-base.splunk",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "search": "",
    "name": "",
    "roles": [
      "user"
    ],
    "searchJobId": {
      "mode": "list",
      "value": ""
    },
    "reportId": {
      "mode": "list",
      "value": ""
    },
    "password": "",
    "operation": "getReport"
  }
}
```

#### Get Metrics Example
```json
{
  "name": "Splunk",
  "type": "nodes-base.splunk",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "search": "",
    "name": "",
    "roles": [
      "user"
    ],
    "searchJobId": {
      "mode": "list",
      "value": ""
    },
    "reportId": {
      "mode": "list",
      "value": ""
    },
    "password": "",
    "operation": "getMetrics"
  }
}
```

---

## Spreadsheet File

## Basic Information

- Node Type: `nodes-base.spreadsheetFile`
- Category: transform
- Package: n8n-nodes-base

### Description

Reads and writes data from a spreadsheet file like CSV, XLS, ODS, etc

### Available Operations

### Read From File
Reads data from a spreadsheet file
- Value: `fromFile`

### Write to File
Writes the workflow data to a spreadsheet file
- Value: `toFile`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `operation` | options | No | `"fromFile"` | - |
| `fileFormat` | options | No | `"autodetect"` | The format of the binary data to read from |
| `fileFormat` | options | No | `"xls"` | The format of the file to save the data as |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `fromFile`: Read From File - Reads data from a spreadsheet file
- `toFile`: Write to File - Writes the workflow data to a spreadsheet file

##### File Format (`fileFormat`)

The format of the binary data to read from

Optional values:
- `autodetect`: Autodetect
- `csv`: CSV - Comma-separated values
- `html`: HTML - HTML Table
- `ods`: ODS - OpenDocument Spreadsheet
- `rtf`: RTF - Rich Text Format
- `xls`: XLS - Excel
- `xlsx`: XLSX - Excel

##### File Format (`fileFormat`)

The format of the file to save the data as

Optional values:
- `csv`: CSV - Comma-separated values
- `html`: HTML - HTML Table
- `ods`: ODS - OpenDocument Spreadsheet
- `rtf`: RTF - Rich Text Format
- `xls`: XLS - Excel
- `xlsx`: XLSX - Excel

##### Options (`options`)

Optional values:
- `undefined`: delimiter - Set the field delimiter, usually a comma
- `undefined`: encoding
- `undefined`: enableBOM - Whether to detect and exclude the byte-order-mark from the CSV Input if present
- `undefined`: relaxQuotes - Whether to handle unclosed quotes in CSV fields as part of the field's content instead of throwing a parsing error
- `undefined`: headerRow - Whether the first row of the file contains the header names
- `undefined`: includeEmptyCells - Whether to include empty cells when reading from file. They will be filled with an empty string.
- `undefined`: maxRowCount - Stop handling records after the requested number of rows are read. Use -1 if you want to load all rows.
- `undefined`: range - The range to read from the table. If set to a number it will be the starting row. If set to string it will be used as A1-style notation range.
- `undefined`: rawData - Whether to return RAW data, instead of parsing it
- `undefined`: readAsString - In some cases and file formats, it is necessary to read as string to ensure special characters are interpreted correctly
- `undefined`: sheetName - Name of the sheet to read from in the spreadsheet (if supported). If not set, the first one will be chosen.
- `undefined`: fromLine - Start handling records from the requested line number. Starts at 0.
- `undefined`: skipRecordsWithErrors

##### Options (`options`)

Optional values:
- `undefined`: compression - Whether compression will be applied or not
- `undefined`: fileName - File name to set in binary data. By default will "spreadsheet.&lt;fileFormat&gt;" be used.
- `undefined`: headerRow - Whether the first row of the file contains the header names
- `undefined`: sheetName - Name of the sheet to create in the spreadsheet

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
  "name": "Spreadsheet File",
  "type": "nodes-base.spreadsheetFile",
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

#### Read From File Example
```json
{
  "name": "Spreadsheet File",
  "type": "nodes-base.spreadsheetFile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryPropertyName": "data",
    "operation": "fromFile"
  }
}
```

#### Write to File Example
```json
{
  "name": "Spreadsheet File",
  "type": "nodes-base.spreadsheetFile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryPropertyName": "data",
    "operation": "toFile"
  }
}
```

---

## Stackby

## Basic Information

- Node Type: `nodes-base.stackby`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Read, write, and delete data in Stackby

### Available Operations

### Append
- Value: `append`

### Delete
- Value: `delete`

### List
- Value: `list`

### Read
- Value: `read`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `stackId` | string | Yes | `""` | The ID of the stack to access |
| `table` | string | Yes | `""` | Enter Table Name |
| `id` | string | Yes | `""` | ID of the record to return |
| `columns` | string | Yes | `""` | Comma-separated list of the properties which should used as columns for the new rows |
| `operation` | options | No | `"append"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `returnAll` | boolean | No | `true` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `1000` | Max number of results to return |

#### Property Details

##### Operation (`operation`)

Optional values:
- `append`: Append
- `delete`: Delete
- `list`: List
- `read`: Read

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: view - The name or ID of a view in the Stories table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view.

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
  "name": "Stackby",
  "type": "nodes-base.stackby",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "stackId": "",
    "table": "",
    "id": "",
    "columns": ""
  }
}
```

#### Append Example
```json
{
  "name": "Stackby",
  "type": "nodes-base.stackby",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "stackId": "",
    "table": "",
    "id": "",
    "columns": "",
    "operation": "append"
  }
}
```

#### Delete Example
```json
{
  "name": "Stackby",
  "type": "nodes-base.stackby",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "stackId": "",
    "table": "",
    "id": "",
    "columns": "",
    "operation": "delete"
  }
}
```

---

## Stripe

## Basic Information

- Node Type: `nodes-base.stripe`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Stripe API

### Available Operations

### Get
Get a balance
- Value: `get`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `value` | number | Yes | `1` | The value of the meter event. Must be an integer. Can be positive or negative. |
| `duration` | options | Yes | `"once"` | How long the discount will be in effect |
| `type` | options | Yes | `"percent"` | Whether the coupon discount is a percentage or a fixed amount |
| `type` | options | Yes | `"wechat"` | Type of source (payment instrument) to create |
| `type` | options | Yes | `"cardToken"` | Type of token to create |
| `customerId` | string | Yes | `""` | ID of the customer to be associated with this card |
| `token` | string | Yes | `""` | Token representing sensitive card information |
| `customerId` | string | Yes | `""` | ID of the customer whose card to remove |
| `cardId` | string | Yes | `""` | ID of the card to remove |
| `customerId` | string | Yes | `""` | ID of the customer whose card to retrieve |

#### Property Details

##### Apply (`duration`)

How long the discount will be in effect

Optional values:
- `forever`: Forever
- `once`: Once

##### Discount Type (`type`)

Whether the coupon discount is a percentage or a fixed amount

Optional values:
- `fixedAmount`: Fixed Amount (in Cents)
- `percent`: Percent

##### Type (`type`)

Type of source (payment instrument) to create

Optional values:
- `wechat`: WeChat

##### Type (`type`)

Type of token to create

Optional values:
- `cardToken`: Card Token

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
  "name": "Stripe",
  "type": "nodes-base.stripe",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": 1,
    "duration": "once",
    "type": "cardToken",
    "customerId": "",
    "token": "",
    "cardId": ""
  }
}
```

#### Get Example
```json
{
  "name": "Stripe",
  "type": "nodes-base.stripe",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": 1,
    "duration": "once",
    "type": "cardToken",
    "customerId": "",
    "token": "",
    "cardId": "",
    "operation": "get"
  }
}
```

---

## Switch

## Basic Information

- Node Type: `nodes-base.switch`
- Category: transform
- Package: n8n-nodes-base

### Description

Route items depending on defined expression or rules

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `mode` | options | No | `"rules"` | How data should be routed |
| `rules` | fixedCollection | No | `{"values":[{"conditions":{"options":{"caseSensitive":true,"leftValue":"","typeValidation":"strict"},"conditions":[{"leftValue":"","rightValue":"","operator":{"type":"string","operation":"equals"}}],"combinator":"and"}}]}` | - |
| `options` | collection | No | `{}` | - |
| `numberOutputs` | number | No | `4` | How many outputs to create |
| `numberOutputs` | number | No | `4` | How many outputs to create |
| `output` | number | No | `"={{}}"` | The output index to send the input item to. Use an expression to calculate which input item should be routed to which output. The expression must return a number. |
| `looseTypeValidation` | boolean | No | `false` | If the type of an expression doesn't match the type of the comparison, n8n will try to cast the expression to the required type. E.g. for booleans <code>"false"</code> or <code>0</code> will be cast to <code>false</code> |

#### Property Details

##### Mode (`mode`)

How data should be routed

Optional values:
- `rules`: Rules - Build a matching rule for each output
- `expression`: Expression - Write an expression to return the output index

##### Routing Rules (`rules`)

Optional values:
- `undefined`: values

##### Options (`options`)

Optional values:
- `undefined`: fallbackOutput - If no rule matches the item will be sent to this output, by default they will be ignored
- `undefined`: ignoreCase - Whether to ignore letter case when evaluating conditions
- `undefined`: looseTypeValidation - If the type of an expression doesn't match the type of the comparison, n8n will try to cast the expression to the required type. E.g. for booleans \<code\>"false"\</code\> or \<code\>0\</code\> will be cast to \<code\>false\</code\>
- `undefined`: renameFallbackOutput
- `undefined`: allMatchingOutputs - Whether to send data to all outputs meeting conditions (and not just the first one)

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 4 (configurable)

Output Details:
1. `0` - Output path 0
2. `1` - Output path 1
3. `2` - Output path 2
4. `3` - Output path 3

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
  "name": "Switch",
  "type": "nodes-base.switch",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Taiga

## Basic Information

- Node Type: `nodes-base.taiga`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Taiga API

### Available Operations

### Create
Create an epic
- Value: `create`

### Delete
Delete an epic
- Value: `delete`

### Get
Get an epic
- Value: `get`

### Get Many
Get many epics
- Value: `getAll`

### Update
Update an epic
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `projectId` | options | Yes | `""` | ID of the project to which the epic belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `epicId` | string | Yes | `""` | ID of the epic to delete |
| `epicId` | string | Yes | `""` | ID of the epic to retrieve |
| `projectId` | options | Yes | `""` | ID of the project to which the epic belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `epicId` | string | Yes | `""` | ID of the epic to update |
| `projectId` | options | Yes | `""` | ID of the project to which the issue belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `issueId` | string | Yes | `""` | ID of the issue to delete |
| `issueId` | string | Yes | `""` | ID of the issue to retrieve |
| `projectId` | options | Yes | `""` | ID of the project to which the issue belongs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `issueId` | string | Yes | `""` | ID of the issue to update |

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
  "name": "Taiga",
  "type": "nodes-base.taiga",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "projectId": "",
    "epicId": "",
    "issueId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Taiga",
  "type": "nodes-base.taiga",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "projectId": "",
    "epicId": "",
    "issueId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Taiga",
  "type": "nodes-base.taiga",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "projectId": "",
    "epicId": "",
    "issueId": "",
    "operation": "delete"
  }
}
```

---

## Tapfiliate

## Basic Information

- Node Type: `nodes-base.tapfiliate`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Tapfiliate API

### Available Operations

### Create
Create an affiliate
- Value: `create`

### Delete
Delete an affiliate
- Value: `delete`

### Get
Get an affiliate by ID
- Value: `get`

### Get Many
Get many affiliates
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"affiliate"` | - |
| `email` | string | Yes | `""` | The affiliate’s email |
| `firstname` | string | Yes | `""` | The affiliate’s firstname |
| `lastname` | string | Yes | `""` | The affiliate’s lastname |
| `affiliateId` | string | Yes | `""` | The ID of the affiliate |
| `affiliateId` | string | Yes | `""` | The ID of the affiliate |
| `affiliateId` | string | Yes | `""` | The ID of the affiliate |
| `affiliateId` | string | Yes | `""` | The ID of the affiliate |
| `affiliateId` | string | Yes | `""` | The ID of the affiliate |
| `programId` | options | Yes | `""` | The ID of the Program to add the affiliate to. This ID can be found as part of the URL when viewing the program on the platform. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

#### Property Details

##### Resource (`resource`)

Optional values:
- `affiliate`: Affiliate
- `affiliateMetadata`: Affiliate Metadata
- `programAffiliate`: Program Affiliate

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
  "name": "Tapfiliate",
  "type": "nodes-base.tapfiliate",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "affiliate",
    "email": "",
    "firstname": "",
    "lastname": "",
    "affiliateId": "",
    "programId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Tapfiliate",
  "type": "nodes-base.tapfiliate",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "affiliate",
    "email": "",
    "firstname": "",
    "lastname": "",
    "affiliateId": "",
    "programId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Tapfiliate",
  "type": "nodes-base.tapfiliate",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "affiliate",
    "email": "",
    "firstname": "",
    "lastname": "",
    "affiliateId": "",
    "programId": "",
    "operation": "delete"
  }
}
```

---

## TheHive

## Basic Information

- Node Type: `nodes-base.theHive`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume TheHive API

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"alert"` | - |
| `operation` | options | Yes | `"getAll"` | - |
| `operation` | options | Yes | `"create"` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `operation` | options | Yes | `"getAll"` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `operation` | options | Yes | `"getAll"` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `operation` | options | Yes | `"getAll"` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `severity` | options | Yes | `2` | Severity of the alert. Default=Medium. |
| `tlp` | options | Yes | `2` | Traffict Light Protocol (TLP). Default=Amber. |
| `status` | options | Yes | `"New"` | Status of the alert |
| `tlp` | options | Yes | `2` | Traffict Light Protocol (TLP). Default=Amber. |

#### Property Details

##### Resource (`resource`)

Optional values:
- `alert`: Alert
- `case`: Case
- `log`: Log
- `observable`: Observable
- `task`: Task

##### Operation (`operation`)

Optional values:
- `create`: Create - Create task log
- `executeResponder`: Execute Responder - Execute a responder on a selected log
- `getAll`: Get Many - Get many task logs
- `get`: Get - Get a single log

##### Severity (`severity`)

Severity of the alert. Default=Medium.

Optional values:
- `1`: Low
- `2`: Medium
- `3`: High

##### TLP (`tlp`)

Traffict Light Protocol (TLP). Default=Amber.

Optional values:
- `0`: White
- `1`: Green
- `2`: Amber
- `3`: Red

##### Status (`status`)

Status of the alert

Optional values:
- `New`: New
- `Updated`: Updated
- `Ignored`: Ignored
- `Imported`: Imported

##### TLP (`tlp`)

Traffict Light Protocol (TLP). Default=Amber.

Optional values:
- `0`: White
- `1`: Green
- `2`: Amber
- `3`: Red

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
  "name": "TheHive",
  "type": "nodes-base.theHive",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "alert",
    "operation": "getAll",
    "severity": 2,
    "tlp": 2,
    "status": "New"
  }
}
```

---

## TheHive 5

## Basic Information

- Node Type: `nodes-base.theHiveProject`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume TheHive 5 API

### Available Operations

### Create
- Value: `create`

### Delete
- Value: `deleteAlert`

### Execute Responder
- Value: `executeResponder`

### Get
- Value: `get`

### Merge Into Case
- Value: `merge`

### Promote to Case
- Value: `promote`

### Search
- Value: `search`

### Update
- Value: `update`

### Update Status
- Value: `status`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"alert"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"add"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"create"` | - |
| `operation` | options | Yes | `"executeQuery"` | - |
| `operation` | options | Yes | `"create"` | - |
| `attachmentsUi` | fixedCollection | Yes | `{}` | Array of supported attachments to add to the message |

#### Property Details

##### Resource (`resource`)

Optional values:
- `alert`: Alert
- `case`: Case
- `comment`: Comment
- `observable`: Observable
- `page`: Page
- `query`: Query
- `task`: Task
- `log`: Task Log

##### Operation (`operation`)

Optional values:
- `create`: Create
- `deleteAlert`: Delete
- `executeResponder`: Execute Responder
- `get`: Get
- `merge`: Merge Into Case
- `promote`: Promote to Case
- `search`: Search
- `update`: Update
- `status`: Update Status

##### Operation (`operation`)

Optional values:
- `addAttachment`: Add Attachment
- `create`: Create
- `deleteAttachment`: Delete Attachment
- `deleteCase`: Delete Case
- `executeResponder`: Execute Responder
- `get`: Get
- `getAttachment`: Get Attachment
- `getTimeline`: Get Timeline
- `search`: Search
- `update`: Update

##### Operation (`operation`)

Optional values:
- `add`: Create
- `deleteComment`: Delete
- `search`: Search
- `update`: Update

##### Operation (`operation`)

Optional values:
- `addAttachment`: Add Attachment
- `create`: Create
- `deleteLog`: Delete
- `deleteAttachment`: Delete Attachment
- `executeResponder`: Execute Responder
- `get`: Get
- `search`: Search

##### Operation (`operation`)

Optional values:
- `create`: Create
- `deleteObservable`: Delete
- `executeAnalyzer`: Execute Analyzer
- `executeResponder`: Execute Responder
- `get`: Get
- `search`: Search
- `update`: Update

##### Operation (`operation`)

Optional values:
- `create`: Create
- `deletePage`: Delete
- `search`: Search
- `update`: Update

##### Operation (`operation`)

Optional values:
- `executeQuery`: Execute Query

##### Operation (`operation`)

Optional values:
- `create`: Create
- `deleteTask`: Delete
- `executeResponder`: Execute Responder
- `get`: Get
- `search`: Search
- `update`: Update

##### Attachments (`attachmentsUi`)

Array of supported attachments to add to the message

Optional values:
- `undefined`: values

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
  "name": "TheHive 5",
  "type": "nodes-base.theHiveProject",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "alert",
    "operation": "create",
    "attachmentsUi": {}
  }
}
```

#### Create Example
```json
{
  "name": "TheHive 5",
  "type": "nodes-base.theHiveProject",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "alert",
    "operation": "create",
    "attachmentsUi": {}
  }
}
```

#### Delete Example
```json
{
  "name": "TheHive 5",
  "type": "nodes-base.theHiveProject",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "alert",
    "operation": "deleteAlert",
    "attachmentsUi": {}
  }
}
```

---

## TOTP

## Basic Information

- Node Type: `nodes-base.totp`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Generate a time-based one-time password

### Available Operations

### Generate Secret
- Value: `generateSecret`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `operation` | options | No | `"generateSecret"` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `generateSecret`: Generate Secret

##### Options (`options`)

Optional values:
- `undefined`: algorithm - HMAC hashing algorithm. Defaults to SHA1.
- `undefined`: digits - Number of digits in the generated TOTP code. Defaults to 6 digits.
- `undefined`: period - How many seconds the generated TOTP code is valid for. Defaults to 30 seconds.

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
  "name": "TOTP",
  "type": "nodes-base.totp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Generate Secret Example
```json
{
  "name": "TOTP",
  "type": "nodes-base.totp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "generateSecret"
  }
}
```

---

## Trello

## Basic Information

- Node Type: `nodes-base.trello`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Create, change and delete boards and cards

### Available Operations

### Create
Create a new attachment for a card
- Value: `create`

### Delete
Delete an attachment
- Value: `delete`

### Get
Get the data of an attachment
- Value: `get`

### Get Many
Returns many attachments for the card
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | The URL of the attachment to add |
| `type` | options | Yes | `"normal"` | Determines the type of membership the user being added should have |
| `color` | options | Yes | `"null"` | The color for the label |
| `cardId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The ID of the card |
| `id` | string | Yes | `""` | The ID of the attachment to delete |
| `id` | string | Yes | `""` | The ID of the attachment to get |
| `name` | string | Yes | `""` | The name of the board |
| `id` | resourceLocator | Yes | `{"mode":"list","value":""}` | The ID of the board |
| `id` | string | Yes | `""` | The ID of the board to get members from |
| `id` | string | Yes | `""` | The ID of the board to add member to |

#### Property Details

##### Type (`type`)

Determines the type of membership the user being added should have

Optional values:
- `normal`: Normal - Invite as normal member
- `admin`: Admin - Invite as admin
- `observer`: Observer - Invite as observer (Trello premium feature)

##### Color (`color`)

The color for the label

Optional values:
- `black`: Black
- `blue`: Blue
- `green`: Green
- `lime`: Lime
- `null`: Null
- `orange`: Orange
- `pink`: Pink
- `purple`: Purple
- `red`: Red
- `sky`: Sky
- `yellow`: Yellow

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
  "name": "Trello",
  "type": "nodes-base.trello",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "type": "normal",
    "color": "null",
    "cardId": {
      "mode": "list",
      "value": ""
    },
    "id": "",
    "name": ""
  }
}
```

#### Create Example
```json
{
  "name": "Trello",
  "type": "nodes-base.trello",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "type": "normal",
    "color": "null",
    "cardId": {
      "mode": "list",
      "value": ""
    },
    "id": "",
    "name": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Trello",
  "type": "nodes-base.trello",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "type": "normal",
    "color": "null",
    "cardId": {
      "mode": "list",
      "value": ""
    },
    "id": "",
    "name": "",
    "operation": "delete"
  }
}
```

---

## Twake

## Basic Information

- Node Type: `nodes-base.twake`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Twake API

### Available Operations

### Send
Send a message
- Value: `send`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `content` | string | Yes | `""` | Message content |
| `resource` | options | No | `"message"` | - |
| `operation` | options | No | `"send"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `channelId` | options | No | `""` | Channel's ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

#### Property Details

##### Resource (`resource`)

Optional values:
- `message`: Message - Send data to the message app

##### Operation (`operation`)

Optional values:
- `send`: Send - Send a message

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: senderIcon - URL of the image/icon
- `undefined`: senderName

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
  "name": "Twake",
  "type": "nodes-base.twake",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "content": ""
  }
}
```

#### Send Example
```json
{
  "name": "Twake",
  "type": "nodes-base.twake",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "content": "",
    "operation": "send"
  }
}
```

---

## Twilio

## Basic Information

- Node Type: `nodes-base.twilio`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Send SMS and WhatsApp messages or make phone calls

### Available Operations

### Send
Send SMS/MMS/WhatsApp message
- Value: `send`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `from` | string | Yes | `""` | The number from which to send the message |
| `to` | string | Yes | `""` | The number to which to send the message |
| `message` | string | Yes | `""` | The message to send |
| `message` | string | Yes | `""` | - |
| `resource` | options | No | `"sms"` | - |
| `operation` | options | No | `"send"` | - |
| `operation` | options | No | `"make"` | - |
| `options` | collection | No | `{}` | - |
| `toWhatsapp` | boolean | No | `false` | Whether the message should be sent to WhatsApp |
| `twiml` | boolean | No | `false` | Whether to use the <a href="https://www.twilio.com/docs/voice/twiml">Twilio Markup Language</a> in the message |

#### Property Details

##### Resource (`resource`)

Optional values:
- `call`: Call
- `sms`: SMS

##### Operation (`operation`)

Optional values:
- `send`: Send - Send SMS/MMS/WhatsApp message

##### Operation (`operation`)

Optional values:
- `make`: Make

##### Options (`options`)

Optional values:
- `undefined`: statusCallback - Status Callbacks allow you to receive events related to the REST resources managed by Twilio: Rooms, Recordings and Compositions

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
  "name": "Twilio",
  "type": "nodes-base.twilio",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "from": "",
    "to": "",
    "message": ""
  }
}
```

#### Send Example
```json
{
  "name": "Twilio",
  "type": "nodes-base.twilio",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "from": "",
    "to": "",
    "message": "",
    "operation": "send"
  }
}
```

---

## Unleashed Software

## Basic Information

- Node Type: `nodes-base.unleashedSoftware`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Unleashed Software API

### Available Operations

### Get Many
Get many sales orders
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | No | `"salesOrder"` | - |
| `operation` | options | No | `"getAll"` | - |
| `operation` | options | No | `"getAll"` | - |
| `filters` | collection | No | `{}` | - |
| `filters` | collection | No | `{}` | - |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `100` | Max number of results to return |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `100` | Max number of results to return |
| `productId` | string | No | `""` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `salesOrder`: Sales Order
- `stockOnHand`: Stock On Hand

##### Operation (`operation`)

Optional values:
- `getAll`: Get Many - Get many sales orders

##### Operation (`operation`)

Optional values:
- `get`: Get - Get a stock on hand
- `getAll`: Get Many - Get many stocks on hand

##### Filters (`filters`)

Optional values:
- `undefined`: customerId - Only returns orders for a specified Customer GUID. The CustomerId can be specified as a list of comma-separated GUIDs.
- `undefined`: customerCode - Returns orders that start with the specific customer code
- `undefined`: endDate - Returns orders with order date before the specified date. UTC.
- `undefined`: modifiedSince - Returns orders created or edited after a specified date, must be UTC format
- `undefined`: orderNumber - Returns a single order with the specified order number. If set, it overrides all other filters.
- `undefined`: orderStatus - Returns orders with the specified status. If no orderStatus filter is specified, then we exclude "Deleted" by default.
- `undefined`: startDate - Returns orders with order date after the specified date. UTC.

##### Filters (`filters`)

Optional values:
- `undefined`: asAtDate - Returns the stock on hand for a specific date
- `undefined`: IsAssembled - Whether the AvailableQty will also include the quantity that can be assembled
- `undefined`: modifiedSince - Returns stock on hand values modified after a specific date
- `undefined`: orderBy - Orders the list by a specific column, by default the list is ordered by productCode
- `undefined`: productId - Returns products with the specific Product Guid. You can enter multiple product IDs separated by commas.
- `undefined`: warehouseCode - Returns stock on hand for a specific warehouse code
- `undefined`: warehouseName - Returns stock on hand for a specific warehouse name

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
  "name": "Unleashed Software",
  "type": "nodes-base.unleashedSoftware",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Get Many Example
```json
{
  "name": "Unleashed Software",
  "type": "nodes-base.unleashedSoftware",
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

## urlscan.io

## Basic Information

- Node Type: `nodes-base.urlScanIo`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Provides various utilities for monitoring websites like health checks or screenshots

### Available Operations

### Get
- Value: `get`

### Get Many
- Value: `getAll`

### Perform
- Value: `perform`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | No | `"scan"` | - |
| `operation` | options | No | `"perform"` | - |
| `url` | string | No | `""` | URL to scan |
| `filters` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |
| `scanId` | string | No | `""` | ID of the scan to retrieve |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `50` | Max number of results to return |

#### Property Details

##### Resource (`resource`)

Optional values:
- `scan`: Scan

##### Operation (`operation`)

Optional values:
- `get`: Get
- `getAll`: Get Many
- `perform`: Perform

##### Filters (`filters`)

Optional values:
- `undefined`: query - Query using the \<a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html#query-dsl-query-string-query"\>Elastic Search Query String syntax\</a\>. See \<a href="https://urlscan.io/docs/search/"\>supported fields\</a\> in the documentation.

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: customAgent - \<code\>User-Agent\</code\> header to set for this scan. Defaults to \<code\>n8n\</code\>
- `undefined`: overrideSafety - Disable reclassification of URLs with potential PII in them
- `undefined`: referer - HTTP referer to set for this scan
- `undefined`: tags - Comma-separated list of user-defined tags to add to this scan. Limited to 10 tags.
- `undefined`: visibility

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
  "name": "urlscan.io",
  "type": "nodes-base.urlScanIo",
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
  "name": "urlscan.io",
  "type": "nodes-base.urlScanIo",
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
  "name": "urlscan.io",
  "type": "nodes-base.urlScanIo",
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

## Webex by Cisco

## Basic Information

- Node Type: `nodes-base.ciscoWebex`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Cisco Webex API

### Available Operations

### Create
- Value: `create`

### Delete
- Value: `delete`

### Get
- Value: `get`

### Get Many
- Value: `getAll`

### Update
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `destination` | options | Yes | `"room"` | - |
| `specifyPersonBy` | options | Yes | `"email"` | - |
| `title` | string | Yes | `""` | Meeting title. The title can be a maximum of 128 characters long. |
| `start` | dateTime | Yes | `""` | Date and time for the start of the meeting. Acceptable <a href="https://datatracker.ietf.org/doc/html/rfc2445"> format</a>. |
| `end` | dateTime | Yes | `""` | Date and time for the end of the meeting. Acceptable <a href="https://datatracker.ietf.org/doc/html/rfc2445"> format</a>. |
| `meetingId` | string | Yes | `""` | ID of the meeting |
| `meetingId` | string | Yes | `""` | ID of the meeting |
| `meetingId` | string | Yes | `""` | ID of the meeting |
| `roomId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `text` | string | Yes | `""` | The message, in plain text |

#### Property Details

##### Destination (`destination`)

Optional values:
- `room`: Room
- `person`: Person

##### Specify Person By (`specifyPersonBy`)

Optional values:
- `email`: Email
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
  "name": "Webex by Cisco",
  "type": "nodes-base.ciscoWebex",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "destination": "room",
    "specifyPersonBy": "email",
    "title": "",
    "start": "",
    "end": "",
    "meetingId": "",
    "roomId": "",
    "text": ""
  }
}
```

#### Create Example
```json
{
  "name": "Webex by Cisco",
  "type": "nodes-base.ciscoWebex",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "destination": "room",
    "specifyPersonBy": "email",
    "title": "",
    "start": "",
    "end": "",
    "meetingId": "",
    "roomId": "",
    "text": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Webex by Cisco",
  "type": "nodes-base.ciscoWebex",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "destination": "room",
    "specifyPersonBy": "email",
    "title": "",
    "start": "",
    "end": "",
    "meetingId": "",
    "roomId": "",
    "text": "",
    "operation": "delete"
  }
}
```

---

## Webflow

## Basic Information

- Node Type: `nodes-base.webflow`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Webflow API

### Available Operations

### Create
- Value: `create`

### Delete
- Value: `deleteItem`

### Get
- Value: `get`

### Get Many
- Value: `getAll`

### Update
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `siteId` | options | Yes | `""` | ID of the site containing the collection whose items to add to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `collectionId` | options | Yes | `""` | ID of the collection to add an item to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `live` | boolean | Yes | `false` | Whether the item should be published on the live site |
| `siteId` | options | Yes | `""` | ID of the site containing the collection whose items to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `collectionId` | options | Yes | `""` | ID of the collection whose items to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `itemId` | string | Yes | `""` | ID of the item to operate on |
| `siteId` | options | Yes | `""` | ID of the site containing the collection whose items to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `collectionId` | options | Yes | `""` | ID of the collection whose items to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `itemId` | string | Yes | `""` | ID of the item to operate on |
| `siteId` | options | Yes | `""` | ID of the site containing the collection whose items to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

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
  "name": "Webflow",
  "type": "nodes-base.webflow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "siteId": "",
    "collectionId": "",
    "live": false,
    "itemId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Webflow",
  "type": "nodes-base.webflow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "siteId": "",
    "collectionId": "",
    "live": false,
    "itemId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Webflow",
  "type": "nodes-base.webflow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "siteId": "",
    "collectionId": "",
    "live": false,
    "itemId": "",
    "operation": "deleteItem"
  }
}
```

---

## Wekan

## Basic Information

- Node Type: `nodes-base.wekan`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Wekan API

### Available Operations

### Create
Create a new board
- Value: `create`

### Delete
Delete a board
- Value: `delete`

### Get
Get the data of a board
- Value: `get`

### Get Many
Get many user boards
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `fromObject` | options | Yes | `""` | - |
| `title` | string | Yes | `""` | The title of the board |
| `owner` | options | Yes | `""` | The user ID in Wekan. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `boardId` | string | Yes | `""` | The ID of the board to delete |
| `boardId` | string | Yes | `""` | The ID of the board to get |
| `IdUser` | options | Yes | `""` | The ID of the user that boards are attached. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `boardId` | options | Yes | `""` | The ID of the board that list belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `listId` | options | Yes | `""` | The ID of the list to create card in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `title` | string | Yes | `""` | The title of the card |
| `swimlaneId` | options | Yes | `""` | The swimlane ID of the new card. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

#### Property Details

##### From Object (`fromObject`)

Optional values:
- `list`: List
- `swimlane`: Swimlane

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
  "name": "Wekan",
  "type": "nodes-base.wekan",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fromObject": "",
    "title": "",
    "owner": "",
    "boardId": "",
    "IdUser": "",
    "listId": "",
    "swimlaneId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Wekan",
  "type": "nodes-base.wekan",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fromObject": "",
    "title": "",
    "owner": "",
    "boardId": "",
    "IdUser": "",
    "listId": "",
    "swimlaneId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Wekan",
  "type": "nodes-base.wekan",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fromObject": "",
    "title": "",
    "owner": "",
    "boardId": "",
    "IdUser": "",
    "listId": "",
    "swimlaneId": "",
    "operation": "delete"
  }
}
```

---

## Wise

## Basic Information

- Node Type: `nodes-base.wise`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Wise API

### Available Operations

### Get Balances
Retrieve balances for all account currencies of this user
- Value: `getBalances`

### Get Currencies
Retrieve currencies in the borderless account of this user
- Value: `getCurrencies`

### Get Statement
Retrieve the statement for the borderless account of this user
- Value: `getStatement`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `profileId` | options | Yes | `[]` | ID of the user profile to retrieve the balance of. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `borderlessAccountId` | options | Yes | `[]` | ID of the borderless account to retrieve the statement of. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `fileName` | string | Yes | `""` | Name of the file that will be downloaded |
| `profileId` | options | Yes | `[]` | ID of the user profile to retrieve. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `profileId` | options | Yes | `[]` | ID of the user profile to create the quote under. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `targetAccountId` | options | Yes | `[]` | ID of the account that will receive the funds. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `quoteId` | string | Yes | `""` | ID of the quote to retrieve |
| `profileId` | options | Yes | `[]` | ID of the user profile to retrieve the balance of. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `quoteId` | string | Yes | `""` | ID of the quote based on which to create the transfer |
| `targetAccountId` | options | Yes | `[]` | ID of the account that will receive the funds. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

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
  "name": "Wise",
  "type": "nodes-base.wise",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "profileId": [],
    "borderlessAccountId": [],
    "fileName": "",
    "targetAccountId": [],
    "quoteId": ""
  }
}
```

#### Get Balances Example
```json
{
  "name": "Wise",
  "type": "nodes-base.wise",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "profileId": [],
    "borderlessAccountId": [],
    "fileName": "",
    "targetAccountId": [],
    "quoteId": "",
    "operation": "getBalances"
  }
}
```

#### Get Currencies Example
```json
{
  "name": "Wise",
  "type": "nodes-base.wise",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "profileId": [],
    "borderlessAccountId": [],
    "fileName": "",
    "targetAccountId": [],
    "quoteId": "",
    "operation": "getCurrencies"
  }
}
```
