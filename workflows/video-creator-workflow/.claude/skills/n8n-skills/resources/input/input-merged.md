# Input Nodes - Node Collection

This file contains complete information for 99 nodes.

## Table of Contents

- [Box](#box)
- [Chargebee](#chargebee)
- [Cloudflare](#cloudflare)
- [Contentful](#contentful)
- [Convert to File](#convert-to-file)
- [ConvertKit](#convertkit)
- [CrateDB](#cratedb)
- [Data table](#data-table)
- [DeepL](#deepl)
- [DHL](#dhl)
- [Discourse](#discourse)
- [Disqus](#disqus)
- [Emelia](#emelia)
- [Execution Data](#execution-data)
- [Extract from File](#extract-from-file)
- [FileMaker](#filemaker)
- [FTP](#ftp)
- [GetResponse](#getresponse)
- [Ghost](#ghost)
- [GitLab](#gitlab)
- [Google BigQuery](#google-bigquery)
- [Google Books](#google-books)
- [Google Business Profile](#google-business-profile)
- [Google Calendar](#google-calendar)
- [Google Chat](#google-chat)
- [Google Cloud Firestore](#google-cloud-firestore)
- [Google Cloud Natural Language](#google-cloud-natural-language)
- [Google Cloud Realtime Database](#google-cloud-realtime-database)
- [Google Contacts](#google-contacts)
- [Google Docs](#google-docs)
- [Google Slides](#google-slides)
- [Google Tasks](#google-tasks)
- [Google Translate](#google-translate)
- [Google Workspace Admin](#google-workspace-admin)
- [Gotify](#gotify)
- [GraphQL](#graphql)
- [Grist](#grist)
- [HaloPSA](#halopsa)
- [Harvest](#harvest)
- [Help Scout](#help-scout)
- [iCalendar](#icalendar)
- [Item Lists](#item-lists)
- [Iterable](#iterable)
- [Keap](#keap)
- [Kitemaker](#kitemaker)
- [Line](#line)
- [LinkedIn](#linkedin)
- [Magento 2](#magento-2)
- [MailerLite](#mailerlite)
- [Microsoft Dynamics CRM](#microsoft-dynamics-crm)
- [Microsoft Excel 365](#microsoft-excel-365)
- [Microsoft OneDrive](#microsoft-onedrive)
- [Microsoft SQL](#microsoft-sql)
- [Microsoft Teams](#microsoft-teams)
- [Microsoft To Do](#microsoft-to-do)
- [Mindee](#mindee)
- [MongoDB](#mongodb)
- [MQTT](#mqtt)
- [n8n Form](#n8n-form)
- [Nextcloud](#nextcloud)
- [NocoDB](#nocodb)
- [Npm](#npm)
- [Onfleet](#onfleet)
- [OpenWeatherMap](#openweathermap)
- [Oracle Database](#oracle-database)
- [Phantombuster](#phantombuster)
- [Philips Hue](#philips-hue)
- [PostHog](#posthog)
- [Pushbullet](#pushbullet)
- [Pushcut](#pushcut)
- [Pushover](#pushover)
- [QuestDB](#questdb)
- [Quick Base](#quick-base)
- [Read Binary File](#read-binary-file)
- [Read Binary Files](#read-binary-files)
- [Read PDF](#read-pdf)
- [Read/Write Files from Disk](#readwrite-files-from-disk)
- [Redis](#redis)
- [Respond to Chat](#respond-to-chat)
- [RSS Read](#rss-read)
- [Sendy](#sendy)
- [Snowflake](#snowflake)
- [Spotify](#spotify)
- [SSH](#ssh)
- [Start](#start)
- [Sticky Note](#sticky-note)
- [Stop and Error](#stop-and-error)
- [Strapi](#strapi)
- [Strava](#strava)
- [Supabase](#supabase)
- [TimescaleDB](#timescaledb)
- [Twist](#twist)
- [Venafi TLS Protect Cloud](#venafi-tls-protect-cloud)
- [Venafi TLS Protect Datacenter](#venafi-tls-protect-datacenter)
- [Vonage](#vonage)
- [Yourls](#yourls)
- [YouTube](#youtube)
- [Zammad](#zammad)
- [Zoom](#zoom)

---

## Box

## Basic Information

- Node Type: `nodes-base.box`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Box API

### Available Operations

### Copy
Copy a file
- Value: `copy`

### Delete
Delete a file
- Value: `delete`

### Download
Download a file
- Value: `download`

### Get
Get a file
- Value: `get`

### Search
Search files
- Value: `search`

### Share
Share a file
- Value: `share`

### Upload
Upload a file
- Value: `upload`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `binaryData` | boolean | Yes | `false` | Whether the data to upload should be taken from binary field |
| `fileContent` | string | Yes | `""` | The text content of the file |
| `name` | string | Yes | `""` | Folder's name |
| `fileId` | string | Yes | `""` | - |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `folderId` | string | Yes | `""` | - |
| `resource` | options | No | `"file"` | - |
| `operation` | options | No | `"upload"` | - |
| `operation` | options | No | `"create"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `file`: File
- `folder`: Folder

##### Operation (`operation`)

Optional values:
- `copy`: Copy - Copy a file
- `delete`: Delete - Delete a file
- `download`: Download - Download a file
- `get`: Get - Get a file
- `search`: Search - Search files
- `share`: Share - Share a file
- `upload`: Upload - Upload a file

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a folder
- `delete`: Delete - Delete a folder
- `get`: Get - Get a folder
- `search`: Search - Search files
- `share`: Share - Share a folder
- `update`: Update - Update folder

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
  "name": "Box",
  "type": "nodes-base.box",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryData": false,
    "fileContent": "",
    "name": "",
    "fileId": "",
    "binaryPropertyName": "data",
    "folderId": ""
  }
}
```

#### Copy Example
```json
{
  "name": "Box",
  "type": "nodes-base.box",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryData": false,
    "fileContent": "",
    "name": "",
    "fileId": "",
    "binaryPropertyName": "data",
    "folderId": "",
    "operation": "copy"
  }
}
```

#### Delete Example
```json
{
  "name": "Box",
  "type": "nodes-base.box",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryData": false,
    "fileContent": "",
    "name": "",
    "fileId": "",
    "binaryPropertyName": "data",
    "folderId": "",
    "operation": "delete"
  }
}
```

---

## Chargebee

## Basic Information

- Node Type: `nodes-base.chargebee`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Retrieve data from Chargebee API

### Available Operations

### Create
Create a customer
- Value: `create`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `invoiceId` | string | Yes | `""` | The ID of the invoice to get |
| `subscriptionId` | string | Yes | `""` | The ID of the subscription to cancel |
| `subscriptionId` | string | Yes | `""` | The ID of the subscription to delete |
| `resource` | options | No | `"invoice"` | - |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"list"` | - |
| `operation` | options | No | `"delete"` | - |
| `properties` | collection | No | `{}` | Properties to set on the new user |
| `filters` | fixedCollection | No | `{}` | Filter for invoices |
| `maxResults` | number | No | `10` | Max. amount of results to return(< 100). |

#### Property Details

##### Resource (`resource`)

Optional values:
- `customer`: Customer
- `invoice`: Invoice
- `subscription`: Subscription

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a customer

##### Operation (`operation`)

Optional values:
- `list`: List - Return the invoices
- `pdfUrl`: PDF Invoice URL - Get URL for the invoice PDF

##### Operation (`operation`)

Optional values:
- `cancel`: Cancel - Cancel a subscription
- `delete`: Delete - Delete a subscription

##### Properties (`properties`)

Properties to set on the new user

Optional values:
- `undefined`: id - ID for the new customer. If not given, this will be auto-generated.
- `undefined`: first_name - The first name of the customer
- `undefined`: last_name - The last name of the customer
- `undefined`: email - The email address of the customer
- `undefined`: phone - The phone number of the customer
- `undefined`: company - The company of the customer
- `undefined`: customProperties - Adds a custom property to set also values which have not been predefined

##### Filters (`filters`)

Filter for invoices

Optional values:
- `undefined`: date
- `undefined`: total

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
  "name": "Chargebee",
  "type": "nodes-base.chargebee",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "invoiceId": "",
    "subscriptionId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Chargebee",
  "type": "nodes-base.chargebee",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "invoiceId": "",
    "subscriptionId": "",
    "operation": "create"
  }
}
```

---

## Cloudflare

## Basic Information

- Node Type: `nodes-base.cloudflare`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Cloudflare API

### Available Operations

### Delete
Delete a certificate
- Value: `delete`

### Get
Get a certificate
- Value: `get`

### Get Many
Get many certificates
- Value: `getMany`

### Upload
Upload a certificate
- Value: `upload`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `zoneId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `certificate` | string | Yes | `""` | The zone's leaf certificate |
| `privateKey` | string | Yes | `""` | - |
| `certificateId` | string | Yes | `""` | - |
| `resource` | options | No | `"zoneCertificate"` | - |
| `operation` | options | No | `"upload"` | - |
| `filters` | collection | No | `{}` | - |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `25` | Max number of results to return |

#### Property Details

##### Resource (`resource`)

Optional values:
- `zoneCertificate`: Zone Certificate

##### Operation (`operation`)

Optional values:
- `delete`: Delete - Delete a certificate
- `get`: Get - Get a certificate
- `getMany`: Get Many - Get many certificates
- `upload`: Upload - Upload a certificate

##### Filters (`filters`)

Optional values:
- `undefined`: status - Status of the zone's custom SSL

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
  "name": "Cloudflare",
  "type": "nodes-base.cloudflare",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "zoneId": "",
    "certificate": "",
    "privateKey": "",
    "certificateId": ""
  }
}
```

#### Delete Example
```json
{
  "name": "Cloudflare",
  "type": "nodes-base.cloudflare",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "zoneId": "",
    "certificate": "",
    "privateKey": "",
    "certificateId": "",
    "operation": "delete"
  }
}
```

#### Get Example
```json
{
  "name": "Cloudflare",
  "type": "nodes-base.cloudflare",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "zoneId": "",
    "certificate": "",
    "privateKey": "",
    "certificateId": "",
    "operation": "get"
  }
}
```

---

## Contentful

## Basic Information

- Node Type: `nodes-base.contentful`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Contentful API

### Available Operations

### Get
- Value: `get`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `contentTypeId` | string | Yes | `""` | - |
| `entryId` | string | Yes | `""` | - |
| `assetId` | string | Yes | `""` | - |
| `resource` | options | No | `"entry"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"getAll"` | - |
| `operation` | options | No | `"getAll"` | - |
| `source` | options | No | `"deliveryApi"` | Pick where your data comes from, delivery or preview API |

#### Property Details

##### Resource (`resource`)

Optional values:
- `asset`: Asset
- `contentType`: Content Type
- `entry`: Entry
- `locale`: Locale
- `space`: Space

##### Operation (`operation`)

Optional values:
- `get`: Get

##### Operation (`operation`)

Optional values:
- `get`: Get

##### Operation (`operation`)

Optional values:
- `get`: Get
- `getAll`: Get Many

##### Operation (`operation`)

Optional values:
- `get`: Get
- `getAll`: Get Many

##### Operation (`operation`)

Optional values:
- `getAll`: Get Many

##### Source (`source`)

Pick where your data comes from, delivery or preview API

Optional values:
- `deliveryApi`: Delivery API
- `previewApi`: Preview API

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
  "name": "Contentful",
  "type": "nodes-base.contentful",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contentTypeId": "",
    "entryId": "",
    "assetId": ""
  }
}
```

#### Get Example
```json
{
  "name": "Contentful",
  "type": "nodes-base.contentful",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contentTypeId": "",
    "entryId": "",
    "assetId": "",
    "operation": "get"
  }
}
```

---

## Convert to File

## Basic Information

- Node Type: `nodes-base.convertToFile`
- Category: input
- Package: n8n-nodes-base

### Description

Convert JSON data to binary data

### Available Operations

### Convert to CSV
Transform input data into a CSV file
- Value: `csv`

### Convert to HTML
Transform input data into a table in an HTML file
- Value: `html`

### Convert to ICS
Converts each input item to an ICS event file
- Value: `iCal`

### Convert to JSON
Transform input data into a single or multiple JSON files
- Value: `toJson`

### Convert to ODS
Transform input data into an ODS file
- Value: `ods`

### Convert to RTF
Transform input data into a table in an RTF file
- Value: `rtf`

### Convert to Text File
Transform input data string into a file
- Value: `toText`

### Convert to XLS
Transform input data into an Excel file
- Value: `xls`

### Convert to XLSX
Transform input data into an Excel file
- Value: `xlsx`

### Move Base64 String to File
Convert a base64-encoded string into its original file format
- Value: `toBinary`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `sourceProperty` | string | Yes | `""` | The name of the input field that contains the base64 string to convert to a file. Use dot-notation for deep fields (e.g. 'level1.level2.currentKey'). |
| `sourceProperty` | string | Yes | `""` | The name of the input field that contains a string to convert to a file. Use dot-notation for deep fields (e.g. 'level1.level2.currentKey'). |
| `start` | dateTime | Yes | `""` | Date and time at which the event begins. (For all-day events, the time will be ignored.). |
| `end` | dateTime | Yes | `""` | Date and time at which the event ends. (For all-day events, the time will be ignored.). |
| `binaryPropertyName` | string | Yes | `"data"` | The field that your iCalendar file will be available under in the output |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `operation` | options | No | `"csv"` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `csv`: Convert to CSV - Transform input data into a CSV file
- `html`: Convert to HTML - Transform input data into a table in an HTML file
- `iCal`: Convert to ICS - Converts each input item to an ICS event file
- `toJson`: Convert to JSON - Transform input data into a single or multiple JSON files
- `ods`: Convert to ODS - Transform input data into an ODS file
- `rtf`: Convert to RTF - Transform input data into a table in an RTF file
- `toText`: Convert to Text File - Transform input data string into a file
- `xls`: Convert to XLS - Transform input data into an Excel file
- `xlsx`: Convert to XLSX - Transform input data into an Excel file
- `toBinary`: Move Base64 String to File - Convert a base64-encoded string into its original file format

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
  "name": "Convert to File",
  "type": "nodes-base.convertToFile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "sourceProperty": "",
    "start": "",
    "end": "",
    "binaryPropertyName": "data"
  }
}
```

#### Convert to CSV Example
```json
{
  "name": "Convert to File",
  "type": "nodes-base.convertToFile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "sourceProperty": "",
    "start": "",
    "end": "",
    "binaryPropertyName": "data",
    "operation": "csv"
  }
}
```

#### Convert to HTML Example
```json
{
  "name": "Convert to File",
  "type": "nodes-base.convertToFile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "sourceProperty": "",
    "start": "",
    "end": "",
    "binaryPropertyName": "data",
    "operation": "html"
  }
}
```

---

## ConvertKit

## Basic Information

- Node Type: `nodes-base.convertKit`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume ConvertKit API

### Available Operations

### Create
Create a field
- Value: `create`

### Delete
Delete a field
- Value: `delete`

### Get Many
Get many fields
- Value: `getAll`

### Update
Update a field
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `id` | string | Yes | `""` | The ID of your custom field |
| `label` | string | Yes | `""` | The label of the custom field |
| `id` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `email` | string | Yes | `""` | The subscriber's email address |
| `id` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `email` | string | Yes | `""` | The subscriber's email address |
| `name` | string | Yes | `""` | Tag name, multiple can be added separated by comma |
| `tagId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `email` | string | Yes | `""` | Subscriber email address |
| `operation` | options | No | `"addSubscriber"` | The operations to perform |

#### Property Details

##### Operation (`operation`)

The operations to perform

Optional values:
- `addSubscriber`: Add Subscriber - Add a subscriber
- `getAll`: Get Many - Get many forms
- `getSubscriptions`: Get Subscriptions - List subscriptions to a form including subscriber data

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
  "name": "ConvertKit",
  "type": "nodes-base.convertKit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "id": "",
    "label": "",
    "email": "",
    "name": "",
    "tagId": ""
  }
}
```

#### Create Example
```json
{
  "name": "ConvertKit",
  "type": "nodes-base.convertKit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "id": "",
    "label": "",
    "email": "",
    "name": "",
    "tagId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "ConvertKit",
  "type": "nodes-base.convertKit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "id": "",
    "label": "",
    "email": "",
    "name": "",
    "tagId": "",
    "operation": "delete"
  }
}
```

---

## CrateDB

## Basic Information

- Node Type: `nodes-base.crateDb`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Add and update data in CrateDB

### Available Operations

### Execute Query
Execute an SQL query
- Value: `executeQuery`

### Insert
Insert rows in database
- Value: `insert`

### Update
Update rows in database
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | The SQL query to execute. You can use n8n expressions or $1 and $2 in conjunction with query parameters. |
| `schema` | string | Yes | `"doc"` | Name of the schema the table belongs to |
| `table` | string | Yes | `""` | Name of the table in which to insert data to |
| `schema` | string | Yes | `"doc"` | Name of the schema the table belongs to |
| `table` | string | Yes | `""` | Name of the table in which to update data in |
| `updateKey` | string | Yes | `"id"` | Comma-separated list of the properties which decides which rows in the database should be updated. Normally that would be "id". |
| `operation` | options | No | `"insert"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `columns` | string | No | `""` | Comma-separated list of the properties which should used as columns for the new rows |
| `columns` | string | No | `""` | Comma-separated list of the properties which should used as columns for rows to update |

#### Property Details

##### Operation (`operation`)

Optional values:
- `executeQuery`: Execute Query - Execute an SQL query
- `insert`: Insert - Insert rows in database
- `update`: Update - Update rows in database

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: mode - The way queries should be sent to database. Can be used in conjunction with \<b\>Continue on Fail\</b\>. See \<a href="https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cratedb/"\>the docs\</a\> for more examples.
- `undefined`: queryParams - Comma-separated list of properties which should be used as query parameters

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
  "name": "CrateDB",
  "type": "nodes-base.crateDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "schema": "doc",
    "table": "",
    "updateKey": "id"
  }
}
```

#### Execute Query Example
```json
{
  "name": "CrateDB",
  "type": "nodes-base.crateDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "schema": "doc",
    "table": "",
    "updateKey": "id",
    "operation": "executeQuery"
  }
}
```

#### Insert Example
```json
{
  "name": "CrateDB",
  "type": "nodes-base.crateDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "schema": "doc",
    "table": "",
    "updateKey": "id",
    "operation": "insert"
  }
}
```

---

## Data table

## Basic Information

- Node Type: `nodes-base.dataTable`
- Category: input
- Package: n8n-nodes-base

### Description

Permanently save data across workflow executions in a table

### Available Operations

### Delete
Delete row(s)
- Value: `deleteRows`

### Get
Get row(s)
- Value: `get`

### If Row Exists
Match input items that are in the data table
- Value: `rowExists`

### If Row Does Not Exist
Match input items that are not in the data table
- Value: `rowNotExists`

### Insert
Insert a new row
- Value: `insert`

### Update
Update row(s) matching certain fields
- Value: `update`

### Upsert
Update row(s), or insert if there is no match
- Value: `upsert`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `dataTableId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `resource` | options | No | `"row"` | - |
| `operation` | options | No | `"insert"` | - |
| `filters` | fixedCollection | No | `{}` | Filter to decide which rows get |
| `filters` | fixedCollection | No | `{}` | Filter to decide which rows get |
| `filters` | fixedCollection | No | `{}` | Filter to decide which rows get |
| `filters` | fixedCollection | No | `{}` | Filter to decide which rows get |

#### Property Details

##### Resource (`resource`)

Optional values:
- `row`: Row

##### Operation (`operation`)

Optional values:
- `deleteRows`: Delete - Delete row(s)
- `get`: Get - Get row(s)
- `rowExists`: If Row Exists - Match input items that are in the data table
- `rowNotExists`: If Row Does Not Exist - Match input items that are not in the data table
- `insert`: Insert - Insert a new row
- `update`: Update - Update row(s) matching certain fields
- `upsert`: Upsert - Update row(s), or insert if there is no match

##### Conditions (`filters`)

Filter to decide which rows get

Optional values:
- `undefined`: conditions

##### Conditions (`filters`)

Filter to decide which rows get

Optional values:
- `undefined`: conditions

##### Conditions (`filters`)

Filter to decide which rows get

Optional values:
- `undefined`: conditions

##### Conditions (`filters`)

Filter to decide which rows get

Optional values:
- `undefined`: conditions

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
  "name": "Data table",
  "type": "nodes-base.dataTable",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dataTableId": {
      "mode": "list",
      "value": ""
    },
    "columns": {
      "mappingMode": "defineBelow",
      "value": null
    }
  }
}
```

#### Delete Example
```json
{
  "name": "Data table",
  "type": "nodes-base.dataTable",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dataTableId": {
      "mode": "list",
      "value": ""
    },
    "columns": {
      "mappingMode": "defineBelow",
      "value": null
    },
    "operation": "deleteRows"
  }
}
```

#### Get Example
```json
{
  "name": "Data table",
  "type": "nodes-base.dataTable",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dataTableId": {
      "mode": "list",
      "value": ""
    },
    "columns": {
      "mappingMode": "defineBelow",
      "value": null
    },
    "operation": "get"
  }
}
```

---

## DeepL

## Basic Information

- Node Type: `nodes-base.deepL`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Translate data using DeepL

### Available Operations

### Translate
Translate data
- Value: `translate`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `text` | string | Yes | `""` | Input text to translate |
| `translateTo` | options | Yes | `""` | Language to translate to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `resource` | options | No | `"language"` | - |
| `operation` | options | No | `"translate"` | - |
| `additionalFields` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `language`: Language

##### Operation (`operation`)

Optional values:
- `translate`: Translate - Translate data

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: sourceLang - Language to translate from. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: splitSentences - How the translation engine should split sentences
- `undefined`: preserveFormatting - Whether the translation engine should respect the original formatting, even if it would usually correct some aspects
- `undefined`: formality - How formal or informal the target text should be. May not be supported with all languages.

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
  "name": "DeepL",
  "type": "nodes-base.deepL",
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
  "name": "DeepL",
  "type": "nodes-base.deepL",
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

## DHL

## Basic Information

- Node Type: `nodes-base.dhl`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume DHL API

### Available Operations

### Get Tracking Details
- Value: `get`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `trackingNumber` | string | Yes | `""` | - |
| `resource` | hidden | No | `"shipment"` | - |
| `operation` | options | No | `"get"` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `shipment`: Shipment

##### Operation (`operation`)

Optional values:
- `get`: Get Tracking Details

##### Options (`options`)

Optional values:
- `undefined`: recipientPostalCode - DHL will return more detailed information on the shipment when you provide the Recipient's Postal Code - it acts as a verification step

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
  "name": "DHL",
  "type": "nodes-base.dhl",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "trackingNumber": ""
  }
}
```

#### Get Tracking Details Example
```json
{
  "name": "DHL",
  "type": "nodes-base.dhl",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "trackingNumber": "",
    "operation": "get"
  }
}
```

---

## Discourse

## Basic Information

- Node Type: `nodes-base.discourse`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Discourse API

### Available Operations

### Create
Create a category
- Value: `create`

### Get Many
Get many categories
- Value: `getAll`

### Update
Update a category
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `operation` | options | Yes | `"create"` | Choose an operation |
| `operation` | options | Yes | `"create"` | Choose an operation |
| `operation` | options | Yes | `"create"` | Choose an operation |
| `operation` | options | Yes | `"create"` | Choose an operation |
| `operation` | options | Yes | `"add"` | Choose an operation |
| `by` | options | Yes | `"username"` | What to search by |
| `name` | string | Yes | `""` | Name of the category |
| `color` | color | Yes | `"0000FF"` | Color of the category |
| `textColor` | color | Yes | `"0000FF"` | Text color of the category |
| `categoryId` | string | Yes | `""` | ID of the category |

#### Property Details

##### Operation (`operation`)

Choose an operation

Optional values:
- `create`: Create - Create a category
- `getAll`: Get Many - Get many categories
- `update`: Update - Update a category

##### Operation (`operation`)

Choose an operation

Optional values:
- `create`: Create - Create a group
- `get`: Get - Get a group
- `getAll`: Get Many - Get many groups
- `update`: Update - Update a group

##### Operation (`operation`)

Choose an operation

Optional values:
- `create`: Create - Create a post
- `get`: Get - Get a post
- `getAll`: Get Many - Get many posts
- `update`: Update - Update a post

##### Operation (`operation`)

Choose an operation

Optional values:
- `create`: Create - Create a user
- `get`: Get - Get a user
- `getAll`: Get Many - Get many users

##### Operation (`operation`)

Choose an operation

Optional values:
- `add`: Add - Create a user to group
- `remove`: Remove - Remove user from group

##### By (`by`)

What to search by

Optional values:
- `username`: Username
- `externalId`: SSO External ID

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
  "name": "Discourse",
  "type": "nodes-base.discourse",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "add",
    "by": "username",
    "name": "",
    "color": "0000FF",
    "textColor": "0000FF",
    "categoryId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Discourse",
  "type": "nodes-base.discourse",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "create",
    "by": "username",
    "name": "",
    "color": "0000FF",
    "textColor": "0000FF",
    "categoryId": ""
  }
}
```

#### Get Many Example
```json
{
  "name": "Discourse",
  "type": "nodes-base.discourse",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "getAll",
    "by": "username",
    "name": "",
    "color": "0000FF",
    "textColor": "0000FF",
    "categoryId": ""
  }
}
```

---

## Disqus

## Basic Information

- Node Type: `nodes-base.disqus`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Access data on Disqus

### Available Operations

### Get
Return forum details
- Value: `get`

### Get All Categories
Return a list of categories within a forum
- Value: `getCategories`

### Get All Threads
Return a list of threads within a forum
- Value: `getThreads`

### Get All Posts
Return a list of posts within a forum
- Value: `getPosts`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `id` | string | Yes | `""` | The short name(aka ID) of the forum to get |
| `id` | string | Yes | `""` | The short name(aka ID) of the forum to get |
| `id` | string | Yes | `""` | The short name(aka ID) of the forum to get Categories |
| `id` | string | Yes | `""` | The short name(aka ID) of the forum to get Threads |
| `resource` | options | No | `"forum"` | - |
| `operation` | options | No | `"get"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `forum`: Forum

##### Operation (`operation`)

Optional values:
- `get`: Get - Return forum details
- `getCategories`: Get All Categories - Return a list of categories within a forum
- `getThreads`: Get All Threads - Return a list of threads within a forum
- `getPosts`: Get All Posts - Return a list of posts within a forum

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: attach
- `undefined`: related - You may specify relations to include with your response

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: filters - You may specify filters for your response
- `undefined`: include - You may specify relations to include with your response
- `undefined`: order - You may specify order to sort your response
- `undefined`: query - You may specify query forChoices: asc, desc your response
- `undefined`: related - You may specify relations to include with your response
- `undefined`: since - Unix timestamp (or ISO datetime standard)

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: order - You may specify order to sort your response

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: related - You may specify relations to include with your response
- `undefined`: include - You may specify relations to include with your response
- `undefined`: order - You may specify order to sort your response
- `undefined`: since - Unix timestamp (or ISO datetime standard)
- `undefined`: thread - Looks up a thread by ID. You may pass us the "ident" query type instead of an ID by including "forum". You may pass us the "link" query type to filter by URL. You must pass the "forum" if you do not have the Pro API Access addon.

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
  "name": "Disqus",
  "type": "nodes-base.disqus",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "id": ""
  }
}
```

#### Get Example
```json
{
  "name": "Disqus",
  "type": "nodes-base.disqus",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "id": "",
    "operation": "get"
  }
}
```

#### Get All Categories Example
```json
{
  "name": "Disqus",
  "type": "nodes-base.disqus",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "id": "",
    "operation": "getCategories"
  }
}
```

---

## Emelia

## Basic Information

- Node Type: `nodes-base.emelia`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Emelia API

### Available Operations

### Add Contact
- Value: `addContact`

### Create
- Value: `create`

### Duplicate
- Value: `duplicate`

### Get
- Value: `get`

### Get Many
- Value: `getAll`

### Pause
- Value: `pause`

### Start
- Value: `start`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"campaign"` | - |
| `campaignId` | options | Yes | `[]` | The ID of the campaign to add the contact to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `contactEmail` | string | Yes | `""` | The email of the contact to add to the campaign |
| `campaignName` | string | Yes | `""` | The name of the campaign to create |
| `campaignId` | string | Yes | `""` | The ID of the campaign to retrieve |
| `campaignId` | string | Yes | `""` | The ID of the campaign to pause. The campaign must be in RUNNING mode. |
| `campaignId` | string | Yes | `""` | The ID of the campaign to start. Email provider and contacts must be set. |
| `campaignId` | options | Yes | `""` | The ID of the campaign to duplicate. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `campaignName` | string | Yes | `""` | The name of the new campaign to create |
| `contactListId` | options | Yes | `[]` | The ID of the contact list to add the contact to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

#### Property Details

##### Resource (`resource`)

Optional values:
- `campaign`: Campaign
- `contactList`: Contact List

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
  "name": "Emelia",
  "type": "nodes-base.emelia",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "campaign",
    "campaignId": "",
    "contactEmail": "",
    "campaignName": "",
    "contactListId": []
  }
}
```

#### Add Contact Example
```json
{
  "name": "Emelia",
  "type": "nodes-base.emelia",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "campaign",
    "campaignId": "",
    "contactEmail": "",
    "campaignName": "",
    "contactListId": [],
    "operation": "addContact"
  }
}
```

#### Create Example
```json
{
  "name": "Emelia",
  "type": "nodes-base.emelia",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "campaign",
    "campaignId": "",
    "contactEmail": "",
    "campaignName": "",
    "contactListId": [],
    "operation": "create"
  }
}
```

---

## Execution Data

## Basic Information

- Node Type: `nodes-base.executionData`
- Category: input
- Package: n8n-nodes-base

### Description

Add execution data for search

### Available Operations

### Save Highlight Data (for Search/review)
- Value: `save`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `operation` | options | No | `"save"` | - |
| `dataToSave` | fixedCollection | No | `{}` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `save`: Save Highlight Data (for Search/review)

##### Data to Save (`dataToSave`)

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
  "name": "Execution Data",
  "type": "nodes-base.executionData",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Save Highlight Data (for Search/review) Example
```json
{
  "name": "Execution Data",
  "type": "nodes-base.executionData",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "save"
  }
}
```

---

## Extract from File

## Basic Information

- Node Type: `nodes-base.extractFromFile`
- Category: input
- Package: n8n-nodes-base

### Description

Convert binary data to JSON

### Available Operations

### Extract From CSV
Transform a CSV file into output items
- Value: `csv`

### Extract From HTML
Transform a table in an HTML file into output items
- Value: `html`

### Extract From ICS
Transform a ICS file into output items
- Value: `fromIcs`

### Extract From JSON
Transform a JSON file into output items
- Value: `fromJson`

### Extract From ODS
Transform an ODS file into output items
- Value: `ods`

### Extract From PDF
Extracts the content and metadata from a PDF file
- Value: `pdf`

### Extract From RTF
Transform a table in an RTF file into output items
- Value: `rtf`

### Extract From Text File
Extracts the content of a text file
- Value: `text`

### Extract From XML
Extracts the content of an XML file
- Value: `xml`

### Extract From XLS
Transform an Excel file into output items
- Value: `xls`

### Extract From XLSX
Transform an Excel file into output items
- Value: `xlsx`

### Move File to Base64 String
Convert a file into a base64-encoded string
- Value: `binaryToPropery`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `destinationKey` | string | Yes | `"data"` | The name of the output field that will contain the extracted data |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `operation` | options | No | `"csv"` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `csv`: Extract From CSV - Transform a CSV file into output items
- `html`: Extract From HTML - Transform a table in an HTML file into output items
- `fromIcs`: Extract From ICS - Transform a ICS file into output items
- `fromJson`: Extract From JSON - Transform a JSON file into output items
- `ods`: Extract From ODS - Transform an ODS file into output items
- `pdf`: Extract From PDF - Extracts the content and metadata from a PDF file
- `rtf`: Extract From RTF - Transform a table in an RTF file into output items
- `text`: Extract From Text File - Extracts the content of a text file
- `xml`: Extract From XML - Extracts the content of an XML file
- `xls`: Extract From XLS - Transform an Excel file into output items
- `xlsx`: Extract From XLSX - Transform an Excel file into output items
- `binaryToPropery`: Move File to Base64 String - Convert a file into a base64-encoded string

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
- `undefined`: sheetName - Name of the sheet to read from in the spreadsheet
- `undefined`: fromLine - Start handling records from the requested line number. Starts at 0.
- `undefined`: skipRecordsWithErrors

##### Options (`options`)

Optional values:
- `undefined`: encoding - Specify the encoding of the file, defaults to UTF-8
- `undefined`: stripBOM - Whether to strip the BOM (Byte Order Mark) from the file, this could help in an environment where the presence of the BOM is causing issues or inconsistencies
- `undefined`: keepSource

##### Options (`options`)

Optional values:
- `undefined`: joinPages - Whether to join the text from all pages or return an array of text from each page
- `undefined`: keepSource
- `undefined`: maxPages - Maximum number of pages to include
- `undefined`: password - Prowide password, if the PDF is encrypted

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
  "name": "Extract from File",
  "type": "nodes-base.extractFromFile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "destinationKey": "data",
    "binaryPropertyName": "data"
  }
}
```

#### Extract From CSV Example
```json
{
  "name": "Extract from File",
  "type": "nodes-base.extractFromFile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "destinationKey": "data",
    "binaryPropertyName": "data",
    "operation": "csv"
  }
}
```

#### Extract From HTML Example
```json
{
  "name": "Extract from File",
  "type": "nodes-base.extractFromFile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "destinationKey": "data",
    "binaryPropertyName": "data",
    "operation": "html"
  }
}
```

---

## FileMaker

## Basic Information

- Node Type: `nodes-base.filemaker`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Retrieve data from the FileMaker data API

### Available Operations

### Create Record
- Value: `create`

### Delete Record
- Value: `delete`

### Duplicate Record
- Value: `duplicate`

### Edit Record
- Value: `edit`

### Find Records
- Value: `find`

### Get Records
- Value: `records`

### Get Records By ID
- Value: `record`

### Perform Script
- Value: `performscript`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `layout` | options | Yes | `""` | FileMaker Layout Name. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `recid` | number | Yes | `""` | Internal Record ID returned by get (recordid) |
| `scriptBefore` | options | Yes | `""` | The name of the FileMaker script to be run after the action specified by the API call and after the subsequent sort. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `scriptSort` | options | Yes | `""` | The name of the FileMaker script to be run after the action specified by the API call but before the subsequent sort. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `scriptAfter` | options | Yes | `""` | The name of the FileMaker script to be run after the action specified by the API call and after the subsequent sort. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `script` | options | Yes | `""` | The name of the FileMaker script to be run. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `action` | options | No | `"record"` | - |
| `sortParametersUi` | fixedCollection | No | `{}` | Sort rules |
| `fieldsParametersUi` | fixedCollection | No | `{}` | Fields to define |
| `queries` | fixedCollection | No | `{}` | - |

#### Property Details

##### Action (`action`)

Optional values:
- `create`: Create Record
- `delete`: Delete Record
- `duplicate`: Duplicate Record
- `edit`: Edit Record
- `find`: Find Records
- `records`: Get Records
- `record`: Get Records By ID
- `performscript`: Perform Script

##### Sort (`sortParametersUi`)

Sort rules

Optional values:
- `undefined`: rules

##### Fields (`fieldsParametersUi`)

Fields to define

Optional values:
- `undefined`: fields

##### Queries (`queries`)

Optional values:
- `undefined`: query

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
  "name": "FileMaker",
  "type": "nodes-base.filemaker",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "layout": "",
    "recid": "",
    "scriptBefore": "",
    "scriptSort": "",
    "scriptAfter": "",
    "script": ""
  }
}
```

#### Create Record Example
```json
{
  "name": "FileMaker",
  "type": "nodes-base.filemaker",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "layout": "",
    "recid": "",
    "scriptBefore": "",
    "scriptSort": "",
    "scriptAfter": "",
    "script": "",
    "operation": "create"
  }
}
```

#### Delete Record Example
```json
{
  "name": "FileMaker",
  "type": "nodes-base.filemaker",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "layout": "",
    "recid": "",
    "scriptBefore": "",
    "scriptSort": "",
    "scriptAfter": "",
    "script": "",
    "operation": "delete"
  }
}
```

---

## FTP

## Basic Information

- Node Type: `nodes-base.ftp`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Transfer files via FTP or SFTP

### Available Operations

### Delete
Delete a file/folder
- Value: `delete`

### Download
Download a file
- Value: `download`

### List
List folder content
- Value: `list`

### Rename
Rename/move oldPath to newPath
- Value: `rename`

### Upload
Upload a file
- Value: `upload`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `path` | string | Yes | `""` | The file path of the file to delete. Has to contain the full path. |
| `path` | string | Yes | `""` | The file path of the file to download. Has to contain the full path. |
| `path` | string | Yes | `""` | The file path of the file to upload. Has to contain the full path. |
| `path` | string | Yes | `"/"` | Path of directory to list contents of |
| `recursive` | boolean | Yes | `false` | Whether to return object representing all directories / objects recursively found within SFTP server |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `oldPath` | string | Yes | `""` | - |
| `newPath` | string | Yes | `""` | - |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `operation` | options | No | `"download"` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `delete`: Delete - Delete a file/folder
- `download`: Download - Download a file
- `list`: List - List folder content
- `rename`: Rename - Rename/move oldPath to newPath
- `upload`: Upload - Upload a file

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
  "name": "FTP",
  "type": "nodes-base.ftp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "path": "/",
    "recursive": false,
    "binaryPropertyName": "data",
    "oldPath": "",
    "newPath": ""
  }
}
```

#### Delete Example
```json
{
  "name": "FTP",
  "type": "nodes-base.ftp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "path": "/",
    "recursive": false,
    "binaryPropertyName": "data",
    "oldPath": "",
    "newPath": "",
    "operation": "delete"
  }
}
```

#### Download Example
```json
{
  "name": "FTP",
  "type": "nodes-base.ftp",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "path": "/",
    "recursive": false,
    "binaryPropertyName": "data",
    "oldPath": "",
    "newPath": "",
    "operation": "download"
  }
}
```

---

## GetResponse

## Basic Information

- Node Type: `nodes-base.getResponse`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume GetResponse API

### Available Operations

### Create
Create a new contact
- Value: `create`

### Delete
Delete a contact
- Value: `delete`

### Get
Get a contact
- Value: `get`

### Get Many
Get many contacts
- Value: `getAll`

### Update
Update contact properties
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `contactId` | string | Yes | `""` | ID of contact to delete |
| `contactId` | string | Yes | `""` | Unique identifier for a particular contact |
| `contactId` | string | Yes | `""` | Unique identifier for a particular contact |
| `authentication` | options | No | `"apiKey"` | - |
| `resource` | options | No | `"contact"` | - |
| `operation` | options | No | `"get"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `apiKey`: API Key
- `oAuth2`: OAuth2

##### Resource (`resource`)

Optional values:
- `contact`: Contact

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new contact
- `delete`: Delete - Delete a contact
- `get`: Get - Get a contact
- `getAll`: Get Many - Get many contacts
- `update`: Update - Update contact properties

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: customFieldsUi
- `undefined`: dayOfCycle - The day on which the contact is in the Autoresponder cycle. null indicates the contacts is not in the cycle.
- `undefined`: ipAddress - The contact's IP address. IPv4 and IPv6 formats are accepted.
- `undefined`: name
- `undefined`: note
- `undefined`: scoring - Contact scoring, pass null to remove the score from a contact
- `undefined`: tags - Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>

##### Options (`options`)

Optional values:
- `undefined`: ipAddress - This makes it possible to pass the IP from which the contact unsubscribed. Used only if the messageId was send.
- `undefined`: messageId - The ID of a message (such as a newsletter, an autoresponder, or an RSS-newsletter). When passed, this method will simulate the unsubscribe process, as if the contact clicked the unsubscribe link in a given message.

##### Options (`options`)

Optional values:
- `undefined`: fields - List of fields that should be returned. ID is always returned. Fields should be separated by comma

##### Options (`options`)

Optional values:
- `undefined`: campaignId - Search contacts by campaign ID
- `undefined`: changeOnFrom - Search contacts edited from this date
- `undefined`: changeOnTo - Search contacts edited to this date
- `undefined`: createdOnFrom - Count data from this date
- `undefined`: createdOnTo - Count data from this date
- `undefined`: exactMatch - Whether to search for contacts with the exact value of the email and name provided in the query string. Without this flag, matching is done via a standard 'like' comparison, which may sometimes be slow.
- `undefined`: fields - List of fields that should be returned. ID is always returned. Fields should be separated by comma
- `undefined`: name - Search contacts by name
- `undefined`: origin - Search contacts by origin
- `undefined`: sortBy
- `undefined`: sortOrder

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
  "name": "GetResponse",
  "type": "nodes-base.getResponse",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contactId": ""
  }
}
```

#### Create Example
```json
{
  "name": "GetResponse",
  "type": "nodes-base.getResponse",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contactId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "GetResponse",
  "type": "nodes-base.getResponse",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contactId": "",
    "operation": "delete"
  }
}
```

---

## Ghost

## Basic Information

- Node Type: `nodes-base.ghost`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Ghost API

### Available Operations

### Get
Get a post
- Value: `get`

### Get Many
Get many posts
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `by` | options | Yes | `"id"` | Get the post either by slug or ID |
| `title` | string | Yes | `""` | Post's title |
| `postId` | string | Yes | `""` | The ID of the post to delete |
| `identifier` | string | Yes | `""` | The ID or slug of the post to get |
| `resource` | options | No | `"post"` | - |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"get"` | - |
| `source` | options | No | `"contentApi"` | Pick where your data comes from, Content or Admin API |
| `contentFormat` | options | No | `"html"` | The format of the post |
| `contentFormat` | options | No | `"html"` | The format of the post |

#### Property Details

##### By (`by`)

Get the post either by slug or ID

Optional values:
- `id`: ID
- `slug`: Slug

##### Resource (`resource`)

Optional values:
- `post`: Post

##### Operation (`operation`)

Optional values:
- `get`: Get - Get a post
- `getAll`: Get Many - Get many posts

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a post
- `delete`: Delete - Delete a post
- `get`: Get - Get a post
- `getAll`: Get Many - Get many posts
- `update`: Update - Update a post

##### Source (`source`)

Pick where your data comes from, Content or Admin API

Optional values:
- `adminApi`: Admin API
- `contentApi`: Content API

##### Content Format (`contentFormat`)

The format of the post

Optional values:
- `html`: HTML
- `mobileDoc`: Mobile Doc
- `lexical`: Lexical

##### Content Format (`contentFormat`)

The format of the post

Optional values:
- `html`: HTML
- `mobileDoc`: Mobile Doc
- `lexical`: Lexical

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
  "name": "Ghost",
  "type": "nodes-base.ghost",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "by": "id",
    "title": "",
    "postId": "",
    "identifier": ""
  }
}
```

#### Get Example
```json
{
  "name": "Ghost",
  "type": "nodes-base.ghost",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "by": "id",
    "title": "",
    "postId": "",
    "identifier": "",
    "operation": "get"
  }
}
```

#### Get Many Example
```json
{
  "name": "Ghost",
  "type": "nodes-base.ghost",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "by": "id",
    "title": "",
    "postId": "",
    "identifier": "",
    "operation": "getAll"
  }
}
```

---

## GitLab

## Basic Information

- Node Type: `nodes-base.gitlab`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Retrieve data from GitLab API

### Available Operations

### Create
Create a new issue
- Value: `create`

### Create Comment
Create a new comment on an issue
- Value: `createComment`

### Edit
Edit an issue
- Value: `edit`

### Get
Get the data of a single issue
- Value: `get`

### Lock
Lock an issue
- Value: `lock`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `owner` | string | Yes | `""` | User, group or namespace of the project |
| `repository` | string | Yes | `""` | The name of the project |
| `title` | string | Yes | `""` | The title of the issue |
| `issueNumber` | number | Yes | `0` | The number of the issue on which to create the comment on |
| `issueNumber` | number | Yes | `0` | The number of the issue edit |
| `issueNumber` | number | Yes | `0` | The number of the issue get data of |
| `issueNumber` | number | Yes | `0` | The number of the issue to lock |
| `releaseTag` | string | Yes | `""` | The tag of the release |
| `projectId` | string | Yes | `""` | The ID or URL-encoded path of the project |
| `tag_name` | string | Yes | `""` | The Git tag the release is associated with |

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
  "name": "GitLab",
  "type": "nodes-base.gitlab",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "owner": "",
    "repository": "",
    "title": "",
    "issueNumber": 0,
    "releaseTag": "",
    "projectId": "",
    "tag_name": ""
  }
}
```

#### Create Example
```json
{
  "name": "GitLab",
  "type": "nodes-base.gitlab",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "owner": "",
    "repository": "",
    "title": "",
    "issueNumber": 0,
    "releaseTag": "",
    "projectId": "",
    "tag_name": "",
    "operation": "create"
  }
}
```

#### Create Comment Example
```json
{
  "name": "GitLab",
  "type": "nodes-base.gitlab",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "owner": "",
    "repository": "",
    "title": "",
    "issueNumber": 0,
    "releaseTag": "",
    "projectId": "",
    "tag_name": "",
    "operation": "createComment"
  }
}
```

---

## Google BigQuery

## Basic Information

- Node Type: `nodes-base.googleBigQuery`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Google BigQuery API

### Available Operations

### Execute Query
Execute a SQL query
- Value: `executeQuery`

### Insert
Insert rows in a table
- Value: `insert`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `projectId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Projects to which you have been granted any project role |
| `datasetId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `tableId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `authentication` | options | No | `"oAuth2"` | - |
| `resource` | hidden | No | `"database"` | - |
| `operation` | options | No | `"executeQuery"` | - |
| `dataMode` | options | No | `"autoMap"` | Whether to insert the input data this node receives in the new row |
| `options` | collection | No | `{}` | - |
| `fieldsUi` | fixedCollection | No | `{}` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `oAuth2`: OAuth2 (recommended)
- `serviceAccount`: Service Account

##### Resource (`resource`)

Optional values:
- `database`: Database

##### Operation (`operation`)

Optional values:
- `executeQuery`: Execute Query - Execute a SQL query
- `insert`: Insert - Insert rows in a table

##### Data Mode (`dataMode`)

Whether to insert the input data this node receives in the new row

Optional values:
- `autoMap`: Auto-Map Input Data - Use when node input properties match destination field names
- `define`: Map Each Field Below - Set the value for each destination field

##### Options (`options`)

Optional values:
- `undefined`: defaultDataset - If not set, all table names in the query string must be qualified in the format 'datasetId.tableId'. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: dryRun - Whether set to true BigQuery doesn't run the job. Instead, if the query is valid, BigQuery returns statistics about the job such as how many bytes would be processed. If the query is invalid, an error returns.
- `undefined`: includeSchema - Whether to include the schema in the output. If set to true, the output will contain key '\_schema' with the schema of the table.
- `undefined`: location - Location or the region where data would be stored and processed. Pricing for storage and analysis is also defined by location of data and reservations, more information \<a href="https://cloud.google.com/bigquery/docs/locations" target="\_blank"\>here\</a\>.
- `undefined`: maximumBytesBilled - Limits the bytes billed for this query. Queries with bytes billed above this limit will fail (without incurring a charge). String in \<a href="https://developers.google.com/discovery/v1/type-format?utm\_source=cloud.google.com&utm\_medium=referral" target="\_blank"\>Int64Value\</a\> format
- `undefined`: maxResults - Maximum number of results to return per page of results. This is particularly useful when dealing with large datasets. It will not affect the total number of results returned, e.g. rows in a table. You can use LIMIT in your SQL query to limit the number of rows returned.
- `undefined`: timeoutMs - Specifies the maximum amount of time, in milliseconds, that the client is willing to wait for the query to complete. Be aware that the call is not guaranteed to wait for the specified timeout; it typically returns after around 200 seconds (200,000 milliseconds), even if the query is not complete.
- `undefined`: rawOutput
- `undefined`: useLegacySql - Whether to use BigQuery's legacy SQL dialect for this query. If set to false, the query will use BigQuery's standard SQL.
- `undefined`: returnAsNumbers - Whether all integer values will be returned as numbers. If set to false, all integer values will be returned as strings.
- `undefined`: queryParameters - Use \<a href="https://cloud.google.com/bigquery/docs/parameterized-queries#using\_structs\_in\_parameterized\_queries" target="\_blank"\>parameterized queries\</a\> to prevent SQL injections. Positional arguments are not supported at the moment. This feature won't be available when using legacy SQL.

##### Fields to Send (`fieldsUi`)

Optional values:
- `undefined`: values

##### Options (`options`)

Optional values:
- `undefined`: batchSize
- `undefined`: ignoreUnknownValues - Whether to gnore row values that do not match the schema
- `undefined`: skipInvalidRows - Whether to skip rows with values that do not match the schema
- `undefined`: templateSuffix - Create a new table based on the destination table and insert rows into the new table. The new table will be named \<code\>{destinationTable}{templateSuffix}\</code\>
- `undefined`: traceId - Unique ID for the request, for debugging only. It is case-sensitive, limited to up to 36 ASCII characters. A UUID is recommended.

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
  "name": "Google BigQuery",
  "type": "nodes-base.googleBigQuery",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "projectId": {
      "mode": "list",
      "value": ""
    },
    "datasetId": {
      "mode": "list",
      "value": ""
    },
    "tableId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

#### Execute Query Example
```json
{
  "name": "Google BigQuery",
  "type": "nodes-base.googleBigQuery",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "projectId": {
      "mode": "list",
      "value": ""
    },
    "datasetId": {
      "mode": "list",
      "value": ""
    },
    "tableId": {
      "mode": "list",
      "value": ""
    },
    "operation": "executeQuery"
  }
}
```

#### Insert Example
```json
{
  "name": "Google BigQuery",
  "type": "nodes-base.googleBigQuery",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "projectId": {
      "mode": "list",
      "value": ""
    },
    "datasetId": {
      "mode": "list",
      "value": ""
    },
    "tableId": {
      "mode": "list",
      "value": ""
    },
    "operation": "insert"
  }
}
```

---

## Google Books

## Basic Information

- Node Type: `nodes-base.googleBooks`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Read data from Google Books

### Available Operations

### Get
Retrieve a specific bookshelf resource for the specified user
- Value: `get`

### Get Many
Get many public bookshelf resource for the specified user
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `searchQuery` | string | Yes | `""` | Full-text search query string |
| `userId` | string | Yes | `""` | ID of user |
| `shelfId` | string | Yes | `""` | ID of the bookshelf |
| `shelfId` | string | Yes | `""` | ID of the bookshelf |
| `volumeId` | string | Yes | `""` | ID of the volume |
| `volumePosition` | string | Yes | `""` | Position on shelf to move the item (0 puts the item before the current first item, 1 puts it between the first and the second and so on) |
| `myLibrary` | boolean | Yes | `false` | - |
| `authentication` | options | No | `"serviceAccount"` | - |
| `authentication` | options | No | `"oAuth2"` | - |
| `resource` | options | No | `"bookshelf"` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `serviceAccount`: Service Account
- `oAuth2`: OAuth2

##### Authentication (`authentication`)

Optional values:
- `oAuth2`: OAuth2 (recommended)
- `serviceAccount`: Service Account

##### Resource (`resource`)

Optional values:
- `bookshelf`: Bookshelf
- `bookshelfVolume`: Bookshelf Volume
- `volume`: Volume

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
  "name": "Google Books",
  "type": "nodes-base.googleBooks",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "searchQuery": "",
    "userId": "",
    "shelfId": "",
    "volumeId": "",
    "volumePosition": "",
    "myLibrary": false
  }
}
```

#### Get Example
```json
{
  "name": "Google Books",
  "type": "nodes-base.googleBooks",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "searchQuery": "",
    "userId": "",
    "shelfId": "",
    "volumeId": "",
    "volumePosition": "",
    "myLibrary": false,
    "operation": "get"
  }
}
```

#### Get Many Example
```json
{
  "name": "Google Books",
  "type": "nodes-base.googleBooks",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "searchQuery": "",
    "userId": "",
    "shelfId": "",
    "volumeId": "",
    "volumePosition": "",
    "myLibrary": false,
    "operation": "getAll"
  }
}
```

---

## Google Business Profile

## Basic Information

- Node Type: `nodes-base.googleBusinessProfile`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Google Business Profile API

### Available Operations

### Create
Create a new post on Google Business Profile
- Value: `create`

### Delete
Delete an existing post
- Value: `delete`

### Get
Retrieve details of a specific post
- Value: `get`

### Get Many
Retrieve multiple posts
- Value: `getAll`

### Update
Update an existing post
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `postType` | options | Yes | `"STANDARD"` | The type of post to create (standard, event, offer, or alert) |
| `alertType` | options | Yes | `"COVID_19"` | The sub-type of the alert |
| `account` | resourceLocator | Yes | `{"mode":"list","value":""}` | The Google Business Profile account |
| `location` | resourceLocator | Yes | `{"mode":"list","value":""}` | The specific location or business associated with the account |
| `summary` | string | Yes | `""` | The main text of the post |
| `title` | string | Yes | `""` | E.g. Sales this week. |
| `startDateTime` | dateTime | Yes | `""` | The start date and time of the event |
| `endDateTime` | dateTime | Yes | `""` | The end date and time of the event |
| `title` | string | Yes | `""` | E.g. 20% off in store or online. |
| `startDate` | string | Yes | `""` | The start date of the offer |

#### Property Details

##### Post Type (`postType`)

The type of post to create (standard, event, offer, or alert)

Optional values:
- `STANDARD`: Standard
- `EVENT`: Event
- `OFFER`: Offer
- `ALERT`: Alert

##### Alert Type (`alertType`)

The sub-type of the alert

Optional values:
- `COVID_19`: Covid 19 - This alert is related to the 2019 Coronavirus Disease pandemic

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
  "name": "Google Business Profile",
  "type": "nodes-base.googleBusinessProfile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "postType": "STANDARD",
    "alertType": "COVID_19",
    "account": {
      "mode": "list",
      "value": ""
    },
    "location": {
      "mode": "list",
      "value": ""
    },
    "summary": "",
    "title": "",
    "startDateTime": "",
    "endDateTime": "",
    "startDate": ""
  }
}
```

#### Create Example
```json
{
  "name": "Google Business Profile",
  "type": "nodes-base.googleBusinessProfile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "postType": "STANDARD",
    "alertType": "COVID_19",
    "account": {
      "mode": "list",
      "value": ""
    },
    "location": {
      "mode": "list",
      "value": ""
    },
    "summary": "",
    "title": "",
    "startDateTime": "",
    "endDateTime": "",
    "startDate": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Google Business Profile",
  "type": "nodes-base.googleBusinessProfile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "postType": "STANDARD",
    "alertType": "COVID_19",
    "account": {
      "mode": "list",
      "value": ""
    },
    "location": {
      "mode": "list",
      "value": ""
    },
    "summary": "",
    "title": "",
    "startDateTime": "",
    "endDateTime": "",
    "startDate": "",
    "operation": "delete"
  }
}
```

---

## Google Calendar

## Basic Information

- Node Type: `nodes-base.googleCalendar`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Google Calendar API

### Available Operations

### Availability
If a time-slot is available in a calendar
- Value: `availability`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `calendar` | resourceLocator | Yes | `{"mode":"list","value":""}` | Google Calendar to operate on |
| `timeMin` | dateTime | Yes | `""` | Start of the interval |
| `timeMax` | dateTime | Yes | `""` | End of the interval |
| `timeMin` | dateTime | Yes | `"={{ $now }}"` | Start of the interval, use <a href="https://docs.n8n.io/code/cookbook/luxon/" target="\_blank">expression</a> to set a date, or switch to fixed mode to choose date from widget |
| `timeMax` | dateTime | Yes | `"={{ $now.plus(1, 'hour') }}"` | End of the interval, use <a href="https://docs.n8n.io/code/cookbook/luxon/" target="\_blank">expression</a> to set a date, or switch to fixed mode to choose date from widget |
| `calendar` | resourceLocator | Yes | `{"mode":"list","value":""}` | Google Calendar to operate on |
| `start` | dateTime | Yes | `""` | Start time of the event |
| `end` | dateTime | Yes | `""` | End time of the event |
| `start` | dateTime | Yes | `"={{ $now }}"` | Start time of the event, use <a href="https://docs.n8n.io/code/cookbook/luxon/" target="\_blank">expression</a> to set a date, or switch to fixed mode to choose date from widget |
| `end` | dateTime | Yes | `"={{ $now.plus(1, 'hour') }}"` | End time of the event, use <a href="https://docs.n8n.io/code/cookbook/luxon/" target="\_blank">expression</a> to set a date, or switch to fixed mode to choose date from widget |

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
  "name": "Google Calendar",
  "type": "nodes-base.googleCalendar",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "calendar": {
      "mode": "list",
      "value": ""
    },
    "timeMin": "={{ $now }}",
    "timeMax": "={{ $now.plus(1, 'hour') }}",
    "start": "={{ $now }}",
    "end": "={{ $now.plus(1, 'hour') }}"
  }
}
```

#### Availability Example
```json
{
  "name": "Google Calendar",
  "type": "nodes-base.googleCalendar",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "calendar": {
      "mode": "list",
      "value": ""
    },
    "timeMin": "={{ $now }}",
    "timeMax": "={{ $now.plus(1, 'hour') }}",
    "start": "={{ $now }}",
    "end": "={{ $now.plus(1, 'hour') }}",
    "operation": "availability"
  }
}
```

---

## Google Chat

## Basic Information

- Node Type: `nodes-base.googleChat`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Google Chat API

### Available Operations

### Get
Get a membership
- Value: `get`

### Get Many
Get many memberships in a space
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"message"` | - |
| `messageUi` | collection | Yes | `{}` | - |
| `updateFieldsUi` | collection | Yes | `{}` | - |
| `memberId` | string | Yes | `""` | Member to be retrieved in the form "spaces/\*/members/\*" |
| `spaceId` | options | Yes | `[]` | The name of the space for which to retrieve members, in the form "spaces/\*". Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `spaceId` | options | Yes | `""` | Space resource name, in the form "spaces/\*". Example: spaces/AAAAMpdlehY. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `messageJson` | json | Yes | `""` | Message input as JSON Object or JSON String |
| `messageId` | string | Yes | `""` | Resource name of the message to be deleted, in the form "spaces//messages/" |
| `messageId` | string | Yes | `""` | Resource name of the message to be retrieved, in the form "spaces//messages/" |
| `messageId` | string | Yes | `""` | Resource name of the message to be updated, in the form "spaces//messages/" |

#### Property Details

##### Resource (`resource`)

Optional values:
- `member`: Member
- `message`: Message
- `space`: Space

##### Message (`messageUi`)

Optional values:
- `undefined`: text

##### Update Fields (`updateFieldsUi`)

Optional values:
- `undefined`: text

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
  "name": "Google Chat",
  "type": "nodes-base.googleChat",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "message",
    "messageUi": {},
    "updateFieldsUi": {},
    "memberId": "",
    "spaceId": "",
    "messageJson": "",
    "messageId": ""
  }
}
```

#### Get Example
```json
{
  "name": "Google Chat",
  "type": "nodes-base.googleChat",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "message",
    "messageUi": {},
    "updateFieldsUi": {},
    "memberId": "",
    "spaceId": "",
    "messageJson": "",
    "messageId": "",
    "operation": "get"
  }
}
```

#### Get Many Example
```json
{
  "name": "Google Chat",
  "type": "nodes-base.googleChat",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "message",
    "messageUi": {},
    "updateFieldsUi": {},
    "memberId": "",
    "spaceId": "",
    "messageJson": "",
    "messageId": "",
    "operation": "getAll"
  }
}
```

---

## Google Cloud Firestore

## Basic Information

- Node Type: `nodes-base.googleFirebaseCloudFirestore`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Interact with Google Firebase - Cloud Firestore API

### Available Operations

### Create
Create a document
- Value: `create`

### Create or Update
Create a new document, or update the current one if it already exists (upsert)
- Value: `upsert`

### Delete
Delete a document
- Value: `delete`

### Get
Get a document
- Value: `get`

### Get Many
Get many documents from a collection
- Value: `getAll`

### Query
Runs a query against your documents
- Value: `query`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | JSON query to execute |
| `projectId` | options | Yes | `""` | As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `database` | string | Yes | `"(default)"` | Usually the provided default value will work |
| `collection` | string | Yes | `""` | Collection name |
| `columns` | string | Yes | `""` | List of attributes to save |
| `projectId` | options | Yes | `""` | As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `database` | string | Yes | `"(default)"` | Usually the provided default value will work |
| `collection` | string | Yes | `""` | Collection name |
| `projectId` | options | Yes | `""` | As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `database` | string | Yes | `"(default)"` | Usually the provided default value will work |

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
  "name": "Google Cloud Firestore",
  "type": "nodes-base.googleFirebaseCloudFirestore",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "projectId": "",
    "database": "(default)",
    "collection": "",
    "columns": ""
  }
}
```

#### Create Example
```json
{
  "name": "Google Cloud Firestore",
  "type": "nodes-base.googleFirebaseCloudFirestore",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "projectId": "",
    "database": "(default)",
    "collection": "",
    "columns": "",
    "operation": "create"
  }
}
```

#### Create or Update Example
```json
{
  "name": "Google Cloud Firestore",
  "type": "nodes-base.googleFirebaseCloudFirestore",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "projectId": "",
    "database": "(default)",
    "collection": "",
    "columns": "",
    "operation": "upsert"
  }
}
```

---

## Google Cloud Natural Language

## Basic Information

- Node Type: `nodes-base.googleCloudNaturalLanguage`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Google Cloud Natural Language API

### Available Operations

### Analyze Sentiment
- Value: `analyzeSentiment`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `source` | options | Yes | `"content"` | The source of the document: a string containing the content or a Google Cloud Storage URI |
| `content` | string | Yes | `""` | The content of the input in string format. Cloud audit logging exempt since it is based on user data. |
| `gcsContentUri` | string | Yes | `""` | The Google Cloud Storage URI where the file content is located. This URI must be of the form: <code>gs://bucket\_name/object\_name</code>. For more details, see <a href="https://cloud.google.com/storage/docs/reference-uris.">reference</a>. |
| `resource` | options | No | `"document"` | - |
| `operation` | options | No | `"analyzeSentiment"` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Source (`source`)

The source of the document: a string containing the content or a Google Cloud Storage URI

Optional values:
- `content`: Content
- `gcsContentUri`: Google Cloud Storage URI

##### Resource (`resource`)

Optional values:
- `document`: Document

##### Operation (`operation`)

Optional values:
- `analyzeSentiment`: Analyze Sentiment

##### Options (`options`)

Optional values:
- `undefined`: documentType - The type of input document
- `undefined`: encodingType - The encoding type used by the API to calculate sentence offsets
- `undefined`: language - The language of the document (if not specified, the language is automatically detected). Both ISO and BCP-47 language codes are accepted.

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
  "name": "Google Cloud Natural Language",
  "type": "nodes-base.googleCloudNaturalLanguage",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "source": "content",
    "content": "",
    "gcsContentUri": ""
  }
}
```

#### Analyze Sentiment Example
```json
{
  "name": "Google Cloud Natural Language",
  "type": "nodes-base.googleCloudNaturalLanguage",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "source": "content",
    "content": "",
    "gcsContentUri": "",
    "operation": "analyzeSentiment"
  }
}
```

---

## Google Cloud Realtime Database

## Basic Information

- Node Type: `nodes-base.googleFirebaseRealtimeDatabase`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Interact with Google Firebase - Realtime Database API

### Available Operations

### Create
Write data to a database
- Value: `create`

### Delete
Delete data from a database
- Value: `delete`

### Get
Get a record from a database
- Value: `get`

### Push
Append to a list of data
- Value: `push`

### Update
Update item on a database
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `operation` | options | Yes | `"create"` | - |
| `path` | string | Yes | `""` | Object path on database. Do not append .json. |
| `projectId` | options | Yes | `""` | As displayed in firebase console URL. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `attributes` | string | Yes | `""` | Attributes to save |
| `path` | string | No | `""` | Object path on database. Do not append .json. |

#### Property Details

##### Operation (`operation`)

Optional values:
- `create`: Create - Write data to a database
- `delete`: Delete - Delete data from a database
- `get`: Get - Get a record from a database
- `push`: Push - Append to a list of data
- `update`: Update - Update item on a database

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
  "name": "Google Cloud Realtime Database",
  "type": "nodes-base.googleFirebaseRealtimeDatabase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "create",
    "path": "",
    "projectId": "",
    "attributes": ""
  }
}
```

#### Create Example
```json
{
  "name": "Google Cloud Realtime Database",
  "type": "nodes-base.googleFirebaseRealtimeDatabase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "create",
    "path": "",
    "projectId": "",
    "attributes": ""
  }
}
```

#### Delete Example
```json
{
  "name": "Google Cloud Realtime Database",
  "type": "nodes-base.googleFirebaseRealtimeDatabase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "delete",
    "path": "",
    "projectId": "",
    "attributes": ""
  }
}
```

---

## Google Contacts

## Basic Information

- Node Type: `nodes-base.googleContacts`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Google Contacts API

### Available Operations

### Create
Create a contact
- Value: `create`

### Delete
Delete a contact
- Value: `delete`

### Get
Get a contact
- Value: `get`

### Get Many
Retrieve many contacts
- Value: `getAll`

### Update
Update a contact
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `contactId` | string | Yes | `""` | - |
| `contactId` | string | Yes | `""` | - |
| `contactId` | string | Yes | `""` | - |
| `resource` | options | No | `"contact"` | - |
| `operation` | options | No | `"create"` | - |
| `query` | string | No | `""` | The plain-text query for the request. The query is used to match prefix phrases of the fields on a person. For example, a person with name "foo name" matches queries such as "f", "fo", "foo", "foo n", "nam", etc., but not "oo n". |
| `fields` | multiOptions | No | `[]` | A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. |
| `fields` | multiOptions | No | `[]` | A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. |
| `fields` | multiOptions | No | `[]` | A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. |
| `additionalFields` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `contact`: Contact

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a contact
- `delete`: Delete - Delete a contact
- `get`: Get - Get a contact
- `getAll`: Get Many - Retrieve many contacts
- `update`: Update - Update a contact

##### Fields (`fields`)

A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas.

Optional values:
- `*`: *
- `addresses`: Addresses
- `biographies`: Biographies
- `birthdays`: Birthdays
- `coverPhotos`: Cover Photos
- `emailAddresses`: Email Addresses
- `events`: Events
- `genders`: Genders
- `imClients`: IM Clients
- `interests`: Interests
- `locales`: Locales
- `memberships`: Memberships
- `metadata`: Metadata
- `names`: Names
- `nicknames`: Nicknames
- `occupations`: Occupations
- `organizations`: Organizations
- `phoneNumbers`: Phone Numbers
- `photos`: Photos
- `relations`: Relations
- `residences`: Residences
- `sipAddresses`: Sip Addresses
- `skills`: Skills
- `urls`: URLs
- `userDefined`: User Defined

##### Fields (`fields`)

A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas.

Optional values:
- `*`: *
- `addresses`: Addresses
- `biographies`: Biographies
- `birthdays`: Birthdays
- `coverPhotos`: Cover Photos
- `emailAddresses`: Email Addresses
- `events`: Events
- `genders`: Genders
- `imClients`: IM Clients
- `interests`: Interests
- `locales`: Locales
- `memberships`: Memberships
- `metadata`: Metadata
- `names`: Names
- `nicknames`: Nicknames
- `occupations`: Occupations
- `organizations`: Organizations
- `phoneNumbers`: Phone Numbers
- `photos`: Photos
- `relations`: Relations
- `residences`: Residences
- `sipAddresses`: Sip Addresses
- `skills`: Skills
- `urls`: URLs
- `userDefined`: User Defined

##### Fields (`fields`)

A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas.

Optional values:
- `*`: *
- `addresses`: Addresses
- `biographies`: Biographies
- `birthdays`: Birthdays
- `coverPhotos`: Cover Photos
- `emailAddresses`: Email Addresses
- `events`: Events
- `genders`: Genders
- `imClients`: IM Clients
- `interests`: Interests
- `locales`: Locales
- `memberships`: Memberships
- `metadata`: Metadata
- `names`: Names
- `nicknames`: Nicknames
- `occupations`: Occupations
- `organizations`: Organizations
- `phoneNumbers`: Phone Numbers
- `photos`: Photos
- `relations`: Relations
- `residences`: Residences
- `sipAddresses`: Sip Addresses
- `skills`: Skills
- `urls`: URLs
- `userDefined`: User Defined

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: addressesUi
- `undefined`: birthday
- `undefined`: companyUi
- `undefined`: customFieldsUi
- `undefined`: emailsUi
- `undefined`: eventsUi - An event related to the person
- `undefined`: fileAs - The name that should be used to sort the person in a list
- `undefined`: group - Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: honorificPrefix
- `undefined`: honorificSuffix
- `undefined`: middleName
- `undefined`: biographies
- `undefined`: phoneUi
- `undefined`: relationsUi

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
  "name": "Google Contacts",
  "type": "nodes-base.googleContacts",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contactId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Google Contacts",
  "type": "nodes-base.googleContacts",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contactId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Google Contacts",
  "type": "nodes-base.googleContacts",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contactId": "",
    "operation": "delete"
  }
}
```

---

## Google Docs

## Basic Information

- Node Type: `nodes-base.googleDocs`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Google Docs API.

### Available Operations

### Create
- Value: `create`

### Get
- Value: `get`

### Update
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `driveId` | options | Yes | `"myDrive"` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `folderId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `documentURL` | string | Yes | `""` | The ID in the document URL (or just paste the whole URL) |
| `documentURL` | string | Yes | `""` | The ID in the document URL (or just paste the whole URL) |
| `title` | string | Yes | `""` | - |
| `authentication` | options | No | `"serviceAccount"` | - |
| `authentication` | options | No | `"oAuth2"` | - |
| `resource` | options | No | `"document"` | - |
| `operation` | options | No | `"create"` | - |
| `actionsUi` | fixedCollection | No | `{"actionFields":[{"object":"text","action":"insert","locationChoice":"endOfSegmentLocation","index":0,"text":""}]}` | Actions applied to update the document |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `serviceAccount`: Service Account
- `oAuth2`: OAuth2

##### Authentication (`authentication`)

Optional values:
- `oAuth2`: OAuth2 (recommended)
- `serviceAccount`: Service Account

##### Resource (`resource`)

Optional values:
- `document`: Document

##### Operation (`operation`)

Optional values:
- `create`: Create
- `get`: Get
- `update`: Update

##### Actions (`actionsUi`)

Actions applied to update the document

Optional values:
- `undefined`: actionFields

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
  "name": "Google Docs",
  "type": "nodes-base.googleDocs",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "driveId": "myDrive",
    "folderId": "",
    "documentURL": "",
    "title": ""
  }
}
```

#### Create Example
```json
{
  "name": "Google Docs",
  "type": "nodes-base.googleDocs",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "driveId": "myDrive",
    "folderId": "",
    "documentURL": "",
    "title": "",
    "operation": "create"
  }
}
```

#### Get Example
```json
{
  "name": "Google Docs",
  "type": "nodes-base.googleDocs",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "driveId": "myDrive",
    "folderId": "",
    "documentURL": "",
    "title": "",
    "operation": "get"
  }
}
```

---

## Google Slides

## Basic Information

- Node Type: `nodes-base.googleSlides`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Google Slides API

### Available Operations

### Create
Create a presentation
- Value: `create`

### Get
Get a presentation
- Value: `get`

### Get Slides
Get presentation slides
- Value: `getSlides`

### Replace Text
Replace text in a presentation
- Value: `replaceText`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `title` | string | Yes | `""` | Title of the presentation to create |
| `presentationId` | string | Yes | `""` | ID of the presentation to retrieve. Found in the presentation URL: <code>https://docs.google.com/presentation/d/PRESENTATION\_ID/edit</code> |
| `pageObjectId` | string | Yes | `""` | ID of the page object to retrieve |
| `binaryProperty` | string | Yes | `"data"` | - |
| `authentication` | options | No | `"serviceAccount"` | - |
| `authentication` | options | No | `"oAuth2"` | - |
| `resource` | options | No | `"presentation"` | - |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"get"` | - |
| `textUi` | fixedCollection | No | `{}` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `oAuth2`: OAuth2
- `serviceAccount`: Service Account

##### Authentication (`authentication`)

Optional values:
- `oAuth2`: OAuth2 (recommended)
- `serviceAccount`: Service Account

##### Resource (`resource`)

Optional values:
- `page`: Page
- `presentation`: Presentation

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a presentation
- `get`: Get - Get a presentation
- `getSlides`: Get Slides - Get presentation slides
- `replaceText`: Replace Text - Replace text in a presentation

##### Operation (`operation`)

Optional values:
- `get`: Get - Get a page
- `getThumbnail`: Get Thumbnail - Get a thumbnail

##### Texts To Replace (`textUi`)

Optional values:
- `undefined`: textValues

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
  "name": "Google Slides",
  "type": "nodes-base.googleSlides",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "presentationId": "",
    "pageObjectId": "",
    "binaryProperty": "data"
  }
}
```

#### Create Example
```json
{
  "name": "Google Slides",
  "type": "nodes-base.googleSlides",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "presentationId": "",
    "pageObjectId": "",
    "binaryProperty": "data",
    "operation": "create"
  }
}
```

#### Get Example
```json
{
  "name": "Google Slides",
  "type": "nodes-base.googleSlides",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "title": "",
    "presentationId": "",
    "pageObjectId": "",
    "binaryProperty": "data",
    "operation": "get"
  }
}
```

---

## Google Tasks

## Basic Information

- Node Type: `nodes-base.googleTasks`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Google Tasks API

### Available Operations

### Create
Add a task to tasklist
- Value: `create`

### Delete
Delete a task
- Value: `delete`

### Get
Retrieve a task
- Value: `get`

### Get Many
Retrieve many tasks from a tasklist
- Value: `getAll`

### Update
Update a task
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `task` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `task` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `task` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `task` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `task` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `taskId` | string | Yes | `""` | - |
| `taskId` | string | Yes | `""` | - |
| `taskId` | string | Yes | `""` | - |
| `resource` | options | No | `"task"` | - |
| `operation` | options | No | `"create"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `task`: Task

##### Operation (`operation`)

Optional values:
- `create`: Create - Add a task to tasklist
- `delete`: Delete - Delete a task
- `get`: Get - Retrieve a task
- `getAll`: Get Many - Retrieve many tasks from a tasklist
- `update`: Update - Update a task

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
  "name": "Google Tasks",
  "type": "nodes-base.googleTasks",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "task": "",
    "taskId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Google Tasks",
  "type": "nodes-base.googleTasks",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "task": "",
    "taskId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Google Tasks",
  "type": "nodes-base.googleTasks",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "task": "",
    "taskId": "",
    "operation": "delete"
  }
}
```

---

## Google Translate

## Basic Information

- Node Type: `nodes-base.googleTranslate`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Translate data using Google Translate

### Available Operations

### Translate
Translate data
- Value: `translate`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `text` | string | Yes | `""` | The input text to translate |
| `translateTo` | options | Yes | `""` | The language to use for translation of the input text, set to one of the language codes listed in <a href="https://cloud.google.com/translate/docs/languages">Language Support</a>. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `authentication` | options | No | `"serviceAccount"` | - |
| `authentication` | options | No | `"oAuth2"` | - |
| `resource` | options | No | `"language"` | - |
| `operation` | options | No | `"translate"` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `serviceAccount`: Service Account
- `oAuth2`: OAuth2

##### Authentication (`authentication`)

Optional values:
- `oAuth2`: OAuth2 (recommended)
- `serviceAccount`: Service Account

##### Resource (`resource`)

Optional values:
- `language`: Language

##### Operation (`operation`)

Optional values:
- `translate`: Translate - Translate data

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
  "name": "Google Translate",
  "type": "nodes-base.googleTranslate",
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
  "name": "Google Translate",
  "type": "nodes-base.googleTranslate",
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

## Google Workspace Admin

## Basic Information

- Node Type: `nodes-base.gSuiteAdmin`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Google Workspace Admin API

### Available Operations

### Get
Get a ChromeOS device
- Value: `get`

### Get Many
Get many ChromeOS devices
- Value: `getAll`

### Update
Update a ChromeOS device
- Value: `update`

### Change Status
Change the status of a ChromeOS device
- Value: `changeStatus`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `action` | options | Yes | `"reenable"` | Set the status of a device |
| `projection` | options | Yes | `"basic"` | What subset of fields to fetch for this device |
| `projection` | options | Yes | `"basic"` | What subset of fields to fetch for this user |
| `projection` | options | Yes | `"basic"` | What subset of fields to fetch for this user |
| `output` | options | Yes | `"simplified"` | - |
| `output` | options | Yes | `"simplified"` | - |
| `deviceId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the device you want to retrieve |
| `groupId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the group to perform the operation on |
| `email` | string | Yes | `""` | The group's email address. If your account has multiple domains, select the appropriate domain for the email address. The email must be unique |
| `userId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the user to perform the operation on |

#### Property Details

##### Status (`action`)

Set the status of a device

Optional values:
- `reenable`: Enabled - Re-enable a disabled chromebook
- `disable`: Disabled - Disable a chromebook

##### Output (`projection`)

What subset of fields to fetch for this device

Optional values:
- `basic`: Basic - Do not include any custom fields for the user
- `full`: Full - Include all fields associated with this user

##### Custom Fields (`projection`)

What subset of fields to fetch for this user

Optional values:
- `basic`: Don't Include - Do not include any custom fields for the user
- `custom`: Custom - Include custom fields from schemas requested in Custom Schema Names or IDs
- `full`: Include All - Include all fields associated with this user

##### Custom Fields (`projection`)

What subset of fields to fetch for this user

Optional values:
- `basic`: Don't Include - Do not include any custom fields for the user
- `custom`: Custom - Include custom fields from schemas requested in Custom Schema Names or IDs
- `full`: Include All - Include all fields associated with this user

##### Output (`output`)

Optional values:
- `simplified`: Simplified - Only return specific fields: kind, ID, primaryEmail, name (with subfields), isAdmin, lastLoginTime, creationTime, and suspended
- `raw`: Raw - Return all fields from the API response
- `select`: Select Included Fields - Choose specific fields to include

##### Output (`output`)

Optional values:
- `simplified`: Simplified - Only return specific fields: kind, ID, primaryEmail, name (with subfields), isAdmin, lastLoginTime, creationTime, and suspended
- `raw`: Raw - Return all fields from the API response
- `select`: Select Included Fields - Choose specific fields to include

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
  "name": "Google Workspace Admin",
  "type": "nodes-base.gSuiteAdmin",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "action": "reenable",
    "projection": "basic",
    "output": "simplified",
    "deviceId": {
      "mode": "list",
      "value": ""
    },
    "groupId": {
      "mode": "list",
      "value": ""
    },
    "email": "",
    "userId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

#### Get Example
```json
{
  "name": "Google Workspace Admin",
  "type": "nodes-base.gSuiteAdmin",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "action": "reenable",
    "projection": "basic",
    "output": "simplified",
    "deviceId": {
      "mode": "list",
      "value": ""
    },
    "groupId": {
      "mode": "list",
      "value": ""
    },
    "email": "",
    "userId": {
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
  "name": "Google Workspace Admin",
  "type": "nodes-base.gSuiteAdmin",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "action": "reenable",
    "projection": "basic",
    "output": "simplified",
    "deviceId": {
      "mode": "list",
      "value": ""
    },
    "groupId": {
      "mode": "list",
      "value": ""
    },
    "email": "",
    "userId": {
      "mode": "list",
      "value": ""
    },
    "operation": "getAll"
  }
}
```

---

## Gotify

## Basic Information

- Node Type: `nodes-base.gotify`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Gotify API

### Available Operations

### Create
- Value: `create`

### Delete
- Value: `delete`

### Get Many
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `message` | string | Yes | `""` | The message to send, If using Markdown add the Content Type option |
| `messageId` | string | Yes | `""` | - |
| `resource` | options | No | `"message"` | - |
| `operation` | options | No | `"create"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `20` | Max number of results to return |

#### Property Details

##### Resource (`resource`)

Optional values:
- `message`: Message

##### Operation (`operation`)

Optional values:
- `create`: Create
- `delete`: Delete
- `getAll`: Get Many

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: priority - The priority of the message
- `undefined`: title - The title of the message

##### Options (`options`)

Optional values:
- `undefined`: contentType - The message content type

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
  "name": "Gotify",
  "type": "nodes-base.gotify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "message": "",
    "messageId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Gotify",
  "type": "nodes-base.gotify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "message": "",
    "messageId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Gotify",
  "type": "nodes-base.gotify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "message": "",
    "messageId": "",
    "operation": "delete"
  }
}
```

---

## GraphQL

## Basic Information

- Node Type: `nodes-base.graphql`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Makes a GraphQL request and returns the received data

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | GraphQL query |
| `requestFormat` | options | Yes | `"graphql"` | The format for the query payload |
| `requestFormat` | options | Yes | `"json"` | The request format for the query payload |
| `endpoint` | string | Yes | `""` | The GraphQL endpoint |
| `dataPropertyName` | string | Yes | `"data"` | Name of the property to which to write the response data |
| `authentication` | options | No | `"none"` | The way to authenticate |
| `requestMethod` | options | No | `"POST"` | The underlying HTTP request method to use |
| `responseFormat` | options | No | `"json"` | The format in which the data gets returned from the URL |
| `headerParametersUi` | fixedCollection | No | `{}` | The headers to send |
| `allowUnauthorizedCerts` | boolean | No | `false` | Whether to download the response even if SSL certificate validation is not possible |

#### Property Details

##### Request Format (`requestFormat`)

The format for the query payload

Optional values:
- `graphql`: GraphQL (Raw)
- `json`: JSON

##### Request Format (`requestFormat`)

The request format for the query payload

Optional values:
- `json`: JSON (Recommended) - JSON object with query, variables, and operationName properties. The standard and most widely supported format for GraphQL requests.
- `graphql`: GraphQL (Raw) - Raw GraphQL query string. Not all servers support this format. Use JSON for better compatibility.

##### Authentication (`authentication`)

The way to authenticate

Optional values:
- `basicAuth`: Basic Auth
- `customAuth`: Custom Auth
- `digestAuth`: Digest Auth
- `headerAuth`: Header Auth
- `none`: None
- `oAuth1`: OAuth1
- `oAuth2`: OAuth2
- `queryAuth`: Query Auth

##### HTTP Request Method (`requestMethod`)

The underlying HTTP request method to use

Optional values:
- `GET`: GET
- `POST`: POST

##### Response Format (`responseFormat`)

The format in which the data gets returned from the URL

Optional values:
- `json`: JSON
- `string`: String

##### Headers (`headerParametersUi`)

The headers to send

Optional values:
- `undefined`: parameter

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
  "name": "GraphQL",
  "type": "nodes-base.graphql",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "requestFormat": "json",
    "endpoint": "",
    "dataPropertyName": "data"
  }
}
```

---

## Grist

## Basic Information

- Node Type: `nodes-base.grist`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Grist API

### Available Operations

### Create Row
Create rows in a table
- Value: `create`

### Delete Row
Delete rows from a table
- Value: `delete`

### Get Many Rows
Read rows from a table
- Value: `getAll`

### Update Row
Update rows in a table
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `docId` | string | Yes | `""` | In your document, click your profile icon, then Document Settings, then copy the value under "This document's ID" |
| `tableId` | string | Yes | `""` | ID of table to operate on. If unsure, look at the Code View. |
| `rowId` | string | Yes | `""` | ID of the row to delete, or comma-separated list of row IDs to delete |
| `rowId` | string | Yes | `""` | ID of the row to update |
| `operation` | options | No | `"getAll"` | - |
| `dataToSend` | options | No | `"defineInNode"` | Whether to insert the input data this node receives in the new row |
| `additionalOptions` | collection | No | `{}` | - |
| `fieldsToSend` | fixedCollection | No | `{}` | - |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `50` | Max number of results to return |

#### Property Details

##### Operation (`operation`)

Optional values:
- `create`: Create Row - Create rows in a table
- `delete`: Delete Row - Delete rows from a table
- `getAll`: Get Many Rows - Read rows from a table
- `update`: Update Row - Update rows in a table

##### Data to Send (`dataToSend`)

Whether to insert the input data this node receives in the new row

Optional values:
- `autoMapInputs`: Auto-Map Input Data to Columns - Use when node input properties match destination column names
- `defineInNode`: Define Below for Each Column - Set the value for each destination column

##### Additional Options (`additionalOptions`)

Optional values:
- `undefined`: filter - Only return rows matching all of the given filters. For complex filters, create a formula column and filter for the value "true".
- `undefined`: sort

##### Fields to Send (`fieldsToSend`)

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
  "name": "Grist",
  "type": "nodes-base.grist",
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
  "name": "Grist",
  "type": "nodes-base.grist",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "docId": "",
    "tableId": "",
    "rowId": "",
    "operation": "create"
  }
}
```

#### Delete Row Example
```json
{
  "name": "Grist",
  "type": "nodes-base.grist",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "docId": "",
    "tableId": "",
    "rowId": "",
    "operation": "delete"
  }
}
```

---

## HaloPSA

## Basic Information

- Node Type: `nodes-base.haloPSA`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume HaloPSA API

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
| `resource` | options | Yes | `"client"` | - |
| `clientName` | string | Yes | `""` | Enter client name |
| `ticketType` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `siteName` | string | Yes | `""` | Enter site name |
| `clientId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `userName` | string | Yes | `""` | Enter user name |
| `siteId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `clientId` | string | Yes | `""` | - |
| `clientId` | string | Yes | `""` | - |
| `summary` | string | Yes | `""` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `client`: Client
- `site`: Site
- `ticket`: Ticket
- `user`: User

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
  "name": "HaloPSA",
  "type": "nodes-base.haloPSA",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "client",
    "clientName": "",
    "ticketType": "",
    "siteName": "",
    "clientId": "",
    "userName": "",
    "siteId": "",
    "summary": ""
  }
}
```

#### Create Example
```json
{
  "name": "HaloPSA",
  "type": "nodes-base.haloPSA",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "client",
    "clientName": "",
    "ticketType": "",
    "siteName": "",
    "clientId": "",
    "userName": "",
    "siteId": "",
    "summary": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "HaloPSA",
  "type": "nodes-base.haloPSA",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "client",
    "clientName": "",
    "ticketType": "",
    "siteName": "",
    "clientId": "",
    "userName": "",
    "siteId": "",
    "summary": "",
    "operation": "delete"
  }
}
```

---

## Harvest

## Basic Information

- Node Type: `nodes-base.harvest`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Access data on Harvest

### Available Operations

### Create
Create a client
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

### Update
Update a client
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `billBy` | options | Yes | `"none"` | The method by which the project is invoiced |
| `accountId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `id` | string | Yes | `""` | The ID of the client you are retrieving |
| `id` | string | Yes | `""` | The ID of the client you want to delete |
| `name` | string | Yes | `""` | The name of the client |
| `id` | string | Yes | `""` | The ID of the client want to update |
| `id` | string | Yes | `""` | The ID of the contact you are retrieving |
| `id` | string | Yes | `""` | The ID of the contact you want to delete |
| `firstName` | string | Yes | `""` | The first name of the contact |
| `clientId` | string | Yes | `""` | The ID of the client associated with this contact |

#### Property Details

##### Bill By (`billBy`)

The method by which the project is invoiced

Optional values:
- `none`: None
- `People`: People
- `Project`: Project
- `Tasks`: Tasks

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
  "name": "Harvest",
  "type": "nodes-base.harvest",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "billBy": "none",
    "accountId": "",
    "id": "",
    "name": "",
    "firstName": "",
    "clientId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Harvest",
  "type": "nodes-base.harvest",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "billBy": "none",
    "accountId": "",
    "id": "",
    "name": "",
    "firstName": "",
    "clientId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Harvest",
  "type": "nodes-base.harvest",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "billBy": "none",
    "accountId": "",
    "id": "",
    "name": "",
    "firstName": "",
    "clientId": "",
    "operation": "delete"
  }
}
```

---

## Help Scout

## Basic Information

- Node Type: `nodes-base.helpScout`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Help Scout API

### Available Operations

### Create
Create a new conversation
- Value: `create`

### Delete
Delete a conversation
- Value: `delete`

### Get
Get a conversation
- Value: `get`

### Get Many
Get many conversations
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `status` | options | Yes | `""` | Conversation status |
| `type` | options | Yes | `""` | Conversation type |
| `type` | options | Yes | `""` | - |
| `mailboxId` | options | Yes | `""` | ID of a mailbox where the conversation is being created. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `subject` | string | Yes | `""` | Conversation’s subject |
| `text` | string | Yes | `""` | The chat text |
| `conversationId` | string | Yes | `""` | - |
| `conversationId` | string | Yes | `""` | - |
| `customerId` | string | Yes | `""` | - |
| `mailboxId` | string | Yes | `""` | - |

#### Property Details

##### Status (`status`)

Conversation status

Optional values:
- `active`: Active
- `closed`: Closed
- `pending`: Pending

##### Type (`type`)

Conversation type

Optional values:
- `chat`: Chat
- `email`: Email
- `phone`: Phone

##### Type (`type`)

Optional values:
- `chat`: Chat
- `customer`: Customer
- `note`: Note
- `phone`: Phone
- `reply`: Reply

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
  "name": "Help Scout",
  "type": "nodes-base.helpScout",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "status": "",
    "type": "",
    "mailboxId": "",
    "subject": "",
    "text": "",
    "conversationId": "",
    "customerId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Help Scout",
  "type": "nodes-base.helpScout",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "status": "",
    "type": "",
    "mailboxId": "",
    "subject": "",
    "text": "",
    "conversationId": "",
    "customerId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Help Scout",
  "type": "nodes-base.helpScout",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "status": "",
    "type": "",
    "mailboxId": "",
    "subject": "",
    "text": "",
    "conversationId": "",
    "customerId": "",
    "operation": "delete"
  }
}
```

---

## iCalendar

## Basic Information

- Node Type: `nodes-base.iCal`
- Category: input
- Package: n8n-nodes-base

### Description

Create iCalendar file

### Available Operations

### Create Event File
- Value: `createEventFile`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `start` | dateTime | Yes | `""` | Date and time at which the event begins. (For all-day events, the time will be ignored.). |
| `end` | dateTime | Yes | `""` | Date and time at which the event ends. (For all-day events, the time will be ignored.). |
| `binaryPropertyName` | string | Yes | `"data"` | The field that your iCalendar file will be available under in the output |
| `operation` | options | No | `"createEventFile"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `allDay` | boolean | No | `false` | Whether the event lasts all day or not |
| `title` | string | No | `""` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `createEventFile`: Create Event File

##### Options (`additionalFields`)

Optional values:
- `undefined`: attendeesUi
- `undefined`: busyStatus - Used to specify busy status for Microsoft applications, like Outlook
- `undefined`: calName - Specifies the calendar (not event) name. Used by Apple iCal and Microsoft Outlook. \<a href="https://docs.microsoft.com/en-us/openspecs/exchange\_server\_protocols/ms-oxcical/1da58449-b97e-46bd-b018-a1ce576f3e6d"\>More info\</a\>.
- `undefined`: description
- `undefined`: fileName - The name of the file to be generated. Default name is event.ics.
- `undefined`: geolocationUi
- `undefined`: location - The intended venue
- `undefined`: recurrenceRule - A rule to define the repeat pattern of the event (RRULE). (\<a href="https://icalendar.org/rrule-tool.html"\>Rule generator\</a\>).
- `undefined`: organizerUi
- `undefined`: sequence - When sending an update for an event (with the same uid), defines the revision sequence number
- `undefined`: status
- `undefined`: uid - Universally unique ID for the event (will be auto-generated if not specified here). Should be globally unique.
- `undefined`: url - URL associated with event
- `undefined`: useWorkflowTimezone - Whether to use the workflow timezone set in node's settings rather than UTC

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
  "name": "iCalendar",
  "type": "nodes-base.iCal",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "start": "",
    "end": "",
    "binaryPropertyName": "data"
  }
}
```

#### Create Event File Example
```json
{
  "name": "iCalendar",
  "type": "nodes-base.iCal",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "start": "",
    "end": "",
    "binaryPropertyName": "data",
    "operation": "createEventFile"
  }
}
```

---

## Item Lists

## Basic Information

- Node Type: `nodes-base.itemLists`
- Category: input
- Package: n8n-nodes-base

### Description

Helper for working with lists of items and transforming arrays

### Available Operations

### Concatenate Items
Combine fields into a list in a single new item
- Value: `concatenateItems`

### Limit
Remove items if there are too many
- Value: `limit`

### Remove Duplicates
Remove extra items that are similar
- Value: `removeDuplicates`

### Sort
Change the item order
- Value: `sort`

### Split Out Items
Turn a list or values of object's properties inside item(s) into separate items
- Value: `splitOutItems`

### Summarize
Aggregate items together (pivot table)
- Value: `summarize`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `fieldToSplitOut` | string | Yes | `""` | The name of the input fields to break out into separate items. Separate multiple field names by commas. For binary data, use $binary. |
| `resource` | hidden | No | `"itemList"` | - |
| `operation` | options | No | `"splitOutItems"` | - |
| `keep` | options | No | `"firstItems"` | When removing items, whether to keep the ones at the start or the ending |
| `compare` | options | No | `"allFields"` | The fields of the input items to compare to see if they are the same |
| `type` | options | No | `"simple"` | The fields of the input items to compare to see if they are the same |
| `sortFieldsUi` | fixedCollection | No | `{}` | The fields of the input items to compare to see if they are the same |
| `include` | options | No | `"noOtherFields"` | Whether to copy any other fields into the new items |
| `aggregate` | options | No | `"aggregateIndividualFields"` | - |
| `fieldsToAggregate` | fixedCollection | No | `{"fieldToAggregate":[{"fieldToAggregate":"","renameField":false}]}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `itemList`: Item List

##### Operation (`operation`)

Optional values:
- `concatenateItems`: Concatenate Items - Combine fields into a list in a single new item
- `limit`: Limit - Remove items if there are too many
- `removeDuplicates`: Remove Duplicates - Remove extra items that are similar
- `sort`: Sort - Change the item order
- `splitOutItems`: Split Out Items - Turn a list or values of object's properties inside item(s) into separate items
- `summarize`: Summarize - Aggregate items together (pivot table)

##### Keep (`keep`)

When removing items, whether to keep the ones at the start or the ending

Optional values:
- `firstItems`: First Items
- `lastItems`: Last Items

##### Compare (`compare`)

The fields of the input items to compare to see if they are the same

Optional values:
- `allFields`: All Fields
- `allFieldsExcept`: All Fields Except
- `selectedFields`: Selected Fields

##### Type (`type`)

The fields of the input items to compare to see if they are the same

Optional values:
- `simple`: Simple
- `random`: Random
- `code`: Code

##### Fields To Sort By (`sortFieldsUi`)

The fields of the input items to compare to see if they are the same

Optional values:
- `undefined`: sortField

##### Include (`include`)

Whether to copy any other fields into the new items

Optional values:
- `noOtherFields`: No Other Fields
- `allOtherFields`: All Other Fields
- `selectedOtherFields`: Selected Other Fields

##### Aggregate (`aggregate`)

Optional values:
- `aggregateIndividualFields`: Individual Fields
- `aggregateAllItemData`: All Item Data (Into a Single List)

##### Fields To Aggregate (`fieldsToAggregate`)

Optional values:
- `undefined`: fieldToAggregate

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
  "name": "Item Lists",
  "type": "nodes-base.itemLists",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fieldToSplitOut": ""
  }
}
```

#### Concatenate Items Example
```json
{
  "name": "Item Lists",
  "type": "nodes-base.itemLists",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fieldToSplitOut": "",
    "operation": "concatenateItems"
  }
}
```

#### Limit Example
```json
{
  "name": "Item Lists",
  "type": "nodes-base.itemLists",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fieldToSplitOut": "",
    "operation": "limit"
  }
}
```

---

## Iterable

## Basic Information

- Node Type: `nodes-base.iterable`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Iterable API

### Available Operations

### Track
Record the actions a user perform
- Value: `track`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `value` | string | Yes | `""` | - |
| `value` | string | Yes | `""` | - |
| `value` | string | Yes | `""` | - |
| `identifier` | options | Yes | `""` | Identifier to be used |
| `by` | options | Yes | `"email"` | Identifier to be used |
| `by` | options | Yes | `"email"` | Identifier to be used |
| `identifier` | options | Yes | `""` | Identifier to be used |
| `identifier` | options | Yes | `""` | Identifier to be used |
| `name` | string | Yes | `""` | The name of the event to track |
| `preferUserId` | boolean | Yes | `true` | Whether to create a new user if the idetifier does not exist |

#### Property Details

##### Identifier (`identifier`)

Identifier to be used

Optional values:
- `email`: Email
- `userId`: User ID

##### By (`by`)

Identifier to be used

Optional values:
- `email`: Email
- `userId`: User ID

##### By (`by`)

Identifier to be used

Optional values:
- `email`: Email
- `userId`: User ID

##### Identifier (`identifier`)

Identifier to be used

Optional values:
- `email`: Email
- `userId`: User ID

##### Identifier (`identifier`)

Identifier to be used

Optional values:
- `email`: Email
- `userId`: User ID

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
  "name": "Iterable",
  "type": "nodes-base.iterable",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "identifier": "",
    "by": "email",
    "name": "",
    "preferUserId": true
  }
}
```

#### Track Example
```json
{
  "name": "Iterable",
  "type": "nodes-base.iterable",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "value": "",
    "identifier": "",
    "by": "email",
    "name": "",
    "preferUserId": true,
    "operation": "track"
  }
}
```

---

## Keap

## Basic Information

- Node Type: `nodes-base.keap`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Keap API

### Available Operations

### Create
Create a company
- Value: `create`

### Get Many
Retrieve many companies
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `duplicateOption` | options | Yes | `"email"` | Performs duplicate checking by one of the following options: Email, EmailAndName. If a match is found using the option provided, the existing contact will be updated. |
| `orderType` | options | Yes | `""` | - |
| `fileAssociation` | options | Yes | `""` | - |
| `tagIds` | multiOptions | Yes | `[]` | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `userId` | options | Yes | `""` | The infusionsoft user to send the email on behalf of. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `fileName` | string | Yes | `""` | The filename of the attached file, including extension |
| `fileData` | string | Yes | `""` | The content of the attachment, encoded in Base64 |
| `companyName` | string | Yes | `""` | - |
| `contactId` | string | Yes | `""` | - |
| `contactId` | string | Yes | `""` | - |

#### Property Details

##### Duplicate Option (`duplicateOption`)

Performs duplicate checking by one of the following options: Email, EmailAndName. If a match is found using the option provided, the existing contact will be updated.

Optional values:
- `email`: Email
- `emailAndName`: Email And Name

##### Order Type (`orderType`)

Optional values:
- `offline`: Offline
- `online`: Online

##### File Association (`fileAssociation`)

Optional values:
- `company`: Company
- `contact`: Contact
- `user`: User

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
  "name": "Keap",
  "type": "nodes-base.keap",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "duplicateOption": "email",
    "orderType": "",
    "fileAssociation": "",
    "tagIds": [],
    "userId": "",
    "fileName": "",
    "fileData": "",
    "companyName": "",
    "contactId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Keap",
  "type": "nodes-base.keap",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "duplicateOption": "email",
    "orderType": "",
    "fileAssociation": "",
    "tagIds": [],
    "userId": "",
    "fileName": "",
    "fileData": "",
    "companyName": "",
    "contactId": "",
    "operation": "create"
  }
}
```

#### Get Many Example
```json
{
  "name": "Keap",
  "type": "nodes-base.keap",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "duplicateOption": "email",
    "orderType": "",
    "fileAssociation": "",
    "tagIds": [],
    "userId": "",
    "fileName": "",
    "fileData": "",
    "companyName": "",
    "contactId": "",
    "operation": "getAll"
  }
}
```

---

## Kitemaker

## Basic Information

- Node Type: `nodes-base.kitemaker`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Kitemaker GraphQL API

### Available Operations

### Get
Retrieve data on the logged-in user's organization
- Value: `get`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"workItem"` | - |
| `title` | string | Yes | `""` | Title of the work item to create |
| `spaceId` | options | Yes | `[]` | ID of the space to retrieve the work items from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `statusId` | options | Yes | `[]` | ID of the status to set on the item to create. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `workItemId` | string | Yes | `""` | ID of the work item to retrieve |
| `spaceId` | options | Yes | `[]` | ID of the space to retrieve the work items from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `workItemId` | string | Yes | `""` | ID of the work item to update |
| `operation` | options | No | `"get"` | - |
| `operation` | options | No | `"getAll"` | - |
| `operation` | options | No | `"getAll"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `organization`: Organization
- `space`: Space
- `user`: User
- `workItem`: Work Item

##### Operation (`operation`)

Optional values:
- `get`: Get - Retrieve data on the logged-in user's organization

##### Operation (`operation`)

Optional values:
- `getAll`: Get Many - Retrieve data on many spaces in the logged-in user's organization

##### Operation (`operation`)

Optional values:
- `getAll`: Get Many - Retrieve data on many users in the logged-in user's organization

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
  "name": "Kitemaker",
  "type": "nodes-base.kitemaker",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "workItem",
    "title": "",
    "spaceId": [],
    "statusId": [],
    "workItemId": ""
  }
}
```

#### Get Example
```json
{
  "name": "Kitemaker",
  "type": "nodes-base.kitemaker",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "workItem",
    "title": "",
    "spaceId": [],
    "statusId": [],
    "workItemId": "",
    "operation": "get"
  }
}
```

---

## Line

## Basic Information

- Node Type: `nodes-base.line`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Line API

### Available Operations

### Send
Sends notifications to users or groups
- Value: `send`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `message` | string | Yes | `""` | - |
| `resource` | options | No | `"notification"` | - |
| `operation` | options | No | `"send"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `notification`: Notification

##### Operation (`operation`)

Optional values:
- `send`: Send - Sends notifications to users or groups

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: imageUi
- `undefined`: notificationDisabled - \<p\>true: The user doesn't receive a push notification when the message is sent.\</p\>\<p\>false: The user receives a push notification when the message is sent\</p\>
- `undefined`: stickerUi

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
  "name": "Line",
  "type": "nodes-base.line",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "message": ""
  }
}
```

#### Send Example
```json
{
  "name": "Line",
  "type": "nodes-base.line",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "message": "",
    "operation": "send"
  }
}
```

---

## LinkedIn

## Basic Information

- Node Type: `nodes-base.linkedIn`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume LinkedIn API

### Available Operations

### Create
Create a new post
- Value: `create`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `person` | options | Yes | `""` | Person as which the post should be posted as. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `authentication` | options | No | `"standard"` | - |
| `resource` | options | No | `"post"` | - |
| `operation` | options | No | `"create"` | - |
| `postAs` | options | No | `"person"` | If to post on behalf of a user or an organization |
| `shareMediaCategory` | options | No | `"NONE"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `organization` | string | No | `""` | URN of Organization as which the post should be posted as |
| `text` | string | No | `""` | The primary content of the post |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `standard`: Standard
- `communityManagement`: Community Management

##### Resource (`resource`)

Optional values:
- `post`: Post

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new post

##### Post As (`postAs`)

If to post on behalf of a user or an organization

Optional values:
- `person`: Person
- `organization`: Organization

##### Media Category (`shareMediaCategory`)

Optional values:
- `NONE`: None - The post does not contain any media, and will only consist of text
- `ARTICLE`: Article - The post contains an article URL
- `IMAGE`: Image - The post contains an image

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: description - Provide a short description for your image or article
- `undefined`: originalUrl - Provide the URL of the article you would like to share here
- `undefined`: thumbnailBinaryPropertyName
- `undefined`: title - Customize the title of your image or article
- `undefined`: visibility - Dictate if post will be seen by the public or only connections

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
  "name": "LinkedIn",
  "type": "nodes-base.linkedIn",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "person": "",
    "binaryPropertyName": "data"
  }
}
```

#### Create Example
```json
{
  "name": "LinkedIn",
  "type": "nodes-base.linkedIn",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "person": "",
    "binaryPropertyName": "data",
    "operation": "create"
  }
}
```

---

## Magento 2

## Basic Information

- Node Type: `nodes-base.magento2`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Magento API

### Available Operations

### Create
Create a new customer
- Value: `create`

### Delete
Delete a customer
- Value: `delete`

### Get
Get a customer
- Value: `get`

### Get Many
Get many customers
- Value: `getAll`

### Update
Update a customer
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `email` | string | Yes | `""` | Email address of the user to create |
| `firstname` | string | Yes | `""` | First name of the user to create |
| `lastname` | string | Yes | `""` | Last name of the user to create |
| `sku` | string | Yes | `""` | Stock-keeping unit of the product |
| `sku` | string | Yes | `""` | Stock-keeping unit of the product |
| `customerId` | string | Yes | `""` | - |
| `orderId` | string | Yes | `""` | - |
| `orderId` | string | Yes | `""` | - |
| `name` | string | Yes | `""` | - |
| `resource` | options | No | `"customer"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `customer`: Customer
- `invoice`: Invoice
- `order`: Order
- `product`: Product

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
  "name": "Magento 2",
  "type": "nodes-base.magento2",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "firstname": "",
    "lastname": "",
    "sku": "",
    "customerId": "",
    "orderId": "",
    "name": ""
  }
}
```

#### Create Example
```json
{
  "name": "Magento 2",
  "type": "nodes-base.magento2",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "firstname": "",
    "lastname": "",
    "sku": "",
    "customerId": "",
    "orderId": "",
    "name": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Magento 2",
  "type": "nodes-base.magento2",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "firstname": "",
    "lastname": "",
    "sku": "",
    "customerId": "",
    "orderId": "",
    "name": "",
    "operation": "delete"
  }
}
```

---

## MailerLite

## Basic Information

- Node Type: `nodes-base.mailerLite`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume MailerLite API

### Available Operations

### Create
Create a new subscriber
- Value: `create`

### Get
Get an subscriber
- Value: `get`

### Get Many
Get many subscribers
- Value: `getAll`

### Update
Update an subscriber
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `email` | string | Yes | `""` | Email of new subscriber |
| `subscriberId` | string | Yes | `""` | Email of subscriber |
| `subscriberId` | string | Yes | `""` | Email of subscriber to delete |
| `subscriberId` | string | Yes | `""` | Email of subscriber to get |
| `resource` | options | No | `"subscriber"` | - |
| `operation` | options | No | `"create"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `filters` | collection | No | `{}` | - |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `50` | Max number of results to return |

#### Property Details

##### Resource (`resource`)

Optional values:
- `subscriber`: Subscriber

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new subscriber
- `get`: Get - Get an subscriber
- `getAll`: Get Many - Get many subscribers
- `update`: Update - Update an subscriber

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: customFieldsUi - Filter by custom fields
- `undefined`: status
- `undefined`: subscribed_at
- `undefined`: ip_address
- `undefined`: opted_in_at
- `undefined`: optin_ip
- `undefined`: unsubscribed_at

##### Filters (`filters`)

Optional values:
- `undefined`: status

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
  "name": "MailerLite",
  "type": "nodes-base.mailerLite",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "subscriberId": ""
  }
}
```

#### Create Example
```json
{
  "name": "MailerLite",
  "type": "nodes-base.mailerLite",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "subscriberId": "",
    "operation": "create"
  }
}
```

#### Get Example
```json
{
  "name": "MailerLite",
  "type": "nodes-base.mailerLite",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "email": "",
    "subscriberId": "",
    "operation": "get"
  }
}
```

---

## Microsoft Dynamics CRM

## Basic Information

- Node Type: `nodes-base.microsoftDynamicsCrm`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Microsoft Dynamics CRM API

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
| `name` | string | Yes | `""` | Company or business name |
| `accountId` | string | Yes | `""` | - |
| `resource` | options | No | `"account"` | - |
| `operation` | options | No | `"create"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `filters` | collection | No | `{}` | - |
| `updateFields` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |

#### Property Details

##### Resource (`resource`)

Optional values:
- `account`: Account

##### Operation (`operation`)

Optional values:
- `create`: Create
- `delete`: Delete
- `get`: Get
- `getAll`: Get Many
- `update`: Update

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: accountcategorycode - Category to indicate whether the customer account is standard or preferred. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: accountratingcode - Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: addresses
- `undefined`: businesstypecode - The legal designation or other business type of the account for contracts or reporting purposes. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: customersizecode - Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: customertypecode - Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: description - Additional information to describe the account, such as an excerpt from the company’s website
- `undefined`: emailaddress1 - The primary email address for the account
- `undefined`: emailaddress2 - The secondary email address for the account
- `undefined`: emailaddress3 - Alternate email address for the account
- `undefined`: fax
- `undefined`: ftpsiteurl - URL for the account’s FTP site to enable users to access data and share documents
- `undefined`: industrycode - The account’s primary industry for use in marketing segmentation and demographic analysis. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: name - Company o business name
- `undefined`: creditlimit - Credit limit of the account. This is a useful reference when you address invoice and accounting issues with the customer.
- `undefined`: numberofemployees - Number of employees that work at the account for use in marketing segmentation and demographic analysis
- `undefined`: paymenttermscode - The payment terms to indicate when the customer needs to pay the total amount. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: preferredappointmentdaycode - Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: preferredappointmenttimecode - Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: preferredcontactmethodcode - Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: primarysatoriid
- `undefined`: primarytwitterid
- `undefined`: revenue - The annual revenue for the account, used as an indicator in financial performance analysis
- `undefined`: sharesoutstanding - The number of shares available to the public for the account. This number is used as an indicator in financial performance analysis.
- `undefined`: shippingmethodcode - Shipping method for deliveries sent to the account’s address to designate the preferred carrier or other delivery option. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: sic - The Standard Industrial Classification (SIC) code that indicates the account’s primary industry of business, for use in marketing segmentation and demographic analysis
- `undefined`: stageid
- `undefined`: stockexchange - The stock exchange at which the account is listed to track their stock and financial performance of the company
- `undefined`: telephone1 - The main phone number for this account
- `undefined`: telephone2 - The second phone number for this account
- `undefined`: telephone3 - The third phone number for this account
- `undefined`: territorycode - Region or territory for the account for use in segmentation and analysis. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: tickersymbol - Type the stock exchange symbol for the account to track financial performance of the company. You can click the code entered in this field to access the latest trading information from MSN Money.
- `undefined`: websiteurl - The account’s website URL to get quick details about the company profile
- `undefined`: yominame - The phonetic spelling of the company name, if specified in Japanese, to make sure the name is pronounced correctly in phone calls and other communications

##### Options (`options`)

Optional values:
- `undefined`: returnFields - Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: expandFields - Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>

##### Filters (`filters`)

Optional values:
- `undefined`: query - Query to filter the results. Check \<a href="https://docs.microsoft.com/en-us/powerapps/developer/data-platform/webapi/query-data-web-api#filter-results" target="\_blank"\>filters\</a\>.

##### Update Fields (`updateFields`)

Optional values:
- `undefined`: accountcategorycode - Category to indicate whether the customer account is standard or preferred. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: accountratingcode - Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: addresses
- `undefined`: businesstypecode - The legal designation or other business type of the account for contracts or reporting purposes. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: customersizecode - Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: customertypecode - Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: description - Additional information to describe the account, such as an excerpt from the company’s website
- `undefined`: emailaddress1 - The primary email address for the account
- `undefined`: emailaddress2 - The secondary email address for the account
- `undefined`: emailaddress3 - Alternate email address for the account
- `undefined`: fax
- `undefined`: ftpsiteurl - URL for the account’s FTP site to enable users to access data and share documents
- `undefined`: industrycode - The account’s primary industry for use in marketing segmentation and demographic analysis. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: name - Company o business name
- `undefined`: creditlimit - Credit limit of the account. This is a useful reference when you address invoice and accounting issues with the customer.
- `undefined`: numberofemployees - Number of employees that work at the account for use in marketing segmentation and demographic analysis
- `undefined`: paymenttermscode - The payment terms to indicate when the customer needs to pay the total amount. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: preferredappointmentdaycode - Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: preferredappointmenttimecode - Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: preferredcontactmethodcode - Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: primarysatoriid
- `undefined`: primarytwitterid
- `undefined`: revenue - The annual revenue for the account, used as an indicator in financial performance analysis
- `undefined`: sharesoutstanding - The number of shares available to the public for the account. This number is used as an indicator in financial performance analysis.
- `undefined`: shippingmethodcode - Shipping method for deliveries sent to the account’s address to designate the preferred carrier or other delivery option. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: sic - The Standard Industrial Classification (SIC) code that indicates the account’s primary industry of business, for use in marketing segmentation and demographic analysis
- `undefined`: stageid
- `undefined`: stockexchange - The stock exchange at which the account is listed to track their stock and financial performance of the company
- `undefined`: telephone1 - The main phone number for this account
- `undefined`: telephone2 - The second phone number for this account
- `undefined`: telephone3 - The third phone number for this account
- `undefined`: territorycode - Region or territory for the account for use in segmentation and analysis. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: tickersymbol - Type the stock exchange symbol for the account to track financial performance of the company. You can click the code entered in this field to access the latest trading information from MSN Money.
- `undefined`: websiteurl - The account’s website URL to get quick details about the company profile
- `undefined`: yominame - The phonetic spelling of the company name, if specified in Japanese, to make sure the name is pronounced correctly in phone calls and other communications

##### Options (`options`)

Optional values:
- `undefined`: returnFields - Fields the response will include. Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.

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
  "name": "Microsoft Dynamics CRM",
  "type": "nodes-base.microsoftDynamicsCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "accountId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Microsoft Dynamics CRM",
  "type": "nodes-base.microsoftDynamicsCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "accountId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Microsoft Dynamics CRM",
  "type": "nodes-base.microsoftDynamicsCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "name": "",
    "accountId": "",
    "operation": "delete"
  }
}
```

---

## Microsoft Excel 365

## Basic Information

- Node Type: `nodes-base.microsoftExcel`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Microsoft Excel API

### Available Operations

### Append
Add rows to the end of the table
- Value: `append`

### Convert to Range
Convert a table to a range
- Value: `convertToRange`

### Create
Add a table based on range
- Value: `addTable`

### Delete
Delete a table
- Value: `deleteTable`

### Get Columns
Retrieve a list of table columns
- Value: `getColumns`

### Get Rows
Retrieve a list of table rows
- Value: `getRows`

### Lookup
Look for rows that match a given value in a column
- Value: `lookup`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `data` | json | Yes | `""` | Raw values for the specified range as array of string arrays in JSON format |
| `lookupColumn` | string | Yes | `""` | The name of the column in which to look for value |
| `lookupValue` | string | Yes | `""` | The value to look for in column |
| `data` | json | Yes | `""` | Raw values for the specified range as array of string arrays in JSON format |
| `data` | json | Yes | `""` | Raw values for the specified range as array of string arrays in JSON format. Should match the specified range: one array item for each row. |
| `workbook` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `worksheet` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `table` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `workbook` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `worksheet` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |

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
  "name": "Microsoft Excel 365",
  "type": "nodes-base.microsoftExcel",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "data": "",
    "lookupColumn": "",
    "lookupValue": "",
    "workbook": {
      "mode": "list",
      "value": ""
    },
    "worksheet": {
      "mode": "list",
      "value": ""
    },
    "table": {
      "mode": "list",
      "value": ""
    }
  }
}
```

#### Append Example
```json
{
  "name": "Microsoft Excel 365",
  "type": "nodes-base.microsoftExcel",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "data": "",
    "lookupColumn": "",
    "lookupValue": "",
    "workbook": {
      "mode": "list",
      "value": ""
    },
    "worksheet": {
      "mode": "list",
      "value": ""
    },
    "table": {
      "mode": "list",
      "value": ""
    },
    "operation": "append"
  }
}
```

#### Convert to Range Example
```json
{
  "name": "Microsoft Excel 365",
  "type": "nodes-base.microsoftExcel",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "data": "",
    "lookupColumn": "",
    "lookupValue": "",
    "workbook": {
      "mode": "list",
      "value": ""
    },
    "worksheet": {
      "mode": "list",
      "value": ""
    },
    "table": {
      "mode": "list",
      "value": ""
    },
    "operation": "convertToRange"
  }
}
```

---

## Microsoft OneDrive

## Basic Information

- Node Type: `nodes-base.microsoftOneDrive`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Microsoft OneDrive API

### Available Operations

### Copy
Copy a file
- Value: `copy`

### Delete
Delete a file
- Value: `delete`

### Download
Download a file
- Value: `download`

### Get
Get a file
- Value: `get`

### Rename
Rename a file
- Value: `rename`

### Search
Search a file
- Value: `search`

### Share
Share a file
- Value: `share`

### Upload
Upload a file up to 4MB in size
- Value: `upload`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `parentId` | string | Yes | `""` | ID of the parent folder that will contain the file |
| `binaryData` | boolean | Yes | `false` | Whether the data to upload should be taken from binary field |
| `fileContent` | string | Yes | `""` | The text content of the file |
| `name` | string | Yes | `""` | The name or path of the folder |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `resource` | options | No | `"file"` | - |
| `operation` | options | No | `"upload"` | - |
| `operation` | options | No | `"getChildren"` | - |
| `query` | string | No | `""` | The query text used to search for items. Values may be matched across several fields including filename, metadata, and file content. |

#### Property Details

##### Resource (`resource`)

Optional values:
- `file`: File
- `folder`: Folder

##### Operation (`operation`)

Optional values:
- `copy`: Copy - Copy a file
- `delete`: Delete - Delete a file
- `download`: Download - Download a file
- `get`: Get - Get a file
- `rename`: Rename - Rename a file
- `search`: Search - Search a file
- `share`: Share - Share a file
- `upload`: Upload - Upload a file up to 4MB in size

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a folder
- `delete`: Delete - Delete a folder
- `getChildren`: Get Children - Get items inside a folder
- `rename`: Rename - Rename a folder
- `search`: Search - Search a folder
- `share`: Share - Share a folder

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
  "name": "Microsoft OneDrive",
  "type": "nodes-base.microsoftOneDrive",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "parentId": "",
    "binaryData": false,
    "fileContent": "",
    "name": "",
    "binaryPropertyName": "data"
  }
}
```

#### Copy Example
```json
{
  "name": "Microsoft OneDrive",
  "type": "nodes-base.microsoftOneDrive",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "parentId": "",
    "binaryData": false,
    "fileContent": "",
    "name": "",
    "binaryPropertyName": "data",
    "operation": "copy"
  }
}
```

#### Delete Example
```json
{
  "name": "Microsoft OneDrive",
  "type": "nodes-base.microsoftOneDrive",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "parentId": "",
    "binaryData": false,
    "fileContent": "",
    "name": "",
    "binaryPropertyName": "data",
    "operation": "delete"
  }
}
```

---

## Microsoft SQL

## Basic Information

- Node Type: `nodes-base.microsoftSql`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Get, add and update data in Microsoft SQL

### Available Operations

### Execute Query
Execute an SQL query
- Value: `executeQuery`

### Insert
Insert rows in database
- Value: `insert`

### Update
Update rows in database
- Value: `update`

### Delete
Delete rows in database
- Value: `delete`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | The SQL query to execute |
| `table` | string | Yes | `""` | Name of the table in which to insert data to |
| `table` | string | Yes | `""` | Name of the table in which to update data in |
| `updateKey` | string | Yes | `"id"` | Name of the property which decides which rows in the database should be updated. Normally that would be "id". |
| `table` | string | Yes | `""` | Name of the table in which to delete data |
| `deleteKey` | string | Yes | `"id"` | Name of the property which decides which rows in the database should be deleted. Normally that would be "id". |
| `operation` | options | No | `"insert"` | - |
| `columns` | string | No | `""` | Comma-separated list of the properties which should used as columns for the new rows |
| `columns` | string | No | `""` | Comma-separated list of the properties which should used as columns for rows to update |

#### Property Details

##### Operation (`operation`)

Optional values:
- `executeQuery`: Execute Query - Execute an SQL query
- `insert`: Insert - Insert rows in database
- `update`: Update - Update rows in database
- `delete`: Delete - Delete rows in database

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
  "name": "Microsoft SQL",
  "type": "nodes-base.microsoftSql",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "table": "",
    "updateKey": "id",
    "deleteKey": "id"
  }
}
```

#### Execute Query Example
```json
{
  "name": "Microsoft SQL",
  "type": "nodes-base.microsoftSql",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "table": "",
    "updateKey": "id",
    "deleteKey": "id",
    "operation": "executeQuery"
  }
}
```

#### Insert Example
```json
{
  "name": "Microsoft SQL",
  "type": "nodes-base.microsoftSql",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "table": "",
    "updateKey": "id",
    "deleteKey": "id",
    "operation": "insert"
  }
}
```

---

## Microsoft Teams

## Basic Information

- Node Type: `nodes-base.microsoftTeams`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Microsoft Teams API

### Available Operations

### Create
Create a channel
- Value: `create`

### Delete
Delete a channel
- Value: `deleteChannel`

### Get
Get a channel
- Value: `get`

### Get Many
Get many channels
- Value: `getAll`

### Update
Update a channel
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `contentType` | options | Yes | `"text"` | Whether the message is plain text or HTML |
| `contentType` | options | Yes | `"text"` | Whether the message is plain text or HTML |
| `tasksFor` | options | Yes | `"member"` | Whether to retrieve the tasks for a user or for a plan |
| `teamId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the team from the list, by URL, or by ID (the ID is the "groupId" parameter in the URL you get from "Get a link to the team") |
| `name` | string | Yes | `""` | The name of the new channel you want to create |
| `teamId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the team from the list, by URL, or by ID (the ID is the "groupId" parameter in the URL you get from "Get a link to the team") |
| `channelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the channel from the list, by URL, or by ID (the ID is the "threadId" in the URL) |
| `teamId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the team from the list, by URL, or by ID (the ID is the "groupId" parameter in the URL you get from "Get a link to the team") |
| `channelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the channel from the list, by URL, or by ID (the ID is the "threadId" in the URL) |
| `teamId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select the team from the list, by URL, or by ID (the ID is the "groupId" parameter in the URL you get from "Get a link to the team") |

#### Property Details

##### Content Type (`contentType`)

Whether the message is plain text or HTML

Optional values:
- `text`: Text
- `html`: HTML

##### Content Type (`contentType`)

Whether the message is plain text or HTML

Optional values:
- `text`: Text
- `html`: HTML

##### Tasks For (`tasksFor`)

Whether to retrieve the tasks for a user or for a plan

Optional values:
- `member`: Group Member - Tasks assigned to group member
- `plan`: Plan - Tasks in group plan

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
  "name": "Microsoft Teams",
  "type": "nodes-base.microsoftTeams",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contentType": "text",
    "tasksFor": "member",
    "teamId": {
      "mode": "list",
      "value": ""
    },
    "name": "",
    "channelId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

#### Create Example
```json
{
  "name": "Microsoft Teams",
  "type": "nodes-base.microsoftTeams",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contentType": "text",
    "tasksFor": "member",
    "teamId": {
      "mode": "list",
      "value": ""
    },
    "name": "",
    "channelId": {
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
  "name": "Microsoft Teams",
  "type": "nodes-base.microsoftTeams",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contentType": "text",
    "tasksFor": "member",
    "teamId": {
      "mode": "list",
      "value": ""
    },
    "name": "",
    "channelId": {
      "mode": "list",
      "value": ""
    },
    "operation": "deleteChannel"
  }
}
```

---

## Microsoft To Do

## Basic Information

- Node Type: `nodes-base.microsoftToDo`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Microsoft To Do API.

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
| `taskListId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `applicationName` | string | Yes | `""` | App name of the source that is sending the linked entity |
| `taskListId` | options | Yes | `""` | The identifier of the list, unique in the user's mailbox. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `title` | string | Yes | `""` | A brief description of the task |
| `taskListId` | options | Yes | `""` | The identifier of the list, unique in the user's mailbox. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `displayName` | string | Yes | `""` | List display name |
| `listId` | string | Yes | `""` | The identifier of the list, unique in the user's mailbox |
| `displayName` | string | Yes | `""` | List display name |
| `taskId` | string | Yes | `""` | - |
| `linkedResourceId` | string | Yes | `""` | - |

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
  "name": "Microsoft To Do",
  "type": "nodes-base.microsoftToDo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "taskListId": "",
    "applicationName": "",
    "title": "",
    "displayName": "",
    "listId": "",
    "taskId": "",
    "linkedResourceId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Microsoft To Do",
  "type": "nodes-base.microsoftToDo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "taskListId": "",
    "applicationName": "",
    "title": "",
    "displayName": "",
    "listId": "",
    "taskId": "",
    "linkedResourceId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Microsoft To Do",
  "type": "nodes-base.microsoftToDo",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "taskListId": "",
    "applicationName": "",
    "title": "",
    "displayName": "",
    "listId": "",
    "taskId": "",
    "linkedResourceId": "",
    "operation": "delete"
  }
}
```

---

## Mindee

## Basic Information

- Node Type: `nodes-base.mindee`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Mindee API

### Available Operations

### Predict
- Value: `predict`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `resource` | options | No | `"receipt"` | - |
| `operation` | options | No | `"predict"` | - |
| `apiVersion` | options | No | `1` | Which Mindee API Version to use |
| `apiVersion` | options | No | `3` | Which Mindee API Version to use |
| `apiVersion` | options | No | `4` | Which Mindee API Version to use |
| `rawData` | boolean | No | `false` | Whether to return the data exactly in the way it got received from the API |

#### Property Details

##### Resource (`resource`)

Optional values:
- `invoice`: Invoice
- `receipt`: Receipt

##### Operation (`operation`)

Optional values:
- `predict`: Predict

##### API Version (`apiVersion`)

Which Mindee API Version to use

Optional values:
- `1`: 1
- `3`: 3
- `4`: 4

##### API Version (`apiVersion`)

Which Mindee API Version to use

Optional values:
- `1`: 1
- `3`: 3
- `4`: 4

##### API Version (`apiVersion`)

Which Mindee API Version to use

Optional values:
- `1`: 1
- `3`: 3
- `4`: 4

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
  "name": "Mindee",
  "type": "nodes-base.mindee",
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

#### Predict Example
```json
{
  "name": "Mindee",
  "type": "nodes-base.mindee",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryPropertyName": "data",
    "operation": "predict"
  }
}
```

---

## MongoDB

## Basic Information

- Node Type: `nodes-base.mongoDb`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Find, insert and update documents in MongoDB

### Available Operations

### Aggregate
Aggregate documents
- Value: `aggregate`

### Delete
Delete documents
- Value: `delete`

### Find
Find documents
- Value: `find`

### Find And Replace
Find and replace documents
- Value: `findOneAndReplace`

### Find And Update
Find and update documents
- Value: `findOneAndUpdate`

### Insert
Insert documents
- Value: `insert`

### Update
Update documents
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | json | Yes | `""` | MongoDB aggregation pipeline query in JSON format |
| `query` | json | Yes | `"{}"` | MongoDB Delete query |
| `query` | json | Yes | `"{}"` | MongoDB Find query |
| `indexType` | options | Yes | `"vectorSearch"` | The search index index type |
| `collection` | string | Yes | `""` | MongoDB Collection |
| `updateKey` | string | Yes | `"id"` | Name of the property which decides which rows in the database should be updated. Normally that would be "id". |
| `indexNameRequired` | string | Yes | `""` | The name of the search index |
| `indexDefinition` | json | Yes | `"{}"` | The search index definition |
| `resource` | options | No | `"document"` | - |
| `operation` | options | No | `"find"` | - |

#### Property Details

##### Index Type (`indexType`)

The search index index type

Optional values:
- `vectorSearch`: Vector Search
- `search`: Search

##### Resource (`resource`)

Optional values:
- `searchIndexes`: Search Index
- `document`: Document

##### Operation (`operation`)

Optional values:
- `aggregate`: Aggregate - Aggregate documents
- `delete`: Delete - Delete documents
- `find`: Find - Find documents
- `findOneAndReplace`: Find And Replace - Find and replace documents
- `findOneAndUpdate`: Find And Update - Find and update documents
- `insert`: Insert - Insert documents
- `update`: Update - Update documents

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
  "name": "MongoDB",
  "type": "nodes-base.mongoDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "{}",
    "indexType": "vectorSearch",
    "collection": "",
    "updateKey": "id",
    "indexNameRequired": "",
    "indexDefinition": "{}"
  }
}
```

#### Aggregate Example
```json
{
  "name": "MongoDB",
  "type": "nodes-base.mongoDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "{}",
    "indexType": "vectorSearch",
    "collection": "",
    "updateKey": "id",
    "indexNameRequired": "",
    "indexDefinition": "{}",
    "operation": "aggregate"
  }
}
```

#### Delete Example
```json
{
  "name": "MongoDB",
  "type": "nodes-base.mongoDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "{}",
    "indexType": "vectorSearch",
    "collection": "",
    "updateKey": "id",
    "indexNameRequired": "",
    "indexDefinition": "{}",
    "operation": "delete"
  }
}
```

---

## MQTT

## Basic Information

- Node Type: `nodes-base.mqtt`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Push messages to MQTT

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `topic` | string | Yes | `""` | The topic to publish to |
| `message` | string | Yes | `""` | The message to publish |
| `options` | collection | No | `{}` | - |
| `sendInputData` | boolean | No | `true` | Whether to send the data the node receives as JSON |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: qos - QoS subscription level
- `undefined`: retain - Normally if a publisher publishes a message to a topic, and no one is subscribed to that topic the message is simply discarded by the broker. However the publisher can tell the broker to keep the last message on that topic by setting the retain flag to true.

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
  "name": "MQTT",
  "type": "nodes-base.mqtt",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "topic": "",
    "message": ""
  }
}
```

---

## n8n Form

## Basic Information

- Node Type: `nodes-base.form`
- Category: input
- Package: n8n-nodes-base

### Description

Generate webforms in n8n and pass their responses to the workflow

### Available Operations

### Next Form Page
- Value: `page`

### Form Ending
- Value: `completion`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `redirectUrl` | string | Yes | `""` | - |
| `completionTitle` | string | Yes | `""` | - |
| `operation` | options | No | `"page"` | - |
| `limitType` | options | No | `"afterTimeInterval"` | Sets the condition for the execution to resume. Can be a specified date or after some time. |
| `resumeUnit` | options | No | `"hours"` | Unit of the interval value |
| `limitType` | options | No | `"afterTimeInterval"` | Sets the condition for the execution to resume. Can be a specified date or after some time. |
| `resumeUnit` | options | No | `"hours"` | Unit of the interval value |
| `defineForm` | options | No | `"fields"` | - |
| `formFields` | fixedCollection | No | `{}` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Page Type (`operation`)

Optional values:
- `page`: Next Form Page
- `completion`: Form Ending

##### Limit Type (`limitType`)

Sets the condition for the execution to resume. Can be a specified date or after some time.

Optional values:
- `afterTimeInterval`: After Time Interval - Waits for a certain amount of time
- `atSpecifiedTime`: At Specified Time - Waits until the set date and time to continue

##### Unit (`resumeUnit`)

Unit of the interval value

Optional values:
- `minutes`: Minutes
- `hours`: Hours
- `days`: Days

##### Limit Type (`limitType`)

Sets the condition for the execution to resume. Can be a specified date or after some time.

Optional values:
- `afterTimeInterval`: After Time Interval - Waits for a certain amount of time
- `atSpecifiedTime`: At Specified Time - Waits until the set date and time to continue

##### Unit (`resumeUnit`)

Unit of the interval value

Optional values:
- `minutes`: Minutes
- `hours`: Hours
- `days`: Days

##### Define Form (`defineForm`)

Optional values:
- `fields`: Using Fields Below
- `json`: Using JSON

##### Form Elements (`formFields`)

Optional values:
- `undefined`: values

##### Options (`options`)

Optional values:
- `undefined`: formTitle - Shown at the top of the form
- `undefined`: formDescription - Shown underneath the Form Title. Can be used to prompt the user on how to complete the form. Accepts HTML.
- `undefined`: buttonLabel
- `undefined`: customCss - Override default styling of the public form interface with CSS

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
  "name": "n8n Form",
  "type": "nodes-base.form",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "redirectUrl": "",
    "completionTitle": ""
  }
}
```

#### Next Form Page Example
```json
{
  "name": "n8n Form",
  "type": "nodes-base.form",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "redirectUrl": "",
    "completionTitle": "",
    "operation": "page"
  }
}
```

#### Form Ending Example
```json
{
  "name": "n8n Form",
  "type": "nodes-base.form",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "redirectUrl": "",
    "completionTitle": "",
    "operation": "completion"
  }
}
```

---

## Nextcloud

## Basic Information

- Node Type: `nodes-base.nextCloud`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Access data on Nextcloud

### Available Operations

### Copy
Copy a file
- Value: `copy`

### Delete
Delete a file
- Value: `delete`

### Download
Download a file
- Value: `download`

### Move
Move a file
- Value: `move`

### Share
Share a file
- Value: `share`

### Upload
Upload a file
- Value: `upload`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `path` | string | Yes | `""` | The path of file or folder to copy. The path should start with "/". |
| `path` | string | Yes | `""` | The path to delete. Can be a single file or a whole folder. The path should start with "/". |
| `path` | string | Yes | `""` | The path of file or folder to move. The path should start with "/". |
| `path` | string | Yes | `""` | The file path of the file to download. Has to contain the full path. The path should start with "/". |
| `path` | string | Yes | `""` | The absolute file path of the file to upload. Has to contain the full path. The parent folder has to exist. Existing files get overwritten. |
| `path` | string | Yes | `""` | The file path of the file to share. Has to contain the full path. The path should start with "/". |
| `path` | string | Yes | `""` | The folder to create. The parent folder has to exist. The path should start with "/". |
| `toPath` | string | Yes | `""` | The destination path of file or folder. The path should start with "/". |
| `toPath` | string | Yes | `""` | The new path of file or folder. The path should start with "/". |
| `userId` | string | Yes | `""` | Username the user will have |

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
  "name": "Nextcloud",
  "type": "nodes-base.nextCloud",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "path": "",
    "toPath": "",
    "userId": ""
  }
}
```

#### Copy Example
```json
{
  "name": "Nextcloud",
  "type": "nodes-base.nextCloud",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "path": "",
    "toPath": "",
    "userId": "",
    "operation": "copy"
  }
}
```

#### Delete Example
```json
{
  "name": "Nextcloud",
  "type": "nodes-base.nextCloud",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "path": "",
    "toPath": "",
    "userId": "",
    "operation": "delete"
  }
}
```

---

## NocoDB

## Basic Information

- Node Type: `nodes-base.nocoDb`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Read, update, write and delete data from NocoDB

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
| `projectId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `projectId` | string | Yes | `""` | The ID of the project |
| `projectId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `table` | options | Yes | `""` | The table to operate on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `table` | string | Yes | `""` | The name of the table |
| `id` | string | Yes | `""` | The value of the ID field |
| `id` | string | Yes | `""` | The value of the ID field |
| `downloadFieldNames` | string | Yes | `""` | Name of the fields of type 'attachment' that should be downloaded. Multiple ones can be defined separated by comma. Case sensitive. |
| `downloadFieldNames` | string | Yes | `""` | Name of the fields of type 'attachment' that should be downloaded. Multiple ones can be defined separated by comma. Case sensitive. |
| `authentication` | options | No | `"nocoDb"` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `nocoDbApiToken`: API Token
- `nocoDb`: User Token

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
  "name": "NocoDB",
  "type": "nodes-base.nocoDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "projectId": "",
    "table": "",
    "id": "",
    "downloadFieldNames": ""
  }
}
```

#### Create Example
```json
{
  "name": "NocoDB",
  "type": "nodes-base.nocoDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "projectId": "",
    "table": "",
    "id": "",
    "downloadFieldNames": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "NocoDB",
  "type": "nodes-base.nocoDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "projectId": "",
    "table": "",
    "id": "",
    "downloadFieldNames": "",
    "operation": "delete"
  }
}
```

---

## Npm

## Basic Information

- Node Type: `nodes-base.npm`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume NPM registry API

### Available Operations

### Get Metadata
Returns all the metadata for a package at a specific version
- Value: `getMetadata`

### Get Versions
Returns all the versions for a package
- Value: `getVersions`

### Search
Search for packages
- Value: `search`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | The query text used to search for packages |
| `packageName` | string | Yes | `""` | - |
| `packageVersion` | string | Yes | `"latest"` | - |
| `packageName` | string | Yes | `""` | - |
| `packageVersion` | string | Yes | `""` | - |
| `distTagName` | string | Yes | `"latest"` | - |
| `resource` | options | No | `"package"` | - |
| `operation` | options | No | `"getMetadata"` | - |
| `operation` | options | No | `"getMany"` | - |
| `limit` | number | No | `10` | Max number of results to return |

#### Property Details

##### Resource (`resource`)

Optional values:
- `package`: Package
- `distTag`: Distribution Tag

##### Operation (`operation`)

Optional values:
- `getMetadata`: Get Metadata - Returns all the metadata for a package at a specific version
- `getVersions`: Get Versions - Returns all the versions for a package
- `search`: Search - Search for packages

##### Operation (`operation`)

Optional values:
- `getMany`: Get All - Returns all the dist-tags for a package
- `update`: Update - Update a the dist-tags for a package

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
  "name": "Npm",
  "type": "nodes-base.npm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "packageName": "",
    "packageVersion": "",
    "distTagName": "latest"
  }
}
```

#### Get Metadata Example
```json
{
  "name": "Npm",
  "type": "nodes-base.npm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "packageName": "",
    "packageVersion": "",
    "distTagName": "latest",
    "operation": "getMetadata"
  }
}
```

#### Get Versions Example
```json
{
  "name": "Npm",
  "type": "nodes-base.npm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "packageName": "",
    "packageVersion": "",
    "distTagName": "latest",
    "operation": "getVersions"
  }
}
```

---

## Onfleet

## Basic Information

- Node Type: `nodes-base.onfleet`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Onfleet API

### Available Operations

### Create
Create a new Onfleet admin
- Value: `create`

### Delete
Delete an Onfleet admin
- Value: `delete`

### Get Many
Get many Onfleet admins
- Value: `getAll`

### Update
Update an Onfleet admin
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `getBy` | options | Yes | `"id"` | The variable that is used for looking up a recipient |
| `containerType` | options | Yes | `""` | - |
| `type` | options | Yes | `""` | - |
| `destination` | fixedCollection | Yes | `{}` | - |
| `id` | string | Yes | `""` | The ID of the admin object for lookup |
| `name` | string | Yes | `""` | The administrator's name |
| `email` | string | Yes | `""` | The administrator's email address |
| `containerId` | string | Yes | `""` | The object ID according to the container chosen |
| `index` | number | Yes | `0` | The index given indicates the position where the tasks are going to be inserted |
| `tasks` | string | Yes | `[]` | Task's ID that are going to be used |

#### Property Details

##### Get By (`getBy`)

The variable that is used for looking up a recipient

Optional values:
- `id`: ID
- `phone`: Phone
- `name`: Name

##### Container Type (`containerType`)

Optional values:
- `organizations`: Organizations
- `teams`: Teams
- `workers`: Workers

##### Insert Type (`type`)

Optional values:
- `-1`: Append
- `0`: Prepend
- `1`: At Specific Index

##### Destination (`destination`)

Optional values:
- `undefined`: destinationProperties

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
  "name": "Onfleet",
  "type": "nodes-base.onfleet",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "getBy": "id",
    "containerType": "",
    "type": "",
    "destination": {},
    "id": "",
    "name": "",
    "email": "",
    "containerId": "",
    "index": 0,
    "tasks": []
  }
}
```

#### Create Example
```json
{
  "name": "Onfleet",
  "type": "nodes-base.onfleet",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "getBy": "id",
    "containerType": "",
    "type": "",
    "destination": {},
    "id": "",
    "name": "",
    "email": "",
    "containerId": "",
    "index": 0,
    "tasks": [],
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Onfleet",
  "type": "nodes-base.onfleet",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "getBy": "id",
    "containerType": "",
    "type": "",
    "destination": {},
    "id": "",
    "name": "",
    "email": "",
    "containerId": "",
    "index": 0,
    "tasks": [],
    "operation": "delete"
  }
}
```

---

## OpenWeatherMap

## Basic Information

- Node Type: `nodes-base.openWeatherMap`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Gets current and future weather information

### Available Operations

### Current Weather
Returns the current weather data
- Value: `currentWeather`

### 5 Day Forecast
Returns the weather data for the next 5 days
- Value: `5DayForecast`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `cityName` | string | Yes | `""` | The name of the city to return the weather of |
| `cityId` | number | Yes | `160001123` | The ID of city to return the weather of. List can be downloaded here: http://bulk.openweathermap.org/sample/. |
| `latitude` | string | Yes | `""` | The latitude of the location to return the weather of |
| `longitude` | string | Yes | `""` | The longitude of the location to return the weather of |
| `zipCode` | string | Yes | `""` | The ID of city to return the weather of. List can be downloaded here: http://bulk.openweathermap.org/sample/. |
| `operation` | options | No | `"currentWeather"` | - |
| `format` | options | No | `"metric"` | The format in which format the data should be returned |
| `locationSelection` | options | No | `"cityName"` | How to define the location for which to return the weather |
| `language` | string | No | `""` | The two letter language code to get your output in (eg. en, de, ...). |

#### Property Details

##### Operation (`operation`)

Optional values:
- `currentWeather`: Current Weather - Returns the current weather data
- `5DayForecast`: 5 Day Forecast - Returns the weather data for the next 5 days

##### Format (`format`)

The format in which format the data should be returned

Optional values:
- `imperial`: Imperial - Fahrenheit \| miles/hour
- `metric`: Metric - Celsius \| meter/sec
- `standard`: Scientific - Kelvin \| meter/sec

##### Location Selection (`locationSelection`)

How to define the location for which to return the weather

Optional values:
- `cityName`: City Name
- `cityId`: City ID
- `coordinates`: Coordinates
- `zipCode`: Zip Code

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
  "name": "OpenWeatherMap",
  "type": "nodes-base.openWeatherMap",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "cityName": "",
    "cityId": 160001123,
    "latitude": "",
    "longitude": "",
    "zipCode": ""
  }
}
```

#### Current Weather Example
```json
{
  "name": "OpenWeatherMap",
  "type": "nodes-base.openWeatherMap",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "cityName": "",
    "cityId": 160001123,
    "latitude": "",
    "longitude": "",
    "zipCode": "",
    "operation": "currentWeather"
  }
}
```

#### 5 Day Forecast Example
```json
{
  "name": "OpenWeatherMap",
  "type": "nodes-base.openWeatherMap",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "cityName": "",
    "cityId": 160001123,
    "latitude": "",
    "longitude": "",
    "zipCode": "",
    "operation": "5DayForecast"
  }
}
```

---

## Oracle Database

## Basic Information

- Node Type: `nodes-base.oracleDatabase`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Get, add and update data in Oracle database

### Available Operations

### Delete
Delete an entire table or rows in a table
- Value: `deleteTable`

### Execute SQL
Execute an SQL
- Value: `execute`

### Insert
Insert rows in a table
- Value: `insert`

### Insert or Update
Insert or update rows in a table
- Value: `upsert`

### Select
Select rows from a table
- Value: `select`

### Update
Update rows in a table
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | The SQL statement to execute. You can use n8n expressions and positional parameters like :1, :2, :3, or named parameters like :name, :ID, etc to refer to the 'Bind Variable Placeholder Values' set in options below. |
| `schema` | resourceLocator | Yes | `{"mode":"list","value":""}` | The schema that contains the table you want to work on |
| `table` | resourceLocator | Yes | `{"mode":"list","value":""}` | The table you want to work on |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `columns` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `resource` | hidden | No | `"database"` | - |
| `operation` | options | No | `"insert"` | - |
| `where` | fixedCollection | No | `{}` | If not set, all rows will be selected |
| `combineConditions` | options | No | `"AND"` | How to combine the conditions defined in "Select Rows": AND requires all conditions to be true, OR requires at least one condition to be true |

#### Property Details

##### Resource (`resource`)

Optional values:
- `database`: Database

##### Operation (`operation`)

Optional values:
- `deleteTable`: Delete - Delete an entire table or rows in a table
- `execute`: Execute SQL - Execute an SQL
- `insert`: Insert - Insert rows in a table
- `upsert`: Insert or Update - Insert or update rows in a table
- `select`: Select - Select rows from a table
- `update`: Update - Update rows in a table

##### Select Rows (`where`)

If not set, all rows will be selected

Optional values:
- `undefined`: values

##### Combine Conditions (`combineConditions`)

How to combine the conditions defined in "Select Rows": AND requires all conditions to be true, OR requires at least one condition to be true

Optional values:
- `AND`: AND - Only rows that meet all the conditions are selected
- `OR`: OR - Rows that meet at least one condition are selected

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
  "name": "Oracle Database",
  "type": "nodes-base.oracleDatabase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "schema": {
      "mode": "list",
      "value": ""
    },
    "table": {
      "mode": "list",
      "value": ""
    },
    "columns": {
      "mappingMode": "defineBelow",
      "value": null
    }
  }
}
```

#### Delete Example
```json
{
  "name": "Oracle Database",
  "type": "nodes-base.oracleDatabase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "schema": {
      "mode": "list",
      "value": ""
    },
    "table": {
      "mode": "list",
      "value": ""
    },
    "columns": {
      "mappingMode": "defineBelow",
      "value": null
    },
    "operation": "deleteTable"
  }
}
```

#### Execute SQL Example
```json
{
  "name": "Oracle Database",
  "type": "nodes-base.oracleDatabase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "schema": {
      "mode": "list",
      "value": ""
    },
    "table": {
      "mode": "list",
      "value": ""
    },
    "columns": {
      "mappingMode": "defineBelow",
      "value": null
    },
    "operation": "execute"
  }
}
```

---

## Phantombuster

## Basic Information

- Node Type: `nodes-base.phantombuster`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Phantombuster API

### Available Operations

### Delete
Delete an agent by ID
- Value: `delete`

### Get
Get an agent by ID
- Value: `get`

### Get Many
Get many agents of the current user's organization
- Value: `getAll`

### Get Output
Get the output of the most recent container of an agent
- Value: `getOutput`

### Launch
Add an agent to the launch queue
- Value: `launch`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `agentId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `agentId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `agentId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `agentId` | string | Yes | `""` | - |
| `resource` | options | No | `"agent"` | - |
| `operation` | options | No | `"launch"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `25` | Max number of results to return |

#### Property Details

##### Resource (`resource`)

Optional values:
- `agent`: Agent

##### Operation (`operation`)

Optional values:
- `delete`: Delete - Delete an agent by ID
- `get`: Get - Get an agent by ID
- `getAll`: Get Many - Get many agents of the current user's organization
- `getOutput`: Get Output - Get the output of the most recent container of an agent
- `launch`: Launch - Add an agent to the launch queue

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: prevContainerId - If set, the output will be retrieved from the container after the specified previous container ID
- `undefined`: prevStatus - If set, allows to define which status was previously retrieved on user-side
- `undefined`: prevRuntimeEventIndex - If set, the container's runtime events will be returned in the response starting from the provided previous runtime event index

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: argumentsJson - Agent argument. Can either be a JSON string or a plain object. The argument can be retrieved with buster.argument in the agent’s script.
- `undefined`: argumentsUi
- `undefined`: bonusArgumentUi
- `undefined`: bonusArgumentJson - Agent bonus argument. Can either be a JSON string or a plain object. This bonus argument is single-use, it will only be used for the current launch. If present, it will be merged with the original argument, resulting in an effective argument that can be retrieved with buster.argument in the agent’s script.
- `undefined`: manualLaunch - Whether the agent will be considered as "launched manually"
- `undefined`: maxInstanceCount - If set, the agent will only be launched if the number of already running instances is below the specified number
- `undefined`: saveArgument - If true, argument will be saved as the default launch options for the agent

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
  "name": "Phantombuster",
  "type": "nodes-base.phantombuster",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "agentId": ""
  }
}
```

#### Delete Example
```json
{
  "name": "Phantombuster",
  "type": "nodes-base.phantombuster",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "agentId": "",
    "operation": "delete"
  }
}
```

#### Get Example
```json
{
  "name": "Phantombuster",
  "type": "nodes-base.phantombuster",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "agentId": "",
    "operation": "get"
  }
}
```

---

## Philips Hue

## Basic Information

- Node Type: `nodes-base.philipsHue`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Philips Hue API

### Available Operations

### Delete
Delete a light
- Value: `delete`

### Get
Retrieve a light
- Value: `get`

### Get Many
Retrieve many lights
- Value: `getAll`

### Update
Update a light
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `lightId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `on` | boolean | Yes | `true` | On/Off state of the light |
| `lightId` | string | Yes | `""` | - |
| `lightId` | string | Yes | `""` | - |
| `resource` | options | No | `"light"` | - |
| `operation` | options | No | `"update"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `100` | Max number of results to return |

#### Property Details

##### Resource (`resource`)

Optional values:
- `light`: Light

##### Operation (`operation`)

Optional values:
- `delete`: Delete - Delete a light
- `get`: Get - Retrieve a light
- `getAll`: Get Many - Retrieve many lights
- `update`: Update - Update a light

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: alert - The alert effect, is a temporary change to the bulb’s state
- `undefined`: bri - The brightness value to set the light to. Brightness is a scale from 1 (the minimum the light is capable of) to 254 (the maximum).
- `undefined`: bri_inc - Increments or decrements the value of the brightness. This value is ignored if the Brightness attribute is provided.
- `undefined`: ct - The Mired color temperature of the light. 2012 connected lights are capable of 153 (6500K) to 500 (2000K).
- `undefined`: ct_inc - Increments or decrements the value of the ct. ct\_inc is ignored if the ct attribute is provided.
- `undefined`: xy - The x and y coordinates of a color in CIE color space. The first entry is the x coordinate and the second entry is the y coordinate. Both x and y are between 0 and 1
- `undefined`: xy_inc - Increments or decrements the value of the xy. This value is ignored if the Coordinates attribute is provided. Any ongoing color transition is stopped. Max value \[0.5, 0.5\]
- `undefined`: effect - The dynamic effect of the light
- `undefined`: hue - The hue value to set light to.The hue value is a wrapping value between 0 and 65535. Both 0 and 65535 are red, 25500 is green and 46920 is blue.
- `undefined`: hue_inc - Increments or decrements the value of the hue. Hue Increments is ignored if the Hue attribute is provided.
- `undefined`: sat - Saturation of the light. 254 is the most saturated (colored) and 0 is the least saturated (white).
- `undefined`: sat_inc - Increments or decrements the value of the sat. This value is ignored if the Saturation attribute is provided.
- `undefined`: transitiontime - The duration in seconds of the transition from the light’s current state to the new state

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
  "name": "Philips Hue",
  "type": "nodes-base.philipsHue",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "lightId": "",
    "on": true
  }
}
```

#### Delete Example
```json
{
  "name": "Philips Hue",
  "type": "nodes-base.philipsHue",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "lightId": "",
    "on": true,
    "operation": "delete"
  }
}
```

#### Get Example
```json
{
  "name": "Philips Hue",
  "type": "nodes-base.philipsHue",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "lightId": "",
    "on": true,
    "operation": "get"
  }
}
```

---

## PostHog

## Basic Information

- Node Type: `nodes-base.postHog`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume PostHog API

### Available Operations

### Create
Create an alias
- Value: `create`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `alias` | string | Yes | `""` | The name of the alias |
| `distinctId` | string | Yes | `""` | The user's distinct ID |
| `eventName` | string | Yes | `""` | The name of the event |
| `distinctId` | string | Yes | `""` | The user's distinct ID |
| `distinctId` | string | Yes | `""` | The identity's distinct ID |
| `distinctId` | string | Yes | `""` | The user's distinct ID |
| `name` | string | Yes | `""` | - |
| `resource` | options | No | `"event"` | - |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"create"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `alias`: Alias
- `event`: Event
- `identity`: Identity
- `track`: Track

##### Operation (`operation`)

Optional values:
- `create`: Create - Create an alias

##### Operation (`operation`)

Optional values:
- `create`: Create - Create an event

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
  "name": "PostHog",
  "type": "nodes-base.postHog",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "alias": "",
    "distinctId": "",
    "eventName": "",
    "name": ""
  }
}
```

#### Create Example
```json
{
  "name": "PostHog",
  "type": "nodes-base.postHog",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "alias": "",
    "distinctId": "",
    "eventName": "",
    "name": "",
    "operation": "create"
  }
}
```

---

## Pushbullet

## Basic Information

- Node Type: `nodes-base.pushbullet`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Pushbullet API

### Available Operations

### Create
Create a push
- Value: `create`

### Delete
Delete a push
- Value: `delete`

### Get Many
Get many pushes
- Value: `getAll`

### Update
Update a push
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | URL of the push |
| `value` | string | Yes | `""` | The value to be set depending on the target selected. For example, if the target selected is email then this field would take the email address of the person you are trying to send the push to. |
| `value` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `target` | options | Yes | `"default"` | Define the medium that will be used to send the push |
| `type` | options | Yes | `"note"` | - |
| `title` | string | Yes | `""` | Title of the push |
| `body` | string | Yes | `""` | Body of the push |
| `dismissed` | boolean | Yes | `false` | Whether to mark a push as having been dismissed by the user, will cause any notifications for the push to be hidden if possible |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `pushId` | string | Yes | `""` | - |

#### Property Details

##### Target (`target`)

Define the medium that will be used to send the push

Optional values:
- `channel_tag`: Channel Tag - Send the push to all subscribers to your channel that has this tag
- `default`: Default - Broadcast it to all of the user's devices
- `device_iden`: Device ID - Send the push to a specific device
- `email`: Email - Send the push to this email address

##### Type (`type`)

Optional values:
- `file`: File
- `link`: Link
- `note`: Note

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
  "name": "Pushbullet",
  "type": "nodes-base.pushbullet",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "value": "",
    "target": "default",
    "type": "note",
    "title": "",
    "body": "",
    "dismissed": false,
    "binaryPropertyName": "data",
    "pushId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Pushbullet",
  "type": "nodes-base.pushbullet",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "value": "",
    "target": "default",
    "type": "note",
    "title": "",
    "body": "",
    "dismissed": false,
    "binaryPropertyName": "data",
    "pushId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Pushbullet",
  "type": "nodes-base.pushbullet",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "value": "",
    "target": "default",
    "type": "note",
    "title": "",
    "body": "",
    "dismissed": false,
    "binaryPropertyName": "data",
    "pushId": "",
    "operation": "delete"
  }
}
```

---

## Pushcut

## Basic Information

- Node Type: `nodes-base.pushcut`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Pushcut API

### Available Operations

### Send
Send a notification
- Value: `send`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | No | `"notification"` | - |
| `operation` | options | No | `"send"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `notificationName` | options | No | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

#### Property Details

##### Resource (`resource`)

Optional values:
- `notification`: Notification

##### Operation (`operation`)

Optional values:
- `send`: Send - Send a notification

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: devices - List of devices this notification is sent to. (default is all devices). Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: input - Value that is passed as input to the notification action
- `undefined`: text - Text that is used instead of the one defined in the app
- `undefined`: title - Title that is used instead of the one defined in the app

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
  "name": "Pushcut",
  "type": "nodes-base.pushcut",
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
  "name": "Pushcut",
  "type": "nodes-base.pushcut",
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

---

## Pushover

## Basic Information

- Node Type: `nodes-base.pushover`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Pushover API

### Available Operations

### Push
- Value: `push`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `userKey` | string | Yes | `""` | The user/group key (not e-mail address) of your user (or you), viewable when logged into the <a href="https://pushover.net/">dashboard</a> (often referred to as <code>USER\_KEY</code> in the <a href="https://support.pushover.net/i44-example-code-and-pushover-libraries">libraries</a> and code examples) |
| `message` | string | Yes | `""` | Your message |
| `retry` | number | Yes | `30` | Specifies how often (in seconds) the Pushover servers will send the same notification to the user. This parameter must have a value of at least 30 seconds between retries. |
| `expire` | number | Yes | `30` | Specifies how many seconds your notification will continue to be retried for (every retry seconds) |
| `resource` | options | No | `"message"` | - |
| `operation` | options | No | `"push"` | - |
| `priority` | options | No | `-2` | Send as -2 to generate no notification/alert, -1 to always send as a quiet notification, 1 to display as high-priority and bypass the user's quiet hours, or 2 to also require confirmation from the user |
| `additionalFields` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `message`: Message

##### Operation (`operation`)

Optional values:
- `push`: Push

##### Priority (`priority`)

Send as -2 to generate no notification/alert, -1 to always send as a quiet notification, 1 to display as high-priority and bypass the user's quiet hours, or 2 to also require confirmation from the user

Optional values:
- `-2`: Lowest Priority
- `-1`: Low Priority
- `0`: Normal Priority
- `1`: High Priority
- `2`: Emergency Priority

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: attachmentsUi
- `undefined`: device - Your user's device name to send the message directly to that device, rather than all of the user's devices (multiple devices may be separated by a comma)
- `undefined`: html - Whether to enable messages formatting with HTML tags
- `undefined`: sound - The name of one of the sounds supported by device clients to override the user's default sound choice. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: timestamp - A Unix timestamp of your message's date and time to display to the user, rather than the time your message is received by our API
- `undefined`: title - Your message's title, otherwise your app's name is used
- `undefined`: timestamp - A Unix timestamp of your message's date and time to display to the user, rather than the time your message is received by our API
- `undefined`: url - A supplementary URL to show with your message
- `undefined`: url_title - A title for your supplementary URL, otherwise just the URL is shown

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
  "name": "Pushover",
  "type": "nodes-base.pushover",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "userKey": "",
    "message": "",
    "retry": 30,
    "expire": 30
  }
}
```

#### Push Example
```json
{
  "name": "Pushover",
  "type": "nodes-base.pushover",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "userKey": "",
    "message": "",
    "retry": 30,
    "expire": 30,
    "operation": "push"
  }
}
```

---

## QuestDB

## Basic Information

- Node Type: `nodes-base.questDb`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Get, add and update data in QuestDB

### Available Operations

### Execute Query
Executes a SQL query
- Value: `executeQuery`

### Insert
Insert rows in database
- Value: `insert`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | The SQL query to execute. You can use n8n expressions or $1 and $2 in conjunction with query parameters. |
| `table` | string | Yes | `""` | Name of the table in which to insert data to |
| `operation` | options | No | `"insert"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `schema` | hidden | No | `""` | Name of the schema the table belongs to |
| `columns` | string | No | `""` | Comma-separated list of the properties which should used as columns for the new rows |
| `returnFields` | string | No | `"*"` | Comma-separated list of the fields that the operation will return |
| `additionalFields` | hidden | No | `{}` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `executeQuery`: Execute Query - Executes a SQL query
- `insert`: Insert - Insert rows in database

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: mode - The way queries should be sent to database. Can be used in conjunction with \<b\>Continue on Fail\</b\>. See \<a href="https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.questdb/"\>the docs\</a\> for more examples.
- `undefined`: queryParams - Comma-separated list of properties which should be used as query parameters

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
  "name": "QuestDB",
  "type": "nodes-base.questDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "table": ""
  }
}
```

#### Execute Query Example
```json
{
  "name": "QuestDB",
  "type": "nodes-base.questDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "table": "",
    "operation": "executeQuery"
  }
}
```

#### Insert Example
```json
{
  "name": "QuestDB",
  "type": "nodes-base.questDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "table": "",
    "operation": "insert"
  }
}
```

---

## Quick Base

## Basic Information

- Node Type: `nodes-base.quickbase`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Integrate with the Quick Base RESTful API

### Available Operations

### Get Many
Get many fields
- Value: `getAll`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `tableId` | string | Yes | `""` | The table identifier |
| `tableId` | string | Yes | `""` | The table identifier |
| `recordId` | string | Yes | `""` | The unique identifier of the record |
| `fieldId` | string | Yes | `""` | The unique identifier of the field |
| `versionNumber` | number | Yes | `1` | The file attachment version number |
| `tableId` | string | Yes | `""` | The table identifier |
| `columns` | string | Yes | `""` | Comma-separated list of the properties which should used as columns for the new rows |
| `tableId` | string | Yes | `""` | The table identifier |
| `where` | string | Yes | `""` | The filter to delete records. To delete all records specify a filter that will include all records, for example {3.GT.0} where 3 is the ID of the Record ID field. |
| `tableId` | string | Yes | `""` | The table identifier |

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
  "name": "Quick Base",
  "type": "nodes-base.quickbase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "tableId": "",
    "recordId": "",
    "fieldId": "",
    "versionNumber": 1,
    "columns": "",
    "where": ""
  }
}
```

#### Get Many Example
```json
{
  "name": "Quick Base",
  "type": "nodes-base.quickbase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "tableId": "",
    "recordId": "",
    "fieldId": "",
    "versionNumber": 1,
    "columns": "",
    "where": "",
    "operation": "getAll"
  }
}
```

---

## Read Binary File

## Basic Information

- Node Type: `nodes-base.readBinaryFile`
- Category: input
- Package: n8n-nodes-base

### Description

Reads a binary file from disk

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `filePath` | string | Yes | `""` | Path of the file to read |
| `dataPropertyName` | string | Yes | `"data"` | Name of the binary property to which to write the data of the read file |

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
  "name": "Read Binary File",
  "type": "nodes-base.readBinaryFile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "filePath": "",
    "dataPropertyName": "data"
  }
}
```

---

## Read Binary Files

## Basic Information

- Node Type: `nodes-base.readBinaryFiles`
- Category: input
- Package: n8n-nodes-base

### Description

Reads binary files from disk

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `fileSelector` | string | Yes | `""` | Pattern for files to read |
| `dataPropertyName` | string | Yes | `"data"` | Name of the binary property to which to write the data of the read files |

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
  "name": "Read Binary Files",
  "type": "nodes-base.readBinaryFiles",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fileSelector": "",
    "dataPropertyName": "data"
  }
}
```

---

## Read PDF

## Basic Information

- Node Type: `nodes-base.readPDF`
- Category: input
- Package: n8n-nodes-base

### Description

Reads a PDF and extracts its content

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `binaryPropertyName` | string | Yes | `"data"` | Name of the binary property from which to read the PDF file |
| `encrypted` | boolean | Yes | `false` | - |
| `password` | string | No | `""` | Password to decrypt the PDF file with |

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
  "name": "Read PDF",
  "type": "nodes-base.readPDF",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryPropertyName": "data",
    "encrypted": false
  }
}
```

---

## Read/Write Files from Disk

## Basic Information

- Node Type: `nodes-base.readWriteFile`
- Category: input
- Package: n8n-nodes-base

### Description

Read or write files from the computer that runs n8n

### Available Operations

### Read File(s) From Disk
Retrieve one or more files from the computer that runs n8n
- Value: `read`

### Write File to Disk
Create a binary file on the computer that runs n8n
- Value: `write`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `fileSelector` | string | Yes | `""` | Specify a file's path or path pattern to read multiple files. Always use forward-slashes for path separator even on Windows. |
| `fileName` | string | Yes | `""` | Path and name of the file that should be written. Also include the file extension. |
| `dataPropertyName` | string | Yes | `"data"` | - |
| `operation` | options | No | `"read"` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `info` | notice | No | `""` | - |

#### Property Details

##### Operation (`operation`)

Optional values:
- `read`: Read File(s) From Disk - Retrieve one or more files from the computer that runs n8n
- `write`: Write File to Disk - Create a binary file on the computer that runs n8n

##### Options (`options`)

Optional values:
- `undefined`: fileExtension - Extension of the file in the output binary
- `undefined`: fileName - Name of the file in the output binary
- `undefined`: mimeType - Mime type of the file in the output binary
- `undefined`: dataPropertyName - By default 'data' is used

##### Options (`options`)

Optional values:
- `undefined`: append - Whether to append to an existing file. While it's commonly used with text files, it's not limited to them, however, it wouldn't be applicable for file types that have a specific structure like most binary formats.

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
  "name": "Read/Write Files from Disk",
  "type": "nodes-base.readWriteFile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fileSelector": "",
    "fileName": "",
    "dataPropertyName": "data"
  }
}
```

#### Read File(s) From Disk Example
```json
{
  "name": "Read/Write Files from Disk",
  "type": "nodes-base.readWriteFile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fileSelector": "",
    "fileName": "",
    "dataPropertyName": "data",
    "operation": "read"
  }
}
```

#### Write File to Disk Example
```json
{
  "name": "Read/Write Files from Disk",
  "type": "nodes-base.readWriteFile",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fileSelector": "",
    "fileName": "",
    "dataPropertyName": "data",
    "operation": "write"
  }
}
```

---

## Redis

## Basic Information

- Node Type: `nodes-base.redis`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Get, send and update data in Redis

### Available Operations

### Delete
Delete a key from Redis
- Value: `delete`

### Get
Get the value of a key from Redis
- Value: `get`

### Increment
Atomically increments a key by 1. Creates the key if it does not exist.
- Value: `incr`

### Info
Returns generic information about the Redis instance
- Value: `info`

### Keys
Returns all the keys matching a pattern
- Value: `keys`

### List Length
Returns the length of a list
- Value: `llen`

### Pop
Pop data from a redis list
- Value: `pop`

### Publish
Publish message to redis channel
- Value: `publish`

### Push
Push data to a redis list
- Value: `push`

### Set
Set the value of a key in redis
- Value: `set`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `key` | string | Yes | `""` | Name of the key to delete from Redis |
| `propertyName` | string | Yes | `"propertyName"` | Name of the property to write received data to. Supports dot-notation. Example: "data.person[0].name". |
| `key` | string | Yes | `""` | Name of the key to get from Redis |
| `key` | string | Yes | `""` | Name of the key to increment |
| `keyPattern` | string | Yes | `""` | The key pattern for the keys to return |
| `list` | string | Yes | `""` | Name of the list in Redis |
| `list` | string | Yes | `""` | Name of the list in Redis |
| `key` | string | Yes | `""` | Name of the key to set in Redis |
| `channel` | string | Yes | `""` | Channel name |
| `messageData` | string | Yes | `""` | Data to publish |

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
  "name": "Redis",
  "type": "nodes-base.redis",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "key": "",
    "propertyName": "propertyName",
    "keyPattern": "",
    "list": "",
    "channel": "",
    "messageData": ""
  }
}
```

#### Delete Example
```json
{
  "name": "Redis",
  "type": "nodes-base.redis",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "key": "",
    "propertyName": "propertyName",
    "keyPattern": "",
    "list": "",
    "channel": "",
    "messageData": "",
    "operation": "delete"
  }
}
```

#### Get Example
```json
{
  "name": "Redis",
  "type": "nodes-base.redis",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "key": "",
    "propertyName": "propertyName",
    "keyPattern": "",
    "list": "",
    "channel": "",
    "messageData": "",
    "operation": "get"
  }
}
```

---

## Respond to Chat

## Basic Information

- Node Type: `nodes-langchain.chat`
- Category: input
- Package: @n8n/n8n-nodes-langchain

### Description

Send a message to a chat

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `message` | string | Yes | `""` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `generalNotice` | notice | No | `""` | - |
| `waitUserReply` | boolean | No | `true` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: memoryConnection
- `undefined`: limitWaitTime - Whether to limit the time this node should wait for a user response before execution resumes

##### Options (`options`)

Optional values:
- `undefined`: limitWaitTime - Whether to limit the time this node should wait for a user response before execution resumes

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
  "name": "Respond to Chat",
  "type": "nodes-langchain.chat",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "message": ""
  }
}
```

---

## RSS Read

## Basic Information

- Node Type: `nodes-base.rssFeedRead`
- Category: input
- Package: n8n-nodes-base

### Description

Reads data from an RSS Feed

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | URL of the RSS feed |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: customFields - A comma-separated list of custom fields to include in the output. For example, "author, contentSnippet".
- `undefined`: ignoreSSL - Whether to ignore SSL/TLS certificate issues or not

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
  "name": "RSS Read",
  "type": "nodes-base.rssFeedRead",
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

---

## Sendy

## Basic Information

- Node Type: `nodes-base.sendy`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Sendy API

### Available Operations

### Create
Create a campaign
- Value: `create`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `brandId` | string | Yes | `""` | - |
| `resource` | options | No | `"subscriber"` | - |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"add"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |
| `fromName` | string | No | `""` | The 'From name' of your campaign |
| `fromEmail` | string | No | `""` | The 'From email' of your campaign |
| `replyTo` | string | No | `""` | The 'Reply to' of your campaign |
| `title` | string | No | `""` | The 'Title' of your campaign |

#### Property Details

##### Resource (`resource`)

Optional values:
- `campaign`: Campaign
- `subscriber`: Subscriber

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a campaign

##### Operation (`operation`)

Optional values:
- `add`: Add - Add a subscriber to a list
- `count`: Count - Count subscribers
- `delete`: Delete - Delete a subscriber from a list
- `remove`: Remove - Unsubscribe user from a list
- `status`: Status - Get the status of subscriber

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: excludeListIds - Lists to exclude from your campaign. List IDs should be single or comma-separated.
- `undefined`: excludeSegmentIds - Segments to exclude from your campaign. Segment IDs should be single or comma-separated.
- `undefined`: listIds - List IDs should be single or comma-separated
- `undefined`: plainText - The 'Plain text version' of your campaign
- `undefined`: queryString - Google Analytics tags
- `undefined`: segmentIds - Segment IDs should be single or comma-separated
- `undefined`: trackClicks - Whether to disable clicks tracking. Default is true.
- `undefined`: trackOpens - Whether to disable opens tracking. Default is true.

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: country - User's 2 letter country code
- `undefined`: gdpr - Whether you're signing up EU users in a GDPR compliant manner
- `undefined`: hp - Include this 'honeypot' field to prevent spambots from signing up via this API call. When spambots fills in this field, this API call will exit, preventing them from signing up fake addresses to your form. This parameter is only supported in Sendy 3.0 onwards.
- `undefined`: ipaddress - User's IP address
- `undefined`: name - User's name
- `undefined`: referrer - The URL where the user signed up from
- `undefined`: silent - Set to "true" if your list is 'Double opt-in' but you want to bypass that and signup the user to the list as 'Single Opt-in instead' (optional)

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
  "name": "Sendy",
  "type": "nodes-base.sendy",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "brandId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Sendy",
  "type": "nodes-base.sendy",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "brandId": "",
    "operation": "create"
  }
}
```

---

## Snowflake

## Basic Information

- Node Type: `nodes-base.snowflake`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Get, add and update data in Snowflake

### Available Operations

### Execute Query
Execute an SQL query
- Value: `executeQuery`

### Insert
Insert rows in database
- Value: `insert`

### Update
Update rows in database
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | The SQL query to execute |
| `table` | string | Yes | `""` | Name of the table in which to insert data to |
| `table` | string | Yes | `""` | Name of the table in which to update data in |
| `updateKey` | string | Yes | `"id"` | Name of the property which decides which rows in the database should be updated. Normally that would be "id". |
| `operation` | options | No | `"insert"` | - |
| `columns` | string | No | `""` | Comma-separated list of the properties which should used as columns for the new rows |
| `columns` | string | No | `""` | Comma-separated list of the properties which should used as columns for rows to update |

#### Property Details

##### Operation (`operation`)

Optional values:
- `executeQuery`: Execute Query - Execute an SQL query
- `insert`: Insert - Insert rows in database
- `update`: Update - Update rows in database

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
  "name": "Snowflake",
  "type": "nodes-base.snowflake",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "table": "",
    "updateKey": "id"
  }
}
```

#### Execute Query Example
```json
{
  "name": "Snowflake",
  "type": "nodes-base.snowflake",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "table": "",
    "updateKey": "id",
    "operation": "executeQuery"
  }
}
```

#### Insert Example
```json
{
  "name": "Snowflake",
  "type": "nodes-base.snowflake",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "table": "",
    "updateKey": "id",
    "operation": "insert"
  }
}
```

---

## Spotify

## Basic Information

- Node Type: `nodes-base.spotify`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Access public song data via the Spotify API

### Available Operations

### Add Song to Queue
Add a song to your queue
- Value: `addSongToQueue`

### Currently Playing
Get your currently playing track
- Value: `currentlyPlaying`

### Next Song
Skip to your next track
- Value: `nextSong`

### Pause
Pause your music
- Value: `pause`

### Previous Song
Skip to your previous song
- Value: `previousSong`

### Recently Played
Get your recently played tracks
- Value: `recentlyPlayed`

### Resume
Resume playback on the current active device
- Value: `resume`

### Set Volume
Set volume on the current active device
- Value: `volume`

### Start Music
Start playing a playlist, artist, or album
- Value: `startMusic`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | The keyword term to search for |
| `query` | string | Yes | `""` | The keyword term to search for |
| `query` | string | Yes | `""` | The keyword term to search for |
| `query` | string | Yes | `""` | The keyword term to search for |
| `id` | string | Yes | `""` | Enter a playlist, artist, or album URI or ID |
| `id` | string | Yes | `""` | Enter a track URI or ID |
| `id` | string | Yes | `""` | The album's Spotify URI or ID |
| `id` | string | Yes | `""` | The artist's Spotify URI or ID |
| `country` | string | Yes | `"US"` | Top tracks in which country? Enter the postal abbreviation |
| `id` | string | Yes | `""` | The playlist's Spotify URI or its ID |

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
  "name": "Spotify",
  "type": "nodes-base.spotify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "id": "",
    "country": "US"
  }
}
```

#### Add Song to Queue Example
```json
{
  "name": "Spotify",
  "type": "nodes-base.spotify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "id": "",
    "country": "US",
    "operation": "addSongToQueue"
  }
}
```

#### Currently Playing Example
```json
{
  "name": "Spotify",
  "type": "nodes-base.spotify",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "id": "",
    "country": "US",
    "operation": "currentlyPlaying"
  }
}
```

---

## SSH

## Basic Information

- Node Type: `nodes-base.ssh`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Execute commands via SSH

### Available Operations

### Execute
Execute a command
- Value: `execute`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `path` | string | Yes | `""` | The directory to upload the file to. The name of the file does not need to be specified, it's taken from the binary data file name. To override this behavior, set the parameter "File Name" under options. |
| `path` | string | Yes | `""` | The file path of the file to download. Has to contain the full path including file name. |
| `binaryPropertyName` | string | Yes | `"data"` | Object property name which holds binary data |
| `cwd` | string | Yes | `"/"` | - |
| `binaryPropertyName` | string | Yes | `"data"` | - |
| `authentication` | options | No | `"password"` | - |
| `resource` | options | No | `"command"` | - |
| `operation` | options | No | `"execute"` | - |
| `operation` | options | No | `"upload"` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `password`: Password
- `privateKey`: Private Key

##### Resource (`resource`)

Optional values:
- `command`: Command
- `file`: File

##### Operation (`operation`)

Optional values:
- `execute`: Execute - Execute a command

##### Operation (`operation`)

Optional values:
- `download`: Download - Download a file
- `upload`: Upload - Upload a file

##### Options (`options`)

Optional values:
- `undefined`: fileName - Overrides the binary data file name

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
  "name": "SSH",
  "type": "nodes-base.ssh",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "path": "",
    "binaryPropertyName": "data",
    "cwd": "/"
  }
}
```

#### Execute Example
```json
{
  "name": "SSH",
  "type": "nodes-base.ssh",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "path": "",
    "binaryPropertyName": "data",
    "cwd": "/",
    "operation": "execute"
  }
}
```

---

## Start

## Basic Information

- Node Type: `nodes-base.start`
- Category: input
- Package: n8n-nodes-base

### Description

Starts the workflow execution from this node

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `notice` | notice | No | `""` | - |

### Connection Guide

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
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Start",
  "type": "nodes-base.start",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Sticky Note

## Basic Information

- Node Type: `nodes-base.stickyNote`
- Category: input
- Package: n8n-nodes-base

### Description

Make your workflow easier to understand

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `height` | number | Yes | `160` | - |
| `width` | number | Yes | `240` | - |
| `color` | number | Yes | `1` | - |
| `content` | string | No | `"## I'm a note \n**Double click** to edit me. [Guide](https://docs.n8n.io/workflows/components/sticky-notes/)"` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Sticky Note",
  "type": "nodes-base.stickyNote",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "height": 160,
    "width": 240,
    "color": 1
  }
}
```

