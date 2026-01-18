# Content Creator Workflow - AI Instructions

AI execution guide for content creator workflow with 32 skills across 8 stages.

## Available Skills (32)

### 1. Trend Discovery & Topic Research
| Skill | Trigger |
|-------|---------|
| weak-signal-synthesizer | weak signals, future trends, 3-6 month forecast, emerging topics |
| content-trend-researcher | trending topics, hot topics, what's popular, content trends |
| competitive-ads-extractor | competitor ads, ad library, competitor messaging, ad analysis |
| twitter-reader | twitter, tweet, X post, fetch tweet |

### 2. Research & Content Ingestion
| Skill | Trigger |
|-------|---------|
| article-extractor | extract article, download blog post, save article |
| youtube-processor | youtube video, summarize video, video to notes |
| youtube-transcript | youtube transcript, video subtitles, captions |
| content-research | research topic, arguments, evidence, counterpoints |

### 3. Content Planning & Briefs
| Skill | Trigger |
|-------|---------|
| content-brief-generator | content brief, audience brief, angle, evidence list |
| content-brief | SEO brief, content plan, keyword brief |
| skill-navigator | which skill, recommend skill, what tool to use |

### 4. Writing & Content Creation
| Skill | Trigger |
|-------|---------|
| blog-post-writer | blog post, write article, transform notes |
| content-research-writer | research and write, help write, article with citations |
| newsletter-coach | newsletter, email draft, substack, weekly update |
| fact-checker | fact check, verify claims, check accuracy |

### 5. Hook & Viral Optimization
| Skill | Trigger |
|-------|---------|
| hook-stack-evaluator | score headline, evaluate hook, improve title, viral check |
| email-subject-line-optimizer | email subject, subject line, open rate, A/B test |
| ai-slop-detector | remove AI, authentic voice, AI taste, sound natural |

### 6. Multi-Platform Distribution
| Skill | Trigger |
|-------|---------|
| content-repurposer | multi-format, slides, script, 8 formats |
| social-repurposer | Twitter thread, LinkedIn post, social media conversion |
| social-media | social posts, content calendar, X/LinkedIn/IG/FB |
| linkedin-announcement-generator | LinkedIn announcement, milestone, professional post |
| podcast-content-suite | podcast, audio content, show notes |

### 7. SEO & Publishing
| Skill | Trigger |
|-------|---------|
| pre-publish-post-assistant | pre-publish check, publish checklist, review before post |
| seo-wordpress-manager | WordPress SEO, publish to WordPress, site SEO |
| gsc-assistant | Google Search Console, indexing, GSC, crawl status |
| astro-cta-injector | Astro CTA, inject CTA, site conversion |

### 8. Visual & Document Tools
| Skill | Trigger |
|-------|---------|
| nano-banana | generate image, AI image, cover image, thumbnail |
| canvas-design | design, visual design, cover, infographic |
| docx | Word, document, export docx |
| pdf | PDF, export pdf |

## 8-Stage Content Pipeline

```
Stage 1: Trend Discovery
├── weak-signal-synthesizer → Find emerging trends 3-6 months ahead
├── content-trend-researcher → Track current hot topics
└── competitive-ads-extractor → Analyze competitor messaging

Stage 2: Research
├── article-extractor → Extract key content from URLs
├── youtube-processor → Summarize videos to markdown notes
└── content-research → Structured research with evidence

Stage 3: Content Planning
├── content-brief-generator → Comprehensive brief (audience, angle, evidence)
├── content-brief → SEO-focused content plan
└── skill-navigator → Recommend which skills to use

Stage 4: Writing
├── blog-post-writer → Transform notes to polished articles
├── content-research-writer → Research-backed writing with citations
├── newsletter-coach → Turn experiences into newsletters
└── fact-checker → Verify all claims

Stage 5: Viral Optimization
├── hook-stack-evaluator → Score & improve headlines/hooks
├── ai-slop-detector → Remove AI-sounding phrases
└── email-subject-line-optimizer → A/B test email subjects

Stage 6: Distribution
├── content-repurposer → Convert to 8+ formats
├── social-repurposer → Platform-specific conversions
├── social-media → Generate posts for all platforms
└── linkedin-announcement-generator → Professional announcements

Stage 7: SEO & Publishing
├── pre-publish-post-assistant → Pre-publish checklist
├── seo-wordpress-manager → WordPress SEO workflow
├── gsc-assistant → Track Google indexing
└── astro-cta-injector → Auto-inject CTAs

Stage 8: Visual Assets
├── nano-banana → AI image generation
├── canvas-design → Visual design creation
├── docx → Word document export
└── pdf → PDF generation
```

## Skill Combinations

### Viral Article Pipeline
```
weak-signal-synthesizer → content-brief-generator → blog-post-writer
→ hook-stack-evaluator → ai-slop-detector → social-repurposer
```

### Research Deep Dive
```
article-extractor + youtube-processor → content-research
→ content-research-writer → fact-checker → blog-post-writer
```

### Newsletter Creation
```
content-trend-researcher → newsletter-coach → ai-slop-detector
→ email-subject-line-optimizer → pre-publish-post-assistant
```

### Full Distribution
```
blog-post-writer → content-repurposer → social-media
→ linkedin-announcement-generator → pre-publish-post-assistant
```

### SEO-First Content
```
content-brief → blog-post-writer → seo-wordpress-manager
→ gsc-assistant → astro-cta-injector
```

## Output Standards

| Format | Requirements |
|--------|--------------|
| Long-form | 1500-3000 words, clear H2/H3 structure |
| Twitter thread | 8-12 tweets, <280 chars each, hook first |
| LinkedIn | Professional tone, <1300 chars, CTA at end |
| Newsletter | Personal voice, clear sections, single CTA |
| Content brief | SEO keywords, competitor analysis, E-E-A-T |

## Quality Gates

1. **Before Writing**: Run content-brief-generator
2. **After Draft**: Run ai-slop-detector to remove AI voice
3. **Headlines**: Run hook-stack-evaluator, score must be >7/10
4. **Before Publish**: Run pre-publish-post-assistant checklist
5. **After Publish**: Track with gsc-assistant

## Prerequisites

Some skills require API keys or tools:
| Skill | Requirement |
|-------|-------------|
| twitter-reader | `JINA_API_KEY` |
| nano-banana | `GEMINI_API_KEY` |
| youtube-processor | `yt-dlp` installed |
| youtube-transcript | `yt-dlp` installed |
| gsc-assistant | Google Search Console access |
| seo-wordpress-manager | WordPress site access |
