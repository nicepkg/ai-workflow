# @splainez/n8n-nodes-phonenumber-parser

## Basic Information

- Package: `@splainez/n8n-nodes-phonenumber-parser`
- Category: 🤖 AI & Voice Tools
- Version: 1.2.0
- Maintainer: splainez
- npm: [View Package](https://www.npmjs.com/package/@splainez/n8n-nodes-phonenumber-parser)
- Repository: [View Source](https://github.com/splainez/n8n-nodes-phonenumber-parser)

## Description

Parse a phone number and return its information

## Installation

```
@splainez/n8n-nodes-phonenumber-parser
```

## Nodes (1)

### Phone Number Parser

- Node Type: `@splainez/n8n-nodes-phonenumber-parser.phoneNumberParser`
- Version: 1

Parse a phone number and return its information

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `defaultCountry` | options | Yes | `""` |
| `phonenumber` | string | Yes | `""` |
| `keepOnlySet` | boolean | No | `false` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Phone Number Parser",
  "type": "@splainez/n8n-nodes-phonenumber-parser.phoneNumberParser",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "defaultCountry": "",
    "phonenumber": ""
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
