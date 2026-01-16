# Content Creator Workflow

自媒体博主、内容创作者专用的Claude Code工作流。

## 适合人群

- 自媒体博主
- 内容创作者 / 作家
- 播客主播
- 个人品牌运营者

## 已安装Skills

| Skill | 功能 | 触发示例 |
|-------|------|---------|
| nano-banana | AI图片生成 (Gemini) | "生成一张博客封面图" |
| canvas-design | AI视觉设计，生成PNG/PDF | "设计一张封面图" |
| blog-post-writer | 将笔记转化为博客文章 | "根据我的笔记写一篇博客" |
| content-brief | SEO内容规划简报 | "为[主题]创建内容规划" |
| docx | Word文档创建和编辑 | "导出为Word文档" |
| pdf | PDF处理和生成 | "生成PDF" |
| social-repurposer | 跨平台内容转换 | "转换为Twitter thread" |
| content-repurposer | 多格式内容改写 | "改写为Newsletter" |
| podcast-content-suite | 播客内容创作 | "生成播客大纲" |

## 快速开始

```bash
# 克隆并进入目录
cd content-creator-workflow

# 启动Claude Code，skills自动激活
```

## 使用示例

### 内容创作流程

```
1. "帮我研究一下 [话题] 的最新趋势"
2. "为 [话题] 创建内容规划简报"
3. "根据我的研究笔记写一篇博客文章"
4. "用 nano-banana 生成一张博客封面图"
5. "用 social-repurposer 转换为 Twitter thread 和 LinkedIn post"
6. "导出为 Word 文档"
```

### 播客创作

```
"用 podcast-content-suite 为这个话题生成播客大纲和问答脚本"
```

## 多AI工具支持

本workflow支持：
- Claude Code (`.claude/skills/`)
- Codex (`.codex/skills/`)
- Cursor (`.cursor/skills/`)
- OpenCode (`.opencode/skill/`)

## License

MIT
