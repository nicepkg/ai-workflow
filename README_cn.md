# AI Workflow Collection

开箱即用的Claude Code工作流集合，支持多种AI工具。

## Workflows

| Workflow | 适合人群 | Skills数量 |
|----------|---------|-----------|
| [content-creator-workflow](./content-creator-workflow/) | 自媒体博主、内容创作者 | 15 |
| [marketing-pro-workflow](./marketing-pro-workflow/) | 数字营销、增长营销、PMM | 18 |
| [video-creator-workflow](./video-creator-workflow/) | YouTuber、TikToker、视频创作者 | 15 |

## 快速使用

```bash
# 1. 克隆仓库
git clone https://github.com/xxx/ai-workflow.git

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

## License

MIT
