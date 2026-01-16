# AI Workflow Collection

开箱即用的Claude Code工作流集合，支持多种AI工具。

## Workflows

| Workflow | 适合人群 | Skills数量 |
|----------|---------|-----------|
| [content-creator-workflow](./content-creator-workflow/) | 自媒体博主、内容创作者 | 15 |
| [marketing-pro-workflow](./marketing-pro-workflow/) | 数字营销、增长营销、PMM | 18 |
| [video-creator-workflow](./video-creator-workflow/) | YouTuber、TikToker、视频创作者 | 15 |
| [stock-trader-workflow](./stock-trader-workflow/) | 股票交易者、投资者（美股/A股/港股） | 25 |

## 安装

使用 [add-skill](https://github.com/nicepkg/add-skill) CLI工具安装skills。

### 一键安装整个Workflow的所有Skills

```bash
# 安装 content-creator-workflow 的所有skills（交互式）
npx add-skill nicepkg/ai-workflow/content-creator-workflow

# 安装 marketing-pro-workflow 的所有skills
npx add-skill nicepkg/ai-workflow/marketing-pro-workflow

# 安装 video-creator-workflow 的所有skills
npx add-skill nicepkg/ai-workflow/video-creator-workflow

# 安装 stock-trader-workflow 的所有skills
npx add-skill nicepkg/ai-workflow/stock-trader-workflow
```

### 安装单个Skill

```bash
# 按名称安装指定skill
npx add-skill nicepkg/ai-workflow/content-creator-workflow --skill seo-optimizer

# 只安装到指定的AI工具
npx add-skill nicepkg/ai-workflow/stock-trader-workflow --skill a-share-analysis -a claude-code
```

### 安装选项

```bash
# 列出可用的skills（不安装）
npx add-skill nicepkg/ai-workflow/content-creator-workflow --list

# 安装到全局目录（用户主目录）
npx add-skill nicepkg/ai-workflow/marketing-pro-workflow --global

# 非交互模式（适合CI/CD）
npx add-skill nicepkg/ai-workflow/video-creator-workflow -y

# 安装到多个指定的AI工具
npx add-skill nicepkg/ai-workflow/stock-trader-workflow -a claude-code -a cursor -a opencode
```

### 支持的AI工具

| 工具 | 项目级路径 | 全局路径 |
|-----|-----------|---------|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |
| Codex | `.codex/skills/` | `~/.codex/skills/` |
| OpenCode | `.opencode/skill/` | `~/.config/opencode/skill/` |
| GitHub Copilot | `.github/skills/` | `~/.copilot/skills/` |
| Amp | `.agents/skills/` | `~/.config/agents/skills/` |
| Roo Code | `.roo/skills/` | `~/.roo/skills/` |
| Kilo Code | `.kilocode/skills/` | `~/.kilocode/skills/` |

## 备选：克隆仓库直接使用

```bash
# 1. 克隆仓库
git clone https://github.com/nicepkg/ai-workflow.git

# 2. 进入想要的workflow
cd ai-workflow/content-creator-workflow

# 3. 启动Claude Code，skills自动激活
```

## 创建新Workflow

在本项目根目录启动Claude Code，直接说：

```
"创建一个开发者工作流"
"Create a researcher workflow"
```

## 多AI工具支持

每个workflow都支持：

| 工具 | 路径 |
|-----|------|
| Claude Code | `.claude/skills/` |
| Codex | `.codex/skills/` |
| Cursor | `.cursor/skills/` |
| OpenCode | `.opencode/skill/` |

## 项目结构

```
ai-workflow/
├── .claude/skills/           # 项目级skills（workflow-creator等）
├── content-creator-workflow/ # 内容创作者
├── marketing-pro-workflow/   # 营销专业人员
├── video-creator-workflow/   # 视频创作者
├── stock-trader-workflow/    # 股票交易者
└── <your-workflow>/          # 你的新workflow
```

## Skills来源

- [Anthropic官方](https://github.com/anthropics/skills)
- [gked2121/claude-skills](https://github.com/gked2121/claude-skills)
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- [kkoppenhaver/cc-nano-banana](https://github.com/kkoppenhaver/cc-nano-banana)
- [MadAppGang/claude-code](https://github.com/MadAppGang/claude-code) - SEO/内容skills
- [nicknisi/dotfiles](https://github.com/nicknisi/dotfiles) - 博客写作skills
- [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills) - Twitter、事实核查
- [alirezarezvani/claude-code-skill-factory](https://github.com/alirezarezvani/claude-code-skill-factory) - 趋势研究
- [michalparkola/tapestry-skills](https://github.com/michalparkola/tapestry-skills-for-claude-code) - YouTube、文章提取
- [skillhub.club](https://www.skillhub.club) - 1000+ skills集合
- [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) - 股票交易skills

## License

MIT
