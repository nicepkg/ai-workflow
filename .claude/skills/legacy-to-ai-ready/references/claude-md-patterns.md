# CLAUDE.md Patterns Reference

## Purpose

CLAUDE.md is the project memory file loaded into every Claude Code conversation. It should contain:
- Project-wide coding standards and conventions
- Common commands and workflows
- Architecture decisions and patterns
- Team-specific knowledge

## Structure Template

```markdown
# [Project Name]

## Quick Reference
- Build: `[build command]`
- Test: `[test command]`
- Lint: `[lint command]`
- Deploy: `[deploy command]`

## Code Style

### Naming Conventions
- [Convention rules]

### File Organization
- [Directory structure conventions]

### Import Order
- [Import ordering rules]

## Architecture

### Core Patterns
- [Key architectural patterns used]

### Data Flow
- [How data moves through the system]

### Error Handling
- [Error handling conventions]

## Testing

### Test Organization
- [How tests are structured]

### Testing Patterns
- [Common testing patterns]

## Git Workflow
- Branch naming: `[pattern]`
- Commit format: `[format]`
- PR requirements: `[requirements]`

## Environment
- Required env vars: `[list]`
- Local setup: `[steps]`
```

## Content Guidelines

### What to Include
1. **Frequently used commands** - Build, test, lint, deploy
2. **Coding conventions** - Naming, formatting, imports
3. **Architecture patterns** - Domain boundaries, data flow
4. **Git workflow** - Branch naming, commit format
5. **Environment setup** - Required variables, local config

### What to Avoid
1. Generic advice Claude already knows
2. Verbose explanations (prefer examples)
3. Information that changes frequently
4. Sensitive data or secrets

## Language-Specific Patterns

### TypeScript/JavaScript Projects
```markdown
## Code Style
- Use TypeScript strict mode
- Prefer `const` over `let`
- Use named exports, avoid default exports
- Imports: external → internal → relative

## Patterns
- Use Zod for runtime validation
- Prefer composition over inheritance
- Use Result types for error handling
```

### Python Projects
```markdown
## Code Style
- Follow PEP 8
- Use type hints for all public functions
- Docstrings: Google style
- Imports: stdlib → third-party → local

## Patterns
- Use dataclasses for data containers
- Prefer Protocol over ABC for interfaces
- Use contextmanager for resource management
```

### Go Projects
```markdown
## Code Style
- Run `gofmt` before commit
- Error handling: wrap with context
- Package naming: singular, lowercase

## Patterns
- Use interfaces at consumption point
- Prefer composition over embedding
- Context propagation for cancellation
```

## Imports in CLAUDE.md

Use `@path/to/file` to import additional files:

```markdown
# Project Memory

## Core Guidelines
@docs/coding-standards.md
@docs/architecture.md

## API Reference
@docs/api/README.md
```

## Rules Directory Alternative

For larger projects, use `.claude/rules/` for modular organization:

```
.claude/rules/
├── code-style.md      # Coding conventions
├── testing.md         # Test guidelines
├── api-design.md      # API patterns
└── security.md        # Security requirements
```

Each rule file can have path-specific scope:

```yaml
---
paths:
  - "src/api/**/*.ts"
---
# API Rules
- All endpoints must validate input
- Use standard error response format
```

## Extraction Patterns

When analyzing a legacy codebase, extract:

1. **From package.json/pyproject.toml/go.mod**
   - Build/test commands
   - Dependencies and their purposes

2. **From .eslintrc/.prettierrc/etc.**
   - Formatting rules
   - Linting conventions

3. **From existing README**
   - Project overview
   - Setup instructions

4. **From code structure**
   - Directory organization patterns
   - Module boundaries
   - Naming conventions

5. **From git history**
   - Commit message format
   - Branch naming patterns
   - PR workflow
