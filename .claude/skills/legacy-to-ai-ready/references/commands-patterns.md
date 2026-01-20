# Slash Commands Design Patterns Reference

## Purpose

Slash commands are quick, reusable prompts triggered by `/command`. Create commands for:
- Frequently used prompts
- Common workflows
- Quick reminders or templates
- Team-standardized operations

## Command Structure

```
.claude/commands/
├── commit.md           # /commit
├── review.md           # /review
├── deploy.md           # /deploy
└── frontend/
    └── component.md    # /component (project:frontend)
```

## Command Template

```markdown
---
description: Brief description shown in /help
allowed-tools: Tool1, Tool2
argument-hint: [optional-args]
---

# Command Instructions

[Detailed prompt for Claude to follow]
```

## Frontmatter Options

| Field | Required | Description |
|-------|----------|-------------|
| `description` | No | Shown in `/help` (uses first line if not set) |
| `allowed-tools` | No | Tools the command can use |
| `argument-hint` | No | Args shown in autocomplete |
| `model` | No | Specific model to use |
| `context` | No | Set to `fork` for isolated execution |
| `agent` | No | Agent type when `context: fork` |

## Common Project Commands

### Git Commit
```markdown
---
description: Create a git commit with proper message format
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
argument-hint: [optional message]
---

## Context
- Current git status: !`git status`
- Current git diff: !`git diff HEAD`
- Recent commits: !`git log --oneline -5`

## Instructions
Create a git commit following this format:
- type(scope): subject
- Body explaining what and why

Types: feat, fix, docs, style, refactor, test, chore

If $ARGUMENTS provided, use as commit message hint.
```

### PR Review
```markdown
---
description: Review pull request changes
allowed-tools: Bash(git:*), Read, Grep
argument-hint: [branch-name]
---

## Context
- Changes to review: !`git diff main...$1`
- Changed files: !`git diff --name-only main...$1`

## Instructions
Review the PR changes for:
1. Code quality and clarity
2. Potential bugs or edge cases
3. Test coverage
4. Security concerns
5. Performance implications

Provide structured feedback with:
- Approval recommendation
- Required changes (if any)
- Suggestions for improvement
```

### Deploy
```markdown
---
description: Deploy to specified environment
allowed-tools: Bash
argument-hint: [staging|production]
---

## Instructions
Deploy to $1 environment:

1. Verify current branch is deployable
2. Run pre-deployment checks
3. Execute deployment command
4. Verify deployment success

For staging: `npm run deploy:staging`
For production: `npm run deploy:prod`
```

### Test
```markdown
---
description: Run tests with coverage
allowed-tools: Bash
argument-hint: [file-pattern]
---

## Instructions
Run tests:
- If $ARGUMENTS provided, run tests matching pattern
- Otherwise, run full test suite

Command: `npm test $ARGUMENTS`

After tests complete:
1. Report pass/fail summary
2. Highlight any failures
3. Show coverage changes if available
```

### Create Component
```markdown
---
description: Create a new React component
allowed-tools: Write, Read
argument-hint: [ComponentName]
---

## Instructions
Create a new React component named $1:

1. Create `src/components/$1/$1.tsx`:
\`\`\`tsx
import { FC } from 'react';
import styles from './$1.module.css';

interface $1Props {
  // TODO: Define props
}

export const $1: FC<$1Props> = (props) => {
  return (
    <div className={styles.container}>
      {/* TODO: Implement */}
    </div>
  );
};
\`\`\`

2. Create `src/components/$1/$1.module.css`
3. Create `src/components/$1/$1.test.tsx`
4. Export from `src/components/$1/index.ts`
```

### API Endpoint
```markdown
---
description: Create a new API endpoint
allowed-tools: Write, Read
argument-hint: [resource] [method]
---

## Instructions
Create API endpoint for $1 with $2 method:

1. Create route handler in `src/api/$1/route.ts`
2. Add request/response types
3. Implement handler logic
4. Add input validation
5. Create test file

Follow project API patterns from .claude/skills/api-patterns/
```

### Database Migration
```markdown
---
description: Create a database migration
allowed-tools: Bash, Write
argument-hint: [migration-name]
---

## Context
- Existing migrations: !`ls -la src/db/migrations/`

## Instructions
Create a new migration named $1:

1. Run: `npm run migrate:create $1`
2. Edit the generated migration file
3. Implement both up and down functions
4. Test locally: `npm run migrate:dev`
```

### Format Code
```markdown
---
description: Format and lint code
allowed-tools: Bash
argument-hint: [file-or-directory]
---

## Instructions
Format and lint code:

1. Run formatter: `npm run format $ARGUMENTS`
2. Run linter: `npm run lint $ARGUMENTS`
3. Report any remaining issues
```

## Bash Command Execution

Use `!` prefix to execute bash commands and include output:

```markdown
## Context
- Current branch: !`git branch --show-current`
- Status: !`git status --short`
- Last commit: !`git log -1 --oneline`
```

## File References

Use `@` to include file contents:

```markdown
Review the implementation in @src/auth/login.ts

Compare @src/old.ts with @src/new.ts
```

## Arguments

### All Arguments
```markdown
# $ARGUMENTS captures all args
Search for: $ARGUMENTS
```

### Positional Arguments
```markdown
# $1, $2, $3 for specific positions
Create $1 in $2 with $3 priority
```

## Namespacing

Subdirectories create namespaced commands:

```
.claude/commands/
├── frontend/
│   └── component.md    # /component (project:frontend)
├── backend/
│   └── endpoint.md     # /endpoint (project:backend)
└── deploy.md           # /deploy (project)
```

## Extraction Patterns

When analyzing legacy code for commands:

1. **Identify common operations**
   - Build/test/deploy commands
   - Code generation patterns
   - Review procedures

2. **Find team workflows**
   - PR review process
   - Release procedures
   - Debugging steps

3. **Document shortcuts**
   - Frequently typed commands
   - Multi-step procedures
   - Environment setup
