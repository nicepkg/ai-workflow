# 参考资料与引用

## 官方资源

- **Claude Code 官方文档**: https://docs.anthropic.com/claude-code
- **官方 Skills 仓库**: https://github.com/anthropics/skills
- **Claude Code CLI**: https://claude.com/claude-code

## 社区 Skills 仓库

- **Vercel Labs**: https://github.com/vercel-labs/agent-skills
- **Microck 社区**: https://github.com/Microck/ordinary-claude-skills
- **gked2121**: https://github.com/gked2121/claude-skills

## 案例 Skills 引用

### ppt-creator
- 来源: `anthropics/skills` 官方仓库
- 路径: `official-anthropic-skills/ppt-creator`
- 特点: 金字塔原则、自我评估、安全默认值

### mermaid-diagrams
- 来源: `Microck/ordinary-claude-skills` 社区仓库
- 路径: `mermaid-diagrams`
- 特点: 单文件设计、10种图表类型速查

## 演讲中提到的概念

### 金字塔原则 (Pyramid Principle)
- 作者: Barbara Minto
- 核心: 结论先行，以上统下，归类分组，逻辑递进
- 应用: 演示文稿结构、商业写作、技术文档

### Conventional Commits
- 规范: https://www.conventionalcommits.org/
- 格式: `type(scope): subject`
- 类型: feat, fix, docs, style, refactor, test, chore

### Mermaid
- 官方文档: https://mermaid.js.org/
- 在线编辑器: https://mermaid.live/
- 支持图表: flowchart, sequence, class, ER, Gantt, state, pie, git, journey, mindmap

## 演讲素材来源

本演讲内容基于以下实际 Skills 项目结构分析：

```
.claude/
└── skills/
    ├── ppt-creator/          # 复杂 Skill 示例
    ├── mermaid-diagrams/     # 简洁 Skill 示例
    ├── theme-factory/        # 主题管理示例
    ├── pexels-media/         # API 集成示例
    └── youtube-transcript/   # 第三方服务示例
```

## 延伸阅读

1. **AI Agents 设计模式**: 如何设计可靠的 AI 代理系统
2. **Prompt Engineering**: 提示词工程最佳实践
3. **MCP (Model Context Protocol)**: 理解 Claude 的上下文管理

---

*本演讲于 2026 年 1 月创建*
*使用 Claude Code ppt-creator Skill 辅助生成*
