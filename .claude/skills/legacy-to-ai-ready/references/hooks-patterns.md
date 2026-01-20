# Hooks Design Patterns Reference

## Purpose

Hooks are shell commands that execute at specific events in Claude Code's lifecycle. Use hooks for:
- Automatic code formatting
- Pre-commit validation
- Custom notifications
- Logging and compliance
- File protection

## Configuration Location

```json
// .claude/settings.json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here"
          }
        ]
      }
    ]
  }
}
```

## Hook Events

| Event | Trigger | Use Case |
|-------|---------|----------|
| `PreToolUse` | Before tool runs | Validation, blocking |
| `PostToolUse` | After tool completes | Formatting, logging |
| `PermissionRequest` | Permission dialog | Auto-allow/deny |
| `UserPromptSubmit` | User submits prompt | Prompt validation |
| `Notification` | Claude sends notification | Custom alerts |
| `Stop` | Claude finishes | Cleanup, summary |
| `SessionStart` | Session begins | Setup, initialization |
| `SessionEnd` | Session ends | Cleanup |

## Matchers

| Pattern | Matches |
|---------|---------|
| `Write` | Exact match |
| `Edit\|Write` | Either Edit or Write |
| `Notebook.*` | Regex pattern |
| `*` or `""` | All tools |

## Common Hook Patterns

### Code Formatting (PostToolUse)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read f; [[ \"$f\" == *.ts ]] && npx prettier --write \"$f\"; }"
          }
        ]
      }
    ]
  }
}
```

### Python Formatting

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read f; [[ \"$f\" == *.py ]] && black \"$f\" && isort \"$f\"; }"
          }
        ]
      }
    ]
  }
}
```

### File Protection (PreToolUse)

Block edits to sensitive files:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 -c \"import json,sys; d=json.load(sys.stdin); p=d.get('tool_input',{}).get('file_path',''); sys.exit(2 if any(x in p for x in ['.env','.git/','secrets/']) else 0)\""
          }
        ]
      }
    ]
  }
}
```

### Command Logging (PreToolUse)

Log all bash commands:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.command' >> ~/.claude/command-log.txt"
          }
        ]
      }
    ]
  }
}
```

### Custom Notifications

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude needs attention\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

### Session Initialization

Install dependencies on session start:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/scripts/setup.sh"
          }
        ]
      }
    ]
  }
}
```

### Lint on Edit

Run linter after file modifications:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read f; [[ -f \"$f\" ]] && npm run lint -- \"$f\"; }"
          }
        ]
      }
    ]
  }
}
```

## Exit Codes

| Exit Code | Behavior |
|-----------|----------|
| 0 | Success, continue |
| 1 | Error, continue with warning |
| 2 | Block the tool operation |

## Hook Input (stdin)

Hooks receive JSON input via stdin:

```json
{
  "session_id": "abc123",
  "tool_name": "Edit",
  "tool_input": {
    "file_path": "/path/to/file.ts",
    "old_string": "...",
    "new_string": "..."
  }
}
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `CLAUDE_PROJECT_DIR` | Project root directory |
| `CLAUDE_SESSION_ID` | Current session ID |
| `CLAUDE_ENV_FILE` | File for persisting env vars |

## Project-Specific Scripts

Reference scripts using `$CLAUDE_PROJECT_DIR`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/format.sh"
          }
        ]
      }
    ]
  }
}
```

Example script `.claude/hooks/format.sh`:

```bash
#!/bin/bash
INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path')

case "$FILE" in
  *.ts|*.tsx) npx prettier --write "$FILE" ;;
  *.py) black "$FILE" && isort "$FILE" ;;
  *.go) gofmt -w "$FILE" ;;
  *.rs) rustfmt "$FILE" ;;
esac
```

## Language-Specific Configurations

### TypeScript/JavaScript

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read f; [[ \"$f\" =~ \\.(ts|tsx|js|jsx)$ ]] && npx prettier --write \"$f\" && npx eslint --fix \"$f\"; }"
          }
        ]
      }
    ]
  }
}
```

### Python

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read f; [[ \"$f\" == *.py ]] && black \"$f\" && isort \"$f\" && ruff check --fix \"$f\"; }"
          }
        ]
      }
    ]
  }
}
```

### Go

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read f; [[ \"$f\" == *.go ]] && gofmt -w \"$f\" && goimports -w \"$f\"; }"
          }
        ]
      }
    ]
  }
}
```

## Extraction Patterns

When analyzing legacy code for hooks:

1. **Check existing tooling**
   - Pre-commit hooks
   - Git hooks
   - CI/CD formatting steps

2. **Identify formatting tools**
   - Prettier, ESLint (JS/TS)
   - Black, isort, ruff (Python)
   - gofmt, goimports (Go)

3. **Find validation rules**
   - Protected files/directories
   - Required checks before commit
   - Lint rules

4. **Note team practices**
   - Auto-formatting expectations
   - Logging requirements
   - Notification preferences