---

## Stop and Error

## Basic Information

- Node Type: `nodes-base.stopAndError`
- Category: input
- Package: n8n-nodes-base

### Description

Throw an error in the workflow

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `errorObject` | json | Yes | `""` | Object containing error properties |
| `errorMessage` | string | Yes | `""` | - |
| `errorType` | options | No | `"errorMessage"` | Type of error to throw |

#### Property Details

##### Error Type (`errorType`)

Type of error to throw

Optional values:
- `errorMessage`: Error Message
- `errorObject`: Error Object

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)

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
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Stop and Error",
  "type": "nodes-base.stopAndError",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "errorObject": "",
    "errorMessage": ""
  }
}
```

---

## Strapi

## Basic Information

- Node Type: `nodes-base.strapi`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Strapi API

### Available Operations

### Create
Create an entry
- Value: `create`

### Delete
Delete an entry
- Value: `delete`

### Get
Get an entry
- Value: `get`

### Get Many
Get many entries
- Value: `getAll`

### Update
Update an entry
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `contentType` | string | Yes | `""` | Name of the content type |
| `contentType` | string | Yes | `""` | Name of the content type |
| `entryId` | string | Yes | `""` | The ID of the entry to delete |
| `contentType` | string | Yes | `""` | Name of the content type |
| `entryId` | string | Yes | `""` | The ID of the entry to get |
| `contentType` | string | Yes | `""` | Name of the content type |
| `contentType` | string | Yes | `""` | Name of the content type |
| `updateKey` | string | Yes | `"id"` | Name of the property which decides which rows in the database should be updated. Normally that would be "id". |
| `authentication` | options | No | `"password"` | - |
| `resource` | options | No | `"entry"` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `password`: Username & Password
- `token`: API Token

##### Resource (`resource`)

Optional values:
- `entry`: Entry

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
  "name": "Strapi",
  "type": "nodes-base.strapi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contentType": "",
    "entryId": "",
    "updateKey": "id"
  }
}
```

