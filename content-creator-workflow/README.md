<div align="center">

# ✍️ Content Creator Workflow

### **Turn Your AI into a Professional Content Strategist**

[← Back to AI Workflow](../README.md)

[简体中文](./README_cn.md) | English

</div>

---

## 🎯 Who Is This For?

- **Bloggers & Writers** - Scale content production
- **SEO Specialists** - Optimize for search rankings
- **Content Marketers** - Build brand authority
- **Personal Brand Builders** - Grow your audience

---

## ⚡ Quick Install

```bash
# Install all 32 skills with one command
npx add-skill nicepkg/ai-workflow/content-creator-workflow

# Or install specific skills
npx add-skill nicepkg/ai-workflow/content-creator-workflow --skill blog-post-writer
```

---

## 📦 Skills Included (32)

### 1️⃣ Trend Discovery & Topic Research
| Skill | What It Does |
|:------|:-------------|
| `weak-signal-synthesizer` | Cross-platform weak signal detection for 3-6 month trend forecasting |
| `content-trend-researcher` | Track hot topics across 10+ platforms |
| `competitive-ads-extractor` | Extract and analyze competitor ad creatives & messaging |
| `twitter-reader` | Fetch Twitter/X content via Jina API |

### 2️⃣ Research & Content Ingestion
| Skill | What It Does |
|:------|:-------------|
| `article-extractor` | Extract clean article content from URLs |
| `youtube-processor` | YouTube video to transcript & Markdown notes |
| `youtube-transcript` | Extract YouTube video transcripts |
| `content-research` | Structured research: arguments, evidence, counterpoints |

### 3️⃣ Content Planning & Briefs
| Skill | What It Does |
|:------|:-------------|
| `content-brief-generator` | Generate comprehensive content briefs with audience, angle, evidence |
| `content-brief` | SEO content planning briefs |
| `skill-navigator` | Recommend which skills to use for your goal |

### 4️⃣ Writing & Content Creation
| Skill | What It Does |
|:------|:-------------|
| `blog-post-writer` | Transform notes into polished blog posts |
| `content-research-writer` | Research + writing partner with citations |
| `newsletter-coach` | Turn experiences into newsletter drafts |
| `fact-checker` | Verify factual claims with sources |

### 5️⃣ Hook & Viral Optimization
| Skill | What It Does |
|:------|:-------------|
| `hook-stack-evaluator` | Score and optimize headlines & hooks for virality |
| `email-subject-line-optimizer` | A/B test email subject lines & predict open rates |
| `ai-slop-detector` | Remove AI-sounding phrases, ensure authentic voice |

### 6️⃣ Multi-Platform Distribution
| Skill | What It Does |
|:------|:-------------|
| `content-repurposer` | Transform content into 8+ formats (slides, scripts, social, etc.) |
| `social-repurposer` | Blog → Twitter thread, article → LinkedIn post |
| `social-media` | Generate posts, threads, calendars for X/LinkedIn/IG/FB |
| `linkedin-announcement-generator` | Professional LinkedIn milestone announcements |
| `podcast-content-suite` | Create podcast content marketing suite |

### 7️⃣ SEO & Publishing
| Skill | What It Does |
|:------|:-------------|
| `pre-publish-post-assistant` | Pre-publish checklist (structure, CTA, links, formatting) |
| `seo-wordpress-manager` | WordPress SEO & publishing workflow |
| `gsc-assistant` | Google Search Console indexing & tracking |
| `astro-cta-injector` | Auto-inject CTAs into Astro site content |

### 8️⃣ Visual & Document Tools
| Skill | What It Does |
|:------|:-------------|
| `nano-banana` | AI image generation (Gemini) |
| `canvas-design` | AI visual design, PNG/PDF export |
| `docx` | Word document creation/editing |
| `pdf` | PDF processing and generation |

---

## 🔄 Complete Content Pipeline (8 Stages)

