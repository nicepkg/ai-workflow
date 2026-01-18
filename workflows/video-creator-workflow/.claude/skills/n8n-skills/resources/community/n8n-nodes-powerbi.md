# n8n-nodes-powerbi

## Basic Information

- Package: `n8n-nodes-powerbi`
- Category: 🔧 Utilities & Tools
- Version: 2.3.8
- Maintainer: androcha
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-powerbi)
- Repository: [View Source](https://github.com/And-Rochaa/n8n-nodes-powerbi)

## Description

n8n nodes for integration with Power BI APIs

## Installation

```
n8n-nodes-powerbi
```

## Nodes (1)

### Power BI

- Node Type: `n8n-nodes-powerbi.powerBi`
- Version: 1
- Requires Credentials: Yes

Work with the Power BI API

#### Available Operations

- **Get Workspace Information** (`getInfo`)
  Get detailed information from workspaces
- **Get Scan Result** (`getScanResult`)
  Get the scan result from a workspace

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `notifyOption` | options | Yes | `"NoNotification"` |
| `workspaces` | multiOptions | Yes | `[]` |
| `scanId` | string | Yes | `""` |
| `dashboardId` | options | Yes | `""` |
| `groupId` | options | Yes | `""` |
| `groupId` | options | Yes | `""` |
| `dataflowId` | options | Yes | `""` |
| `groupId` | options | Yes | `""` |
| `dataflowId` | options | Yes | `""` |
| `groupId` | options | Yes | `""` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Power BI",
  "type": "n8n-nodes-powerbi.powerBi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "notifyOption": "NoNotification",
    "workspaces": [],
    "scanId": "",
    "dashboardId": "",
    "groupId": "",
    "operation": "getInfo"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
