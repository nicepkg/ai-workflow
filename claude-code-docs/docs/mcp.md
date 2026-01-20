---
source: https://code.claude.com/docs/en/mcp
title: Connect Claude Code to tools via MCP
---

Claude Code can connect to hundreds of external tools and data sources through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction), an open source standard for AI-tool integrations. MCP servers give Claude Code access to your tools, databases, and APIs.

## [​](#what-you-can-do-with-mcp) What you can do with MCP

With MCP servers connected, you can ask Claude Code to:

- **Implement features from issue trackers**: “Add the feature described in JIRA issue ENG-4521 and create a PR on GitHub.”
- **Analyze monitoring data**: “Check Sentry and Statsig to check the usage of the feature described in ENG-4521.”
- **Query databases**: “Find emails of 10 random users who used feature ENG-4521, based on our PostgreSQL database.”
- **Integrate designs**: “Update our standard email template based on the new Figma designs that were posted in Slack”
- **Automate workflows**: “Create Gmail drafts inviting these 10 users to a feedback session about the new feature.”

## [​](#popular-mcp-servers) Popular MCP servers

Here are some commonly used MCP servers you can connect to Claude Code:

Use third party MCP servers at your own risk - Anthropic has not verified
the correctness or security of all these servers.
Make sure you trust MCP servers you are installing.
Be especially careful when using MCP servers that could fetch untrusted
content, as these can expose you to prompt injection risk.