#### Create Example
```json
{
  "name": "Strapi",
  "type": "nodes-base.strapi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contentType": "",
    "entryId": "",
    "updateKey": "id",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Strapi",
  "type": "nodes-base.strapi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "contentType": "",
    "entryId": "",
    "updateKey": "id",
    "operation": "delete"
  }
}
```

---

## Strava

## Basic Information

- Node Type: `nodes-base.strava`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Strava API

### Available Operations

### Create
Create a new activity
- Value: `create`

### Get
Get an activity
- Value: `get`

### Get Comments
Get all activity comments
- Value: `getComments`

### Get Kudos
Get all activity kudos
- Value: `getKudos`

### Get Laps
Get all activity laps
- Value: `getLaps`

### Get Many
Get many activities
- Value: `getAll`

### Get Streams
Get activity streams
- Value: `getStreams`

### Get Zones
Get all activity zones
- Value: `getZones`

### Update
Update an activity
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `keys` | multiOptions | Yes | `[]` | Desired stream types to return |
| `name` | string | Yes | `""` | The name of the activity |
| `type` | string | Yes | `""` | Type of activity. For example - Run, Ride etc. |
| `startDate` | dateTime | Yes | `""` | ISO 8601 formatted date time |
| `elapsedTime` | number | Yes | `0` | In seconds |
| `activityId` | string | Yes | `""` | ID or email of activity |
| `activityId` | string | Yes | `""` | ID or email of activity |
| `activityId` | string | Yes | `""` | ID or email of activity |
| `resource` | options | No | `"activity"` | - |
| `operation` | options | No | `"create"` | - |

