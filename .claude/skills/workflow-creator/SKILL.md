---
name: workflow-creator
description: Create complete Claude Code workflow directories with curated skills. Use when user wants to (1) create a new workflow for specific use case (media creator, developer, marketer, etc.), (2) set up a Claude Code project with pre-configured skills, (3) download and organize skills from GitHub repositories, or (4) generate README.md and AGENTS.md documentation for workflows. Triggers on phrases like "create workflow", "new workflow", "set up workflow", "build a xxx-workflow".
---

# Workflow Creator

Create complete workflow directories with curated skills downloaded from GitHub.

## Workflow Creation Process

### Step 1: Create directory structure

Run `scripts/create_workflow.py` to initialize:

```bash
python scripts/create_workflow.py <workflow-name> --path <output-dir>
```

Creates (with multi-AI tool support):
```
<workflow-name>-workflow/
├── README.md          # User documentation
├── AGENTS.md          # AI context (auto-loaded)
├── .claude/
│   ├── settings.json
│   └── skills/        # Skills go here (primary storage)
├── .codex/
│   └── skills -> ../.claude/skills
├── .cursor/
│   └── skills -> ../.claude/skills
├── .opencode/
│   └── skill -> ../.claude/skills
├── .agents/
│   └── skills -> ../.claude/skills
├── .kilocode/
│   └── skills -> ../.claude/skills
├── .roo/
│   └── skills -> ../.claude/skills
├── .goose/
│   └── skills -> ../.claude/skills
├── .gemini/
│   └── skills -> ../.claude/skills
├── .agent/
│   └── skills -> ../.claude/skills
├── .github/
│   └── skills -> ../.claude/skills
├── skills -> .claude/skills
├── .factory/
│   └── skills -> ../.claude/skills
└── .windsurf/
    └── skills -> ../.claude/skills
```

Symlinks enable all AI tools to use the same skills from .claude/skills/.

### Step 2: Select and download skills

1. Read `references/skill-sources.md` to find relevant skills for the workflow type
2. Download each skill using `scripts/download_skill.py`:

```bash
python scripts/download_skill.py <repo-url> <skill-path> --output <workflow>/.claude/skills/
```

**Examples:**

```bash
# Official Anthropic skills
python scripts/download_skill.py https://github.com/anthropics/skills skills/docx --output ./media-workflow/.claude/skills/

# Community skills (root level)
python scripts/download_skill.py https://github.com/gked2121/claude-skills social-repurposer --output ./media-workflow/.claude/skills/
```

### Step 3: Generate README.md

Write user documentation covering:
- Workflow purpose and target users
- Installed skills table with descriptions
- Quick start guide
- Usage examples
- FAQ

Use `assets/templates/README.template.md` as reference.

### Step 4: Generate AGENTS.md

Write AI instructions covering:
- Workflow overview
- Available skills list with trigger conditions
- Recommended workflow steps
- Skill usage guidelines and combinations
- Output standards

Use `assets/templates/AGENTS.template.md` as reference.

**Important:** AGENTS.md is auto-loaded by Claude Code. Keep it concise (<500 lines) and focused on actionable instructions.

## Workflow Type Recommendations

### Media Creator / Content Creator
Skills: content-research-writer, social-repurposer, canvas-design, web-asset-generator, twitter-reader, youtube-transcript, article-extractor, docx, pdf, pptx

### Marketing Professional
Skills: seo-optimizer, linkedin-post-optimizer, social-repurposer, landing-page-copywriter, email-template-generator, content-research-writer, web-asset-generator

### Developer
Skills: code-review-pro, api-documentation-writer, technical-writer, database-schema-designer, screenshot-to-code, regex-debugger, mermaid-tools, frontend-design

### Researcher
Skills: content-research-writer, fact-checker, article-extractor, youtube-transcript, pdf, docx

See `references/skill-sources.md` for complete skill catalog and repository URLs.

## Dynamic Skill Search

When curated list lacks needed skills:

1. Search GitHub: `"claude" "skills" "SKILL.md" <topic>`
2. Validate: Check SKILL.md has valid YAML frontmatter with name/description
3. Download using download_skill.py

### Step 5: Update project README

After creating a workflow in the ai-workflow project, update the project's root README.md:
- Add new workflow to the workflow list/table
- Include workflow name, target users, and brief description
- Update any workflow counts

## Output Checklist

After workflow creation, verify:
- [ ] `.claude/skills/` contains downloaded skill folders
- [ ] Each skill folder has `SKILL.md`
- [ ] All symlinks work (`.codex/skills`, `.cursor/skills`, `.opencode/skill`, `.agents/skills`, `.kilocode/skills`, `.roo/skills`, `.goose/skills`, `.gemini/skills`, `.agent/skills`, `.github/skills`, `skills`, `.factory/skills`, `.windsurf/skills`)
- [ ] `README.md` documents all skills with usage examples
- [ ] `AGENTS.md` provides clear AI instructions (<500 lines)
- [ ] `settings.json` exists in `.claude/`
- [ ] Project README.md updated with new workflow
