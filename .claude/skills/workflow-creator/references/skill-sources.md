# Skill Sources Reference

Curated list of high-quality Claude Code skills organized by category.

## Official Anthropic Skills

Repository: `https://github.com/anthropics/skills`
Path prefix: `skills/`

| Skill | Description | Tags |
|-------|-------------|------|
| docx | Word document creation and editing | document, office |
| pdf | PDF processing and generation | document, office |
| pptx | PowerPoint presentation creation | document, office, presentation |
| xlsx | Excel spreadsheet manipulation | document, office, data |
| canvas-design | Visual design and image creation | design, image, creative |
| algorithmic-art | Generative art with p5.js | design, creative, art |
| frontend-design | Web frontend development | development, web, design |
| internal-comms | Internal communications writing | writing, communication |
| slack-gif-creator | Create GIFs for Slack | creative, communication |
| skill-creator | Create new skills | meta, development |

## Community Skills - gked2121

Repository: `https://github.com/gked2121/claude-skills`
Path prefix: (root level)

| Skill | Description | Tags |
|-------|-------------|------|
| social-repurposer | Cross-platform content adaptation | social-media, content, marketing |
| linkedin-post-optimizer | LinkedIn post optimization | social-media, linkedin, marketing |
| content-repurposer | Multi-format content transformation | content, writing |
| seo-optimizer | SEO content optimization | seo, marketing, content |
| seo-keyword-cluster-builder | SEO keyword research | seo, marketing |
| landing-page-copywriter | Landing page copy creation | copywriting, marketing |
| email-template-generator | Email marketing templates | email, marketing |
| cold-email-sequence-generator | Cold email sequences | email, sales, marketing |
| podcast-content-suite | Podcast content creation | podcast, content, audio |
| webinar-content-repurposer | Webinar to content conversion | webinar, content |
| technical-writer | Technical documentation | documentation, writing |
| api-documentation-writer | API documentation | documentation, api, development |
| code-review-pro | Code review assistance | development, code-quality |
| screenshot-to-code | Convert screenshots to code | development, design |
| database-schema-designer | Database schema design | development, database |
| regex-debugger | Regex debugging and testing | development, tools |

## Community Skills - ComposioHQ

Repository: `https://github.com/ComposioHQ/awesome-claude-skills`
Path prefix: (root level)

| Skill | Description | Tags |
|-------|-------------|------|
| content-research-writer | Research-based content writing | research, writing, content |
| domain-ideas | Domain name brainstorming | business, naming |
| video-downloader | Video download assistance | video, tools |

## Community Skills - alonw0

Repository: `https://github.com/alonw0/web-asset-generator`
Path prefix: `skills/`

| Skill | Description | Tags |
|-------|-------------|------|
| web-asset-generator | Favicons, app icons, social media images | design, web, social-media |

## Community Skills - daymade

Repository: `https://github.com/daymade/claude-code-skills`
Path prefix: (root level)

| Skill | Description | Tags |
|-------|-------------|------|
| twitter-reader | Twitter/X content fetching | social-media, twitter, research |
| youtube-downloader | YouTube video/audio download | video, youtube, tools |
| pdf-creator | PDF document creation | document, pdf |
| ppt-creator | PowerPoint creation | document, presentation |
| mermaid-tools | Mermaid diagram generation | diagram, documentation |
| prompt-optimizer | Prompt engineering optimization | ai, prompt |
| fact-checker | Fact verification | research, verification |
| skill-creator | Skill creation assistant | meta, development |

## Community Skills - michalparkola

Repository: `https://github.com/michalparkola/tapestry-skills-for-claude-code`
Path prefix: (root level)

| Skill | Description | Tags |
|-------|-------------|------|
| youtube-transcript | YouTube transcript extraction | youtube, video, research |
| article-extractor | Web article extraction | research, web, content |

## Community Skills - kkoppenhaver (Nano Banana)

Repository: `https://github.com/kkoppenhaver/cc-nano-banana`
Path prefix: (root level, single skill)

| Skill | Description | Tags |
|-------|-------------|------|
| nano-banana | AI image generation using Gemini CLI (Nano Banana Pro) | image, ai, creative, design |

## Skillhub Collection

Repository: `https://github.com/keyuyuan/skillhub-awesome-skills`
Website: `https://www.skillhub.club`

A curated collection of **1000+ skills** across 18 categories:
- Development (311 skills)
- DevOps (90 skills)
- Productivity (82 skills)
- Testing (76 skills)
- And more...

Browse the website for the full catalog.

## Workflow-Specific Recommendations

### Media Creator / Content Creator Workflow
- `content-research-writer` - Research and writing
- `social-repurposer` - Multi-platform content
- `canvas-design` - Visual design
- `web-asset-generator` - Social media images
- `twitter-reader` - Social media research
- `youtube-transcript` - Video research
- `article-extractor` - Web research
- `docx` - Document export
- `pdf` - PDF export
- `pptx` - Presentation creation

### Marketing Professional Workflow
- `seo-optimizer` - SEO optimization
- `linkedin-post-optimizer` - LinkedIn optimization
- `social-repurposer` - Content adaptation
- `landing-page-copywriter` - Landing pages
- `email-template-generator` - Email marketing
- `cold-email-sequence-generator` - Sales emails
- `content-research-writer` - Research
- `web-asset-generator` - Marketing assets

### Developer Workflow
- `code-review-pro` - Code review
- `api-documentation-writer` - API docs
- `technical-writer` - Technical docs
- `database-schema-designer` - DB design
- `screenshot-to-code` - Design to code
- `regex-debugger` - Regex tools
- `mermaid-tools` - Diagrams
- `frontend-design` - Frontend development

### Researcher Workflow
- `content-research-writer` - Research writing
- `fact-checker` - Fact verification
- `article-extractor` - Web research
- `youtube-transcript` - Video research
- `pdf` - PDF processing
- `docx` - Document processing

### Podcast / Video Creator Workflow
- `podcast-content-suite` - Podcast content
- `youtube-transcript` - Transcript extraction
- `youtube-downloader` - Video download
- `webinar-content-repurposer` - Webinar content
- `social-repurposer` - Content adaptation
- `canvas-design` - Cover art

## Dynamic Search Fallback

When skills are not found in the curated list, search GitHub with:

```
"claude" "skills" "SKILL.md" <topic> site:github.com
```

Validate downloaded skills by checking:
1. SKILL.md exists with valid YAML frontmatter
2. Has `name` and `description` fields
3. No obvious security issues in scripts
