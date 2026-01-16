# Video Creator Workflow

YouTuber、TikToker、视频创作者专用的Claude Code工作流。

## 适合人群

- YouTuber / B站UP主
- 抖音 / TikTok 创作者
- 短视频创作者
- 视频剪辑师 / 制作人
- 直播主播

## 已安装Skills (15个)

### 选题与研究
| Skill | 功能 | 触发示例 |
|-------|------|---------|
| content-trend-researcher | 跨10+平台热点追踪 | "找一下游戏领域的热门话题" |
| youtube-transcript | 提取视频字幕用于研究 | "获取这个YouTube视频的字幕" |
| video-downloader | 下载视频作为参考素材 | "下载这个YouTube视频" |

### 脚本与钩子
| Skill | 功能 | 触发示例 |
|-------|------|---------|
| video-script-writer | 撰写完整视频脚本含结构 | "写一个10分钟教程脚本" |
| video-hook-generator | 生成病毒式开场钩子（前3秒） | "为[主题]视频创建5个钩子" |

### 标题与封面
| Skill | 功能 | 触发示例 |
|-------|------|---------|
| video-title-optimizer | 优化标题以提高点击率和SEO | "为[主题]生成标题选项" |
| thumbnail-concept-generator | 创建缩略图概念和设计简报 | "设计[视频]的缩略图概念" |
| canvas-design | AI视觉设计生成缩略图 | "设计一个YouTube缩略图" |

### SEO与分发
| Skill | 功能 | 触发示例 |
|-------|------|---------|
| youtube-seo-optimizer | 优化描述、标签、章节 | "为我的视频创建YouTube SEO" |
| short-form-converter | 长视频转短视频/TikTok | "从这个视频创建3个短片" |
| social-repurposer | 跨平台内容适配 | "转换为TikTok格式" |
| srt-translator | 翻译字幕拓展全球受众 | "把这个SRT翻译成西班牙语" |

### 数据与变现
| Skill | 功能 | 触发示例 |
|-------|------|---------|
| video-analytics-interpreter | 解读YouTube/TikTok数据 | "分析这个视频为什么表现不好" |
| sponsor-pitch-generator | 创建赞助商提案和媒体包 | "为我的频道创建媒体包" |
| video-comparer | 视频质量对比（制作用） | "对比这两个视频文件" |

## 快速开始

```bash
cd video-creator-workflow
# 启动Claude Code，skills自动激活
```

## 自动化视频工作流

### 1. 完整视频生产流水线
```
1. "找一下[领域]的热门话题"
2. "写一个关于[话题]的视频脚本"
3. "创建5个开场钩子变体"
4. "生成视频标题选项"
5. "创建YouTube SEO（描述、标签、章节）"
6. "设计缩略图概念"
```

### 2. 病毒式短视频内容
```
1. "分析这个长视频的爆款片段"
2. "转换成5个短视频片段"
3. "为每个片段创建钩子"
4. "优化TikTok/Shorts标题"
```

### 3. 国际化拓展
```
1. "获取我视频的字幕"
2. "翻译字幕到西班牙语、葡萄牙语、日语"
3. "为每个市场适配标题"
4. "创建本地化描述"
```

### 4. 频道增长分析
```
1. "分析我最近10个视频的表现"
2. "找出表现最好视频的规律"
3. "诊断最近视频表现不佳的原因"
4. "建议内容策略改进"
```

### 5. 商务合作外联
```
1. "为我的频道创建媒体包"
2. "写一份给[品牌]的赞助提案"
3. "生成合作创意"
```

### 6. 竞品研究
```
1. "下载竞品视频的字幕"
2. "分析他们的内容结构"
3. "找出我能填补的空白"
4. "生成差异化内容创意"
```

## Skill组合

- **爆款视频**: content-trend-researcher → video-script-writer → video-hook-generator → video-title-optimizer → youtube-seo-optimizer
- **短视频工厂**: youtube-transcript → short-form-converter → video-hook-generator → social-repurposer
- **全球化**: youtube-transcript → srt-translator → video-title-optimizer（每种语言）
- **频道优化**: video-analytics-interpreter → content-trend-researcher → video-script-writer
- **变现**: video-analytics-interpreter → sponsor-pitch-generator

## 输出标准

- **脚本**: 完整时间戳、B-roll建议、文字叠加
- **钩子**: 多变体、文字叠加、3秒优化
- **标题**: CTR优化、含关键词、字符数验证
- **缩略图**: 构图、配色、文字、表情的视觉简报
- **SEO**: 完整描述、8-12标签、章节、话题标签
- **翻译**: 保留时间轴、文化适配、平台就绪

## 平台支持

| 平台 | 可用优化 |
|------|---------|
| YouTube长视频 | 脚本、SEO、缩略图、数据分析 |
| YouTube Shorts | 钩子、标题、竖屏转换 |
| TikTok/抖音 | 钩子、热门音乐、字幕 |
| Instagram Reels | 视觉优化、话题标签 |
| B站 | 中文本地化、热点研究 |

## 多AI工具支持

本workflow支持：
- Claude Code (`.claude/skills/`)
- Codex (`.codex/skills/`)
- Cursor (`.cursor/skills/`)
- OpenCode (`.opencode/skill/`)

## 前置要求

部分skill需要外部工具：
- `yt-dlp` - youtube-transcript、video-downloader需要
- `ffmpeg` - video-comparer需要

## License

MIT
