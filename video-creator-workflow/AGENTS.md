# Video Creator Workflow - AI Instructions

AI execution guide for video creator workflow.

## Available Skills (15)

### Research & Ideation
| Skill | Trigger |
|-------|---------|
| content-trend-researcher | trending topics, hot topics, what's popular, content trends |
| youtube-transcript | youtube transcript, video subtitles, captions, get transcript |
| video-downloader | download video, save video, grab video |

### Scripting & Hooks
| Skill | Trigger |
|-------|---------|
| video-script-writer | video script, write script, YouTube script, tutorial script |
| video-hook-generator | hook, opening, first 3 seconds, attention grab, scroll stop |

### Titles & Thumbnails
| Skill | Trigger |
|-------|---------|
| video-title-optimizer | video title, YouTube title, CTR, title ideas |
| thumbnail-concept-generator | thumbnail, cover image, thumbnail concept, click-worthy |
| canvas-design | design thumbnail, create image, visual design |

### SEO & Distribution
| Skill | Trigger |
|-------|---------|
| youtube-seo-optimizer | YouTube SEO, description, tags, chapters, hashtags |
| short-form-converter | shorts, TikTok, reels, clip, cut from long video |
| social-repurposer | multi-platform, repurpose, convert format |
| srt-translator | translate subtitles, SRT, VTT, multilingual, captions |

### Analytics & Monetization
| Skill | Trigger |
|-------|---------|
| video-analytics-interpreter | analytics, metrics, CTR, retention, views, performance |
| sponsor-pitch-generator | sponsor, brand deal, media kit, pitch, collaboration |
| video-comparer | compare videos, video quality, compression |

## Recommended Workflows

### Complete Video Production
1. **Research** - Use content-trend-researcher to find hot topics
2. **Script** - Use video-script-writer for complete script
3. **Hook** - Use video-hook-generator for opening variations
4. **Title** - Use video-title-optimizer for CTR-optimized title
5. **SEO** - Use youtube-seo-optimizer for description, tags, chapters
6. **Thumbnail** - Use thumbnail-concept-generator for visual brief

### Short-Form Content Factory
1. **Extract** - Use youtube-transcript to get source content
2. **Identify** - Use short-form-converter to find viral moments
3. **Hook** - Use video-hook-generator for each clip
4. **Distribute** - Use social-repurposer for platform adaptation

### International Expansion
1. **Transcript** - Use youtube-transcript to extract text
2. **Translate** - Use srt-translator for target languages
3. **Localize** - Use video-title-optimizer per market

### Channel Optimization
1. **Analyze** - Use video-analytics-interpreter for performance data
2. **Research** - Use content-trend-researcher for opportunities
3. **Plan** - Use video-script-writer for new content

### Monetization
1. **Analyze** - Use video-analytics-interpreter for channel stats
2. **Pitch** - Use sponsor-pitch-generator for media kit and proposals

## Skill Combinations

- **Viral Video**: content-trend-researcher → video-script-writer → video-hook-generator → video-title-optimizer → youtube-seo-optimizer
- **Shorts Factory**: youtube-transcript → short-form-converter → video-hook-generator → social-repurposer
- **Global Reach**: youtube-transcript → srt-translator → video-title-optimizer
- **Growth Strategy**: video-analytics-interpreter → content-trend-researcher → video-script-writer

## Output Standards

### Video Scripts
- Complete timestamps throughout
- B-roll suggestions included
- Text overlay recommendations
- Clear section breaks (Hook, Content, CTA)

### Hooks
- Multiple variations (5+)
- First 3 seconds optimized
- Text overlay included
- Platform-specific versions

### Titles
- CTR-optimized
- Keywords in first 50 characters
- Character count validated (60-70 for YouTube)
- A/B test variations

### Thumbnails
- Visual composition guide
- Color palette specified
- Text overlay (3-4 words max)
- Emotion/expression direction
- Platform-appropriate dimensions

### SEO Package
- Full description (200+ words)
- 8-12 relevant tags
- Chapters with timestamps
- 3-5 hashtags
- Keyword density optimized

### Translations
- Timing preserved from original
- Cultural adaptations noted
- Platform-ready format (SRT/VTT)
- Quality checklist completed

## Platform-Specific Guidelines

### YouTube Long-form
- Scripts: 8-15 minutes optimal
- Retention patterns: Open loops, pattern breaks
- SEO: Front-load keywords
- Thumbnails: Face + Text + Contrast

### YouTube Shorts / TikTok
- Length: 15-60 seconds optimal
- Hook: First 1-2 seconds critical
- Captions: Essential (85% watch muted)
- Vertical: 9:16 aspect ratio

### Instagram Reels
- Slightly more polished aesthetic
- Trending audio helps
- Hashtags in caption, not on video

## Key Metrics

### YouTube
- CTR: 4-10% good, 10%+ excellent
- AVD: 50%+ of video length
- Engagement: 4-8% good

### TikTok
- Watch Full Video: 30%+ good
- Engagement: 5-10% good
- Shares: Most important metric

## Prerequisites

Some skills require:
- `yt-dlp`: Install via `brew install yt-dlp` or `pip install yt-dlp`
- `ffmpeg`: Install via `brew install ffmpeg` or `apt install ffmpeg`
