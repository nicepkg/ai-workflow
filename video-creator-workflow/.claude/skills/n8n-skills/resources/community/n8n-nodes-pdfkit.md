# n8n-nodes-pdfkit

## Basic Information

- Package: `n8n-nodes-pdfkit`
- Category: 📄 Document Processing
- Version: 0.1.2
- Maintainer: bramknuever
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-pdfkit)
- Repository: [View Source](https://github.com/bramkn/n8n-nodes-pdfkit)

## Description

Node for using PDFKit to tranform images into PDF, more functionality may be added later.

## Installation

```
n8n-nodes-pdfkit
```

## Nodes (1)

### PdfKit

- Node Type: `n8n-nodes-pdfkit.pdfKit`
- Version: 1

PDFKit Node

#### Available Operations

- **Covert Images To PDF** (`imagesToPDF`)

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `operation` | options | Yes | `"imagesToPDF"` |
| `outputKey` | string | Yes | `"data"` |
| `pdfName` | string | Yes | `""` |
| `keepImages` | boolean | No | `false` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "PdfKit",
  "type": "n8n-nodes-pdfkit.pdfKit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "imagesToPDF",
    "outputKey": "data",
    "pdfName": ""
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
