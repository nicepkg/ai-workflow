# Content Creator Workflow

自媒体博主、内容创作者专用的Claude Code工作流。

## 适合人群

- 自媒体博主
- 内容创作者 / 作家
- 播客主播
- 个人品牌运营者

## 已安装Skills (15个)

### 热点追踪与选题
| Skill | 功能 | 触发示例 |
|-------|------|---------|
| content-trend-researcher | 跨10+平台热点追踪 | "找一下AI领域的热门话题" |
| twitter-reader | 通过Jina API获取Twitter内容 | "获取这条推文的内容" |
| youtube-transcript | 提取YouTube视频字幕 | "下载这个视频的字幕" |
| article-extractor | 从URL提取干净的文章内容 | "提取这篇博客文章" |

### 写作与内容创作
| Skill | 功能 | 触发示例 |
|-------|------|---------|
| blog-post-writer | 将笔记转化为博客文章 | "根据我的笔记写一篇博客" |
| content-research-writer | 研究+写作助手（带引用） | "帮我写一篇关于[主题]的文章" |
| content-brief | SEO内容规划简报 | "为[主题]创建内容规划" |
| fact-checker | 事实核查并提供来源 | "核查这篇文档的事实" |

### 视觉与设计
| Skill | 功能 | 触发示例 |
|-------|------|---------|
| nano-banana | AI图片生成 (Gemini) | "生成一张博客封面图" |
| canvas-design | AI视觉设计，PNG/PDF导出 | "设计一张封面图" |

### 分发与导出
| Skill | 功能 | 触发示例 |
|-------|------|---------|
| social-repurposer | 跨平台内容转换 | "转换为Twitter thread" |
| content-repurposer | 多格式内容改写 | "改写为Newsletter" |
| podcast-content-suite | 播客内容创作 | "生成播客大纲" |
| docx | Word文档创建和编辑 | "导出为Word文档" |
| pdf | PDF处理和生成 | "生成PDF" |

## 快速开始

```bash
cd content-creator-workflow
# 启动Claude Code，skills自动激活
```

## 自动化内容工作流

### 1. 热点追踪与选题
```
"找一下今天[科技/金融/生活]领域最火的话题"
"Twitter上关于AI的热门讨论是什么？"
"分析[主题]在各平台的内容趋势"
```

### 2. 素材搜集
```
"提取这篇文章：[URL]"
"下载这个YouTube视频的字幕：[URL]"
"研究[主题]并整理资料来源"
```

### 3. 内容创作
```
"为[主题]创建内容规划，目标受众是[人群]"
"根据我的研究笔记写一篇博客"
"为这篇文章生成5个爆款标题"
```

### 4. 视觉素材
```
"为[主题]生成一张博客封面图"
"设计一个YouTube缩略图"
```

### 5. 多平台分发
```
"把这篇文章转换为Twitter thread"
"改写为LinkedIn版本（专业语调）"
"生成Instagram轮播文案"
```

### 6. 导出与发布
```
"导出为Word文档"
"生成PDF版本"
```

## 发布集成

如需自动发布到各平台，可配置MCP服务器：

| 平台 | MCP服务器 |
|------|----------|
| Medium | mcp-medium (需API token) |
| WordPress | mcp-wordpress (需站点URL+凭证) |
| Notion | mcp-notion (需集成token) |
| GitHub Pages | gh CLI (已支持) |
| 微信公众号 | 需手动发布或第三方工具 |

## 多AI工具支持

本workflow支持：
- Claude Code (`.claude/skills/`)
- Codex (`.codex/skills/`)
- Cursor (`.cursor/skills/`)
- OpenCode (`.opencode/skill/`)

## License

MIT
