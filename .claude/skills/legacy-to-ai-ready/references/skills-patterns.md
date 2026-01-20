# Skills Design Patterns Reference

## Purpose

Skills give Claude specialized knowledge for specific tasks. Create project-specific skills when:
- There are complex domain-specific workflows
- Certain tasks require consistent procedures
- Team knowledge needs to be codified

## Skill Structure

```
.claude/skills/
└── skill-name/
    ├── SKILL.md         # Required: main instructions
    ├── scripts/         # Optional: executable code
    ├── references/      # Optional: detailed docs
    └── assets/          # Optional: templates/files
```

## When to Create Skills

### Good Candidates
1. **API Integration Patterns** - Custom API workflows
2. **Database Operations** - Complex query patterns, migrations
3. **Deployment Procedures** - Release workflows
4. **Code Generation** - Project-specific generators
5. **Testing Strategies** - Complex test scenarios
6. **Documentation** - Doc generation patterns

### Not Suitable for Skills
1. Simple, one-off tasks
2. Generic coding knowledge
3. Information that changes frequently

## SKILL.md Template

```markdown
---
name: skill-name
description: What this skill does and when to use it. Use when [specific triggers]. Handles [specific tasks].
---

# Skill Name

## Quick Start
[Minimal example to get started]

## Workflow
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Patterns

### Pattern 1: [Name]
[Description and example]

### Pattern 2: [Name]
[Description and example]

## Scripts
- `scripts/script-name.py`: [What it does]

## References
- [reference-name.md](references/reference-name.md): [When to read]
```

## Common Project Skills

### API Skill
```markdown
---
name: api-patterns
description: Project API design patterns. Use when creating/modifying API endpoints, handling requests, or working with API responses.
---

# API Patterns

## Endpoint Structure
All endpoints follow: `/api/v1/[resource]/[action]`

## Request Validation
Use Zod schemas in `src/schemas/`:
\`\`\`typescript
const CreateUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1)
});
\`\`\`

## Response Format
\`\`\`json
{
  "success": true,
  "data": { ... },
  "error": null
}
\`\`\`

## Error Handling
Use `ApiError` class from `src/lib/errors`:
\`\`\`typescript
throw new ApiError(400, "VALIDATION_ERROR", "Invalid input");
\`\`\`
```

### Database Skill
```markdown
---
name: database-patterns
description: Database operations and query patterns. Use when writing queries, creating migrations, or working with data models.
---

# Database Patterns

## Schema Reference
See [references/schema.md](references/schema.md) for full schema.

## Common Queries
### User lookup
\`\`\`sql
SELECT * FROM users WHERE id = $1 AND deleted_at IS NULL;
\`\`\`

## Migration Pattern
1. Create migration: `npm run migrate:create [name]`
2. Write up/down functions
3. Test locally: `npm run migrate:dev`
4. Apply: `npm run migrate:prod`
```

### Testing Skill
```markdown
---
name: testing-patterns
description: Testing strategies and patterns. Use when writing tests, setting up test data, or debugging test failures.
---

# Testing Patterns

## Test Organization
- Unit tests: `*.test.ts` next to source
- Integration: `tests/integration/`
- E2E: `tests/e2e/`

## Fixtures
Use factories in `tests/factories/`:
\`\`\`typescript
import { createUser } from '@/tests/factories';
const user = await createUser({ role: 'admin' });
\`\`\`

## Mocking Patterns
\`\`\`typescript
vi.mock('@/lib/email', () => ({
  sendEmail: vi.fn().mockResolvedValue({ sent: true })
}));
\`\`\`
```

### Deployment Skill
```markdown
---
name: deployment-guide
description: Deployment procedures and release workflow. Use when deploying, creating releases, or troubleshooting deployments.
---

# Deployment Guide

## Pre-Deployment Checklist
- [ ] All tests pass
- [ ] Version bumped
- [ ] Changelog updated
- [ ] PR approved

## Deployment Steps
1. Merge to main
2. Tag release: `git tag v[version]`
3. Push tag: `git push --tags`
4. Monitor CI/CD pipeline
5. Verify deployment

## Rollback
\`\`\`bash
./scripts/rollback.sh [previous-version]
\`\`\`
```

## Extraction Patterns

When analyzing legacy code for skills:

1. **Identify repeated patterns**
   - Common query patterns
   - API response handling
   - Error handling workflows

2. **Find domain knowledge**
   - Business logic rules
   - Data validation rules
   - Calculation formulas

3. **Document complex workflows**
   - Multi-step procedures
   - Decision trees
   - State machines

4. **Extract tool-specific knowledge**
   - Build tool configurations
   - Test framework patterns
   - Deployment procedures

## Progressive Disclosure

Keep SKILL.md concise (<500 lines). Split into references:

```markdown
## Quick Start
[Essential info here]

## Advanced Topics
- **Complex Queries**: See [references/queries.md](references/queries.md)
- **Error Codes**: See [references/errors.md](references/errors.md)
- **Performance**: See [references/performance.md](references/performance.md)
```
