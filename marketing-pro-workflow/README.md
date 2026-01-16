# Marketing Pro Workflow

Claude Code workflow for digital marketers, growth hackers, and marketing teams.

[中文文档](./README_cn.md)

## Target Users

- Digital Marketers
- Growth Marketers & Demand Gen
- Product Marketing Managers (PMM)
- Social Media Managers
- SEO Specialists
- Paid Media Specialists

## Installed Skills (18)

### Strategy & Research
| Skill | Function | Trigger Example |
|-------|----------|-----------------|
| marketing-strategy-pmm | Product marketing, positioning, GTM, ICP definition, competitive battlecards | "Create positioning for [product]" |
| marketing-demand-acquisition | Multi-channel demand gen, paid media optimization, SEO strategy, CAC calculator | "Plan demand gen campaign" |
| buyer-persona-generator | Create detailed buyer personas and ICP | "Create buyer persona for [role]" |
| competitive-ads-extractor | Extract and analyze competitor ads from ad libraries | "Analyze competitor ads for [company]" |
| lead-research-assistant | Identify and qualify leads for your product | "Find 10 leads for [product]" |

### SEO & Content
| Skill | Function | Trigger Example |
|-------|----------|-----------------|
| seo-optimizer | SEO content optimization | "Optimize this article for SEO" |
| content-optimizer | On-page SEO, keyword density, meta tags | "Check keyword density" |
| serp-analysis | SERP analysis and competitor intelligence | "Analyze SERP for [keyword]" |
| keyword-cluster-builder | Keyword expansion and clustering | "Build keyword cluster for [topic]" |
| content-brief | SEO content planning briefs | "Create a content brief" |

### Advertising & Campaigns
| Skill | Function | Trigger Example |
|-------|----------|-----------------|
| ad-copy-generator | Generate ad copy for Google, Meta, LinkedIn, TikTok | "Create 5 Google Ads variations" |
| landing-page-copywriter | Landing page copy with AIDA framework | "Write landing page copy" |
| email-template-generator | Email marketing templates and sequences | "Generate email sequence" |
| utm-builder | Generate UTM-tagged URLs for campaign tracking | "Create UTM links for campaign" |

### Social Media
| Skill | Function | Trigger Example |
|-------|----------|-----------------|
| linkedin-post-optimizer | LinkedIn post optimization | "Optimize LinkedIn post" |
| social-repurposer | Cross-platform content conversion | "Convert to all platform formats" |
| social-media-analyzer | Analyze campaign performance, engagement, ROI | "Analyze this campaign data" |

### Analytics
| Skill | Function | Trigger Example |
|-------|----------|-----------------|
| analytics-interpretation | GA4/GSC data interpretation | "Interpret this analytics data" |

## Quick Start

```bash
cd marketing-pro-workflow
# Launch Claude Code - skills activate automatically
```

## Automated Marketing Workflows

### 1. Complete GTM Strategy
```
1. "Create ICP and 3 buyer personas for [product]"
2. "Develop positioning using April Dunford method"
3. "Create competitive battlecards for [competitors]"
4. "Plan 90-day GTM launch"
```

### 2. Full-Funnel Campaign
```
1. "Plan demand gen campaign for [product]"
2. "Generate ad copy for Google and LinkedIn"
3. "Create UTM links for all channels"
4. "Write email nurture sequence (5 emails)"
5. "Create landing page copy"
```

### 3. SEO Content Strategy
```
1. "Build keyword cluster for [topic]"
2. "Analyze SERP for [primary keyword]"
3. "Create content brief based on analysis"
4. "Use content-optimizer to check SEO requirements"
```

### 4. Competitive Intelligence
```
1. "Analyze competitor ads for [company]"
2. "Create competitive battlecard"
3. "Identify gaps in competitor messaging"
4. "Generate differentiated ad copy"
```

### 5. Lead Generation Campaign
```
1. "Find 20 qualified leads matching our ICP"
2. "Create personalized outreach messages"
3. "Generate LinkedIn ad campaign targeting this segment"
4. "Create UTM tracking for all touchpoints"
```

### 6. Performance Analysis
```
1. "Analyze this GA4 campaign data"
2. "Calculate CAC by channel"
3. "Interpret social media engagement metrics"
4. "Provide optimization recommendations"
```

## Skill Combinations

- **Product Launch**: buyer-persona-generator → marketing-strategy-pmm → ad-copy-generator → landing-page-copywriter → email-template-generator
- **ABM Campaign**: lead-research-assistant → buyer-persona-generator → ad-copy-generator → linkedin-post-optimizer
- **SEO Campaign**: keyword-cluster-builder → serp-analysis → content-brief → content-optimizer
- **Paid Media Optimization**: competitive-ads-extractor → ad-copy-generator → utm-builder → analytics-interpretation
- **Brand Awareness**: marketing-strategy-pmm → ad-copy-generator → social-repurposer → social-media-analyzer

## Output Standards

- **Positioning**: April Dunford framework, competitive alternatives mapped
- **Personas**: Full demographic, psychographic, and behavioral profiles
- **Ad Copy**: Platform-specific formats with character count validation
- **Email Sequences**: 3-5 emails, progressive engagement model
- **UTM Links**: Consistent naming convention, documented in spreadsheet
- **Reports**: Actionable insights with specific recommendations

## Multi-AI Tool Support

This workflow supports:
- Claude Code (`.claude/skills/`)
- Codex (`.codex/skills/`)
- Cursor (`.cursor/skills/`)
- OpenCode (`.opencode/skill/`)

## License

MIT