#### Property Details

##### Keys (`keys`)

Desired stream types to return

Optional values:
- `altitude`: Altitude
- `cadence`: Cadence
- `distance`: Distance
- `grade_smooth`: Gradient
- `heartrate`: Heartrate
- `latlng`: Latitude / Longitude
- `moving`: Moving
- `temp`: Temperature
- `time`: Time
- `velocity_smooth`: Velocity
- `watts`: Watts

##### Resource (`resource`)

Optional values:
- `activity`: Activity

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new activity
- `get`: Get - Get an activity
- `getComments`: Get Comments - Get all activity comments
- `getKudos`: Get Kudos - Get all activity kudos
- `getLaps`: Get Laps - Get all activity laps
- `getAll`: Get Many - Get many activities
- `getStreams`: Get Streams - Get activity streams
- `getZones`: Get Zones - Get all activity zones
- `update`: Update - Update an activity

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
  "name": "Strava",
  "type": "nodes-base.strava",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "keys": [],
    "name": "",
    "type": "",
    "startDate": "",
    "elapsedTime": 0,
    "activityId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Strava",
  "type": "nodes-base.strava",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "keys": [],
    "name": "",
    "type": "",
    "startDate": "",
    "elapsedTime": 0,
    "activityId": "",
    "operation": "create"
  }
}
```

#### Get Example
```json
{
  "name": "Strava",
  "type": "nodes-base.strava",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "keys": [],
    "name": "",
    "type": "",
    "startDate": "",
    "elapsedTime": 0,
    "activityId": "",
    "operation": "get"
  }
}
```

---

## Supabase

## Basic Information

- Node Type: `nodes-base.supabase`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Add, get, delete and update data in a table

### Available Operations

### Create
Create a new row
- Value: `create`

### Delete
Delete a row
- Value: `delete`

### Get
Get a row
- Value: `get`

### Get Many
Get many rows
- Value: `getAll`

### Update
Update a row
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `tableId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `resource` | options | No | `"row"` | - |
| `operation` | options | No | `"create"` | - |
| `filters` | fixedCollection | No | `{}` | Filter to decide which rows get updated |
| `filters` | fixedCollection | No | `{}` | Filter to decide which rows get deleted |
| `filters` | fixedCollection | No | `{}` | Filter to decide which rows get retrieved |
| `filterType` | options | No | `"manual"` | - |
| `matchType` | options | No | `"anyFilter"` | - |
| `dataToSend` | options | No | `"defineBelow"` | - |
| `fieldsUi` | fixedCollection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `row`: Row

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a new row
- `delete`: Delete - Delete a row
- `get`: Get - Get a row
- `getAll`: Get Many - Get many rows
- `update`: Update - Update a row

