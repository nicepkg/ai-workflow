# AI Workflow Collection

Ready-to-use Claude Code workflow collections with multi-AI tool support.

[中文文档](./README_cn.md)

## Workflows

| Workflow | Target Users | Skills |
|----------|-------------|--------|
| [content-creator-workflow](./content-creator-workflow/) | Bloggers, Content Creators | 9 |
| [marketing-pro-workflow](./marketing-pro-workflow/) | Digital Marketers, Social Media Managers | 10 |

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/xxx/ai-workflow.git

# 2. Navigate to desired workflow
cd ai-workflow/content-creator-workflow

# 3. Launch Claude Code - skills activate automatically
```

## Create New Workflow

Launch Claude Code in the project root and say:

```
"Create a developer workflow"
"Create a researcher workflow"
```

## Multi-AI Tool Support

Each workflow supports:

| Tool | Path |
|------|------|
| Claude Code | `.claude/skills/` |
| Codex | `.codex/skills/` |
| Cursor | `.cursor/skills/` |
| OpenCode | `.opencode/skill/` |

## Project Structure

```
ai-workflow/
├── .claude/skills/           # Project-level skills (workflow-creator, etc.)
├── content-creator-workflow/ # Content creators
├── marketing-pro-workflow/   # Marketing professionals
└── <your-workflow>/          # Your new workflows
```

## Skill Sources

- [Anthropic Official](https://github.com/anthropics/skills)
- [gked2121/claude-skills](https://github.com/gked2121/claude-skills)
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [kkoppenhaver/cc-nano-banana](https://github.com/kkoppenhaver/cc-nano-banana)
- [MadAppGang/claude-code](https://github.com/MadAppGang/claude-code) - SEO/content skills
- [nicknisi/dotfiles](https://github.com/nicknisi/dotfiles) - Blog writing skills
- [skillhub.club](https://www.skillhub.club) - 1000+ skills collection

## License

MIT
