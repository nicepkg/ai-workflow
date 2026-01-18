# AWS Certificate Manager

## Basic Information

- Node Type: `nodes-base.awsCertificateManager`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Sends data to AWS Certificate Manager

## Available Operations

### Delete
Delete a certificate
- Value: `delete`

### Get
Get a certificate
- Value: `get`

### Get Many
Get many certificates
- Value: `getMany`

### Get Metadata
Get certificate metadata
- Value: `getMetadata`

### Renew
Renew a certificate
- Value: `renew`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `certificateArn` | string | Yes | `""` | String that contains the ARN of the ACM certificate to be renewed. This must be of the form: arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012. |
| `bucketName` | string | Yes | `""` | - |
| `certificateKey` | string | Yes | `""` | - |
| `authentication` | options | No | `"iam"` | - |
| `resource` | options | No | `"certificate"` | - |
| `operation` | options | No | `"renew"` | - |
| `options` | collection | No | `{}` | - |
| `returnAll` | boolean | No | `false` | Whether to return all results or only up to a given limit |
| `limit` | number | No | `100` | Max number of results to return |

### Property Details

#### Authentication (`authentication`)

Optional values:
- `iam`: AWS (IAM)
- `assumeRole`: AWS (Assume Role)

#### Resource (`resource`)

Optional values:
- `certificate`: Certificate

#### Operation (`operation`)

Optional values:
- `delete`: Delete - Delete a certificate
- `get`: Get - Get a certificate
- `getMany`: Get Many - Get many certificates
- `getMetadata`: Get Metadata - Get certificate metadata
- `renew`: Renew - Renew a certificate

#### Options (`options`)

Optional values:
- `undefined`: certificateStatuses - Filter the certificate list by status value
- `undefined`: extendedKeyUsage - Specify one or more ExtendedKeyUsage extension values
- `undefined`: keyTypes - Specify one or more algorithms that can be used to generate key pairs
- `undefined`: keyUsage - Specify one or more KeyUsage extension values

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
  "name": "AWS Certificate Manager",
  "type": "nodes-base.awsCertificateManager",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "certificateArn": "",
    "bucketName": "",
    "certificateKey": ""
  }
}
```

### Delete Example
```json
{
  "name": "AWS Certificate Manager",
  "type": "nodes-base.awsCertificateManager",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "certificateArn": "",
    "bucketName": "",
    "certificateKey": "",
    "operation": "delete"
  }
}
```

### Get Example
```json
{
  "name": "AWS Certificate Manager",
  "type": "nodes-base.awsCertificateManager",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "certificateArn": "",
    "bucketName": "",
    "certificateKey": "",
    "operation": "get"
  }
}
```