##### Select Conditions (`filters`)

Filter to decide which rows get updated

Optional values:
- `undefined`: conditions

##### Select Conditions (`filters`)

Filter to decide which rows get deleted

Optional values:
- `undefined`: conditions

##### Filters (`filters`)

Filter to decide which rows get retrieved

Optional values:
- `undefined`: conditions

##### Select Type (`filterType`)

Optional values:
- `manual`: Build Manually
- `string`: String

##### Must Match (`matchType`)

Optional values:
- `anyFilter`: Any Select Condition
- `allFilters`: All Select Conditions

##### Data to Send (`dataToSend`)

Optional values:
- `autoMapInputData`: Auto-Map Input Data to Columns - Use when node input properties match destination column names
- `defineBelow`: Define Below for Each Column - Set the value for each destination column

##### Fields to Send (`fieldsUi`)

Optional values:
- `undefined`: fieldValues

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
  "name": "Supabase",
  "type": "nodes-base.supabase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "tableId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Supabase",
  "type": "nodes-base.supabase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "tableId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Supabase",
  "type": "nodes-base.supabase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "tableId": "",
    "operation": "delete"
  }
}
```

---

## TimescaleDB

## Basic Information

- Node Type: `nodes-base.timescaleDb`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Add and update data in TimescaleDB

### Available Operations

### Execute Query
Execute an SQL query
- Value: `executeQuery`

### Insert
Insert rows in database
- Value: `insert`

### Update
Update rows in database
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | The SQL query to execute. You can use n8n expressions or $1 and $2 in conjunction with query parameters. |
| `schema` | string | Yes | `"public"` | Name of the schema the table belongs to |
| `table` | string | Yes | `""` | Name of the table in which to insert data to |
| `schema` | string | Yes | `"public"` | Name of the schema the table belongs to |
| `table` | string | Yes | `""` | Name of the table in which to update data in |
| `updateKey` | string | Yes | `"id"` | Name of the property which decides which rows in the database should be updated. Normally that would be "id". |
| `operation` | options | No | `"insert"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `columns` | string | No | `""` | Comma-separated list of the properties which should used as columns for the new rows |
| `columns` | string | No | `""` | Comma-separated list of the properties which should used as columns for rows to update |

