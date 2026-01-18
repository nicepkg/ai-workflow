# AI Workflow Collection - AI Instructions

This is the master repository for curated Claude Code workflow collections.

## Language Guidelines

**IMPORTANT**: All `AGENTS.md` files in this project MUST be written in English only. This ensures consistent AI behavior across different language contexts.

- `AGENTS.md` - English only (AI instructions)
- `README.md` - English (primary)
- `README_cn.md` - Chinese translation (optional)

## Project Structure

```
ai-workflow/
├── AGENTS.md              # This file (AI context)
├── README.md              # User documentation (update after creating workflows)
├── .claude/skills/        # Shared skills for this project
│   ├── workflow-creator/  # Create new workflows
│   └── skill-creator/     # Create new skills
├── workflows/
│   ├── content-creator-workflow/   # Example workflow
│   ├── marketing-pro-workflow/     # Example workflow
│   └── <new-workflow>/             # New workflows created here
```

## Available Skills

### workflow-creator
**Trigger**: "create workflow", "new workflow", "set up workflow", "build a xxx-workflow"

Creates complete workflow directories with:
- Multi-AI tool support (.claude, .codex, .cursor, .opencode, .agents, .kilocode, .roo, .goose, .gemini, .agent, .github, skills, .factory, .windsurf)
- Curated skills downloaded from GitHub
- README.md (user documentation)
- AGENTS.md (AI instructions)

### skill-creator
**Trigger**: "create skill", "new skill", "build a skill"

Creates new skills following Anthropic's specification.

## Workflow Creation Process

When user requests a new workflow:

1. **Create directory** using `workflow-creator/scripts/create_workflow.py` (default target: `workflows/`)
2. **Select skills** from `workflow-creator/references/skill-sources.md`
3. **Download skills** using `workflow-creator/scripts/download_skill.py`
4. **Generate README.md** for users
5. **Generate AGENTS.md** for AI
6. **Update project README.md** - Add new workflow to the list

## Post-Creation Tasks

After creating any workflow, ALWAYS update the project README.md:

1. Add new workflow to the workflow list table
2. Update workflow count
3. Add brief description

## Output Standards

### Workflow Directory Structure
```
workflows/<workflow name>/
├── README.md              # User documentation
├── AGENTS.md              # AI instructions (concise, <500 lines)
├── .claude/
│   ├── settings.json
│   └── skills/            # Downloaded skills (primary storage)
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

### README.md Content
- Workflow purpose and target users
- Installed skills table
- Quick start guide
- Usage examples

### AGENTS.md Content
- Workflow overview
- Available skills with triggers
- Recommended workflow steps
- Skill usage guidelines

## Skill Sources Priority

1. **Anthropic Official**: `github.com/anthropics/skills`
2. **Curated Community**: Listed in `skill-sources.md`
3. **Dynamic Search**: GitHub search as fallback

## Quality Checklist

Before completing workflow creation:
- [ ] All skills have valid SKILL.md
- [ ] Symlinks work for all AI tools
- [ ] README.md is complete
- [ ] AGENTS.md is concise and actionable
- [ ] Project README.md updated with new workflow
