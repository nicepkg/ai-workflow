---
name: running-marketing-campaigns
description: >
  Plans, creates, and optimizes digital marketing campaigns including content
  strategy, social media, email marketing, SEO, and AI visibility (GEO). Generates UTM
  parameters and tracking URLs. Helps develop go-to-market strategies,
  campaign messaging, content calendars, and performance measurement frameworks.
  Use when asked to "create a marketing campaign", "plan content strategy",
  "build email sequences", "set up UTM tracking", "analyze marketing metrics",
  "launch a product", "optimize for SEO", "improve AI visibility", "optimize for voice search",
  "set up IndexNow", "check accessibility for SEO", or "create social media previews".
  Supports both marketing beginners and experienced marketers needing templates.
license: MIT
metadata:
  version: 1.3.0
  domains: [content, social, email, analytics, gtm, brand, seo, geo, voice-search, accessibility]
  author: Claude Skills
---

# Marketing Campaign Execution

Plan, execute, and measure digital marketing campaigns across content, social, email, and analytics.

## Contents

- [Quick Start](#quick-start)
- [Domain Reference Guide](#domain-reference-guide)
- [Scripts](#scripts)
- [Workflow Decision Tree](#workflow-decision-tree)
- [Multi-Domain Queries](#multi-domain-queries)
- [Campaign Validation Checklist](#campaign-validation-checklist)
- [Persona Adaptation](#persona-adaptation)
- [Boundaries](#boundaries)

## Quick Start

### Generate UTM Parameters
```
Source: where traffic originates (google, facebook, newsletter)
Medium: how it arrives (cpc, email, social, organic)
Campaign: initiative name (spring-sale-2025, product-launch)

Format: lowercase, hyphens, no spaces
Input: "Spring Sale 2025" → Output: "spring-sale-2025"
Input: "Q1 Launch Campaign" → Output: "q1-launch-campaign"

Example: ?utm_source=linkedin&utm_medium=social&utm_campaign=q1-launch
```

### Create Email Sequence
1. Welcome (immediate): Set expectations, deliver promised value
2. Value (day 2-3): Best content or quick win
3. Engagement (day 5-7): Encourage reply or action
4. Offer (day 10): Clear CTA with incentive

### Plan Content Calendar
Essential fields: Title, Target keyword, Funnel stage (TOFU/MOFU/BOFU), Format, Owner, Publish date, Distribution channels.

### Check Campaign Performance
Primary metrics by channel:
- Email: Open rate (43% avg), CTR (2% avg), Conversion rate
- Social: Engagement rate, Reach, Click-through
- Paid: ROAS, CPA, CTR
- Content: Traffic, Time on page, Conversions

## Domain Reference Guide

| Need | Reference | When to Load |
|------|-----------|--------------|
| Plan content strategy | [content-strategy.md](references/content-strategy.md) | Topic clusters, calendars, funnel mapping, repurposing |
| Execute social media | [social-media.md](references/social-media.md) | Platform tactics, posting times, engagement benchmarks |
| Build email campaigns | [email-marketing.md](references/email-marketing.md) | Sequences, subject lines, segmentation, deliverability |
| Track campaigns | [utm-tracking.md](references/utm-tracking.md) | UTM formatting, naming conventions, GA4 alignment |
| Measure performance | [analytics-measurement.md](references/analytics-measurement.md) | KPIs, GA4 setup, attribution, ROI calculations |
| Launch products | [gtm-tools.md](references/gtm-tools.md) | GTM frameworks, positioning, tool selection |
| Define brand voice | [brand-guidelines.md](references/brand-guidelines.md) | Voice dimensions, tone, messaging framework, terminology |
| Optimize for search | [seo-optimization.md](references/seo-optimization.md) | Technical SEO, on-page, content SEO, link building, E-E-A-T |
| Optimize for AI | [geo-optimization.md](references/geo-optimization.md) | GEO, LLMO, AEO, AI Overviews, chatbot visibility |

## Scripts

Python utilities for campaign automation:

| Script | Purpose | Usage |
|--------|---------|-------|
| [utm_tools.py](scripts/utm_tools.py) | UTM generation, validation, batch processing, QR codes | `python utm_tools.py generate --source facebook --medium paid-social --campaign q1-launch` |
| [brand_checker.py](scripts/brand_checker.py) | Brand voice compliance, readability scoring, banned words | `python brand_checker.py check --file copy.txt` |

### Script Quick Reference

**Generate and validate UTMs:**
```bash
# Generate UTM parameters
python scripts/utm_tools.py generate -s facebook -m paid-social -c spring-2025

# Build complete tracking URL
python scripts/utm_tools.py build -u https://example.com -s email -m newsletter -c q1-launch

# Validate existing URL
python scripts/utm_tools.py validate -u "https://example.com?utm_source=email&utm_medium=cpc"

# Batch process from CSV
python scripts/utm_tools.py batch -f campaigns.csv -u https://example.com -o tracking.csv

# Check GA4 channel mapping
python scripts/utm_tools.py ga4-check -s facebook -m paid-social
```

**Check brand compliance:**
```bash
# Full compliance check
python scripts/brand_checker.py check --file marketing_copy.txt

# Check readability score
python scripts/brand_checker.py readability --text "Your marketing copy here"

# Find banned words
python scripts/brand_checker.py banned --file email_draft.txt

# Full audit with JSON output
python scripts/brand_checker.py full-audit --file campaign.txt --output report.json
```

## Workflow Decision Tree

**What does the user need?**

```
Creating or planning content?
├─ Yes → content-strategy.md
│        • Topic clusters, pillar pages
│        • Content calendars (annual/quarterly/weekly)
│        • TOFU/MOFU/BOFU mapping
│        • Repurposing workflows
└─ No ↓

Platform-specific social guidance?
├─ Yes → social-media.md
│        • Instagram, LinkedIn, TikTok, X, Facebook
│        • Posting cadence and timing
│        • Algorithm priorities
│        • Engagement benchmarks
└─ No ↓

Email campaigns or sequences?
├─ Yes → email-marketing.md
│        • Welcome, drip, re-engagement sequences
│        • Subject line optimization
│        • Segmentation strategies
│        • Deliverability requirements
└─ No ↓

UTM parameters or tracking URLs?
├─ Yes → utm-tracking.md + scripts/utm_tools.py
│        • Parameter formatting rules
│        • Naming conventions
│        • GA4 channel alignment
│        • Dynamic parameters for ads
│        • Batch URL generation
└─ No ↓

Analytics, metrics, or reporting?
├─ Yes → analytics-measurement.md
│        • KPIs by channel
│        • GA4 configuration checklist
│        • Attribution models
│        • ROI formulas
└─ No ↓

Product launch or go-to-market?
├─ Yes → gtm-tools.md
│        • SOSTAC, RACE, AARRR frameworks
│        • Launch campaign structure
│        • Positioning methodology
│        • Marketing tool selection
└─ No ↓

Brand voice, tone, or messaging?
├─ Yes → brand-guidelines.md + scripts/brand_checker.py
│        • Voice dimension matrix
│        • This-but-not-that chart
│        • Messaging framework
│        • Terminology standards
│        • Compliance checking
└─ No ↓

SEO or search engine optimization?
├─ Yes → seo-optimization.md
│        • Technical SEO (crawling, indexing, speed)
│        • On-page SEO (titles, headers, content)
│        • Content SEO (E-E-A-T, topic clusters)
│        • Link building strategies
│        • Core Web Vitals
└─ No ↓

AI visibility, GEO, or chatbot optimization?
├─ Yes → geo-optimization.md
│        • Generative Engine Optimization (GEO)
│        • LLMO (Large Language Model Optimization)
│        • AEO (Answer Engine Optimization)
│        • ChatGPT, Perplexity, AI Overviews visibility
│        • Content structure for AI citation
└─ No → Clarify the specific marketing need
```

## Multi-Domain Loading Order

For requests spanning multiple domains, load references in priority order:

| Request Type | Primary | Secondary | Supporting |
|--------------|---------|-----------|------------|
| Product launch | gtm-tools.md | brand-guidelines.md, content-strategy.md | email-marketing.md, social-media.md |
| Campaign tracking | utm-tracking.md | analytics-measurement.md | — |
| Quarterly plan | content-strategy.md | social-media.md, email-marketing.md | analytics-measurement.md |
| Performance optimization | analytics-measurement.md | (channel-specific) | — |
| Brand voice | brand-guidelines.md | brand_checker.py | — |
| Search rankings | seo-optimization.md | content-strategy.md | analytics-measurement.md |
| AI visibility | geo-optimization.md | seo-optimization.md | content-strategy.md |
| Full strategy | seo-optimization.md, geo-optimization.md | content-strategy.md, social-media.md | email-marketing.md, analytics-measurement.md |

## Campaign Validation Checklist

Before launching any campaign, verify:

### Strategy
- [ ] Target audience clearly defined
- [ ] Campaign goals documented with baseline metrics
- [ ] Success criteria established (KPIs + targets)
- [ ] Timeline and milestones set

### Tracking
- [ ] UTM parameters validated (lowercase, hyphens, no spaces)
- [ ] GA4 channel alignment confirmed
- [ ] Conversion tracking tested
- [ ] Attribution model selected

### Content
- [ ] Brand voice checklist completed
- [ ] No banned words or unsubstantiated claims
- [ ] Readability score acceptable (60+ Flesch)
- [ ] CTA clear and actionable

### Technical
- [ ] Email sequences tested in preview
- [ ] Links verified working
- [ ] Mobile responsiveness checked
- [ ] Analytics tracking confirmed

## Persona Adaptation

**Beginner signals:** Asks "what is," "how do I," "why should I," unfamiliar terminology, requests explanations.
→ Provide concept context before tactics. Explain frameworks. Offer templates.

**Experienced signals:** Uses correct terminology, asks for benchmarks, requests templates, mentions specific tools.
→ Skip fundamentals. Provide benchmarks, templates, advanced tactics directly.

## Boundaries

**In scope:**
- Campaign strategy and planning
- Content calendars and topic clusters
- Social media tactics and scheduling guidance
- Email sequences and copy frameworks
- UTM parameter generation and governance
- Marketing analytics and KPI frameworks
- Go-to-market planning and positioning
- Marketing tool recommendations
- Brand voice and messaging frameworks
- Copy compliance checking
- SEO optimization (technical, on-page, content, E-E-A-T)
- GEO/AI visibility optimization (ChatGPT, Perplexity, AI Overviews)

**Out of scope (suggest alternatives):**
- Paid ad campaign management (bid strategies, audience targeting)
- CRM workflow implementation
- Website design/development
- Brand identity design (logos, colors, visual design)
- PR and media relations
- General copywriting (not campaign-specific)

**Clarify before proceeding:**
- "Help with marketing" → Which domain?
- "Improve my ads" → Creative/copy (in scope) or campaign management (out of scope)?
- "Analytics setup" → Marketing analytics or general web analytics?
- "Brand guidelines" → Voice/messaging (in scope) or visual identity (out of scope)?
