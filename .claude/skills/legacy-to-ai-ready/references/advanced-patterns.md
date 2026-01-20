# Advanced Patterns & Edge Cases

Handling special scenarios, migrations, and team collaboration.

## Table of Contents
- [Local Configuration](#local-configuration)
- [File Ignoring](#file-ignoring)
- [Permissions](#permissions)
- [Migration Strategies](#migration-strategies)
- [Team Collaboration](#team-collaboration)
- [Monorepo Patterns](#monorepo-patterns)
- [Sensitive Files](#sensitive-files)

---

## Local Configuration

### CLAUDE.local.md

Personal preferences not shared with team. Place at project root.

**Use cases:**
- Personal shortcuts and aliases
- Local environment specifics
- Individual workflow preferences
- Experimental settings

**Example:**
```markdown
# My Local Preferences

## Shortcuts
- I prefer verbose error messages
- Always show full stack traces
- Use my preferred test runner flags: --watch --coverage

## Environment
- My local DB is on port 5433 (not 5432)
- Use localhost instead of Docker for services

## Personal Style
- I like detailed comments explaining "why"
- Prefer longer variable names for clarity
```

**Git configuration:**
```gitignore
# .gitignore
CLAUDE.local.md
```

### When to Use CLAUDE.local.md

| Scenario | Use CLAUDE.md | Use CLAUDE.local.md |
|----------|---------------|---------------------|
| Coding standards | ✓ | |
| Build commands | ✓ | |
| Personal shortcuts | | ✓ |
| Local port overrides | | ✓ |
| Experimental features | | ✓ |

---

## File Ignoring

### .claudeignore

Control which files Claude should not read or modify.

**Location:** Project root (`.claudeignore`)

**Syntax:** Same as .gitignore

**Common patterns:**
```gitignore
# Secrets and credentials
.env
.env.*
*.pem
*.key
credentials.json
secrets/

# Large generated files
dist/
build/
node_modules/
*.min.js
*.bundle.js

# Binary files
*.png
*.jpg
*.pdf
*.zip

# Sensitive data
**/data/production/
**/backups/
*.sql.gz

# Vendor code (don't modify)
vendor/
third_party/
```

### Auto-generating .claudeignore

Based on .gitignore analysis:

```python
# Patterns to always include in .claudeignore
ALWAYS_IGNORE = [
    "# Secrets",
    ".env",
    ".env.*",
    "*.pem",
    "*.key",
    "credentials*.json",
    "secrets/",
    "",
    "# Large/Binary",
    "*.min.js",
    "*.bundle.js",
    "*.map",
    "",
    "# Data",
    "*.sql",
    "*.db",
    "*.sqlite",
]
```

---

## Permissions

### .claude/settings.json permissions

Control what tools Claude can use:

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Edit",
      "Write",
      "Bash(npm:*)",
      "Bash(git:*)",
      "Bash(pnpm:*)"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(sudo:*)",
      "Bash(curl|wget:*)"
    ]
  }
}
```

### Permission patterns

| Pattern | Meaning |
|---------|---------|
| `Bash(npm:*)` | Allow npm commands |
| `Bash(git add:*)` | Allow git add only |
| `mcp__github` | Allow all GitHub MCP tools |
| `mcp__postgres__query` | Allow only query, not execute |

### Recommended defaults

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Glob",
      "Grep",
      "Bash(npm:*)",
      "Bash(pnpm:*)",
      "Bash(yarn:*)",
      "Bash(git:*)",
      "Bash(python:*)",
      "Bash(pytest:*)",
      "Edit",
      "Write"
    ],
    "deny": [
      "Bash(rm -rf /*:*)",
      "Bash(sudo:*)",
      "Bash(*--force*:*)"
    ]
  }
}
```

---

## Migration Strategies

### Scenario 1: No existing configuration

Standard workflow applies. Create from scratch.

### Scenario 2: Has README but no CLAUDE.md

1. **Extract from README:**
   - Build/test commands
   - Setup instructions
   - Architecture overview

2. **Convert to CLAUDE.md format:**
   - Keep README for humans
   - CLAUDE.md for AI-specific instructions

### Scenario 3: Has basic CLAUDE.md

1. **Audit existing content:**
   - Check if follows best practices
   - Identify gaps

2. **Enhance incrementally:**
   - Add missing sections
   - Don't remove working content
   - Add rules/skills as needed

### Scenario 4: Has complete .claude/ setup

1. **Validate structure:**
   - Check skill formats
   - Verify agent configurations
   - Test commands

2. **Update patterns:**
   - Align with latest best practices
   - Add new features (MCP, hooks)

### Migration checklist

```markdown
## Migration Audit

### Current State
- [ ] Has CLAUDE.md?
- [ ] Has .claude/ directory?
- [ ] Has rules files?
- [ ] Has skills?
- [ ] Has agents?
- [ ] Has commands?
- [ ] Has hooks configured?

### Quality Check
- [ ] CLAUDE.md < 500 lines?
- [ ] Skills have proper frontmatter?
- [ ] Commands have descriptions?
- [ ] No sensitive data exposed?

### Gaps to Fill
- [ ] Missing: ___
- [ ] Outdated: ___
- [ ] Needs improvement: ___
```

---

## Team Collaboration

### Git workflow for .claude/

**What to commit:**
```
CLAUDE.md              ✓ Commit
.claude/rules/         ✓ Commit
.claude/skills/        ✓ Commit
.claude/agents/        ✓ Commit
.claude/commands/      ✓ Commit
.claude/settings.json  ✓ Commit (without secrets)
```

**What to ignore:**
```gitignore
CLAUDE.local.md
.claude/settings.local.json
```

### Code review for AI configs

When reviewing .claude/ changes:

1. **CLAUDE.md changes:**
   - Does it accurately reflect current practices?
   - Is it concise enough?
   - Any outdated information?

2. **Skill changes:**
   - Is the description clear?
   - Does it follow skill patterns?
   - Is it tested?

3. **Command changes:**
   - Is it useful for the team?
   - Does it have proper permissions?

### Ownership model

```markdown
## Config Ownership

| Config | Owner | Review Required |
|--------|-------|-----------------|
| CLAUDE.md | Tech Lead | Yes |
| rules/*.md | Module Owner | Yes |
| skills/* | Skill Author | Yes |
| commands/* | Any | Lightweight |
| settings.json | DevOps | Yes |
```

---

## Monorepo Patterns

### Structure

```
monorepo/
├── CLAUDE.md                    # Root: shared conventions
├── .claude/
│   ├── rules/
│   │   └── shared.md            # Shared rules
│   └── skills/
│       └── monorepo-nav/        # Navigation helper
├── packages/
│   ├── frontend/
│   │   ├── CLAUDE.md            # Package-specific
│   │   └── .claude/rules/
│   ├── backend/
│   │   ├── CLAUDE.md
│   │   └── .claude/rules/
│   └── shared/
│       └── CLAUDE.md
└── apps/
    └── web/
        └── CLAUDE.md
```

### Root CLAUDE.md

```markdown
# Monorepo

## Structure
- `packages/` - Shared libraries
- `apps/` - Applications
- `tools/` - Build tools

## Commands
- `pnpm install` - Install all deps
- `pnpm build` - Build all packages
- `pnpm test` - Test all packages

## Working in packages
Each package has its own CLAUDE.md with specific conventions.
Navigate to package directory for package-specific context.

## Cross-package changes
When modifying shared packages, check dependents:
\`\`\`bash
pnpm why [package-name]
\`\`\`
```

### Package-specific CLAUDE.md

```markdown
# Frontend Package

## This Package
React component library for the design system.

## Local Commands
- `pnpm dev` - Storybook
- `pnpm test` - Jest tests
- `pnpm build` - Build library

## Dependencies
- Uses: `@repo/shared`, `@repo/types`
- Used by: `apps/web`, `apps/mobile`

## Conventions
[Package-specific patterns]
```

---

## Sensitive Files

### Detection patterns

Files to protect:

```python
SENSITIVE_PATTERNS = [
    # Environment
    ".env", ".env.*",

    # Keys and certs
    "*.pem", "*.key", "*.crt", "*.p12",
    "*.keystore", "*.jks",

    # Credentials
    "credentials*.json",
    "service-account*.json",
    "*secret*",
    "*password*",

    # Cloud configs
    ".aws/", ".gcp/", ".azure/",
    "kubeconfig*",

    # Database
    "*.sql", "*.dump",
    "database.yml",

    # IDE with potential secrets
    ".idea/", ".vscode/settings.json",
]
```

### Protection strategies

1. **Add to .claudeignore:**
   ```gitignore
   .env*
   *.pem
   credentials*.json
   ```

2. **Configure hooks to block:**
   ```json
   {
     "hooks": {
       "PreToolUse": [{
         "matcher": "Edit|Write|Read",
         "hooks": [{
           "type": "command",
           "command": "python -c \"import sys,json; p=json.load(sys.stdin).get('tool_input',{}).get('file_path',''); sys.exit(2 if any(x in p for x in ['.env','.pem','secret','credential']) else 0)\""
         }]
       }]
     }
   }
   ```

3. **Document in CLAUDE.md:**
   ```markdown
   ## Security
   NEVER read or modify:
   - .env files
   - Any file with 'secret' or 'credential' in name
   - *.pem, *.key files
   ```

### Audit command

```bash
# Find potentially sensitive files
find . -type f \( \
  -name "*.env*" -o \
  -name "*.pem" -o \
  -name "*.key" -o \
  -name "*secret*" -o \
  -name "*credential*" \
\) -not -path "./node_modules/*" -not -path "./.git/*"
```
