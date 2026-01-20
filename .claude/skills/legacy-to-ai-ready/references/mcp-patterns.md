# MCP Servers Configuration Patterns

## Purpose

MCP (Model Context Protocol) servers connect Claude Code to external tools and data sources. Consider MCP servers when:
- Project uses external APIs/services frequently
- Team has internal tools that could benefit Claude
- Database queries are common operations
- External data sources need integration

## Configuration Location

MCP servers are configured in Claude Code settings:
- User-level: `~/.claude/settings.json`
- Project-level: `.claude/settings.json`

```json
{
  "mcpServers": {
    "server-name": {
      "command": "command-to-run",
      "args": ["arg1", "arg2"],
      "env": {
        "ENV_VAR": "value"
      }
    }
  }
}
```

## Common MCP Server Patterns

### Database Access

For projects with frequent database operations:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "${POSTGRES_URL}"
      }
    }
  }
}
```

### Filesystem Access

For projects needing broader file access:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/dir"]
    }
  }
}
```

### GitHub Integration

For GitHub-heavy workflows:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

### Slack Integration

For team communication:

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_TOKEN}"
      }
    }
  }
}
```

### Memory/Knowledge Base

For persistent context across sessions:

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
```

## When to Add MCP Servers

| Project Pattern | Recommended MCP |
|-----------------|-----------------|
| Database-heavy backend | postgres/mysql server |
| GitHub PR workflow | github server |
| Documentation site | filesystem server |
| Slack-integrated team | slack server |
| Multi-repo monorepo | filesystem + github |

## Security Considerations

1. **Environment Variables** - Never hardcode secrets in settings
2. **Minimal Permissions** - Only enable needed capabilities
3. **Project vs User** - Project MCP configs are shared via git
4. **Token Scoping** - Use minimal-scope tokens

## Environment Variable Pattern

Use `${VAR_NAME}` syntax for sensitive values:

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "CONNECTION_STRING": "${DATABASE_URL}"
      }
    }
  }
}
```

Then set in `.env` or shell:
```bash
export DATABASE_URL="postgres://user:pass@host:5432/db"
```

## Custom MCP Servers

For project-specific tools, create custom MCP servers:

```json
{
  "mcpServers": {
    "internal-api": {
      "command": "node",
      "args": [".claude/mcp/internal-api-server.js"],
      "env": {
        "API_KEY": "${INTERNAL_API_KEY}"
      }
    }
  }
}
```

## MCP Permission Rules

Control which MCP tools are allowed:

```json
{
  "permissions": {
    "allow": [
      "mcp__github",
      "mcp__postgres__query"
    ],
    "deny": [
      "mcp__postgres__execute"
    ]
  }
}
```

## Extraction Patterns

When analyzing legacy code for MCP needs:

1. **Check for API integrations**
   - REST API calls
   - GraphQL queries
   - Third-party services

2. **Identify data sources**
   - Database connections
   - External data files
   - Cloud storage

3. **Find team tools**
   - Internal dashboards
   - Deployment tools
   - Monitoring systems

4. **Note common operations**
   - Frequent queries
   - Repeated API calls
   - Data transformations
