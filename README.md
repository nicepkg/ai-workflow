# AI Workflow Collection

Ready-to-use Claude Code workflow collections with multi-AI tool support.

[中文文档](./README_cn.md)

## Workflows

| Workflow | Target Users | Skills |
|----------|-------------|--------|
| [content-creator-workflow](./content-creator-workflow/) | Bloggers, Content Creators | 15 |
| [marketing-pro-workflow](./marketing-pro-workflow/) | Digital Marketers, Growth Marketers, PMMs | 18 |
| [video-creator-workflow](./video-creator-workflow/) | YouTubers, TikTokers, Video Creators | 15 |
| [stock-trader-workflow](./stock-trader-workflow/) | Stock Traders, Investors (US/A-share/HK) | 25 |

## Installation

Install skills using [add-skill](https://github.com/nicepkg/add-skill) CLI tool.

### Install All Skills from a Workflow

```bash
# Install all skills from content-creator-workflow (interactive)
npx add-skill nicepkg/ai-workflow/content-creator-workflow

# Install all skills from marketing-pro-workflow
npx add-skill nicepkg/ai-workflow/marketing-pro-workflow

# Install all skills from video-creator-workflow
npx add-skill nicepkg/ai-workflow/video-creator-workflow

# Install all skills from stock-trader-workflow
npx add-skill nicepkg/ai-workflow/stock-trader-workflow
```

### Install a Single Skill

```bash
# Install specific skill by name
npx add-skill nicepkg/ai-workflow/content-creator-workflow --skill seo-optimizer

# Install to specific agent only
npx add-skill nicepkg/ai-workflow/stock-trader-workflow --skill a-share-analysis -a claude-code
```

### Installation Options

```bash
# List available skills without installing
npx add-skill nicepkg/ai-workflow/content-creator-workflow --list

# Install to global scope (user home directory)
npx add-skill nicepkg/ai-workflow/marketing-pro-workflow --global

# Non-interactive mode (CI/CD friendly)
npx add-skill nicepkg/ai-workflow/video-creator-workflow -y

# Install to multiple specific agents
npx add-skill nicepkg/ai-workflow/stock-trader-workflow -a claude-code -a cursor -a opencode
```

### Supported Agents

| Agent | Project Path | Global Path |
|-------|--------------|-------------|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |
| Codex | `.codex/skills/` | `~/.codex/skills/` |
| OpenCode | `.opencode/skill/` | `~/.config/opencode/skill/` |
| GitHub Copilot | `.github/skills/` | `~/.copilot/skills/` |
| Amp | `.agents/skills/` | `~/.config/agents/skills/` |
| Roo Code | `.roo/skills/` | `~/.roo/skills/` |
| Kilo Code | `.kilocode/skills/` | `~/.kilocode/skills/` |

## Alternative: Clone and Use Directly

```bash
# 1. Clone the repository
git clone https://github.com/nicepkg/ai-workflow.git

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
├── video-creator-workflow/   # Video creators
├── stock-trader-workflow/    # Stock traders
└── <your-workflow>/          # Your new workflows
```

## Skill Sources

- [Anthropic Official](https://github.com/anthropics/skills)
- [gked2121/claude-skills](https://github.com/gked2121/claude-skills)
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [kkoppenhaver/cc-nano-banana](https://github.com/kkoppenhaver/cc-nano-banana)
- [MadAppGang/claude-code](https://github.com/MadAppGang/claude-code) - SEO/content skills
- [nicknisi/dotfiles](https://github.com/nicknisi/dotfiles) - Blog writing skills
- [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills) - Twitter, fact-checker
- [alirezarezvani/claude-code-skill-factory](https://github.com/alirezarezvani/claude-code-skill-factory) - Trend research
- [michalparkola/tapestry-skills](https://github.com/michalparkola/tapestry-skills-for-claude-code) - YouTube, article extraction
- [skillhub.club](https://www.skillhub.club) - 1000+ skills collection
- [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) - Stock trading skills

## License

MIT
