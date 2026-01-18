# n8n-nodes-zohozeptomail

## Basic Information

- Package: `n8n-nodes-zohozeptomail`
- Category: 🤖 AI & Voice Tools
- Version: 1.0.3
- Maintainer: zohomail
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-zohozeptomail)
- Repository: [View Source](https://github.com/zohomail/zoho_zeptomail_n8n)

## Description

This is an n8n community node. It lets you use Zoho ZeptoMail in your n8n workflows.

## Installation

```
n8n-nodes-zohozeptomail
```

## Nodes (1)

### Zoho Zeptomail

- Node Type: `n8n-nodes-zohozeptomail.zohoZeptomail`
- Version: 1
- Requires Credentials: Yes

Consume Zoho ZeptoMail API

#### Available Operations

- **Send Mail** (`sendmail`)
  This action will send an email.
- **Send Template Mail** (`sendtemplatemail`)
  Send custom Template Mail.

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `resource` | options | Yes | `"message"` |
| `mailagent` | options | Yes | `""` |
| `template` | options | Yes | `""` |
| `toaddress` | string | Yes | `""` |
| `subject` | string | Yes | `""` |
| `mergeinfo` | string | Yes | `""` |
| `operation` | options | No | `"sendmail"` |
| `fromaddress` | collection | No | `{}` |
| `attachment` | collection | No | `null` |
| `htmlbody` | string | No | `""` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Zoho Zeptomail",
  "type": "n8n-nodes-zohozeptomail.zohoZeptomail",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "message",
    "mailagent": "",
    "template": "",
    "toaddress": "",
    "subject": "",
    "operation": "sendmail"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
