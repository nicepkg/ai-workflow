# SEO Optimization

Comprehensive guide to search engine optimization covering technical SEO, on-page optimization, content strategy, and link building aligned with Google's 2025 ranking factors.

## Contents

- [Core Ranking Factors](#core-ranking-factors)
- [Technical SEO](#technical-seo)
- [Social Media Preview Optimization](#social-media-preview-optimization)
- [On-Page SEO](#on-page-seo)
- [Content SEO](#content-seo)
- [Accessibility for SEO](#accessibility-for-seo)
- [E-E-A-T Guidelines](#e-e-a-t-guidelines)
- [Link Building](#link-building)
- [SEO Audit Checklist](#seo-audit-checklist)

---

## Core Ranking Factors

Google's algorithm prioritizes these factors in 2025:

### Factor Priority Matrix

| Factor | Priority | Impact |
|--------|----------|--------|
| High-quality, helpful content | Critical | Direct ranking signal |
| Relevance & intent matching | Critical | Determines visibility |
| Links & authority | High | Trust and discovery signal |
| Technical accessibility | High | Crawling and indexing |
| Page experience (Core Web Vitals) | Medium | User experience signal |
| Mobile-first design | Medium | Required for indexing |
| Structured data | Medium | Rich results eligibility |

### Intent Types

| Intent Type | User Goal | Content Format |
|-------------|-----------|----------------|
| Informational | Learn something | Guides, tutorials, definitions |
| Commercial | Research before buying | Comparisons, reviews, lists |
| Transactional | Complete an action | Product pages, checkout, signup |
| Navigational | Find specific site/page | Brand pages, login, support |

---

## Technical SEO

Ensure your site is crawlable, indexable, fast, and machine-readable.

### Crawlability & Indexation

| Element | Best Practice | Tool to Verify |
|---------|---------------|----------------|
| XML Sitemap | Submit to Google Search Console | GSC Sitemaps |
| Robots.txt | Don't block important content | GSC URL Inspection |
| Internal linking | Logical hierarchy, all pages reachable | Screaming Frog |
| Canonical tags | One canonical per page, self-referencing | Site audit tools |
| HTTP status | Fix 4xx/5xx errors, proper redirects | Log file analysis |

### Robots.txt Template

```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /private/
Disallow: /*?*utm_

Sitemap: https://example.com/sitemap.xml
```

### Core Web Vitals Targets

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP (Largest Contentful Paint) | ≤2.5s | 2.5-4s | >4s |
| INP (Interaction to Next Paint) | ≤200ms | 200-500ms | >500ms |
| CLS (Cumulative Layout Shift) | ≤0.1 | 0.1-0.25 | >0.25 |

### Performance Optimization

| Issue | Solution |
|-------|----------|
| Slow LCP | Optimize hero images, preload critical resources |
| High CLS | Set dimensions on images/embeds, reserve ad space |
| Poor INP | Reduce main-thread blocking JS, defer non-critical scripts |
| Large page size | Compress images (WebP/AVIF), minify CSS/JS |
| Render blocking | Inline critical CSS, defer non-critical JS |

### Mobile-First Checklist

- [ ] Responsive design (no horizontal scroll)
- [ ] Readable font sizes (16px+ base)
- [ ] Tap targets ≥48px with adequate spacing
- [ ] No intrusive interstitials
- [ ] Same content on mobile and desktop
- [ ] Fast mobile load time (<3s)

### Structured Data Types

| Schema Type | Use Case | Rich Result |
|-------------|----------|-------------|
| Article | Blog posts, news | Article carousel |
| Product | E-commerce products | Price, availability, reviews |
| FAQPage | Q&A content | FAQ accordion in SERP |
| HowTo | Step-by-step guides | Step carousel |
| LocalBusiness | Physical locations | Local pack, knowledge panel |
| BreadcrumbList | Site navigation | Breadcrumb trail in SERP |
| Review | Product/service reviews | Star ratings |
| VideoObject | Video content | Video thumbnails |

### Schema Validation

```bash
# Test your structured data
# Google Rich Results Test: https://search.google.com/test/rich-results
# Schema Markup Validator: https://validator.schema.org/
```

### Social Media Preview Optimization

Proper Open Graph and Twitter Card meta tags ensure content displays correctly when shared.

#### Image Dimensions by Platform

| Platform | Recommended Size | Aspect Ratio | Notes |
|----------|------------------|--------------|-------|
| Facebook | 1200 × 630 px | 1.91:1 | Standard og:image |
| LinkedIn | 1200 × 627 px | 1.91:1 | Custom URL preview |
| WhatsApp | 1200 × 630 px | 1.91:1 | Uses Open Graph |
| Twitter/X | 1200 × 628 px | 1.91:1 | summary_large_image |
| Instagram Feed | 1080 × 1350 px | 4:5 | Vertical preferred |
| Instagram Stories | 1080 × 1920 px | 9:16 | Full screen mobile |

#### Required Meta Tags

```html
<!-- Open Graph (Facebook, LinkedIn, WhatsApp) -->
<meta property="og:title" content="Your Page Title" />
<meta property="og:description" content="Compelling description under 160 chars" />
<meta property="og:image" content="https://example.com/image-1200x630.jpg" />
<meta property="og:url" content="https://example.com/page" />
<meta property="og:type" content="article" />

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Your Page Title" />
<meta name="twitter:description" content="Compelling description" />
<meta name="twitter:image" content="https://example.com/image-1200x628.jpg" />
```

#### Social Preview Checklist

- [ ] og:image is 1200×630px minimum
- [ ] Image uses absolute URL (https://...)
- [ ] og:title is under 60 characters
- [ ] og:description is under 160 characters
- [ ] No text in safe zone margins (keep text centered)
- [ ] Test with platform validators

#### Validation Tools

- [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/)
- [Twitter Card Validator](https://cards-dev.twitter.com/validator)
- [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/)

---

## On-Page SEO

Optimize individual pages for target keywords and user intent.

### Title Tag Guidelines

| Element | Best Practice |
|---------|---------------|
| Length | 50-60 characters (display limit) |
| Primary keyword | Include near the beginning |
| Brand | Add at end if space permits |
| Uniqueness | Each page needs unique title |
| Intent | Match search intent |

**Examples:**
```
Good: "How to Create UTM Parameters for Campaign Tracking | Guide"
Bad: "UTM Parameters" (too short, no context)
Bad: "The Ultimate Complete Comprehensive Guide to UTM Parameters" (keyword stuffing)
```

### Meta Description Guidelines

| Element | Best Practice |
|---------|---------------|
| Length | 150-160 characters |
| Call to action | Include compelling reason to click |
| Primary keyword | Include naturally |
| Uniqueness | Each page needs unique description |

**Note:** Meta descriptions don't directly affect rankings but impact CTR.

### Header Hierarchy

```
H1: Primary topic (one per page)
├── H2: Major section
│   ├── H3: Subsection
│   │   └── H4: Detail
│   └── H3: Subsection
├── H2: Major section
└── H2: Major section
```

### URL Structure

| Rule | Example |
|------|---------|
| Short and descriptive | `/utm-tracking-guide` |
| Lowercase | `/marketing-campaign` not `/Marketing-Campaign` |
| Hyphens for spaces | `/content-strategy` not `/content_strategy` |
| No parameters when possible | `/products/shoes` not `/products?id=123` |
| Keyword inclusion | `/email-marketing-sequences` |

### Image Optimization

| Element | Best Practice |
|---------|---------------|
| File name | `utm-parameter-structure.webp` not `IMG_1234.jpg` |
| Alt text | Descriptive, include keyword naturally |
| Format | WebP or AVIF for web, PNG for transparency |
| Compression | Balance quality vs. file size |
| Dimensions | Serve correct size for viewport |
| Lazy loading | Defer below-the-fold images |

**Alt text examples:**
```
Good: "Diagram showing the five UTM parameters and their purposes"
Bad: "image1" or "utm parameters marketing tracking campaign"
```

### Internal Linking Strategy

| Principle | Implementation |
|-----------|----------------|
| Contextual relevance | Link where naturally helpful |
| Descriptive anchors | "content strategy guide" not "click here" |
| Pillar-cluster model | Pillars link to clusters, clusters link back |
| Flat architecture | Important pages within 3 clicks of homepage |
| Link equity flow | Point links to priority pages |

---

## Content SEO

Create content that satisfies search intent and demonstrates expertise.

### Content Quality Criteria

| Factor | Description |
|--------|-------------|
| Helpful | Directly answers the search query |
| Original | Unique insights, not rehashed content |
| Comprehensive | Covers topic thoroughly |
| Accurate | Factually correct, well-researched |
| Up-to-date | Current information, recent examples |
| Well-structured | Scannable with clear hierarchy |

### Topic Cluster Model

**Pillar Page:**
- 2,500-5,000+ words
- Comprehensive overview of core topic
- Links to 8-20 cluster articles
- Updated quarterly

**Cluster Articles:**
- 1,000-2,000 words
- Single subtopic focus
- Links back to pillar
- Cross-links to related clusters

### Content Depth by Intent

| Intent | Content Approach |
|--------|------------------|
| Informational | Comprehensive guides, step-by-step tutorials |
| Commercial | Comparison tables, pros/cons, buyer guides |
| Transactional | Clear CTAs, trust signals, urgency |
| Navigational | Clean landing pages, clear branding |

### Featured Snippet Optimization

| Snippet Type | Format |
|--------------|--------|
| Paragraph | 40-60 word concise answer |
| List | Numbered/bulleted steps |
| Table | Comparison or data |
| Video | Embedded with chapters |

**Optimization tactics:**
- Use question headings (H2/H3)
- Provide immediate, concise answers
- Follow with detailed explanation
- Use tables for comparisons
- Include numbered steps for processes

### Content Refresh Strategy

| Timeframe | Action |
|-----------|--------|
| Weekly | Check for broken links |
| Monthly | Review traffic trends |
| Quarterly | Update statistics, examples |
| Annually | Major content refresh or consolidation |

---

## Accessibility for SEO

Accessibility improvements directly impact SEO through better crawlability, semantic structure, and page experience signals.

### Why Accessibility Matters for SEO

| Factor | SEO Impact |
|--------|------------|
| Semantic HTML | Helps crawlers understand content hierarchy |
| Alt text | Enables image search visibility |
| Heading structure | Reinforces content relevance signals |
| Keyboard navigation | Improves page experience metrics |
| Fast load times | Core Web Vitals improvement |
| Mobile accessibility | Required for mobile-first indexing |

### WCAG 2.1 AA Checklist (SEO-Relevant)

#### Perceivable

- [ ] All images have descriptive alt text (or alt="" for decorative)
- [ ] Videos have captions and transcripts
- [ ] Color contrast ratio ≥4.5:1 for text
- [ ] Text can be resized to 200% without loss of content
- [ ] No content relies solely on color to convey meaning

#### Operable

- [ ] All functionality available via keyboard
- [ ] No keyboard traps (users can navigate away)
- [ ] Skip navigation links for screen readers
- [ ] Focus indicators visible on interactive elements
- [ ] No content flashes more than 3 times per second

#### Understandable

- [ ] Page language declared (`<html lang="en">`)
- [ ] Form inputs have associated labels
- [ ] Error messages identify the field and describe the error
- [ ] Consistent navigation across pages

#### Robust

- [ ] Valid HTML (passes W3C validation)
- [ ] ARIA attributes used correctly
- [ ] Custom components have appropriate roles

### Semantic HTML for SEO

```html
<!-- Good: Semantic structure -->
<header>
  <nav aria-label="Main navigation">...</nav>
</header>
<main>
  <article>
    <h1>Primary Topic</h1>
    <section>
      <h2>Subtopic</h2>
      <p>Content...</p>
    </section>
  </article>
  <aside aria-label="Related content">...</aside>
</main>
<footer>...</footer>

<!-- Bad: Non-semantic structure -->
<div class="header">
  <div class="nav">...</div>
</div>
<div class="content">
  <div class="title">Primary Topic</div>
  <div class="section">...</div>
</div>
```

### ARIA Labels for Navigation

```html
<!-- Help screen readers and crawlers understand navigation -->
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/products">Products</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>

<nav aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/products">Products</a></li>
    <li aria-current="page">Widget</li>
  </ol>
</nav>
```

### Accessibility Testing Tools

| Tool | Purpose |
|------|---------|
| [WAVE](https://wave.webaim.org/) | Visual accessibility checker |
| [axe DevTools](https://www.deque.com/axe/) | Browser extension for WCAG testing |
| [Lighthouse](https://developers.google.com/web/tools/lighthouse) | Accessibility score in Chrome DevTools |
| [Pa11y](https://pa11y.org/) | CLI accessibility testing |
| [NVDA](https://www.nvaccess.org/) | Free screen reader for testing |

---

## E-E-A-T Guidelines

Demonstrate Experience, Expertise, Authoritativeness, and Trustworthiness.

### E-E-A-T Components

| Component | Definition | How to Demonstrate |
|-----------|------------|--------------------|
| Experience | First-hand experience with topic | Personal examples, case studies, original research |
| Expertise | Knowledge and skill in the field | Credentials, depth of content, technical accuracy |
| Authoritativeness | Recognition as a go-to source | Industry mentions, backlinks, author profiles |
| Trustworthiness | Accuracy and honesty | Citations, transparency, contact info |

### Implementation Tactics

**Author Signals:**
- Detailed author bios with credentials
- Links to author's social profiles
- Author schema markup
- Multiple articles by same author

**Author Bio Format (GEO-Optimized):**
```markdown
**Author**: Dr. Sarah Johnson, MD, PhD, FAAD
**Affiliation**: Stanford School of Medicine
**Published**: 2025-01-15 | **Updated**: 2025-06-10
```

**Person Schema:**
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Dr. Sarah Johnson",
  "jobTitle": "Chief Medical Officer",
  "affiliation": {
    "@type": "Organization",
    "name": "Stanford School of Medicine"
  },
  "sameAs": [
    "https://linkedin.com/in/sarahjohnsonmd",
    "https://scholar.google.com/citations?user=xyz"
  ]
}
```

**Content Signals:**
- Cite primary sources for claims
- Link to authoritative external sources
- Include original data/research
- Show publication and update dates

**Site Signals:**
- Clear about page with company info
- Accessible contact information
- Privacy policy and terms
- HTTPS and security badges
- Customer reviews and testimonials

### YMYL Considerations

"Your Money or Your Life" topics require higher E-E-A-T standards:
- Health and medical
- Financial advice
- Legal information
- News and current events
- Safety information

---

## Link Building

Earn authoritative links through quality content and outreach.

### Link Quality Factors

| Factor | High Quality | Low Quality |
|--------|--------------|-------------|
| Relevance | Topically related site | Random, unrelated site |
| Authority | High DR/DA, trusted domain | Low authority, spammy |
| Placement | In-content, editorial | Footer, sidebar, directory |
| Anchor text | Natural, varied | Exact match, manipulative |
| Context | Natural recommendation | Paid, forced, exchanged |

### Legitimate Link Building Tactics

| Tactic | Description | Effort |
|--------|-------------|--------|
| Content marketing | Create link-worthy assets | High |
| Digital PR | Newsworthy announcements, research | High |
| Guest contributions | Quality posts on relevant sites | Medium |
| Broken link building | Replace dead links with your content | Medium |
| Resource page outreach | Get listed on curated lists | Low |
| HARO/Expert quotes | Respond to journalist queries | Low |

### Link-Worthy Content Types

| Type | Example |
|------|---------|
| Original research | Survey data, industry studies |
| Tools/calculators | Free utilities solving problems |
| Comprehensive guides | "Ultimate guide to..." |
| Data visualizations | Infographics with original data |
| Templates | Downloadable resources |
| Expert roundups | Curated industry insights |

### What to Avoid

- Paid links (unless nofollow)
- Private blog networks (PBNs)
- Link exchanges at scale
- Low-quality guest posting
- Automated link building
- Comment/forum spam

---

## SEO Audit Checklist

### Technical Audit

- [ ] Site loads under 3 seconds
- [ ] Core Web Vitals pass
- [ ] Mobile-friendly (responsive)
- [ ] HTTPS enabled
- [ ] XML sitemap submitted
- [ ] Robots.txt configured correctly
- [ ] No crawl errors in GSC
- [ ] No duplicate content issues
- [ ] Canonical tags implemented
- [ ] Structured data validated
- [ ] Internal linking healthy
- [ ] 404 errors fixed

### On-Page Audit

- [ ] Unique title tags (50-60 chars)
- [ ] Unique meta descriptions (150-160 chars)
- [ ] One H1 per page
- [ ] Logical header hierarchy
- [ ] Keyword in URL, title, H1
- [ ] Images have alt text
- [ ] Images optimized (WebP, compressed)
- [ ] Internal links with descriptive anchors
- [ ] External links to authoritative sources
- [ ] Content matches search intent

### Content Audit

- [ ] Content is comprehensive for topic
- [ ] Content is up-to-date
- [ ] Author information displayed
- [ ] Sources cited where appropriate
- [ ] No thin or duplicate pages
- [ ] Featured snippet opportunities addressed
- [ ] FAQ content for relevant queries
- [ ] Topic clusters organized

### Authority Audit

- [ ] Quality backlink profile
- [ ] No toxic links (disavow if needed)
- [ ] Author bios with credentials
- [ ] About page with company info
- [ ] Contact information accessible
- [ ] Trust signals visible
- [ ] Reviews and testimonials

---

## Quick Reference

### SEO Priority by Site Type

| Site Type | Top Priorities |
|-----------|----------------|
| E-commerce | Product schema, page speed, mobile UX |
| SaaS | Feature pages, comparison content, technical SEO |
| Local business | Google Business Profile, local schema, reviews |
| Publisher | Core Web Vitals, article schema, E-E-A-T |
| B2B | Thought leadership, case studies, long-form content |

### Monthly SEO Tasks

| Task | Frequency |
|------|-----------|
| Check GSC for errors | Weekly |
| Review keyword rankings | Weekly |
| Monitor Core Web Vitals | Monthly |
| Audit new content | Monthly |
| Review backlink profile | Monthly |
| Update top-performing content | Quarterly |
| Comprehensive site audit | Quarterly |
| Competitor analysis | Quarterly |

### Authoritative Resources

- [Google Search Central](https://developers.google.com/search) - Official documentation
- [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Moz Beginner's Guide to SEO](https://moz.com/beginners-guide-to-seo)
- [Ahrefs SEO Learning Hub](https://ahrefs.com/seo)
- [Backlinko SEO Strategy Guide](https://backlinko.com/seo-strategy)
- [Search Engine Journal](https://www.searchenginejournal.com/)
