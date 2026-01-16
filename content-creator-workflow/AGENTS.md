# Content Creator Workflow - AI Instructions

AI execution guide for content creator workflow.

## Available Skills

### Research & Trend Discovery
| Skill | Trigger |
|-------|---------|
| content-trend-researcher | trending topics, hot topics, what's popular, content trends |
| twitter-reader | twitter, tweet, X post, fetch tweet |
| youtube-transcript | youtube transcript, video subtitles, captions |
| article-extractor | extract article, download blog post, save article |

### Writing & Content Creation
| Skill | Trigger |
|-------|---------|
| blog-post-writer | blog post, write article, transform notes |
| content-research-writer | research and write, help write, article with citations |
| content-brief | content brief, content plan, SEO brief |
| fact-checker | fact check, verify claims, check accuracy |

### Visual & Design
| Skill | Trigger |
|-------|---------|
| nano-banana | generate image, AI image, cover image, thumbnail |
| canvas-design | design, visual design, cover, infographic |

### Distribution & Export
| Skill | Trigger |
|-------|---------|
| social-repurposer | Twitter thread, LinkedIn, social media conversion |
| content-repurposer | rewrite, Newsletter, multi-format |
| podcast-content-suite | podcast, audio content, show notes |
| docx | Word, document, export docx |
| pdf | PDF, export pdf |

## Recommended Workflow

### Full Content Pipeline

1. **Trend Discovery** - Use content-trend-researcher to find hot topics
2. **Material Collection** - Use twitter-reader, youtube-transcript, article-extractor
3. **Planning** - Use content-brief to create SEO-optimized content plan
4. **Research** - Use content-research-writer to gather citations
5. **Writing** - Use blog-post-writer to transform notes into articles
6. **Verification** - Use fact-checker to verify claims
7. **Design** - Use nano-banana or canvas-design for visuals
8. **Distribution** - Use social-repurposer for multi-platform versions
9. **Export** - Use docx/pdf for document export

## Skill Combinations

- **Hot Topic Article**: content-trend-researcher → content-brief → blog-post-writer → nano-banana → social-repurposer
- **Research Deep Dive**: article-extractor + youtube-transcript → content-research-writer → fact-checker → blog-post-writer
- **Video to Blog**: youtube-transcript → content-repurposer → blog-post-writer → social-repurposer
- **Podcast Episode**: content-trend-researcher → podcast-content-suite → content-repurposer

## Headline Generation

Use content-trend-researcher's headline formulas:
- Hook patterns with proven engagement
- Data-driven title optimization
- Platform-specific headline styles

## Output Standards

- Long-form: 1500-3000 words, clear structure
- Twitter thread: 8-12 tweets, <280 characters each
- LinkedIn: Professional tone, under 1300 characters
- Podcast outline: Clear segments, timestamp suggestions
- Content brief: SEO requirements, competitor analysis, E-E-A-T guidelines

## Prerequisites

Some skills require API keys:
- `JINA_API_KEY` - Required for twitter-reader
- `GEMINI_API_KEY` - Required for nano-banana image generation
