<div align="center">

# 🎬 Video Creator Workflow

### **Your AI Video Production Team**

[← Back to AI Workflow](../../README.md)

[简体中文](./README_cn.md) | English

</div>

---

## 🎯 Who Is This For?

- **YouTubers** - Long-form content creators
- **TikTokers** - Short-form viral content
- **Video Editors** - Production professionals
- **Live Streamers** - Content repurposing

---

## ⚡ Quick Install

```bash
# Install all 29 skills with one command
npx add-skill nicepkg/ai-workflow/workflows/video-creator-workflow

# Or install specific skills
npx add-skill nicepkg/ai-workflow/workflows/video-creator-workflow --skill video-script-writer
```

---

## 📦 Skills Included (29)

### 1️⃣ Trend Discovery & Topic Research
| Skill | What It Does |
|:------|:-------------|
| `serpapi` | Search Google/YouTube trends, generate topic pool |
| `content-trend-researcher` | Track trending topics across 10+ platforms |
| `content-research` | Cross-platform research with citations |
| `capture-triage` | Sort captured ideas into actionable tasks |

### 2️⃣ Competitor Analysis & Material Collection
| Skill | What It Does |
|:------|:-------------|
| `youtube-transcript` | Extract video transcripts for analysis |
| `youtube-to-markdown` | Convert YouTube videos to summary + transcript |
| `transcribe-and-analyze` | Local transcription with WhisperKit |
| `video-downloader` | Download videos for reference/editing |
| `tapestry` | Auto-detect content type and route to right skill |

### 3️⃣ Scripting & Voice Optimization
| Skill | What It Does |
|:------|:-------------|
| `video-script-writer` | Write complete video scripts with structure |
| `video-script-collaborial` | Make scripts sound natural and conversational |
| `video-hook-generator` | Generate viral opening hooks (first 3 seconds) |

### 4️⃣ Titles & Thumbnails
| Skill | What It Does |
|:------|:-------------|
| `video-title-optimizer` | Optimize titles for CTR and SEO |
| `thumbnail-concept-generator` | Create thumbnail concepts and briefs |
| `canvas-design` | AI visual design for thumbnails |

### 5️⃣ B-Roll & Media Processing
| Skill | What It Does |
|:------|:-------------|
| `pexels-media` | Source royalty-free images/videos from Pexels |
| `media-processing` | FFmpeg batch processing: cut, merge, watermark |
| `video-to-gif` | Convert video clips to high-quality GIFs |

### 6️⃣ SEO & Distribution
| Skill | What It Does |
|:------|:-------------|
| `youtube-seo-optimizer` | Optimize descriptions, tags, chapters |
| `short-form-converter` | Convert long videos to Shorts/TikTok |
| `social-repurposer` | Cross-platform content adaptation |
| `srt-translator` | Translate subtitles for global reach |
| `instagram` | Publish directly to Instagram via Graph API |

### 7️⃣ Analytics & Growth
| Skill | What It Does |
|:------|:-------------|
| `video-analytics-interpreter` | Interpret YouTube/TikTok analytics |
| `posthog-analytics` | Product analytics and growth dashboards |
| `webfluence` | Build content systems for audience binge |

### 8️⃣ Monetization & Automation
| Skill | What It Does |
|:------|:-------------|
| `sponsor-pitch-generator` | Create sponsorship pitches and media kits |
| `video-comparer` | Compare video quality for production |
| `n8n-skills` | Workflow automation with n8n |

---

## 🔄 Industrial Video Pipeline

```
Stage 1: Trend Radar
├── serpapi → Daily keyword monitoring (20+ keywords)
├── content-trend-researcher → Hot topics across platforms
└── capture-triage → Sort ideas into actionable tasks

Stage 2: Competitor Research
├── youtube-transcript → Analyze competitor videos
├── youtube-to-markdown → Batch process 50+ competitor videos
└── transcribe-and-analyze → Transcribe your own recordings

Stage 3: Script Writing
├── video-script-writer → Full script with structure
├── video-script-collaborial → Make it sound natural
└── video-hook-generator → Nail the first 3 seconds

Stage 4: Production
├── pexels-media → Auto-fetch B-roll footage
├── media-processing → Batch edit, cut, watermark
└── video-to-gif → Create promotional GIFs

Stage 5: Optimization
├── video-title-optimizer → CTR-optimized titles
├── thumbnail-concept-generator → Thumbnail concepts
└── youtube-seo-optimizer → Tags, descriptions, chapters

Stage 6: Distribution
├── short-form-converter → Long → Shorts/TikTok
├── social-repurposer → Cross-platform versions
├── instagram → Direct publish to IG
└── srt-translator → Multi-language subtitles

Stage 7: Growth Loop
├── video-analytics-interpreter → Performance analysis
├── posthog-analytics → Conversion tracking
└── webfluence → Build content moat
```

---

## 💡 Example Workflows

### Viral Video Factory
```
1. "Search trending topics in [niche] for this week"
2. "Download and analyze top 5 competitor videos"
3. "Write a script with viral hook"
4. "Make the script sound more natural"
5. "Find B-roll footage for [scene]"
6. "Create 3 title options and thumbnail concepts"
7. "Publish to Instagram"
```

### Shorts Mass Production
```
1. "Transcribe my long video"
2. "Find 5 viral moments for shorts"
3. "Create hooks for each clip"
4. "Convert to vertical format"
5. "Generate GIFs for promotion"
```

### Content Repurposing
```
1. "Extract transcript from YouTube video"
2. "Convert to blog post + Twitter thread"
3. "Translate subtitles to Spanish, Japanese"
4. "Create Instagram carousel version"
```

---

## 🌐 Platform Support

| Platform | Features |
|:---------|:---------|
| YouTube Long | Scripts, SEO, Thumbnails, Analytics, Chapters |
| YouTube Shorts | Hooks, Titles, Vertical conversion |
| TikTok | Hooks, Trending sounds, Captions |
| Instagram Reels | Direct publish, Visual optimization |

---

## 🔧 Prerequisites

```bash
# Required for media skills
brew install yt-dlp ffmpeg

# Optional: Local transcription
pip install whisperkit
```

| Skill | Requirement |
|-------|-------------|
| `serpapi` | `SERPAPI_KEY` |
| `instagram` | Instagram Graph API token |
| `pexels-media` | `PEXELS_API_KEY` |
| `posthog-analytics` | PostHog project key |

---

## 📄 License

MIT © [nicepkg](https://github.com/nicepkg)

<div align="center">

**[⬆ Back to Main Project](../../README.md)**

</div>
