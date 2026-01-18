# n8n-nodes-mcp

## Basic Information

- Package: `n8n-nodes-mcp`
- Category: 🤖 AI & Voice Tools
- Version: 0.1.33
- Maintainer: iamfiscus
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-mcp)
- Repository: [View Source](https://github.com/nerding-io/n8n-nodes-mcp)

## Description

MCP nodes for n8n

## Installation

```
n8n-nodes-mcp
```

## Nodes (1)

### MCP Client

- Node Type: `n8n-nodes-mcp.mcpClient`
- Version: 1
- Requires Credentials: Yes

Use MCP client

#### Available Operations

- **Execute Tool** (`executeTool`)
  Execute a specific tool
- **Get Prompt** (`getPrompt`)
  Get a specific prompt template
- **List Prompts** (`listPrompts`)
  Get available prompts
- **List Resource Templates** (`listResourceTemplates`)
  Get a list of available resource templates
- **List Resources** (`listResources`)
  Get a list of available resources
- **List Tools** (`listTools`)
  Get available tools
- **Read Resource** (`readResource`)
  Read a specific resource by URI

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `operation` | options | Yes | `"listTools"` |
| `resourceUri` | string | Yes | `""` |
| `toolName` | string | Yes | `""` |
| `toolParameters` | json | Yes | `"{}"` |
| `promptName` | string | Yes | `""` |
| `connectionType` | options | No | `"cmd"` |
| `uriOverride` | string | No | `""` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "MCP Client",
  "type": "n8n-nodes-mcp.mcpClient",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "executeTool",
    "resourceUri": "",
    "toolName": "",
    "toolParameters": "{}",
    "promptName": ""
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
