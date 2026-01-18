<div align="center">

# ✍️ 内容创作者工作流

### **让你的 AI 变身专业内容策略师**

[← 返回 AI Workflow](../README_cn.md)

简体中文 | [English](./README.md)

</div>

---

## 🎯 适合谁？

- **博主 & 作家** - 规模化内容产出
- **SEO 专家** - 优化搜索排名
- **内容营销** - 建立品牌影响力
- **个人品牌运营者** - 扩大受众

---

## ⚡ 快速安装

```bash
# 一键安装全部 32 个技能
npx add-skill nicepkg/ai-workflow/content-creator-workflow

# 或安装单个技能
npx add-skill nicepkg/ai-workflow/content-creator-workflow --skill blog-post-writer
```

---

## 📦 包含技能 (32个)

### 1️⃣ 趋势发现与选题研究
| 技能 | 功能描述 |
|:-----|:---------|
| `weak-signal-synthesizer` | 跨平台弱信号检测，预测 3-6 个月趋势 |
| `content-trend-researcher` | 跨 10+ 平台热点追踪 |
| `competitive-ads-extractor` | 提取分析竞品广告创意和文案 |
| `twitter-reader` | 通过 Jina API 获取 Twitter 内容 |

### 2️⃣ 研究与内容摄取
| 技能 | 功能描述 |
|:-----|:---------|
| `article-extractor` | 从 URL 提取干净的文章内容 |
| `youtube-processor` | YouTube 视频转文字稿和 Markdown 笔记 |
| `youtube-transcript` | 提取 YouTube 视频字幕 |
| `content-research` | 结构化研究：论点、证据、反对观点 |

### 3️⃣ 内容规划与简报
| 技能 | 功能描述 |
|:-----|:---------|
| `content-brief-generator` | 生成完整内容简报：受众、角度、证据 |
| `content-brief` | SEO 内容规划简报 |
| `skill-navigator` | 推荐应该使用哪些技能 |

### 4️⃣ 写作与内容创作
| 技能 | 功能描述 |
|:-----|:---------|
| `blog-post-writer` | 将笔记转化为博客文章 |
| `content-research-writer` | 研究+写作助手（带引用） |
| `newsletter-coach` | 把经历转化为 Newsletter 草稿 |
| `fact-checker` | 事实核查并提供来源 |

### 5️⃣ 爆款优化
| 技能 | 功能描述 |
|:-----|:---------|
| `hook-stack-evaluator` | 标题/开头 hook 评分与优化 |
| `email-subject-line-optimizer` | 邮件标题 A/B 测试与打开率预测 |
| `ai-slop-detector` | 去除 AI 味，确保真实声音 |

### 6️⃣ 多平台分发
| 技能 | 功能描述 |
|:-----|:---------|
| `content-repurposer` | 内容转换为 8+ 格式（PPT、脚本、社媒等） |
| `social-repurposer` | 博客 → Twitter thread，文章 → LinkedIn 帖子 |
| `social-media` | 生成 X/LinkedIn/IG/FB 帖子、线程、日历 |
| `linkedin-announcement-generator` | 专业的 LinkedIn 里程碑公告 |
| `podcast-content-suite` | 播客内容营销套件 |

### 7️⃣ SEO 与发布
| 技能 | 功能描述 |
|:-----|:---------|
| `pre-publish-post-assistant` | 发布前检查清单（结构、CTA、链接、排版） |
| `seo-wordpress-manager` | WordPress SEO 与发布流程 |
| `gsc-assistant` | Google Search Console 收录追踪 |
| `astro-cta-injector` | 自动为 Astro 站点内容注入 CTA |

### 8️⃣ 视觉与文档工具
| 技能 | 功能描述 |
|:-----|:---------|
| `nano-banana` | AI 图片生成 (Gemini) |
| `canvas-design` | AI 视觉设计，PNG/PDF 导出 |
| `docx` | Word 文档创建和编辑 |
| `pdf` | PDF 处理和生成 |

---

## 🔄 完整内容流水线（8 阶段）

