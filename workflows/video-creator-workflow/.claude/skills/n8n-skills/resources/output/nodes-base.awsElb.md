# AWS ELB

## Basic Information

- Node Type: `nodes-base.awsElb`
- Category: output
- Package: n8n-nodes-base
- Requires Credentials: Yes

## Description

Sends data to AWS ELB API

## Available Operations

### Create
Create a load balancer
- Value: `create`

### Delete
Delete a load balancer
- Value: `delete`

### Get
Get a load balancer
- Value: `get`

### Get Many
Get many load balancers
- Value: `getMany`

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `ipAddressType` | options | Yes | `"ipv4"` | The type of IP addresses used by the subnets for your load balancer |
| `schema` | options | Yes | `"internet-facing"` | - |
| `type` | options | Yes | `"application"` | - |
| `name` | string | Yes | `""` | This name must be unique per region per account, can have a maximum of 32 characters |
| `subnets` | multiOptions | Yes | `[]` | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `loadBalancerId` | string | Yes | `""` | Unique identifier for a particular loadBalancer |
| `loadBalancerId` | string | Yes | `""` | ID of loadBalancer to delete |
| `loadBalancerId` | options | Yes | `""` | Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `listenerId` | options | Yes | `""` | Unique identifier for a particular loadBalancer. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `certificateId` | string | Yes | `""` | Unique identifier for a particular loadBalancer |

### Property Details

#### IP Address Type (`ipAddressType`)

The type of IP addresses used by the subnets for your load balancer

Optional values:
- `ipv4`: Ipv4
- `dualstack`: Dualstack

#### Schema (`schema`)

Optional values:
- `internal`: Internal
- `internet-facing`: Internet Facing

#### Type (`type`)

Optional values:
- `application`: Application
- `network`: Network

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
  "name": "AWS ELB",
  "type": "nodes-base.awsElb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "ipAddressType": "ipv4",
    "schema": "internet-facing",
    "type": "application",
    "name": "",
    "subnets": [],
    "loadBalancerId": "",
    "listenerId": "",
    "certificateId": ""
  }
}
```

### Create Example
```json
{
  "name": "AWS ELB",
  "type": "nodes-base.awsElb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "ipAddressType": "ipv4",
    "schema": "internet-facing",
    "type": "application",
    "name": "",
    "subnets": [],
    "loadBalancerId": "",
    "listenerId": "",
    "certificateId": "",
    "operation": "create"
  }
}
```

### Delete Example
```json
{
  "name": "AWS ELB",
  "type": "nodes-base.awsElb",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "ipAddressType": "ipv4",
    "schema": "internet-facing",
    "type": "application",
    "name": "",
    "subnets": [],
    "loadBalancerId": "",
    "listenerId": "",
    "certificateId": "",
    "operation": "delete"
  }
}
```