#### Property Details

##### Operation (`operation`)

Optional values:
- `executeQuery`: Execute Query - Execute an SQL query
- `insert`: Insert - Insert rows in database
- `update`: Update - Update rows in database

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: mode - The way queries should be sent to database. Can be used in conjunction with \<b\>Continue on Fail\</b\>. See \<a href="https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb/"\>the docs\</a\> for more examples
- `undefined`: queryParams - Comma-separated list of properties which should be used as query parameters

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
  "name": "TimescaleDB",
  "type": "nodes-base.timescaleDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "schema": "public",
    "table": "",
    "updateKey": "id"
  }
}
```

#### Execute Query Example
```json
{
  "name": "TimescaleDB",
  "type": "nodes-base.timescaleDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "schema": "public",
    "table": "",
    "updateKey": "id",
    "operation": "executeQuery"
  }
}
```

#### Insert Example
```json
{
  "name": "TimescaleDB",
  "type": "nodes-base.timescaleDb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "schema": "public",
    "table": "",
    "updateKey": "id",
    "operation": "insert"
  }
}
```

---

## Twist

## Basic Information

- Node Type: `nodes-base.twist`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Twist API

### Available Operations

### Archive
Archive a channel
- Value: `archive`

### Create
Initiates a public or private channel-based conversation
- Value: `create`

### Delete
Delete a channel
- Value: `delete`

### Get
Get information about a channel
- Value: `get`

### Get Many
Get many channels
- Value: `getAll`

### Unarchive
Unarchive a channel
- Value: `unarchive`

### Update
Update a channel
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `workspaceId` | options | Yes | `""` | The ID of the workspace. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `name` | string | Yes | `""` | The name of the channel |
| `channelId` | string | Yes | `""` | The ID of the channel |
| `workspaceId` | options | Yes | `""` | The ID of the workspace. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `channelId` | string | Yes | `""` | The ID of the channel |
| `threadId` | string | Yes | `""` | The ID of the thread |
| `content` | string | Yes | `""` | The content of the comment |
| `commentId` | string | Yes | `""` | The ID of the comment |
| `threadId` | string | Yes | `""` | The ID of the channel |
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
  "name": "Twist",
  "type": "nodes-base.twist",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workspaceId": "",
    "name": "",
    "channelId": "",
    "threadId": "",
    "content": "",
    "commentId": ""
  }
}
```