**Need a specific integration?** [Find hundreds more MCP servers on GitHub](https://github.com/modelcontextprotocol/servers), or build your own using the [MCP SDK](https://modelcontextprotocol.io/quickstart/server).

## [​](#installing-mcp-servers) Installing MCP servers

MCP servers can be configured in three different ways depending on your needs:

### [​](#option-1:-add-a-remote-http-server) Option 1: Add a remote HTTP server

HTTP servers are the recommended option for connecting to remote MCP servers. This is the most widely supported transport for cloud-based services.

```bash
# Basic syntax
claude mcp add --transport http <name> <url>

# Real example: Connect to Notion
claude mcp add --transport http notion https://mcp.notion.com/mcp

# Example with Bearer token
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### [​](#option-2:-add-a-remote-sse-server) Option 2: Add a remote SSE server

The SSE (Server-Sent Events) transport is deprecated. Use HTTP servers instead, where available.

```bash
# Basic syntax
claude mcp add --transport sse <name> <url>

# Real example: Connect to Asana
claude mcp add --transport sse asana https://mcp.asana.com/sse

# Example with authentication header
claude mcp add --transport sse private-api https://api.company.com/sse \
  --header "X-API-Key: your-key-here"
```

### [​](#option-3:-add-a-local-stdio-server) Option 3: Add a local stdio server

Stdio servers run as local processes on your machine. They’re ideal for tools that need direct system access or custom scripts.

```bash
# Basic syntax
claude mcp add [options] <name> -- <command> [args...]

# Real example: Add Airtable server
claude mcp add --transport stdio --env AIRTABLE_API_KEY=YOUR_KEY airtable \
  -- npx -y airtable-mcp-server
```

**Important: Option ordering**All options (`--transport`, `--env`, `--scope`, `--header`) must come **before** the server name. The `--` (double dash) then separates the server name from the command and arguments that get passed to the MCP server.For example:

- `claude mcp add --transport stdio myserver -- npx server` → runs `npx server`
- `claude mcp add --transport stdio --env KEY=value myserver -- python server.py --port 8080` → runs `python server.py --port 8080` with `KEY=value` in environment

This prevents conflicts between Claude’s flags and the server’s flags.

### [​](#managing-your-servers) Managing your servers

Once configured, you can manage your MCP servers with these commands:

```bash
# List all configured servers
claude mcp list

# Get details for a specific server
claude mcp get github

# Remove a server
claude mcp remove github

# (within Claude Code) Check server status
/mcp
```

### [​](#dynamic-tool-updates) Dynamic tool updates

Claude Code supports MCP `list_changed` notifications, allowing MCP servers to dynamically update their available tools, prompts, and resources without requiring you to disconnect and reconnect. When an MCP server sends a `list_changed` notification, Claude Code automatically refreshes the available capabilities from that server.

Tips:

- Use the `--scope` flag to specify where the configuration is stored:
  - `local` (default): Available only to you in the current project (was called `project` in older versions)
  - `project`: Shared with everyone in the project via `.mcp.json` file
  - `user`: Available to you across all projects (was called `global` in older versions)
- Set environment variables with `--env` flags (for example, `--env KEY=value`)
- Configure MCP server startup timeout using the MCP\_TIMEOUT environment variable (for example, `MCP_TIMEOUT=10000 claude` sets a 10-second timeout)
- Claude Code will display a warning when MCP tool output exceeds 10,000 tokens. To increase this limit, set the `MAX_MCP_OUTPUT_TOKENS` environment variable (for example, `MAX_MCP_OUTPUT_TOKENS=50000`)
- Use `/mcp` to authenticate with remote servers that require OAuth 2.0 authentication

**Windows Users**: On native Windows (not WSL), local MCP servers that use `npx` require the `cmd /c` wrapper to ensure proper execution.

```bash
# This creates command="cmd" which Windows can execute
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

Without the `cmd /c` wrapper, you’ll encounter “Connection closed” errors because Windows cannot directly execute `npx`. (See the note above for an explanation of the `--` parameter.)

### [​](#plugin-provided-mcp-servers) Plugin-provided MCP servers

[Plugins](/docs/en/plugins) can bundle MCP servers, automatically providing tools and integrations when the plugin is enabled. Plugin MCP servers work identically to user-configured servers.
**How plugin MCP servers work**:

- Plugins define MCP servers in `.mcp.json` at the plugin root or inline in `plugin.json`
- When a plugin is enabled, its MCP servers start automatically
- Plugin MCP tools appear alongside manually configured MCP tools
- Plugin servers are managed through plugin installation (not `/mcp` commands)

**Example plugin MCP configuration**:
In `.mcp.json` at plugin root:

```bash
{
  "database-tools": {
    "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
    "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
    "env": {
      "DB_URL": "${DB_URL}"
    }
  }
}
```

Or inline in `plugin.json`:

```bash
{
  "name": "my-plugin",
  "mcpServers": {
    "plugin-api": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/api-server",
      "args": ["--port", "8080"]
    }
  }
}
```

**Plugin MCP features**:

- **Automatic lifecycle**: Servers start when plugin enables, but you must restart Claude Code to apply MCP server changes (enabling or disabling)
- **Environment variables**: Use `${CLAUDE_PLUGIN_ROOT}` for plugin-relative paths
- **User environment access**: Access to same environment variables as manually configured servers
- **Multiple transport types**: Support stdio, SSE, and HTTP transports (transport support may vary by server)

**Viewing plugin MCP servers**:

```bash
# Within Claude Code, see all MCP servers including plugin ones
/mcp
```

Plugin servers appear in the list with indicators showing they come from plugins.
**Benefits of plugin MCP servers**:

- **Bundled distribution**: Tools and servers packaged together
- **Automatic setup**: No manual MCP configuration needed
- **Team consistency**: Everyone gets the same tools when plugin is installed

See the [plugin components reference](/docs/en/plugins-reference#mcp-servers) for details on bundling MCP servers with plugins.

## [​](#mcp-installation-scopes) MCP installation scopes

MCP servers can be configured at three different scope levels, each serving distinct purposes for managing server accessibility and sharing. Understanding these scopes helps you determine the best way to configure servers for your specific needs.

### [​](#local-scope) Local scope

Local-scoped servers represent the default configuration level and are stored in `~/.claude.json` under your project’s path. These servers remain private to you and are only accessible when working within the current project directory. This scope is ideal for personal development servers, experimental configurations, or servers containing sensitive credentials that shouldn’t be shared.

```bash
# Add a local-scoped server (default)
claude mcp add --transport http stripe https://mcp.stripe.com

# Explicitly specify local scope
claude mcp add --transport http stripe --scope local https://mcp.stripe.com
```

### [​](#project-scope) Project scope

Project-scoped servers enable team collaboration by storing configurations in a `.mcp.json` file at your project’s root directory. This file is designed to be checked into version control, ensuring all team members have access to the same MCP tools and services. When you add a project-scoped server, Claude Code automatically creates or updates this file with the appropriate configuration structure.

```bash
# Add a project-scoped server
claude mcp add --transport http paypal --scope project https://mcp.paypal.com/mcp
```

The resulting `.mcp.json` file follows a standardized format:

```bash
{
  "mcpServers": {
    "shared-server": {
      "command": "/path/to/server",
      "args": [],
      "env": {}
    }
  }
}
```

For security reasons, Claude Code prompts for approval before using project-scoped servers from `.mcp.json` files. If you need to reset these approval choices, use the `claude mcp reset-project-choices` command.

### [​](#user-scope) User scope

User-scoped servers are stored in `~/.claude.json` and provide cross-project accessibility, making them available across all projects on your machine while remaining private to your user account. This scope works well for personal utility servers, development tools, or services you frequently use across different projects.

```bash
# Add a user server
claude mcp add --transport http hubspot --scope user https://mcp.hubspot.com/anthropic
```

### [​](#choosing-the-right-scope) Choosing the right scope

Select your scope based on:

- **Local scope**: Personal servers, experimental configurations, or sensitive credentials specific to one project
- **Project scope**: Team-shared servers, project-specific tools, or services required for collaboration
- **User scope**: Personal utilities needed across multiple projects, development tools, or frequently used services

**Where are MCP servers stored?**

- **User and local scope**: `~/.claude.json` (in the `mcpServers` field or under project paths)
- **Project scope**: `.mcp.json` in your project root (checked into source control)
- **Managed**: `managed-mcp.json` in system directories (see [Managed MCP configuration](#managed-mcp-configuration))

### [​](#scope-hierarchy-and-precedence) Scope hierarchy and precedence

MCP server configurations follow a clear precedence hierarchy. When servers with the same name exist at multiple scopes, the system resolves conflicts by prioritizing local-scoped servers first, followed by project-scoped servers, and finally user-scoped servers. This design ensures that personal configurations can override shared ones when needed.

### [​](#environment-variable-expansion-in-mcp-json) Environment variable expansion in `.mcp.json`

Claude Code supports environment variable expansion in `.mcp.json` files, allowing teams to share configurations while maintaining flexibility for machine-specific paths and sensitive values like API keys.
**Supported syntax:**

- `${VAR}` - Expands to the value of environment variable `VAR`
- `${VAR:-default}` - Expands to `VAR` if set, otherwise uses `default`

**Expansion locations:**
Environment variables can be expanded in:

- `command` - The server executable path
- `args` - Command-line arguments
- `env` - Environment variables passed to the server
- `url` - For HTTP server types
- `headers` - For HTTP server authentication

**Example with variable expansion:**

```bash
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}"
      }
    }
  }
}
```

If a required environment variable is not set and has no default value, Claude Code will fail to parse the config.

## [​](#practical-examples) Practical examples

### [​](#example:-monitor-errors-with-sentry) Example: Monitor errors with Sentry

```bash
# 1. Add the Sentry MCP server
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp

# 2. Use /mcp to authenticate with your Sentry account
> /mcp

# 3. Debug production issues
> "What are the most common errors in the last 24 hours?"
> "Show me the stack trace for error ID abc123"
> "Which deployment introduced these new errors?"
```

### [​](#example:-connect-to-github-for-code-reviews) Example: Connect to GitHub for code reviews

```bash
# 1. Add the GitHub MCP server
claude mcp add --transport http github https://api.githubcopilot.com/mcp/

# 2. In Claude Code, authenticate if needed
> /mcp
# Select "Authenticate" for GitHub

# 3. Now you can ask Claude to work with GitHub
> "Review PR #456 and suggest improvements"
> "Create a new issue for the bug we just found"
> "Show me all open PRs assigned to me"
```

### [​](#example:-query-your-postgresql-database) Example: Query your PostgreSQL database

```bash
# 1. Add the database server with your connection string
claude mcp add --transport stdio db -- npx -y @bytebase/dbhub \
  --dsn "postgresql://readonly:[email protected]:5432/analytics"

# 2. Query your database naturally
> "What's our total revenue this month?"
> "Show me the schema for the orders table"
> "Find customers who haven't made a purchase in 90 days"
```

## [​](#authenticate-with-remote-mcp-servers) Authenticate with remote MCP servers

Many cloud-based MCP servers require authentication. Claude Code supports OAuth 2.0 for secure connections.

1

Add the server that requires authentication

For example:

```bash
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
```

2

Use the /mcp command within Claude Code

In Claude code, use the command:

```bash
> /mcp
```

Then follow the steps in your browser to login.

Tips:

- Authentication tokens are stored securely and refreshed automatically
- Use “Clear authentication” in the `/mcp` menu to revoke access
- If your browser doesn’t open automatically, copy the provided URL
- OAuth authentication works with HTTP servers

## [​](#add-mcp-servers-from-json-configuration) Add MCP servers from JSON configuration

If you have a JSON configuration for an MCP server, you can add it directly:

1

Add an MCP server from JSON

```bash
# Basic syntax
claude mcp add-json <name> '<json>'

# Example: Adding an HTTP server with JSON configuration
claude mcp add-json weather-api '{"type":"http","url":"https://api.weather.com/mcp","headers":{"Authorization":"Bearer token"}}'

# Example: Adding a stdio server with JSON configuration
claude mcp add-json local-weather '{"type":"stdio","command":"/path/to/weather-cli","args":["--api-key","abc123"],"env":{"CACHE_DIR":"/tmp"}}'
```

2

Verify the server was added

```bash
claude mcp get weather-api
```

Tips:

- Make sure the JSON is properly escaped in your shell
- The JSON must conform to the MCP server configuration schema
- You can use `--scope user` to add the server to your user configuration instead of the project-specific one

## [​](#import-mcp-servers-from-claude-desktop) Import MCP servers from Claude Desktop

If you’ve already configured MCP servers in Claude Desktop, you can import them:

1

Import servers from Claude Desktop

```bash
# Basic syntax
claude mcp add-from-claude-desktop
```

2

Select which servers to import

After running the command, you’ll see an interactive dialog that allows you to select which servers you want to import.

3

Verify the servers were imported

```bash
claude mcp list
```

Tips:

- This feature only works on macOS and Windows Subsystem for Linux (WSL)
- It reads the Claude Desktop configuration file from its standard location on those platforms
- Use the `--scope user` flag to add servers to your user configuration
- Imported servers will have the same names as in Claude Desktop
- If servers with the same names already exist, they will get a numerical suffix (for example, `server_1`)

## [​](#use-claude-code-as-an-mcp-server) Use Claude Code as an MCP server

You can use Claude Code itself as an MCP server that other applications can connect to:

```bash
# Start Claude as a stdio MCP server
claude mcp serve
```

You can use this in Claude Desktop by adding this configuration to claude\_desktop\_config.json:

```bash
{
  "mcpServers": {
    "claude-code": {
      "type": "stdio",
      "command": "claude",
      "args": ["mcp", "serve"],
      "env": {}
    }
  }
}
```

**Configuring the executable path**: The `command` field must reference the Claude Code executable. If the `claude` command is not in your system’s PATH, you’ll need to specify the full path to the executable.To find the full path:

```bash
which claude
```

Then use the full path in your configuration:

```bash
{
  "mcpServers": {
    "claude-code": {
      "type": "stdio",
      "command": "/full/path/to/claude",
      "args": ["mcp", "serve"],
      "env": {}
    }
  }
}
```

Without the correct executable path, you’ll encounter errors like `spawn claude ENOENT`.

Tips:

- The server provides access to Claude’s tools like View, Edit, LS, etc.
- In Claude Desktop, try asking Claude to read files in a directory, make edits, and more.
- Note that this MCP server is only exposing Claude Code’s tools to your MCP client, so your own client is responsible for implementing user confirmation for individual tool calls.

## [​](#mcp-output-limits-and-warnings) MCP output limits and warnings

When MCP tools produce large outputs, Claude Code helps manage the token usage to prevent overwhelming your conversation context:

- **Output warning threshold**: Claude Code displays a warning when any MCP tool output exceeds 10,000 tokens
- **Configurable limit**: You can adjust the maximum allowed MCP output tokens using the `MAX_MCP_OUTPUT_TOKENS` environment variable
- **Default limit**: The default maximum is 25,000 tokens

To increase the limit for tools that produce large outputs:

```bash
# Set a higher limit for MCP tool outputs
export MAX_MCP_OUTPUT_TOKENS=50000
claude
```

This is particularly useful when working with MCP servers that:

- Query large datasets or databases
- Generate detailed reports or documentation
- Process extensive log files or debugging information

If you frequently encounter output warnings with specific MCP servers, consider increasing the limit or configuring the server to paginate or filter its responses.

## [​](#use-mcp-resources) Use MCP resources

MCP servers can expose resources that you can reference using @ mentions, similar to how you reference files.

### [​](#reference-mcp-resources) Reference MCP resources

1

List available resources

Type `@` in your prompt to see available resources from all connected MCP servers. Resources appear alongside files in the autocomplete menu.

2

Reference a specific resource

Use the format `@server:protocol://resource/path` to reference a resource:

```bash
> Can you analyze @github:issue://123 and suggest a fix?
```

```bash
> Please review the API documentation at @docs:file://api/authentication
```

3

Multiple resource references

You can reference multiple resources in a single prompt:

```bash
> Compare @postgres:schema://users with @docs:file://database/user-model
```

Tips:

- Resources are automatically fetched and included as attachments when referenced
- Resource paths are fuzzy-searchable in the @ mention autocomplete
- Claude Code automatically provides tools to list and read MCP resources when servers support them
- Resources can contain any type of content that the MCP server provides (text, JSON, structured data, etc.)

## [​](#scale-with-mcp-tool-search) Scale with MCP Tool Search

When you have many MCP servers configured, tool definitions can consume a significant portion of your context window. MCP Tool Search solves this by dynamically loading tools on-demand instead of preloading all of them.

### [​](#how-it-works) How it works

Claude Code automatically enables Tool Search when your MCP tool descriptions would consume more than 10% of the context window. You can [adjust this threshold](#configure-tool-search) or disable tool search entirely. When triggered:

1. MCP tools are deferred rather than loaded into context upfront
2. Claude uses a search tool to discover relevant MCP tools when needed
3. Only the tools Claude actually needs are loaded into context
4. MCP tools continue to work exactly as before from your perspective

### [​](#for-mcp-server-authors) For MCP server authors

If you’re building an MCP server, the server instructions field becomes more useful with Tool Search enabled. Server instructions help Claude understand when to search for your tools, similar to how [skills](/docs/en/skills) work.
Add clear, descriptive server instructions that explain:

- What category of tasks your tools handle
- When Claude should search for your tools
- Key capabilities your server provides

### [​](#configure-tool-search) Configure tool search

Tool search runs in auto mode by default, meaning it activates only when your MCP tool definitions exceed the context threshold. If you have few tools, they load normally without tool search. This feature requires models that support `tool_reference` blocks: Sonnet 4 and later, or Opus 4 and later. Haiku models do not support tool search.
Control tool search behavior with the `ENABLE_TOOL_SEARCH` environment variable:

| Value | Behavior |
| --- | --- |
| `auto` | Activates when MCP tools exceed 10% of context (default) |
| `auto:<N>` | Activates at custom threshold, where `<N>` is a percentage (e.g., `auto:5` for 5%) |
| `true` | Always enabled |
| `false` | Disabled, all MCP tools loaded upfront |

```bash
# Use a custom 5% threshold
ENABLE_TOOL_SEARCH=auto:5 claude

# Disable tool search entirely
ENABLE_TOOL_SEARCH=false claude
```

Or set the value in your [settings.json `env` field](/docs/en/settings#available-settings).
You can also disable the MCPSearch tool specifically using the `disallowedTools` setting:

```bash
{
  "permissions": {
    "deny": ["MCPSearch"]
  }
}
```

## [​](#use-mcp-prompts-as-slash-commands) Use MCP prompts as slash commands

MCP servers can expose prompts that become available as slash commands in Claude Code.

### [​](#execute-mcp-prompts) Execute MCP prompts

1

Discover available prompts

Type `/` to see all available commands, including those from MCP servers. MCP prompts appear with the format `/mcp__servername__promptname`.

2

Execute a prompt without arguments

```bash
> /mcp__github__list_prs
```

3

Execute a prompt with arguments

Many prompts accept arguments. Pass them space-separated after the command:

```bash
> /mcp__github__pr_review 456
```

```bash
> /mcp__jira__create_issue "Bug in login flow" high
```

Tips:

- MCP prompts are dynamically discovered from connected servers
- Arguments are parsed based on the prompt’s defined parameters
- Prompt results are injected directly into the conversation
- Server and prompt names are normalized (spaces become underscores)

## [​](#managed-mcp-configuration) Managed MCP configuration

For organizations that need centralized control over MCP servers, Claude Code supports two configuration options:

1. **Exclusive control with `managed-mcp.json`**: Deploy a fixed set of MCP servers that users cannot modify or extend
2. **Policy-based control with allowlists/denylists**: Allow users to add their own servers, but restrict which ones are permitted

These options allow IT administrators to:

- **Control which MCP servers employees can access**: Deploy a standardized set of approved MCP servers across the organization
- **Prevent unauthorized MCP servers**: Restrict users from adding unapproved MCP servers
- **Disable MCP entirely**: Remove MCP functionality completely if needed

### [​](#option-1:-exclusive-control-with-managed-mcp-json) Option 1: Exclusive control with managed-mcp.json

When you deploy a `managed-mcp.json` file, it takes **exclusive control** over all MCP servers. Users cannot add, modify, or use any MCP servers other than those defined in this file. This is the simplest approach for organizations that want complete control.
System administrators deploy the configuration file to a system-wide directory:

- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux and WSL: `/etc/claude-code/managed-mcp.json`
- Windows: `C:\Program Files\ClaudeCode\managed-mcp.json`

These are system-wide paths (not user home directories like `~/Library/...`) that require administrator privileges. They are designed to be deployed by IT administrators.

The `managed-mcp.json` file uses the same format as a standard `.mcp.json` file:

```bash
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "sentry": {
      "type": "http",
      "url": "https://mcp.sentry.dev/mcp"
    },
    "company-internal": {
      "type": "stdio",
      "command": "/usr/local/bin/company-mcp-server",
      "args": ["--config", "/etc/company/mcp-config.json"],
      "env": {
        "COMPANY_API_URL": "https://internal.company.com"
      }
    }
  }
}
```

### [​](#option-2:-policy-based-control-with-allowlists-and-denylists) Option 2: Policy-based control with allowlists and denylists

Instead of taking exclusive control, administrators can allow users to configure their own MCP servers while enforcing restrictions on which servers are permitted. This approach uses `allowedMcpServers` and `deniedMcpServers` in the [managed settings file](/docs/en/settings#settings-files).

**Choosing between options**: Use Option 1 (`managed-mcp.json`) when you want to deploy a fixed set of servers with no user customization. Use Option 2 (allowlists/denylists) when you want to allow users to add their own servers within policy constraints.

#### [​](#restriction-options) Restriction options

Each entry in the allowlist or denylist can restrict servers in three ways:

1. **By server name** (`serverName`): Matches the configured name of the server
2. **By command** (`serverCommand`): Matches the exact command and arguments used to start stdio servers
3. **By URL pattern** (`serverUrl`): Matches remote server URLs with wildcard support

**Important**: Each entry must have exactly one of `serverName`, `serverCommand`, or `serverUrl`.

#### [​](#example-configuration) Example configuration

```bash
{
  "allowedMcpServers": [
    // Allow by server name
    { "serverName": "github" },
    { "serverName": "sentry" },

    // Allow by exact command (for stdio servers)
    { "serverCommand": ["npx", "-y", "@modelcontextprotocol/server-filesystem"] },
    { "serverCommand": ["python", "/usr/local/bin/approved-server.py"] },

    // Allow by URL pattern (for remote servers)
    { "serverUrl": "https://mcp.company.com/*" },
    { "serverUrl": "https://*.internal.corp/*" }
  ],
  "deniedMcpServers": [
    // Block by server name
    { "serverName": "dangerous-server" },

    // Block by exact command (for stdio servers)
    { "serverCommand": ["npx", "-y", "unapproved-package"] },

    // Block by URL pattern (for remote servers)
    { "serverUrl": "https://*.untrusted.com/*" }
  ]
}
```

#### [​](#how-command-based-restrictions-work) How command-based restrictions work

**Exact matching**:

- Command arrays must match **exactly** - both the command and all arguments in the correct order
- Example: `["npx", "-y", "server"]` will NOT match `["npx", "server"]` or `["npx", "-y", "server", "--flag"]`

**Stdio server behavior**:

- When the allowlist contains **any** `serverCommand` entries, stdio servers **must** match one of those commands
- Stdio servers cannot pass by name alone when command restrictions are present
- This ensures administrators can enforce which commands are allowed to run

**Non-stdio server behavior**:

- Remote servers (HTTP, SSE, WebSocket) use URL-based matching when `serverUrl` entries exist in the allowlist
- If no URL entries exist, remote servers fall back to name-based matching
- Command restrictions do not apply to remote servers

#### [​](#how-url-based-restrictions-work) How URL-based restrictions work

URL patterns support wildcards using `*` to match any sequence of characters. This is useful for allowing entire domains or subdomains.
**Wildcard examples**:

- `https://mcp.company.com/*` - Allow all paths on a specific domain
- `https://*.example.com/*` - Allow any subdomain of example.com
- `http://localhost:*/*` - Allow any port on localhost

**Remote server behavior**:

- When the allowlist contains **any** `serverUrl` entries, remote servers **must** match one of those URL patterns
- Remote servers cannot pass by name alone when URL restrictions are present
- This ensures administrators can enforce which remote endpoints are allowed

Example: URL-only allowlist

```bash
{
  "allowedMcpServers": [
    { "serverUrl": "https://mcp.company.com/*" },
    { "serverUrl": "https://*.internal.corp/*" }
  ]
}
```

**Result**:

- HTTP server at `https://mcp.company.com/api`: ✅ Allowed (matches URL pattern)
- HTTP server at `https://api.internal.corp/mcp`: ✅ Allowed (matches wildcard subdomain)
- HTTP server at `https://external.com/mcp`: ❌ Blocked (doesn’t match any URL pattern)
- Stdio server with any command: ❌ Blocked (no name or command entries to match)

Example: Command-only allowlist

```bash
{
  "allowedMcpServers": [
    { "serverCommand": ["npx", "-y", "approved-package"] }
  ]
}
```

**Result**:

- Stdio server with `["npx", "-y", "approved-package"]`: ✅ Allowed (matches command)
- Stdio server with `["node", "server.js"]`: ❌ Blocked (doesn’t match command)
- HTTP server named “my-api”: ❌ Blocked (no name entries to match)

Example: Mixed name and command allowlist

```bash
{
  "allowedMcpServers": [
    { "serverName": "github" },
    { "serverCommand": ["npx", "-y", "approved-package"] }
  ]
}
```

**Result**:

- Stdio server named “local-tool” with `["npx", "-y", "approved-package"]`: ✅ Allowed (matches command)
- Stdio server named “local-tool” with `["node", "server.js"]`: ❌ Blocked (command entries exist but doesn’t match)
- Stdio server named “github” with `["node", "server.js"]`: ❌ Blocked (stdio servers must match commands when command entries exist)
- HTTP server named “github”: ✅ Allowed (matches name)
- HTTP server named “other-api”: ❌ Blocked (name doesn’t match)

Example: Name-only allowlist

```bash
{
  "allowedMcpServers": [
    { "serverName": "github" },
    { "serverName": "internal-tool" }
  ]
}
```

**Result**:

- Stdio server named “github” with any command: ✅ Allowed (no command restrictions)
- Stdio server named “internal-tool” with any command: ✅ Allowed (no command restrictions)
- HTTP server named “github”: ✅ Allowed (matches name)
- Any server named “other”: ❌ Blocked (name doesn’t match)

#### [​](#allowlist-behavior-allowedmcpservers) Allowlist behavior (`allowedMcpServers`)

- `undefined` (default): No restrictions - users can configure any MCP server
- Empty array `[]`: Complete lockdown - users cannot configure any MCP servers
- List of entries: Users can only configure servers that match by name, command, or URL pattern

#### [​](#denylist-behavior-deniedmcpservers) Denylist behavior (`deniedMcpServers`)

- `undefined` (default): No servers are blocked
- Empty array `[]`: No servers are blocked
- List of entries: Specified servers are explicitly blocked across all scopes

#### [​](#important-notes) Important notes

- **Option 1 and Option 2 can be combined**: If `managed-mcp.json` exists, it has exclusive control and users cannot add servers. Allowlists/denylists still apply to the managed servers themselves.
- **Denylist takes absolute precedence**: If a server matches a denylist entry (by name, command, or URL), it will be blocked even if it’s on the allowlist
- Name-based, command-based, and URL-based restrictions work together: a server passes if it matches **either** a name entry, a command entry, or a URL pattern (unless blocked by denylist)

**When using `managed-mcp.json`**: Users cannot add MCP servers through `claude mcp add` or configuration files. The `allowedMcpServers` and `deniedMcpServers` settings still apply to filter which managed servers are actually loaded.