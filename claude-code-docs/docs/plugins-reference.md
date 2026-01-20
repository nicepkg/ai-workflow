---
source: https://code.claude.com/docs/en/plugins-reference
title: Plugins reference
---

Looking to install plugins? See [Discover and install plugins](/docs/en/discover-plugins). For creating plugins, see [Plugins](/docs/en/plugins). For distributing plugins, see [Plugin marketplaces](/docs/en/plugin-marketplaces).

This reference provides complete technical specifications for the Claude Code plugin system, including component schemas, CLI commands, and development tools.

## [​](#plugin-components-reference) Plugin components reference

This section documents the five types of components that plugins can provide.

### [​](#commands) Commands

Plugins add custom slash commands that integrate seamlessly with Claude Code’s command system.
**Location**: `commands/` directory in plugin root
**File format**: Markdown files with frontmatter
For complete details on plugin command structure, invocation patterns, and features, see [Plugin commands](/docs/en/slash-commands#plugin-commands).

### [​](#agents) Agents

Plugins can provide specialized subagents for specific tasks that Claude can invoke automatically when appropriate.
**Location**: `agents/` directory in plugin root
**File format**: Markdown files describing agent capabilities
**Agent structure**:

```bash
---
description: What this agent specializes in
capabilities: ["task1", "task2", "task3"]
---

# Agent Name

Detailed description of the agent's role, expertise, and when Claude should invoke it.

## Capabilities
- Specific task the agent excels at
- Another specialized capability
- When to use this agent vs others

## Context and examples
Provide examples of when this agent should be used and what kinds of problems it solves.
```

**Integration points**:

- Agents appear in the `/agents` interface
- Claude can invoke agents automatically based on task context
- Agents can be invoked manually by users
- Plugin agents work alongside built-in Claude agents

### [​](#skills) Skills

Plugins can provide Agent Skills that extend Claude’s capabilities. Skills are model-invoked—Claude autonomously decides when to use them based on the task context.
**Location**: `skills/` directory in plugin root
**File format**: Directories containing `SKILL.md` files with frontmatter
**Skill structure**:

```bash
skills/
├── pdf-processor/
│   ├── SKILL.md
│   ├── reference.md (optional)
│   └── scripts/ (optional)
└── code-reviewer/
    └── SKILL.md
```

**Integration behavior**:

- Plugin Skills are automatically discovered when the plugin is installed
- Claude autonomously invokes Skills based on matching task context
- Skills can include supporting files alongside SKILL.md

For SKILL.md format and complete Skill authoring guidance, see:

- [Use Skills in Claude Code](/docs/en/skills)
- [Agent Skills overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview#skill-structure)

### [​](#hooks) Hooks

Plugins can provide event handlers that respond to Claude Code events automatically.
**Location**: `hooks/hooks.json` in plugin root, or inline in plugin.json
**Format**: JSON configuration with event matchers and actions
**Hook configuration**:

```bash
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/format-code.sh"
          }
        ]
      }
    ]
  }
}
```

**Available events**:

- `PreToolUse`: Before Claude uses any tool
- `PostToolUse`: After Claude successfully uses any tool
- `PostToolUseFailure`: After Claude tool execution fails
- `PermissionRequest`: When a permission dialog is shown
- `UserPromptSubmit`: When user submits a prompt
- `Notification`: When Claude Code sends notifications
- `Stop`: When Claude attempts to stop
- `SubagentStart`: When a subagent is started
- `SubagentStop`: When a subagent attempts to stop
- `SessionStart`: At the beginning of sessions
- `SessionEnd`: At the end of sessions
- `PreCompact`: Before conversation history is compacted

**Hook types**:

- `command`: Execute shell commands or scripts
- `prompt`: Evaluate a prompt with an LLM (uses `$ARGUMENTS` placeholder for context)
- `agent`: Run an agentic verifier with tools for complex verification tasks

### [​](#mcp-servers) MCP servers

Plugins can bundle Model Context Protocol (MCP) servers to connect Claude Code with external tools and services.
**Location**: `.mcp.json` in plugin root, or inline in plugin.json
**Format**: Standard MCP server configuration
**MCP server configuration**:

```bash
{
  "mcpServers": {
    "plugin-database": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
      "env": {
        "DB_PATH": "${CLAUDE_PLUGIN_ROOT}/data"
      }
    },
    "plugin-api-client": {
      "command": "npx",
      "args": ["@company/mcp-server", "--plugin-mode"],
      "cwd": "${CLAUDE_PLUGIN_ROOT}"
    }
  }
}
```

**Integration behavior**:

- Plugin MCP servers start automatically when the plugin is enabled
- Servers appear as standard MCP tools in Claude’s toolkit
- Server capabilities integrate seamlessly with Claude’s existing tools
- Plugin servers can be configured independently of user MCP servers

### [​](#lsp-servers) LSP servers

Looking to use LSP plugins? Install them from the official marketplace—search for “lsp” in the `/plugin` Discover tab. This section documents how to create LSP plugins for languages not covered by the official marketplace.

Plugins can provide [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) (LSP) servers to give Claude real-time code intelligence while working on your codebase.
LSP integration provides:

- **Instant diagnostics**: Claude sees errors and warnings immediately after each edit
- **Code navigation**: go to definition, find references, and hover information
- **Language awareness**: type information and documentation for code symbols

**Location**: `.lsp.json` in plugin root, or inline in `plugin.json`
**Format**: JSON configuration mapping language server names to their configurations
**`.lsp.json` file format**:

```bash
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}
```

**Inline in `plugin.json`**:

```bash
{
  "name": "my-plugin",
  "lspServers": {
    "go": {
      "command": "gopls",
      "args": ["serve"],
      "extensionToLanguage": {
        ".go": "go"
      }
    }
  }
}
```

**Required fields:**

| Field | Description |
| --- | --- |
| `command` | The LSP binary to execute (must be in PATH) |
| `extensionToLanguage` | Maps file extensions to language identifiers |

**Optional fields:**

| Field | Description |
| --- | --- |
| `args` | Command-line arguments for the LSP server |
| `transport` | Communication transport: `stdio` (default) or `socket` |
| `env` | Environment variables to set when starting the server |
| `initializationOptions` | Options passed to the server during initialization |
| `settings` | Settings passed via `workspace/didChangeConfiguration` |
| `workspaceFolder` | Workspace folder path for the server |
| `startupTimeout` | Max time to wait for server startup (milliseconds) |
| `shutdownTimeout` | Max time to wait for graceful shutdown (milliseconds) |
| `restartOnCrash` | Whether to automatically restart the server if it crashes |
| `maxRestarts` | Maximum number of restart attempts before giving up |

**You must install the language server binary separately.** LSP plugins configure how Claude Code connects to a language server, but they don’t include the server itself. If you see `Executable not found in $PATH` in the `/plugin` Errors tab, install the required binary for your language.

**Available LSP plugins:**

| Plugin | Language server | Install command |
| --- | --- | --- |
| `pyright-lsp` | Pyright (Python) | `pip install pyright` or `npm install -g pyright` |
| `typescript-lsp` | TypeScript Language Server | `npm install -g typescript-language-server typescript` |
| `rust-lsp` | rust-analyzer | [See rust-analyzer installation](https://rust-analyzer.github.io/manual.html#installation) |

Install the language server first, then install the plugin from the marketplace.

---

## [​](#plugin-installation-scopes) Plugin installation scopes

When you install a plugin, you choose a **scope** that determines where the plugin is available and who else can use it:

| Scope | Settings file | Use case |
| --- | --- | --- |
| `user` | `~/.claude/settings.json` | Personal plugins available across all projects (default) |
| `project` | `.claude/settings.json` | Team plugins shared via version control |
| `local` | `.claude/settings.local.json` | Project-specific plugins, gitignored |
| `managed` | `managed-settings.json` | Managed plugins (read-only, update only) |

Plugins use the same scope system as other Claude Code configurations. For installation instructions and scope flags, see [Install plugins](/docs/en/discover-plugins#install-plugins). For a complete explanation of scopes, see [Configuration scopes](/docs/en/settings#configuration-scopes).

---

## [​](#plugin-manifest-schema) Plugin manifest schema

The `plugin.json` file defines your plugin’s metadata and configuration. This section documents all supported fields and options.

### [​](#complete-schema) Complete schema

```bash
{
  "name": "plugin-name",
  "version": "1.2.0",
  "description": "Brief plugin description",
  "author": {
    "name": "Author Name",
    "email": "[email protected]",
    "url": "https://github.com/author"
  },
  "homepage": "https://docs.example.com/plugin",
  "repository": "https://github.com/author/plugin",
  "license": "MIT",
  "keywords": ["keyword1", "keyword2"],
  "commands": ["./custom/commands/special.md"],
  "agents": "./custom/agents/",
  "skills": "./custom/skills/",
  "hooks": "./config/hooks.json",
  "mcpServers": "./mcp-config.json",
  "outputStyles": "./styles/",
  "lspServers": "./.lsp.json"
}
```

### [​](#required-fields) Required fields

| Field | Type | Description | Example |
| --- | --- | --- | --- |
| `name` | string | Unique identifier (kebab-case, no spaces) | `"deployment-tools"` |

### [​](#metadata-fields) Metadata fields

| Field | Type | Description | Example |
| --- | --- | --- | --- |
| `version` | string | Semantic version | `"2.1.0"` |
| `description` | string | Brief explanation of plugin purpose | `"Deployment automation tools"` |
| `author` | object | Author information | `{"name": "Dev Team", "email": "[email protected]"}` |
| `homepage` | string | Documentation URL | `"https://docs.example.com"` |
| `repository` | string | Source code URL | `"https://github.com/user/plugin"` |
| `license` | string | License identifier | `"MIT"`, `"Apache-2.0"` |
| `keywords` | array | Discovery tags | `["deployment", "ci-cd"]` |

### [​](#component-path-fields) Component path fields

| Field | Type | Description | Example |
| --- | --- | --- | --- |
| `commands` | string|array | Additional command files/directories | `"./custom/cmd.md"` or `["./cmd1.md"]` |
| `agents` | string|array | Additional agent files | `"./custom/agents/"` |
| `skills` | string|array | Additional skill directories | `"./custom/skills/"` |
| `hooks` | string|object | Hook config path or inline config | `"./hooks.json"` |
| `mcpServers` | string|object | MCP config path or inline config | `"./mcp-config.json"` |
| `outputStyles` | string|array | Additional output style files/directories | `"./styles/"` |
| `lspServers` | string|object | [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) config for code intelligence (go to definition, find references, etc.) | `"./.lsp.json"` |

### [​](#path-behavior-rules) Path behavior rules

**Important**: Custom paths supplement default directories - they don’t replace them.

- If `commands/` exists, it’s loaded in addition to custom command paths
- All paths must be relative to plugin root and start with `./`
- Commands from custom paths use the same naming and namespacing rules
- Multiple paths can be specified as arrays for flexibility

**Path examples**:

```bash
{
  "commands": [
    "./specialized/deploy.md",
    "./utilities/batch-process.md"
  ],
  "agents": [
    "./custom-agents/reviewer.md",
    "./custom-agents/tester.md"
  ]
}
```

### [​](#environment-variables) Environment variables

**`${CLAUDE_PLUGIN_ROOT}`**: Contains the absolute path to your plugin directory. Use this in hooks, MCP servers, and scripts to ensure correct paths regardless of installation location.

```bash
{
  "hooks": {
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/process.sh"
          }
        ]
      }
    ]
  }
}
```

---

## [​](#plugin-caching-and-file-resolution) Plugin caching and file resolution

For security and verification purposes, Claude Code copies plugins to a cache directory rather than using them in-place. Understanding this behavior is important when developing plugins that reference external files.

### [​](#how-plugin-caching-works) How plugin caching works

When you install a plugin, Claude Code copies the plugin files to a cache directory:

- **For marketplace plugins with relative paths**: The path specified in the `source` field is copied recursively. For example, if your marketplace entry specifies `"source": "./plugins/my-plugin"`, the entire `./plugins` directory is copied.
- **For plugins with `.claude-plugin/plugin.json`**: The implicit root directory (the directory containing `.claude-plugin/plugin.json`) is copied recursively.

### [​](#path-traversal-limitations) Path traversal limitations

Plugins cannot reference files outside their copied directory structure. Paths that traverse outside the plugin root (such as `../shared-utils`) will not work after installation because those external files are not copied to the cache.

### [​](#working-with-external-dependencies) Working with external dependencies

If your plugin needs to access files outside its directory, you have two options:
**Option 1: Use symlinks**
Create symbolic links to external files within your plugin directory. Symlinks are honored during the copy process:

```bash
# Inside your plugin directory
ln -s /path/to/shared-utils ./shared-utils
```

The symlinked content will be copied into the plugin cache.
**Option 2: Restructure your marketplace**
Set the plugin path to a parent directory that contains all required files, then provide the rest of the plugin manifest directly in the marketplace entry:

```bash
{
  "name": "my-plugin",
  "source": "./",
  "description": "Plugin that needs root-level access",
  "commands": ["./plugins/my-plugin/commands/"],
  "agents": ["./plugins/my-plugin/agents/"],
  "strict": false
}
```

This approach copies the entire marketplace root, giving your plugin access to sibling directories.

Symlinks that point to locations outside the plugin’s logical root are followed during copying. This provides flexibility while maintaining the security benefits of the caching system.

---

## [​](#plugin-directory-structure) Plugin directory structure

### [​](#standard-plugin-layout) Standard plugin layout

A complete plugin follows this structure:

```bash
enterprise-plugin/
├── .claude-plugin/           # Metadata directory
│   └── plugin.json          # Required: plugin manifest
├── commands/                 # Default command location
│   ├── status.md
│   └── logs.md
├── agents/                   # Default agent location
│   ├── security-reviewer.md
│   ├── performance-tester.md
│   └── compliance-checker.md
├── skills/                   # Agent Skills
│   ├── code-reviewer/
│   │   └── SKILL.md
│   └── pdf-processor/
│       ├── SKILL.md
│       └── scripts/
├── hooks/                    # Hook configurations
│   ├── hooks.json           # Main hook config
│   └── security-hooks.json  # Additional hooks
├── .mcp.json                # MCP server definitions
├── .lsp.json                # LSP server configurations
├── scripts/                 # Hook and utility scripts
│   ├── security-scan.sh
│   ├── format-code.py
│   └── deploy.js
├── LICENSE                  # License file
└── CHANGELOG.md             # Version history
```

The `.claude-plugin/` directory contains the `plugin.json` file. All other directories (commands/, agents/, skills/, hooks/) must be at the plugin root, not inside `.claude-plugin/`.

### [​](#file-locations-reference) File locations reference

| Component | Default Location | Purpose |
| --- | --- | --- |
| **Manifest** | `.claude-plugin/plugin.json` | Required metadata file |
| **Commands** | `commands/` | Slash command Markdown files |
| **Agents** | `agents/` | Subagent Markdown files |
| **Skills** | `skills/` | Agent Skills with SKILL.md files |
| **Hooks** | `hooks/hooks.json` | Hook configuration |
| **MCP servers** | `.mcp.json` | MCP server definitions |
| **LSP servers** | `.lsp.json` | Language server configurations |

---

## [​](#cli-commands-reference) CLI commands reference

Claude Code provides CLI commands for non-interactive plugin management, useful for scripting and automation.

### [​](#plugin-install) plugin install

Install a plugin from available marketplaces.

```bash
claude plugin install <plugin> [options]
```

**Arguments:**

- `<plugin>`: Plugin name or `plugin-name@marketplace-name` for a specific marketplace

**Options:**

| Option | Description | Default |
| --- | --- | --- |
| `-s, --scope <scope>` | Installation scope: `user`, `project`, or `local` | `user` |
| `-h, --help` | Display help for command |  |

**Examples:**

```bash
# Install to user scope (default)
claude plugin install formatter@my-marketplace

# Install to project scope (shared with team)
claude plugin install formatter@my-marketplace --scope project

# Install to local scope (gitignored)
claude plugin install formatter@my-marketplace --scope local
```

### [​](#plugin-uninstall) plugin uninstall

Remove an installed plugin.

```bash
claude plugin uninstall <plugin> [options]
```

**Arguments:**

- `<plugin>`: Plugin name or `plugin-name@marketplace-name`

**Options:**

| Option | Description | Default |
| --- | --- | --- |
| `-s, --scope <scope>` | Uninstall from scope: `user`, `project`, or `local` | `user` |
| `-h, --help` | Display help for command |  |

**Aliases:** `remove`, `rm`

### [​](#plugin-enable) plugin enable

Enable a disabled plugin.

```bash
claude plugin enable <plugin> [options]
```

**Arguments:**

- `<plugin>`: Plugin name or `plugin-name@marketplace-name`

**Options:**

| Option | Description | Default |
| --- | --- | --- |
| `-s, --scope <scope>` | Scope to enable: `user`, `project`, or `local` | `user` |
| `-h, --help` | Display help for command |  |

### [​](#plugin-disable) plugin disable

Disable a plugin without uninstalling it.

```bash
claude plugin disable <plugin> [options]
```

**Arguments:**

- `<plugin>`: Plugin name or `plugin-name@marketplace-name`

**Options:**

| Option | Description | Default |
| --- | --- | --- |
| `-s, --scope <scope>` | Scope to disable: `user`, `project`, or `local` | `user` |
| `-h, --help` | Display help for command |  |

### [​](#plugin-update) plugin update

Update a plugin to the latest version.

```bash
claude plugin update <plugin> [options]
```

**Arguments:**

- `<plugin>`: Plugin name or `plugin-name@marketplace-name`

**Options:**

| Option | Description | Default |
| --- | --- | --- |
| `-s, --scope <scope>` | Scope to update: `user`, `project`, `local`, or `managed` | `user` |
| `-h, --help` | Display help for command |  |

---

## [​](#debugging-and-development-tools) Debugging and development tools

### [​](#debugging-commands) Debugging commands

Use `claude --debug` to see plugin loading details:

```bash
claude --debug
```

This shows:

- Which plugins are being loaded
- Any errors in plugin manifests
- Command, agent, and hook registration
- MCP server initialization

### [​](#common-issues) Common issues

| Issue | Cause | Solution |
| --- | --- | --- |
| Plugin not loading | Invalid `plugin.json` | Validate JSON syntax with `claude plugin validate` or `/plugin validate` |
| Commands not appearing | Wrong directory structure | Ensure `commands/` at root, not in `.claude-plugin/` |
| Hooks not firing | Script not executable | Run `chmod +x script.sh` |
| MCP server fails | Missing `${CLAUDE_PLUGIN_ROOT}` | Use variable for all plugin paths |
| Path errors | Absolute paths used | All paths must be relative and start with `./` |
| LSP `Executable not found in $PATH` | Language server not installed | Install the binary (e.g., `npm install -g typescript-language-server typescript`) |

### [​](#example-error-messages) Example error messages

**Manifest validation errors**:

- `Invalid JSON syntax: Unexpected token } in JSON at position 142`: check for missing commas, extra commas, or unquoted strings
- `Plugin has an invalid manifest file at .claude-plugin/plugin.json. Validation errors: name: Required`: a required field is missing
- `Plugin has a corrupt manifest file at .claude-plugin/plugin.json. JSON parse error: ...`: JSON syntax error

**Plugin loading errors**:

- `Warning: No commands found in plugin my-plugin custom directory: ./cmds. Expected .md files or SKILL.md in subdirectories.`: command path exists but contains no valid command files
- `Plugin directory not found at path: ./plugins/my-plugin. Check that the marketplace entry has the correct path.`: the `source` path in marketplace.json points to a non-existent directory
- `Plugin my-plugin has conflicting manifests: both plugin.json and marketplace entry specify components.`: remove duplicate component definitions or set `strict: true` in marketplace entry

### [​](#hook-troubleshooting) Hook troubleshooting

**Hook script not executing**:

1. Check the script is executable: `chmod +x ./scripts/your-script.sh`
2. Verify the shebang line: First line should be `#!/bin/bash` or `#!/usr/bin/env bash`
3. Check the path uses `${CLAUDE_PLUGIN_ROOT}`: `"command": "${CLAUDE_PLUGIN_ROOT}/scripts/your-script.sh"`
4. Test the script manually: `./scripts/your-script.sh`

**Hook not triggering on expected events**:

1. Verify the event name is correct (case-sensitive): `PostToolUse`, not `postToolUse`
2. Check the matcher pattern matches your tools: `"matcher": "Write|Edit"` for file operations
3. Confirm the hook type is valid: `command`, `prompt`, or `agent`

### [​](#mcp-server-troubleshooting) MCP server troubleshooting

**Server not starting**:

1. Check the command exists and is executable
2. Verify all paths use `${CLAUDE_PLUGIN_ROOT}` variable
3. Check the MCP server logs: `claude --debug` shows initialization errors
4. Test the server manually outside of Claude Code

**Server tools not appearing**:

1. Ensure the server is properly configured in `.mcp.json` or `plugin.json`
2. Verify the server implements the MCP protocol correctly
3. Check for connection timeouts in debug output

### [​](#directory-structure-mistakes) Directory structure mistakes

**Symptoms**: Plugin loads but components (commands, agents, hooks) are missing.
**Correct structure**: Components must be at the plugin root, not inside `.claude-plugin/`. Only `plugin.json` belongs in `.claude-plugin/`.

```bash
my-plugin/
├── .claude-plugin/
│   └── plugin.json      ← Only manifest here
├── commands/            ← At root level
├── agents/              ← At root level
└── hooks/               ← At root level
```

If your components are inside `.claude-plugin/`, move them to the plugin root.
**Debug checklist**:

1. Run `claude --debug` and look for “loading plugin” messages
2. Check that each component directory is listed in the debug output
3. Verify file permissions allow reading the plugin files

---

## [​](#distribution-and-versioning-reference) Distribution and versioning reference

### [​](#version-management) Version management

Follow semantic versioning for plugin releases:

```bash
{
  "name": "my-plugin",
  "version": "2.1.0"
}
```

**Version format**: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (incompatible API changes)
- **MINOR**: New features (backward-compatible additions)
- **PATCH**: Bug fixes (backward-compatible fixes)

**Best practices**:

- Start at `1.0.0` for your first stable release
- Update the version in `plugin.json` before distributing changes
- Document changes in a `CHANGELOG.md` file
- Use pre-release versions like `2.0.0-beta.1` for testing

---

## [​](#see-also) See also

- [Plugins](/docs/en/plugins) - Tutorials and practical usage
- [Plugin marketplaces](/docs/en/plugin-marketplaces) - Creating and managing marketplaces
- [Slash commands](/docs/en/slash-commands) - Command development details
- [Subagents](/docs/en/sub-agents) - Agent configuration and capabilities
- [Agent Skills](/docs/en/skills) - Extend Claude’s capabilities
- [Hooks](/docs/en/hooks) - Event handling and automation
- [MCP](/docs/en/mcp) - External tool integration
- [Settings](/docs/en/settings) - Configuration options for plugins