#### Archive Example
```json
{
  "name": "Twist",
  "type": "nodes-base.twist",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workspaceId": "",
    "name": "",
    "channelId": "",
    "threadId": "",
    "content": "",
    "commentId": "",
    "operation": "archive"
  }
}
```

#### Create Example
```json
{
  "name": "Twist",
  "type": "nodes-base.twist",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workspaceId": "",
    "name": "",
    "channelId": "",
    "threadId": "",
    "content": "",
    "commentId": "",
    "operation": "create"
  }
}
```

---

## Venafi TLS Protect Cloud

## Basic Information

- Node Type: `nodes-base.venafiTlsProtectCloud`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Venafi TLS Protect Cloud API

### Available Operations

### Delete
Delete a certificate
- Value: `delete`

### Download
Download a certificate
- Value: `download`

### Get
Retrieve a certificate
- Value: `get`

### Get Many
Retrieve many certificates
- Value: `getMany`

### Renew
Renew a certificate
- Value: `renew`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `binaryProperty` | string | Yes | `"data"` | The name of the input field containing the binary file data to be uploaded |
| `commonName` | string | Yes | `"n8n.io"` | The Common Name field for the certificate Subject (CN) |
| `certificateId` | string | Yes | `""` | - |
| `certificateLabel` | string | Yes | `""` | - |
| `privateKeyPassphrase` | string | Yes | `""` | - |
| `keystorePassphrase` | string | Yes | `""` | - |
| `certificateId` | string | Yes | `""` | - |
| `certificateRequestId` | string | Yes | `""` | - |
| `resource` | options | No | `"certificateRequest"` | - |
| `operation` | options | No | `"delete"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `certificate`: Certificate
- `certificateRequest`: Certificate Request

##### Operation (`operation`)

Optional values:
- `delete`: Delete - Delete a certificate
- `download`: Download - Download a certificate
- `get`: Get - Retrieve a certificate
- `getMany`: Get Many - Retrieve many certificates
- `renew`: Renew - Renew a certificate

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
  "name": "Venafi TLS Protect Cloud",
  "type": "nodes-base.venafiTlsProtectCloud",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryProperty": "data",
    "commonName": "n8n.io",
    "certificateId": "",
    "certificateLabel": "",
    "privateKeyPassphrase": "",
    "keystorePassphrase": "",
    "certificateRequestId": ""
  }
}
```

