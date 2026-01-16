# Content Creator Workflow

Claude Code workflow for bloggers, content creators, and personal brand builders.

[中文文档](./README_cn.md)

## Target Users

- Bloggers & Writers
- Content Creators
- Podcasters
- Personal Brand Builders

## Installed Skills (15)

### Research & Trend Discovery
| Skill | Function | Trigger Example |
|-------|----------|-----------------|
| content-trend-researcher | Hot topic tracking across 10+ platforms | "Find trending topics in AI" |
| twitter-reader | Fetch Twitter/X content via Jina API | "Get this tweet content" |
| youtube-transcript | Extract YouTube video transcripts | "Download transcript from this video" |
| article-extractor | Extract clean article from URLs | "Extract this blog post" |

### Writing & Content Creation
| Skill | Function | Trigger Example |
|-------|----------|-----------------|
| blog-post-writer | Transform notes into polished blog posts | "Write a blog post from my notes" |
| content-research-writer | Research + writing partner with citations | "Help me write an article on [topic]" |
| content-brief | SEO content planning briefs | "Create a content brief for [topic]" |
| fact-checker | Verify factual claims with sources | "Fact-check this document" |

### Visual & Design
| Skill | Function | Trigger Example |
|-------|----------|-----------------|
| nano-banana | AI image generation (Gemini) | "Generate a blog cover image" |
| canvas-design | AI visual design, PNG/PDF export | "Design a cover image" |

### Distribution & Export
| Skill | Function | Trigger Example |
|-------|----------|-----------------|
| social-repurposer | Cross-platform content conversion | "Convert to Twitter thread" |
| content-repurposer | Multi-format content rewriting | "Rewrite as Newsletter" |
| podcast-content-suite | Podcast content creation | "Generate podcast outline" |
| docx | Word document creation/editing | "Export to Word document" |
| pdf | PDF processing and generation | "Generate PDF" |

## Quick Start

```bash
cd content-creator-workflow
# Launch Claude Code - skills activate automatically
```

## Automated Content Workflow

### 1. Trend Discovery & Topic Selection
```
"Find today's hottest topics in [tech/finance/lifestyle]"
"What's trending on Twitter about AI?"
"Analyze content trends for [topic] across platforms"
```

### 2. Research & Material Collection
```
"Extract this article: [URL]"
"Download transcript from this YouTube video: [URL]"
"Research [topic] and compile sources"
```

### 3. Content Creation
```
"Create a content brief for [topic] targeting [audience]"
"Write a blog post from my research notes"
"Generate 5 viral headline options for this article"
```

### 4. Visual Assets
```
"Generate a blog cover image for [topic]"
"Design a thumbnail for YouTube"
```

### 5. Multi-Platform Distribution
```
"Convert this article to Twitter thread"
"Rewrite for LinkedIn (professional tone)"
"Create Instagram carousel text"
```

### 6. Export & Publish
```
"Export to Word document"
"Generate PDF version"
```

## Publishing Integration

For automated publishing to platforms, configure MCP servers:

| Platform | MCP Server |
|----------|------------|
| Medium | mcp-medium (API token required) |
| WordPress | mcp-wordpress (site URL + credentials) |
| Notion | mcp-notion (integration token) |
| GitHub Pages | gh CLI (already supported) |

## Multi-AI Tool Support

This workflow supports:
- Claude Code (`.claude/skills/`)
- Codex (`.codex/skills/`)
- Cursor (`.cursor/skills/`)
- OpenCode (`.opencode/skill/`)

## License

MIT