```
Stage 1: Trend Discovery
  → "Find weak signals in AI/tech for next quarter"
  → "Analyze competitor content strategy"

Stage 2: Research
  → "Extract key points from this article: [URL]"
  → "Summarize this YouTube video: [URL]"

Stage 3: Content Planning
  → "Create a content brief for [topic]"
  → "What skills should I use for writing a viral thread?"

Stage 4: Writing
  → "Write a blog post from my research notes"
  → "Draft a newsletter about my experience with [topic]"

Stage 5: Viral Optimization
  → "Score and improve these 5 headline options"
  → "Remove AI-sounding phrases from this draft"

Stage 6: Distribution
  → "Convert this article to Twitter thread + LinkedIn post"
  → "Create a LinkedIn announcement for this milestone"

Stage 7: SEO & Publishing
  → "Run pre-publish checklist on this post"
  → "Check my GSC indexing status"

Stage 8: Visual Assets
  → "Generate a cover image for this article"
  → "Export to Word document"
```

---

## 💡 Example Workflows

### Viral Blog Post Factory
```
1. "Find weak signals in AI tools space for next 3 months"
2. "Extract key points from these 5 competitor articles: [URLs]"
3. "Create a content brief for 'AI coding assistants comparison'"
4. "Write a 2000-word blog post based on the brief"
5. "Score these 5 headline options and improve the best one"
6. "Remove any AI-sounding phrases from the draft"
7. "Run the pre-publish checklist"
8. "Generate a cover image"
9. "Convert to Twitter thread + LinkedIn post"
```

### Newsletter Creation Pipeline
```
1. "Help me brainstorm newsletter topics from my week"
2. "Turn my experience with [tool] into a newsletter draft"
3. "Optimize the email subject line for open rates"
4. "Remove AI taste and make it sound more personal"
5. "Create 3 A/B test subject line variations"
```

### Research-to-Content Pipeline
```
1. "Extract this article: https://example.com/article"
2. "Summarize this YouTube video: https://youtube.com/watch?v=xxx"
3. "Do structured research on [topic] with arguments and counterpoints"
4. "Write a research-backed article with proper citations"
5. "Fact-check all claims in the article"
```

### SEO Content Machine
```
1. "Create an SEO content brief for keyword '[keyword]'"
2. "Write a blog post optimized for the target keyword"
3. "Run pre-publish SEO checklist"
4. "Publish to WordPress with proper meta tags"
5. "Track indexing status in Google Search Console"
```

### Multi-Platform Distribution
```
1. "Convert this blog post into 8 different formats"
2. "Create a Twitter thread version (10-12 tweets)"
3. "Write a LinkedIn post version"
4. "Generate Instagram carousel content"
5. "Create a podcast script from the article"
6. "Draft an email newsletter version"
```

### Content Refresh Workflow
```
1. "Analyze competitor content on [topic]"
2. "Find content gaps in my existing article"
3. "Update the article with new information"
4. "Re-optimize headlines for better CTR"
5. "Republish and track GSC indexing"
```

---

## 🔧 Prerequisites

```bash
# Required for some skills
brew install yt-dlp

# Optional: For local AI image generation
# Requires GEMINI_API_KEY for nano-banana
```

| Skill | Requirement |
|-------|-------------|
| `twitter-reader` | `JINA_API_KEY` |
| `nano-banana` | `GEMINI_API_KEY` |
| `youtube-processor` | `yt-dlp` installed |
| `youtube-transcript` | `yt-dlp` installed |
| `gsc-assistant` | Google Search Console access |
| `seo-wordpress-manager` | WordPress site access |

---

## 🔗 Publishing Integration

| Platform | Integration |
|:---------|:------------|
| WordPress | seo-wordpress-manager skill |
| Medium | mcp-medium (API token) |
| Notion | mcp-notion |
| GitHub Pages | gh CLI (built-in) |
| Astro Sites | astro-cta-injector skill |

---

## 📄 License

MIT © [nicepkg](https://github.com/nicepkg)

<div align="center">

**[⬆ Back to Main Project](../README.md)**

</div>
