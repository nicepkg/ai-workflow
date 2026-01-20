# Rules Patterns Reference

## Purpose

`.claude/rules/` provides modular, path-specific instructions that supplement CLAUDE.md. Use rules for:
- Language-specific guidelines
- Module-specific conventions
- Team-specific workflows
- Conditional instructions

## Structure

```
.claude/rules/
├── code-style.md       # General coding style
├── testing.md          # Testing conventions
├── api-design.md       # API patterns
├── security.md         # Security requirements
├── frontend/
│   ├── react.md        # React-specific rules
│   └── styles.md       # CSS conventions
└── backend/
    ├── api.md          # Backend API rules
    └── database.md     # Database conventions
```

## Rule File Template

### Unconditional Rule (applies to all files)

```markdown
# Code Style Rules

## Naming Conventions
- Use camelCase for variables and functions
- Use PascalCase for classes and types
- Use UPPER_SNAKE_CASE for constants

## Comments
- Document public APIs with JSDoc
- Avoid obvious comments
- Explain "why" not "what"
```

### Conditional Rule (applies to specific paths)

```yaml
---
paths:
  - "src/api/**/*.ts"
---
```

```markdown
# API Development Rules

## Request Validation
- Validate all input with Zod schemas
- Return typed responses
- Use standard error format

## Security
- Authenticate all endpoints
- Check authorization
- Sanitize user input
```

## Path Patterns

| Pattern | Matches |
|---------|---------|
| `**/*.ts` | All TypeScript files |
| `src/**/*` | All files under src/ |
| `*.md` | Markdown files in root |
| `src/api/**/*.ts` | TS files in API directory |
| `tests/**/*.test.ts` | Test files |

## Brace Expansion

```yaml
---
paths:
  - "src/**/*.{ts,tsx}"
  - "{src,lib}/**/*.ts"
---
```

## Common Rule Files

### Code Style (`code-style.md`)

```markdown
# Code Style

## TypeScript
- Enable strict mode
- Prefer `const` over `let`
- Use explicit return types for public functions
- Avoid `any`, use `unknown` if needed

## Formatting
- 2-space indentation
- Single quotes for strings
- Trailing commas in multiline
- No semicolons (per project preference)

## Imports
1. External packages (alphabetical)
2. Internal modules (alphabetical)
3. Relative imports (by distance)
```

### Testing (`testing.md`)

```markdown
# Testing Rules

## Test Organization
- Unit tests: `*.test.ts` alongside source
- Integration: `tests/integration/`
- E2E: `tests/e2e/`

## Naming
- Describe behavior: `should [expected behavior] when [condition]`
- Group by function/component

## Coverage Requirements
- Minimum 80% coverage for new code
- Critical paths must have integration tests
```

### API Design (`api-design.md`)

```yaml
---
paths:
  - "src/api/**/*"
  - "src/routes/**/*"
---
```

```markdown
# API Design Rules

## Endpoint Structure
- REST: `/api/v1/[resource]/[id]/[action]`
- Use plural nouns for resources

## Response Format
\`\`\`json
{
  "success": boolean,
  "data": object | null,
  "error": { "code": string, "message": string } | null
}
\`\`\`

## Status Codes
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Server Error

## Validation
- Use Zod schemas for all inputs
- Return detailed validation errors
```

### Security (`security.md`)

```markdown
# Security Rules

## Input Validation
- Never trust user input
- Validate and sanitize all inputs
- Use parameterized queries

## Authentication
- Use secure session management
- Implement rate limiting
- Log authentication events

## Secrets
- Never commit secrets
- Use environment variables
- Rotate credentials regularly

## Dependencies
- Keep dependencies updated
- Review security advisories
- Use lockfiles
```

### React Components (`frontend/react.md`)

```yaml
---
paths:
  - "src/components/**/*.tsx"
  - "src/pages/**/*.tsx"
---
```

```markdown
# React Rules

## Component Structure
1. Imports
2. Types/Interfaces
3. Component function
4. Styles (if co-located)

## Hooks
- Custom hooks in `src/hooks/`
- Prefix with `use`
- Document dependencies

## State Management
- Local state: useState
- Server state: React Query
- Global state: Context/Zustand

## Performance
- Memoize expensive computations
- Use `memo` for pure components
- Lazy load routes
```

### Database (`backend/database.md`)

```yaml
---
paths:
  - "src/db/**/*"
  - "src/models/**/*"
  - "prisma/**/*"
---
```

```markdown
# Database Rules

## Queries
- Use ORM for standard operations
- Raw SQL for complex queries
- Always use transactions for multi-step operations

## Migrations
- One migration per change
- Always write down migrations
- Test migrations locally first

## Naming
- Tables: snake_case, plural
- Columns: snake_case
- Foreign keys: `[table]_id`

## Indexes
- Primary keys: automatic
- Foreign keys: always index
- Query patterns: create indexes
```

## User-Level Rules

Personal rules in `~/.claude/rules/`:

```
~/.claude/rules/
├── preferences.md      # Personal coding style
└── workflows.md        # Personal workflows
```

## Extraction Patterns

When analyzing legacy code for rules:

1. **Check existing configs**
   - .eslintrc, .prettierrc
   - tsconfig.json strict settings
   - .editorconfig

2. **Analyze code patterns**
   - Common coding conventions
   - Import organization
   - Error handling patterns

3. **Identify module boundaries**
   - API vs frontend vs shared
   - Test organization
   - Module-specific conventions

4. **Document team standards**
   - Code review requirements
   - Merge criteria
   - Documentation expectations
