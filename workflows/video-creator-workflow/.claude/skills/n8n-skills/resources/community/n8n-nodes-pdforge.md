# n8n-nodes-pdforge

## Basic Information

- Package: `n8n-nodes-pdforge`
- Category: 🤖 AI & Voice Tools
- Version: 2.3.3
- Maintainer: mabreum
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-pdforge)
- Repository: [View Source](https://github.com/pdfnoodle/n8n-nodes-pdforge)

## Description

pdf noodle (previously pdforge) automates PDF Generation in minutes using AI.Create custom PDF templates in seconds using our AI Agents, fine tune the design with our PDF builder and automate the PDF delivery with our native pdforge node inside n8n. No co

## Installation

```
n8n-nodes-pdforge
```

## Nodes (1)

### PDF Noodle

- Node Type: `n8n-nodes-pdforge.pdforge`
- Version: 1
- Requires Credentials: Yes

Generate PDF from HTML or reusable templates with PDF Noodle (previously pdforge).

#### Available Operations

- **Generate Syncronously** (`sync`)
  Generate PDF syncronously
- **Generate Asynchronously** (`async`)
  Generate PDF asynchronously

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `templateId` | options | Yes | `""` |
| `html` | string | Yes | `""` |
| `resource` | options | No | `"pdf"` |
| `operation` | options | No | `"sync"` |
| `operation` | options | No | `"sync"` |
| `operation` | options | No | `"sync"` |
| `options` | collection | No | `{}` |
| `variables` | json | No | `"{}"` |
| `pdfParams` | json | No | `"{}"` |
| `webhook` | string | No | `""` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "PDF Noodle",
  "type": "n8n-nodes-pdforge.pdforge",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "templateId": "",
    "html": "",
    "operation": "sync"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
