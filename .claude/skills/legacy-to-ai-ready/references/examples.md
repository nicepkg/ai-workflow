# Complete Examples

Real-world examples of AI-ready configurations for common project types.

## Table of Contents
- [Next.js Web Application](#nextjs-web-application)
- [Python FastAPI Backend](#python-fastapi-backend)
- [Go Microservice](#go-microservice)
- [React Component Library](#react-component-library)

---

## Next.js Web Application

### Generated CLAUDE.md

```markdown
# MyApp - Next.js E-commerce Platform

## Quick Reference

| Command | Purpose |
|---------|---------|
| `pnpm dev` | Start development server |
| `pnpm build` | Production build |
| `pnpm test` | Run tests |
| `pnpm lint` | Run ESLint |
| `pnpm format` | Format with Prettier |

## Code Style

### Naming
- Components: PascalCase (`ProductCard.tsx`)
- Hooks: camelCase with `use` prefix (`useCart.ts`)
- Utils: camelCase (`formatPrice.ts`)
- API routes: kebab-case (`/api/get-products`)

### Imports
1. React/Next imports
2. Third-party packages
3. Internal modules (`@/`)
4. Relative imports
5. Type imports last

### Components
- Prefer functional components with TypeScript
- Use named exports
- Props interface above component
- Extract complex logic to custom hooks

## Architecture

```
src/
├── app/           # Next.js App Router pages
├── components/    # Reusable UI components
├── hooks/         # Custom React hooks
├── lib/           # Utilities and helpers
├── services/      # API client functions
└── types/         # TypeScript types
```

### Data Flow
- Server Components for data fetching
- Client Components for interactivity
- React Query for client-side data
- Zustand for global client state

## Testing

- Unit tests: Vitest + React Testing Library
- E2E: Playwright
- Test files: `*.test.tsx` next to source

## Git Workflow

- Branch: `feature/[ticket]-description`
- Commits: conventional commits (`feat:`, `fix:`, etc.)
- PR: requires 1 approval + passing CI
```

### Generated .claude/rules/api.md

```yaml
---
paths:
  - "src/app/api/**/*"
---
```

```markdown
# API Route Rules

## Response Format
Always use this structure:
\`\`\`ts
return NextResponse.json({
  success: true,
  data: result,
  error: null
});
\`\`\`

## Error Handling
\`\`\`ts
try {
  // logic
} catch (error) {
  return NextResponse.json(
    { success: false, data: null, error: error.message },
    { status: 500 }
  );
}
\`\`\`

## Validation
Use Zod for all inputs:
\`\`\`ts
const schema = z.object({ ... });
const result = schema.safeParse(body);
if (!result.success) {
  return NextResponse.json({ error: result.error }, { status: 400 });
}
\`\`\`
```

### Generated .claude/commands/commit.md

```markdown
---
description: Create conventional commit
allowed-tools: Bash(git:*)
---

## Context
- Status: !`git status --short`
- Diff: !`git diff --stat`

## Instructions
Create commit following conventional commits:
- feat: new feature
- fix: bug fix
- docs: documentation
- style: formatting
- refactor: code restructure
- test: adding tests
- chore: maintenance

Format: `type(scope): description`
```

### Generated .claude/settings.json

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | { read f; [[ \"$f\" =~ \\.(ts|tsx|js|jsx)$ ]] && npx prettier --write \"$f\" 2>/dev/null; exit 0; }"
          }
        ]
      }
    ]
  }
}
```

---

## Python FastAPI Backend

### Generated CLAUDE.md

```markdown
# UserService - FastAPI Microservice

## Quick Reference

| Command | Purpose |
|---------|---------|
| `uv run uvicorn main:app --reload` | Dev server |
| `uv run pytest` | Run tests |
| `uv run ruff check .` | Lint |
| `uv run ruff format .` | Format |
| `uv run mypy .` | Type check |

## Code Style

### Naming
- Modules: snake_case (`user_service.py`)
- Classes: PascalCase (`UserRepository`)
- Functions: snake_case (`get_user_by_id`)
- Constants: UPPER_SNAKE (`MAX_RETRIES`)

### Type Hints
- Required for all public functions
- Use `Optional[T]` explicitly
- Prefer `list[T]` over `List[T]` (Python 3.9+)

### Docstrings
Google style:
\`\`\`python
def get_user(user_id: int) -> User:
    """Fetch user by ID.

    Args:
        user_id: The unique user identifier.

    Returns:
        User object if found.

    Raises:
        NotFoundError: If user doesn't exist.
    """
\`\`\`

## Architecture

```
src/
├── api/           # FastAPI routers
├── models/        # Pydantic models
├── services/      # Business logic
├── repositories/  # Data access
└── core/          # Config, dependencies
```

### Dependency Injection
Use FastAPI's `Depends()`:
\`\`\`python
@router.get("/users/{user_id}")
async def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    return await service.get(user_id)
\`\`\`

## Database

- ORM: SQLAlchemy 2.0 with async
- Migrations: Alembic
- Always use transactions for writes

## Testing

- Framework: pytest + pytest-asyncio
- Fixtures in `conftest.py`
- Use factories for test data

## Environment

Required variables:
- `DATABASE_URL`
- `REDIS_URL`
- `JWT_SECRET`
```

### Generated .claude/skills/database/SKILL.md

```yaml
---
name: database-patterns
description: SQLAlchemy patterns and migration workflow. Use when writing queries, creating models, or managing migrations.
---
```

```markdown
# Database Patterns

## Model Definition
\`\`\`python
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
\`\`\`

## Async Queries
\`\`\`python
async with async_session() as session:
    result = await session.execute(
        select(User).where(User.email == email)
    )
    user = result.scalar_one_or_none()
\`\`\`

## Migrations

Create: `alembic revision --autogenerate -m "description"`
Apply: `alembic upgrade head`
Rollback: `alembic downgrade -1`
```

---

## Go Microservice

### Generated CLAUDE.md

```markdown
# OrderService - Go gRPC Service

## Quick Reference

| Command | Purpose |
|---------|---------|
| `make run` | Run service |
| `make test` | Run tests |
| `make lint` | Run golangci-lint |
| `make proto` | Generate protobuf |
| `make build` | Build binary |

## Code Style

### Naming
- Packages: lowercase, single word (`user`, `order`)
- Interfaces: `-er` suffix when possible (`Reader`, `UserStore`)
- Exported: PascalCase
- Unexported: camelCase

### Error Handling
Always wrap errors with context:
\`\`\`go
if err != nil {
    return fmt.Errorf("failed to get user %d: %w", userID, err)
}
\`\`\`

### Interfaces
Define at point of use, not implementation:
\`\`\`go
// In the consumer package
type UserGetter interface {
    GetUser(ctx context.Context, id int64) (*User, error)
}
\`\`\`

## Architecture

```
cmd/
├── server/        # Main entry point
internal/
├── api/           # gRPC handlers
├── domain/        # Business entities
├── service/       # Business logic
├── repository/    # Data access
└── pkg/           # Shared utilities
```

### Context Propagation
Always pass context as first argument:
\`\`\`go
func (s *Service) Process(ctx context.Context, req *Request) error
\`\`\`

## Testing

- Table-driven tests
- Use testify for assertions
- Mock interfaces with mockgen
```

---

## React Component Library

### Generated CLAUDE.md

```markdown
# UIKit - React Component Library

## Quick Reference

| Command | Purpose |
|---------|---------|
| `pnpm dev` | Storybook dev |
| `pnpm test` | Run tests |
| `pnpm build` | Build library |
| `pnpm lint` | ESLint + Stylelint |

## Code Style

### Component Structure
\`\`\`tsx
// Button.tsx
export interface ButtonProps {
  variant?: 'primary' | 'secondary';
  size?: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = 'primary', size = 'md', children, ...props }, ref) => {
    return (
      <button ref={ref} className={styles[variant]} {...props}>
        {children}
      </button>
    );
  }
);

Button.displayName = 'Button';
\`\`\`

### File Organization
```
src/components/Button/
├── Button.tsx         # Component
├── Button.test.tsx    # Tests
├── Button.stories.tsx # Storybook
├── Button.module.css  # Styles
└── index.ts           # Export
```

### Exports
- Named exports only
- Re-export from index.ts
- Types exported separately

## Styling

- CSS Modules for component styles
- Design tokens in CSS variables
- No inline styles

## Testing

- React Testing Library
- Test behavior, not implementation
- Test accessibility with jest-axe

## Documentation

Every component needs:
1. TypeScript types (self-documenting)
2. Storybook stories (visual docs)
3. JSDoc for complex props
```

### Generated .claude/agents/accessibility-reviewer.md

```markdown
---
name: accessibility-reviewer
description: Review components for accessibility compliance. Use after creating or modifying UI components.
tools: Read, Grep, Glob
model: sonnet
---

You are an accessibility expert reviewing React components.

## Review Checklist
- Semantic HTML elements
- ARIA attributes when needed
- Keyboard navigation support
- Focus management
- Color contrast
- Screen reader compatibility

## Output Format
### Issues Found
- [Issue with severity and fix]

### Recommendations
- [Improvement suggestion]
```