```
阶段 1: 趋势发现
  → "找一下 AI/科技领域下个季度的弱信号"
  → "分析竞品内容策略"

阶段 2: 研究
  → "提取这篇文章的要点：[URL]"
  → "总结这个 YouTube 视频：[URL]"

阶段 3: 内容规划
  → "为 [主题] 创建内容简报"
  → "写爆款 thread 应该用哪些技能？"

阶段 4: 写作
  → "根据我的研究笔记写一篇博客"
  → "把我的 [主题] 经历写成 Newsletter 草稿"

阶段 5: 爆款优化
  → "给这 5 个标题打分并优化"
  → "去除这篇草稿的 AI 味"

阶段 6: 分发
  → "把这篇文章转换为 Twitter thread + LinkedIn 帖子"
  → "为这个里程碑创建 LinkedIn 公告"

阶段 7: SEO 与发布
  → "运行发布前检查清单"
  → "检查我的 GSC 收录状态"

阶段 8: 视觉素材
  → "为这篇文章生成封面图"
  → "导出为 Word 文档"
```

---

## 💡 使用示例

### 爆款博客文章流水线
```
1. "找一下 AI 工具领域未来 3 个月的弱信号"
2. "提取这 5 篇竞品文章的要点：[URLs]"
3. "为'AI 编程助手对比'创建内容简报"
4. "根据简报写一篇 2000 字的博客"
5. "给这 5 个标题选项打分，优化最好的那个"
6. "去除草稿中的 AI 味"
7. "运行发布前检查清单"
8. "生成封面图"
9. "转换为 Twitter thread + LinkedIn 帖子"
```

### Newsletter 创作流水线
```
1. "帮我从这周的经历中头脑风暴 newsletter 话题"
2. "把我使用 [工具] 的经历写成 newsletter 草稿"
3. "优化邮件标题以提高打开率"
4. "去除 AI 味，让它听起来更个人化"
5. "创建 3 个 A/B 测试标题变体"
```

### 研究转内容流水线
```
1. "提取这篇文章：https://example.com/article"
2. "总结这个 YouTube 视频：https://youtube.com/watch?v=xxx"
3. "对 [主题] 做结构化研究，包含论点和反对观点"
4. "写一篇带正确引用的研究型文章"
5. "核查文章中所有声明的事实"
```

### SEO 内容机器
```
1. "为关键词 '[关键词]' 创建 SEO 内容简报"
2. "写一篇针对目标关键词优化的博客"
3. "运行发布前 SEO 检查清单"
4. "发布到 WordPress 并设置正确的 meta 标签"
5. "在 Google Search Console 追踪收录状态"
```

### 多平台分发
```
1. "把这篇博客转换为 8 种不同格式"
2. "创建 Twitter thread 版本（10-12 条推文）"
3. "写一个 LinkedIn 帖子版本"
4. "生成 Instagram 轮播内容"
5. "从文章创建播客脚本"
6. "起草邮件 newsletter 版本"
```

### 内容更新工作流
```
1. "分析 [主题] 的竞品内容"
2. "找出我现有文章的内容空白"
3. "用新信息更新文章"
4. "重新优化标题以提高点击率"
5. "重新发布并追踪 GSC 收录"
```

---

## 🔧 前置要求

```bash
# 部分技能需要
brew install yt-dlp

# 可选：本地 AI 图片生成
# nano-banana 需要 GEMINI_API_KEY
```

| 技能 | 需要 |
|------|------|
| `twitter-reader` | `JINA_API_KEY` |
| `nano-banana` | `GEMINI_API_KEY` |
| `youtube-processor` | `yt-dlp` 已安装 |
| `youtube-transcript` | `yt-dlp` 已安装 |
| `gsc-assistant` | Google Search Console 访问权限 |
| `seo-wordpress-manager` | WordPress 站点访问权限 |

---

## 🔗 发布集成

| 平台 | 集成方式 |
|:-----|:---------|
| WordPress | seo-wordpress-manager 技能 |
| Medium | mcp-medium (API token) |
| Notion | mcp-notion |
| GitHub Pages | gh CLI (内置) |
| Astro 站点 | astro-cta-injector 技能 |
| 微信公众号 | 手动发布或第三方工具 |

---

## 📄 开源协议

MIT © [nicepkg](https://github.com/nicepkg)

<div align="center">

**[⬆ 返回主项目](../README_cn.md)**

</div>
