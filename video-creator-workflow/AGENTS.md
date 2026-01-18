# Video Creator Workflow - AI Instructions

AI execution guide for video creator workflow with 29 skills for industrial-scale video production.

## Available Skills (29)

### 1. Trend Discovery & Topic Research
| Skill | Trigger |
|-------|---------|
| serpapi | search trends, keyword monitoring, topic pool, Google trends |
| content-trend-researcher | trending topics, hot topics, what's popular, content trends |
| content-research | research topic, cross-platform research, citations |
| capture-triage | sort ideas, organize captures, actionable tasks |

### 2. Competitor Analysis & Material Collection
| Skill | Trigger |
|-------|---------|
| youtube-transcript | youtube transcript, video subtitles, captions, get transcript |
| youtube-to-markdown | youtube summary, video to markdown, batch transcripts |
| transcribe-and-analyze | transcribe video, whisper, local transcription, audio to text |
| video-downloader | download video, save video, grab video |
| tapestry | auto-detect content, route to skill, unified extraction |

### 3. Scripting & Voice Optimization
| Skill | Trigger |
|-------|---------|
| video-script-writer | video script, write script, YouTube script, tutorial script |
| video-script-collaborial | make natural, conversational, sound human, oral style |
| video-hook-generator | hook, opening, first 3 seconds, attention grab, scroll stop |

### 4. Titles & Thumbnails
| Skill | Trigger |
|-------|---------|
| video-title-optimizer | video title, YouTube title, CTR, title ideas |
| thumbnail-concept-generator | thumbnail, cover image, thumbnail concept, click-worthy |
| canvas-design | design thumbnail, create image, visual design |

### 5. B-Roll & Media Processing
| Skill | Trigger |
|-------|---------|
| pexels-media | B-roll, stock footage, royalty-free, pexels, stock video |
| media-processing | ffmpeg, cut video, merge, watermark, batch edit |
| video-to-gif | convert to gif, GIF, animated preview, promo gif |

### 6. SEO & Distribution
| Skill | Trigger |
|-------|---------|
| youtube-seo-optimizer | YouTube SEO, description, tags, chapters, hashtags |
| short-form-converter | shorts, TikTok, reels, clip, cut from long video |
| social-repurposer | multi-platform, repurpose, convert format |
| srt-translator | translate subtitles, SRT, VTT, multilingual, captions |
| instagram | post to instagram, instagram publish, IG, reels |

### 7. Analytics & Growth
| Skill | Trigger |
|-------|---------|
| video-analytics-interpreter | analytics, metrics, CTR, retention, views, performance |
| posthog-analytics | product analytics, conversion, growth dashboard |
| webfluence | content system, binge, channel architecture |

### 8. Monetization & Automation
| Skill | Trigger |
|-------|---------|
| sponsor-pitch-generator | sponsor, brand deal, media kit, pitch, collaboration |
| video-comparer | compare videos, video quality, compression |
| n8n-skills | automation, n8n, workflow, scheduled tasks |

## Industrial Video Pipeline

```
Stage 1: Trend Radar
├── serpapi → Daily keyword monitoring (20+ keywords)
├── content-trend-researcher → Hot topics across platforms
└── capture-triage → Sort ideas into actionable tasks

Stage 2: Competitor Research
├── youtube-transcript → Analyze competitor videos
├── youtube-to-markdown → Batch process 50+ videos
└── transcribe-and-analyze → Transcribe your recordings

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

## Skill Combinations

### Viral Video Factory
```
serpapi → content-research → video-script-writer
→ video-script-collaborial → video-hook-generator
→ video-title-optimizer → youtube-seo-optimizer → instagram
```

### Competitor Teardown
```
video-downloader → youtube-to-markdown (batch 50 videos)
→ content-research → video-script-writer
```

### Shorts Mass Production
```
youtube-transcript → short-form-converter → video-hook-generator
→ pexels-media → media-processing → social-repurposer
```

### Global Reach
```
youtube-transcript → srt-translator → video-title-optimizer
→ thumbnail-concept-generator
```

### Full Automation
```
serpapi (scheduled) → capture-triage → n8n-skills
→ video-analytics-interpreter → webfluence
```

## Quality Gates

1. **Before Script**: Run serpapi + content-research
2. **After Script**: Run video-script-collaborial for natural voice
3. **Hook Check**: Run video-hook-generator, must have 5+ variations
4. **Title Check**: Run video-title-optimizer, CTR estimate >5%
5. **Before Publish**: Run youtube-seo-optimizer
6. **After Publish**: Track with video-analytics-interpreter

## Output Standards

### Video Scripts
- Complete timestamps throughout
- B-roll suggestions (with pexels-media sources)
- Text overlay recommendations
- Clear section breaks (Hook, Content, CTA)
- Natural conversational tone (after video-script-collaborial)

### Hooks
- 5+ variations per video
- First 3 seconds optimized
- Text overlay included
- Platform-specific versions (YouTube vs TikTok)

### Titles
- CTR-optimized (target 5-10%)
- Keywords in first 50 characters
- Character count: 60-70 for YouTube
- A/B test variations

### Thumbnails
- Visual composition guide
- Color palette specified
- Text overlay (3-4 words max)
- Emotion/expression direction
- Platform dimensions (1280x720 YouTube)

### SEO Package
- Description: 200+ words, front-loaded keywords
- Tags: 8-12 relevant tags
- Chapters: Timestamps every 2-3 minutes
- Hashtags: 3-5 relevant hashtags

### Shorts/TikTok
- Length: 15-60 seconds
- Vertical 9:16
- Auto-captions enabled
- Hook in first 1 second

## Platform Metrics

| Platform | Good CTR | Good Retention | Key Metric |
|----------|----------|----------------|------------|
| YouTube Long | 4-10% | 50%+ AVD | Watch Time |
| YouTube Shorts | N/A | 90%+ loop | Shares |
| TikTok | N/A | 30%+ full watch | Shares |
| Instagram Reels | N/A | 50%+ | Saves |

## Prerequisites

| Skill | Requirement |
|-------|-------------|
| youtube-transcript | `yt-dlp` |
| video-downloader | `yt-dlp` |
| transcribe-and-analyze | `whisperkit` |
| media-processing | `ffmpeg` |
| video-to-gif | `ffmpeg` |
| serpapi | `SERPAPI_KEY` |
| instagram | Instagram Graph API token |
| pexels-media | `PEXELS_API_KEY` |
| posthog-analytics | PostHog project key |

```bash
# Install required tools
brew install yt-dlp ffmpeg
pip install whisperkit
```
