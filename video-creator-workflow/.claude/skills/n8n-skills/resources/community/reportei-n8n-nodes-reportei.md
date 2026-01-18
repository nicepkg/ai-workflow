# @reportei/n8n-nodes-reportei

## Basic Information

- Package: `@reportei/n8n-nodes-reportei`
- Category: 🔧 Utilities & Tools
- Version: 0.1.5
- Maintainer: eduardo_lelis
- npm: [View Package](https://www.npmjs.com/package/@reportei/n8n-nodes-reportei)
- Repository: [View Source](https://github.com/reportei/reportei-n8n-node)

## Description

n8n nodes for integrating with Reportei

## Installation

```
@reportei/n8n-nodes-reportei
```

## Nodes (2)

### Reportei

- Node Type: `@reportei/n8n-nodes-reportei.reportei`
- Version: 1
- Requires Credentials: Yes

Perform actions with Reportei API

#### Available Operations

- **Create a Report** (`create`)
  Creates a new report in Reportei

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `resource` | options | Yes | `"report"` |
| `operation` | options | No | `"create"` |
| `operation` | options | No | `"create"` |
| `operation` | options | No | `"create"` |
| `projectId` | options | No | `""` |
| `integrationsIds` | multiOptions | No | `[]` |
| `templateId` | options | No | `""` |
| `reportTitle` | string | No | `""` |
| `reportSubtitle` | string | No | `""` |
| `startDate` | dateTime | No | `""` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Reportei",
  "type": "@reportei/n8n-nodes-reportei.reportei",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "report",
    "operation": "create"
  }
}
```

---

### Reportei Trigger

- Node Type: `@reportei/n8n-nodes-reportei.reporteiTrigger`
- Version: 1
- Requires Credentials: Yes

Handle Reportei events via webhooks

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `event` | options | Yes | `"report_created"` |
| `clientId` | options | No | `""` |
| `customWebhookBaseUrl` | string | No | `""` |

#### Connection

- Input Types: 
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Reportei Trigger",
  "type": "@reportei/n8n-nodes-reportei.reporteiTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": "report_created"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
