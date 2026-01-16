# Video Creator Workflow

Claude Code workflow for YouTubers, TikTokers, and video content creators.

[中文文档](./README_cn.md)

## Target Users

- YouTubers & Video Bloggers
- TikTok / Douyin Creators
- Shorts / Reels Creators
- Video Editors & Producers
- Live Streamers

## Installed Skills (15)

### Research & Ideation
| Skill | Function | Trigger Example |
|-------|----------|-----------------|
| content-trend-researcher | Track trending topics across 10+ platforms | "Find trending topics in gaming" |
| youtube-transcript | Extract video transcripts for research | "Get transcript from this YouTube URL" |
| video-downloader | Download videos for reference/editing | "Download this YouTube video" |

### Scripting & Hooks
| Skill | Function | Trigger Example |
|-------|----------|-----------------|
| video-script-writer | Write complete video scripts with structure | "Write a script for a 10-min tutorial" |
| video-hook-generator | Generate viral opening hooks (first 3 seconds) | "Create 5 hooks for a video about [topic]" |

### Titles & Thumbnails
| Skill | Function | Trigger Example |
|-------|----------|-----------------|
| video-title-optimizer | Optimize titles for CTR and SEO | "Generate title options for [topic]" |
| thumbnail-concept-generator | Create thumbnail concepts and briefs | "Design thumbnail concept for [video]" |
| canvas-design | AI visual design for thumbnails | "Design a YouTube thumbnail" |

### SEO & Distribution
| Skill | Function | Trigger Example |
|-------|----------|-----------------|
| youtube-seo-optimizer | Optimize descriptions, tags, chapters | "Create YouTube SEO for my video" |
| short-form-converter | Convert long videos to Shorts/TikTok | "Create 3 short clips from this video" |
| social-repurposer | Cross-platform content adaptation | "Convert to TikTok format" |
| srt-translator | Translate subtitles for global reach | "Translate this SRT to Spanish" |

### Analytics & Monetization
| Skill | Function | Trigger Example |
|-------|----------|-----------------|
| video-analytics-interpreter | Interpret YouTube/TikTok analytics | "Analyze why this video underperformed" |
| sponsor-pitch-generator | Create sponsorship pitches and media kits | "Create media kit for my channel" |
| video-comparer | Compare video quality for production | "Compare these two video files" |

## Quick Start

```bash
cd video-creator-workflow
# Launch Claude Code - skills activate automatically
```

## Automated Video Workflows

### 1. Complete Video Production Pipeline
```
1. "Find trending topics in [niche]"
2. "Write a video script about [topic]"
3. "Create 5 hook variations"
4. "Generate title options for the video"
5. "Create YouTube SEO (description, tags, chapters)"
6. "Design thumbnail concepts"
```

### 2. Viral Short-Form Content
```
1. "Analyze this long video for viral moments"
2. "Convert to 5 short-form clips"
3. "Create hooks for each clip"
4. "Optimize titles for TikTok/Shorts"
```

### 3. International Expansion
```
1. "Get transcript from my video"
2. "Translate subtitles to Spanish, Portuguese, Japanese"
3. "Adapt titles for each market"
4. "Create localized descriptions"
```

### 4. Channel Growth Analysis
```
1. "Analyze my last 10 videos' performance"
2. "Identify patterns in my best performers"
3. "Diagnose why recent videos underperformed"
4. "Suggest content strategy improvements"
```

### 5. Sponsorship Outreach
```
1. "Create a media kit for my channel"
2. "Write sponsorship pitch for [brand]"
3. "Generate collaboration ideas"
```

### 6. Competitor Research
```
1. "Download transcript from competitor video"
2. "Analyze their content structure"
3. "Identify gaps I can fill"
4. "Generate differentiated content ideas"
```

## Skill Combinations

- **Viral Video**: content-trend-researcher → video-script-writer → video-hook-generator → video-title-optimizer → youtube-seo-optimizer
- **Shorts Factory**: youtube-transcript → short-form-converter → video-hook-generator → social-repurposer
- **Global Reach**: youtube-transcript → srt-translator → video-title-optimizer (per language)
- **Channel Optimization**: video-analytics-interpreter → content-trend-researcher → video-script-writer
- **Monetization**: video-analytics-interpreter → sponsor-pitch-generator

## Output Standards

- **Scripts**: Complete with timestamps, B-roll suggestions, text overlays
- **Hooks**: Multiple variations with text overlays, 3-second optimized
- **Titles**: CTR-optimized, keyword-included, character-count validated
- **Thumbnails**: Visual brief with composition, colors, text, emotion
- **SEO**: Full description, 8-12 tags, chapters, hashtags
- **Translations**: Timing-preserved, culturally adapted, platform-ready

## Platform Support

| Platform | Optimizations Available |
|----------|------------------------|
| YouTube Long | Scripts, SEO, Thumbnails, Analytics |
| YouTube Shorts | Hooks, Titles, Vertical conversion |
| TikTok | Hooks, Trending sounds, Captions |
| Instagram Reels | Visual optimization, Hashtags |
| Douyin | Chinese localization, Trend research |

## Multi-AI Tool Support

This workflow supports:
- Claude Code (`.claude/skills/`)
- Codex (`.codex/skills/`)
- Cursor (`.cursor/skills/`)
- OpenCode (`.opencode/skill/`)

## Prerequisites

Some skills require external tools:
- `yt-dlp` - Required for youtube-transcript, video-downloader
- `ffmpeg` - Required for video-comparer

## License

MIT
