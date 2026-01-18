# n8n-nodes-cronlytic

## Basic Information

- Package: `n8n-nodes-cronlytic`
- Category: 🔧 Utilities & Tools
- Version: 0.1.4
- Maintainer: cronlytic
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-cronlytic)
- Repository: [View Source](https://github.com/Cronlytic/n8n-nodes-cronlytic)

## Description

n8n community node for Cronlytic advanced cron scheduling

## Installation

```
n8n-nodes-cronlytic
```

## Nodes (1)

### Cronlytic Trigger

- Node Type: `n8n-nodes-cronlytic.cronlyticTrigger`
- Version: 1
- Requires Credentials: Yes

Trigger workflows using Cronlytic advanced cron scheduling

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `jobName` | string | Yes | `""` |
| `cronExpression` | string | Yes | `"0 9 * * *"` |
| `webhookHeaders` | fixedCollection | No | `{}` |
| `webhookBody` | json | No | `"{}"` |

#### Connection

- Input Types: 
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Cronlytic Trigger",
  "type": "n8n-nodes-cronlytic.cronlyticTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "jobName": "",
    "cronExpression": "0 9 * * *"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