#### Delete Example
```json
{
  "name": "Venafi TLS Protect Cloud",
  "type": "nodes-base.venafiTlsProtectCloud",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryProperty": "data",
    "commonName": "n8n.io",
    "certificateId": "",
    "certificateLabel": "",
    "privateKeyPassphrase": "",
    "keystorePassphrase": "",
    "certificateRequestId": "",
    "operation": "delete"
  }
}
```

#### Download Example
```json
{
  "name": "Venafi TLS Protect Cloud",
  "type": "nodes-base.venafiTlsProtectCloud",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryProperty": "data",
    "commonName": "n8n.io",
    "certificateId": "",
    "certificateLabel": "",
    "privateKeyPassphrase": "",
    "keystorePassphrase": "",
    "certificateRequestId": "",
    "operation": "download"
  }
}
```

---

## Venafi TLS Protect Datacenter

## Basic Information

- Node Type: `nodes-base.venafiTlsProtectDatacenter`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Venafi TLS Protect Datacenter

### Available Operations

### Create
Provision a new certificate
- Value: `create`

### Delete
Delete a certificate
- Value: `delete`

### Download
Download a certificate
- Value: `download`

### Get
Retrieve a certificate
- Value: `get`

### Get Many
Retrieve many certificates
- Value: `getMany`

### Renew
Renew a certificate
- Value: `renew`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `binaryProperty` | string | Yes | `"data"` | The name of the input field containing the binary file data to be uploaded |
| `certificateId` | string | Yes | `""` | A GUID that uniquely identifies the certificate |
| `certificateDN` | string | Yes | `""` | The Distinguished Name (DN) of the certificate to renew |
| `policyDn` | string | Yes | `""` | The Distinguished Name (DN) of the policy folder |
| `certificateDn` | string | Yes | `""` | - |
| `password` | string | Yes | `""` | - |
| `resource` | options | No | `"certificate"` | - |
| `operation` | options | No | `"create"` | - |
| `operation` | options | No | `"get"` | - |
| `additionalFields` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `certificate`: Certificate
- `policy`: Policy

##### Operation (`operation`)

Optional values:
- `create`: Create - Provision a new certificate
- `delete`: Delete - Delete a certificate
- `download`: Download - Download a certificate
- `get`: Get - Retrieve a certificate
- `getMany`: Get Many - Retrieve many certificates
- `renew`: Renew - Renew a certificate

##### Operation (`operation`)

Optional values:
- `get`: Get - Get a policy

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: Approvers - An array of one or more identities for certificate workflow approvers
- `undefined`: CADN - Only required when no policy sets a CA template. The Distinguished Name (DN) of the Trust Protection Platform Certificate Authority Template object for enrolling the certificate.
- `undefined`: CertificateType - One of the following Certificate objects. Ignores any other value.
- `undefined`: City - The City field for the certificate Subject DN. Specify a value when requesting a centrally generated CSR.
- `undefined`: Contacts - An array of one or more identities for users or groups who receive notifications about events pertaining to the object
- `undefined`: Country - The Country field for the certificate Subject DN. Specify a value when requesting a centrally generated CSR.
- `undefined`: customFieldsUi
- `undefined`: CreatedBy - The person, entity, or caller of this request. The default is Web SDK. Avoid overriding the default unless the caller is a significant enterprise application that is tightly integrated with Trust Protection Platform, such as a custom web portal. To add details, use Origin instead. If you want both attributes to have the same value, set only CreatedBy.
- `undefined`: Devices
- `undefined`: DisableAutomaticRenewal - The setting to control whether manual intervention is required for certificate renewal
- `undefined`: EllipticCurve - For Elliptic Curve Cryptography (ECC), use this parameter in conjunction with KeyAlgorithm
- `undefined`: KeyAlgorithm - The encryption algorithm for the public ke:
- `undefined`: KeyBitSize - Use this parameter when KeyAlgorithm is RSA. The number of bits to allow for key generation.
- `undefined`: ManagementType - The level of management that Trust Protection Platform applies to the certificate
- `undefined`: origin - Additional information, such as the name and version of the calling application, that describes the source of this enrollment, renewal, or provisioning request. The default is Web SDK.
- `undefined`: Organization - The Organization field for the certificate Subject DN. Specify a value when the CSR centrally generates.
- `undefined`: OrganizationalUnit - The department or division within the organization that is responsible for maintaining the certificate
- `undefined`: PKCS10 - The PKCS#10 Certificate Signing Request (CSR). Omit escape characters such as or . If this value is provided, any Subject DN fields and the KeyBitSize in the request are ignored.
- `undefined`: Reenable - The action to control a previously disabled certificate
- `undefined`: SetWorkToDo - The setting to control certificate processing
- `undefined`: State - The State field for the certificate Subject DN. Specify a value when requesting a centrally generated CSR.
- `undefined`: SubjectAltNamesUi

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
  "name": "Venafi TLS Protect Datacenter",
  "type": "nodes-base.venafiTlsProtectDatacenter",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryProperty": "data",
    "certificateId": "",
    "certificateDN": "",
    "policyDn": "",
    "certificateDn": "",
    "password": ""
  }
}
```

#### Create Example
```json
{
  "name": "Venafi TLS Protect Datacenter",
  "type": "nodes-base.venafiTlsProtectDatacenter",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryProperty": "data",
    "certificateId": "",
    "certificateDN": "",
    "policyDn": "",
    "certificateDn": "",
    "password": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Venafi TLS Protect Datacenter",
  "type": "nodes-base.venafiTlsProtectDatacenter",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "binaryProperty": "data",
    "certificateId": "",
    "certificateDN": "",
    "policyDn": "",
    "certificateDn": "",
    "password": "",
    "operation": "delete"
  }
}
```

---

## Vonage

## Basic Information

- Node Type: `nodes-base.vonage`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Vonage API

### Available Operations

### Send
- Value: `send`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | No | `"sms"` | - |
| `operation` | options | No | `"send"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `from` | string | No | `""` | The name or number the message should be sent from |
| `to` | string | No | `""` | The number that the message should be sent to. Numbers are specified in E.164 format. |
| `message` | string | No | `""` | The body of the message being sent |

#### Property Details

##### Resource (`resource`)

Optional values:
- `sms`: SMS

##### Operation (`operation`)

Optional values:
- `send`: Send

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: account-ref - An optional string used to identify separate accounts using the SMS endpoint for billing purposes. To use this feature, please email support@nexmo.com.
- `undefined`: callback - The webhook endpoint the delivery receipt for this sms is sent to. This parameter overrides the webhook endpoint you set in Dashboard.
- `undefined`: client-ref - You can optionally include your own reference of up to 40 characters
- `undefined`: message-class - The Data Coding Scheme value of the message
- `undefined`: protocol-id - The value of the protocol identifier to use. Ensure that the value is aligned with udh.
- `undefined`: status-report-req - Whether to receive a Delivery Receipt
- `undefined`: ttl - By default Nexmo attempt delivery for 72 hours

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
  "name": "Vonage",
  "type": "nodes-base.vonage",
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
  "name": "Vonage",
  "type": "nodes-base.vonage",
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

---

## Yourls

## Basic Information

- Node Type: `nodes-base.yourls`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Yourls API

### Available Operations

### Expand
Expand a URL
- Value: `expand`

### Shorten
Shorten a URL
- Value: `shorten`

### Stats
Get stats about one short URL
- Value: `stats`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | The URL to shorten |
| `shortUrl` | string | Yes | `""` | The short URL to expand |
| `shortUrl` | string | Yes | `""` | The short URL for which to get stats |
| `resource` | options | No | `"url"` | - |
| `operation` | options | No | `"shorten"` | - |
| `additionalFields` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `url`: URL

##### Operation (`operation`)

Optional values:
- `expand`: Expand - Expand a URL
- `shorten`: Shorten - Shorten a URL
- `stats`: Stats - Get stats about one short URL

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: keyword
- `undefined`: title - Title for custom short URLs

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
  "name": "Yourls",
  "type": "nodes-base.yourls",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "shortUrl": ""
  }
}
```

#### Expand Example
```json
{
  "name": "Yourls",
  "type": "nodes-base.yourls",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "shortUrl": "",
    "operation": "expand"
  }
}
```

#### Shorten Example
```json
{
  "name": "Yourls",
  "type": "nodes-base.yourls",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": "",
    "shortUrl": "",
    "operation": "shorten"
  }
}
```

---

## YouTube

## Basic Information

- Node Type: `nodes-base.youTube`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume YouTube API

### Available Operations

### Get
Retrieve a channel
- Value: `get`

### Get Many
Retrieve many channels
- Value: `getAll`

### Update
Update a channel
- Value: `update`

### Upload Banner
Upload a channel banner
- Value: `uploadBanner`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `part` | multiOptions | Yes | `["*"]` | The fields parameter specifies a comma-separated list of one or more channel resource properties that the API response will include |
| `part` | multiOptions | Yes | `["*"]` | The fields parameter specifies a comma-separated list of one or more channel resource properties that the API response will include |
| `part` | multiOptions | Yes | `["*"]` | The fields parameter specifies a comma-separated list of one or more playlist resource properties that the API response will include |
| `part` | multiOptions | Yes | `["*"]` | The fields parameter specifies a comma-separated list of one or more playlist resource properties that the API response will include |
| `part` | multiOptions | Yes | `["*"]` | The fields parameter specifies a comma-separated list of one or more playlistItem resource properties that the API response will include |
| `part` | multiOptions | Yes | `["*"]` | The fields parameter specifies a comma-separated list of one or more playlistItem resource properties that the API response will include |
| `part` | multiOptions | Yes | `["*"]` | The fields parameter specifies a comma-separated list of one or more video resource properties that the API response will include |
| `channelId` | string | Yes | `""` | ID of the channel |
| `channelId` | string | Yes | `""` | ID of the channel |
| `title` | string | Yes | `""` | The playlist's title |

#### Property Details

##### Fields (`part`)

The fields parameter specifies a comma-separated list of one or more channel resource properties that the API response will include

Optional values:
- `*`: *
- `brandingSettings`: Branding Settings
- `contentDetails`: Content Details
- `contentOwnerDetails`: Content Owner Details
- `id`: ID
- `localizations`: Localizations
- `snippet`: Snippet
- `statistics`: Statistics
- `status`: Status
- `topicDetails`: Topic Details

##### Fields (`part`)

The fields parameter specifies a comma-separated list of one or more channel resource properties that the API response will include

Optional values:
- `*`: *
- `brandingSettings`: Branding Settings
- `contentDetails`: Content Details
- `contentOwnerDetails`: Content Owner Details
- `id`: ID
- `localizations`: Localizations
- `snippet`: Snippet
- `statistics`: Statistics
- `status`: Status
- `topicDetails`: Topic Details

##### Fields (`part`)

The fields parameter specifies a comma-separated list of one or more playlist resource properties that the API response will include

Optional values:
- `*`: *
- `contentDetails`: Content Details
- `id`: ID
- `localizations`: Localizations
- `player`: Player
- `snippet`: Snippet
- `status`: Status

##### Fields (`part`)

The fields parameter specifies a comma-separated list of one or more playlist resource properties that the API response will include

Optional values:
- `*`: *
- `contentDetails`: Content Details
- `id`: ID
- `localizations`: Localizations
- `player`: Player
- `snippet`: Snippet
- `status`: Status

##### Fields (`part`)

The fields parameter specifies a comma-separated list of one or more playlistItem resource properties that the API response will include

Optional values:
- `*`: *
- `contentDetails`: Content Details
- `id`: ID
- `snippet`: Snippet
- `status`: Status

##### Fields (`part`)

The fields parameter specifies a comma-separated list of one or more playlistItem resource properties that the API response will include

Optional values:
- `*`: *
- `contentDetails`: Content Details
- `id`: ID
- `snippet`: Snippet
- `status`: Status

##### Fields (`part`)

The fields parameter specifies a comma-separated list of one or more video resource properties that the API response will include

Optional values:
- `*`: *
- `contentDetails`: Content Details
- `id`: ID
- `liveStreamingDetails`: Live Streaming Details
- `localizations`: Localizations
- `player`: Player
- `recordingDetails`: Recording Details
- `snippet`: Snippet
- `statistics`: Statistics
- `status`: Status
- `topicDetails`: Topic Details

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
  "name": "YouTube",
  "type": "nodes-base.youTube",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "part": [
      "*"
    ],
    "channelId": "",
    "title": ""
  }
}
```

#### Get Example
```json
{
  "name": "YouTube",
  "type": "nodes-base.youTube",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "part": [
      "*"
    ],
    "channelId": "",
    "title": "",
    "operation": "get"
  }
}
```

#### Get Many Example
```json
{
  "name": "YouTube",
  "type": "nodes-base.youTube",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "part": [
      "*"
    ],
    "channelId": "",
    "title": "",
    "operation": "getAll"
  }
}
```

---

## Zammad

## Basic Information

- Node Type: `nodes-base.zammad`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume the Zammad API

### Available Operations

### Create
Create a group
- Value: `create`

### Delete
Delete a group
- Value: `delete`

### Get
Retrieve a group
- Value: `get`

### Get Many
Get many groups
- Value: `getAll`

### Update
Update a group
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `""` | - |
| `article` | fixedCollection | Yes | `{}` | - |
| `id` | string | Yes | `""` | Group to update. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `id` | string | Yes | `""` | Group to delete. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `id` | string | Yes | `""` | Group to retrieve. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `id` | string | Yes | `""` | Organization to update. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `id` | string | Yes | `""` | Organization to delete. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `id` | string | Yes | `""` | Organization to retrieve. Specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `title` | string | Yes | `""` | Title of the ticket to create |
| `group` | options | Yes | `""` | Group that will own the ticket to create. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

#### Property Details

##### Article (`article`)

Optional values:
- `undefined`: articleDetails

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
  "name": "Zammad",
  "type": "nodes-base.zammad",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "article": {},
    "id": "",
    "title": "",
    "group": ""
  }
}
```

#### Create Example
```json
{
  "name": "Zammad",
  "type": "nodes-base.zammad",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "article": {},
    "id": "",
    "title": "",
    "group": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Zammad",
  "type": "nodes-base.zammad",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "",
    "article": {},
    "id": "",
    "title": "",
    "group": "",
    "operation": "delete"
  }
}
```

---

## Zoom

## Basic Information

- Node Type: `nodes-base.zoom`
- Category: input
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Zoom API

### Available Operations

### Create
Create a meeting
- Value: `create`

### Delete
Delete a meeting
- Value: `delete`

### Get
Retrieve a meeting
- Value: `get`

### Get Many
Retrieve many meetings
- Value: `getAll`

### Update
Update a meeting
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `meetingId` | string | Yes | `""` | Meeting ID |
| `meetingId` | string | Yes | `""` | Meeting ID |
| `meetingId` | string | Yes | `""` | Meeting ID |
| `authentication` | options | No | `"accessToken"` | - |
| `resource` | options | No | `"meeting"` | - |
| `operation` | options | No | `"create"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |
| `filters` | collection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `accessToken`: Access Token
- `oAuth2`: OAuth2

##### Resource (`resource`)

Optional values:
- `meeting`: Meeting

##### Operation (`operation`)

Optional values:
- `create`: Create - Create a meeting
- `delete`: Delete - Delete a meeting
- `get`: Get - Retrieve a meeting
- `getAll`: Get Many - Retrieve many meetings
- `update`: Update - Update a meeting

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: agenda - Meeting agenda
- `undefined`: duration - Meeting duration (minutes)
- `undefined`: password - Password to join the meeting with maximum 10 characters
- `undefined`: scheduleFor - Schedule meeting for someone else from your account, provide their email ID
- `undefined`: settings
- `undefined`: startTime - Start time should be used only for scheduled or recurring meetings with fixed time
- `undefined`: timeZone - Time zone used in the response. The default is the time zone of the calendar. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: type - Meeting type

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: occurrenceId - To view meeting details of a particular occurrence of the recurring meeting
- `undefined`: showPreviousOccurrences - Whether to view meeting details of all previous occurrences of the recurring meeting

##### Filters (`filters`)

Optional values:
- `undefined`: type - Meeting type

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: occurrenceId - Meeting occurrence ID
- `undefined`: scheduleForReminder - Whether to notify hosts and alternative hosts about meeting cancellation via email

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
  "name": "Zoom",
  "type": "nodes-base.zoom",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "meetingId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Zoom",
  "type": "nodes-base.zoom",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "meetingId": "",
    "operation": "create"
  }
}
```

#### Delete Example
```json
{
  "name": "Zoom",
  "type": "nodes-base.zoom",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "meetingId": "",
    "operation": "delete"
  }
}
```
