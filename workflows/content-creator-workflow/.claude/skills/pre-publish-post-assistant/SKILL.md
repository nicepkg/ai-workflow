---
name: pre-publish-post-assistant
description: Pre-publish assistant for new blog posts. Use when the user wants to classify a new post with categories and tags, generate SEO metadata (title, description, focus keyphrase), or get intelligent suggestions with rationale. Works with draft content (file path, URL, or text) and suggests from existing taxonomy to maintain balanced distribution.
---

# Pre-publish Post Assistant Skill

## Purpose

This skill helps prepare blog posts for publication by providing intelligent suggestions for:

1. **Categories** - From existing site categories, with distribution awareness
2. **Tags** - From existing tags, avoiding tag pollution
3. **SEO Metadata** - Title, meta description, and focus keyphrase

All suggestions include rationale explaining the reasoning.

## When to Use This Skill

- User says "classify this post" or "suggest categories/tags"
- User asks to "prepare this post for publishing"
- User wants "SEO suggestions" for a draft
- User provides a draft post and asks for taxonomy suggestions
- User mentions "new blog post" and needs categorization help

## Key Principles

### Category Selection
- **Limit to 1-2 categories** per post (primary + optional secondary)
- Prefer categories with moderate post counts (avoid over/under-populated)
- Match content theme, not just keywords
- Consider category hierarchy if applicable

### Tag Selection
- **Limit to 3-5 tags** per post
- Only use existing tags (no new tag creation unless explicitly requested)
- Avoid tag pollution (tags with only 1-2 posts are low value)
- Prefer tags that group related content meaningfully
- Consider tag search potential

### SEO Metadata
- **Title**: 50-60 characters, include primary keyword, compelling
- **Meta Description**: 150-160 characters, summarize value proposition, include CTA
- **Focus Keyphrase**: 2-4 words, searchable, relevant to content

## Input Formats

The skill accepts draft content in multiple formats:

```
# File path
"Classify this post: /path/to/draft.md"

# URL (for already-published posts needing optimization)
"Suggest tags for https://example.com/my-post/"

# Inline text
"Here's my draft: [content]... What categories fit?"
```

## Data Sources

### Categories and Tags
Can be retrieved from:
1. **WordPress GraphQL** - Live data from WP
2. **Static dist folder** - Parse from built site (`/category/`, `/tag/` pages)
3. **Cached taxonomy file** - Pre-generated `taxonomy.json`

### Distribution Data
For balanced suggestions, the skill needs post counts per category/tag:
- Categories: Aim for even distribution, flag if category would become oversized
- Tags: Prefer tags with 5+ posts, warn about orphan tags

## Output Format

```markdown
## Suggested Categories

| Category | Post Count | Confidence | Rationale |
|----------|------------|------------|-----------|
| personal-development | 245 | High | Core theme matches self-improvement focus |
| productivity-effectiveness | 89 | Medium | Secondary theme around habits and routines |

**Recommendation**: Use "personal-development" as primary category.

---

## Suggested Tags

| Tag | Post Count | Confidence | Rationale |
|-----|------------|------------|-----------|
| habits | 45 | High | Central topic of the post |
| productivity | 67 | High | Directly discussed |
| morning-routine | 12 | Medium | Specific example in content |

**Recommendation**: Use all 3 tags. Avoid creating new tags.

---

## SEO Metadata

**Title** (58 chars):
> How to Build Morning Habits That Actually Stick | Your Blog

**Meta Description** (156 chars):
> Discover the science-backed approach to building morning habits that last. Learn the 3-step framework used by high performers. Start your transformation today.

**Focus Keyphrase**:
> morning habits

**Rationale**:
- "morning habits" has good search volume and matches user intent
- Title includes keyphrase naturally at the beginning
- Description creates urgency and promises specific value
```

## Workflow

### 1. Analyze Content
- Extract main themes and topics
- Identify key concepts and terminology
- Determine content type (how-to, opinion, review, etc.)

### 2. Load Taxonomy
- Fetch existing categories with post counts
- Fetch existing tags with post counts
- Identify distribution patterns

### 3. Match & Score
- Score each category/tag by relevance
- Consider distribution balance
- Flag potential issues (orphan tags, oversized categories)

### 4. Generate SEO
- Craft title with primary keyword
- Write compelling meta description
- Suggest focus keyphrase

### 5. Present with Rationale
- Show recommendations in table format
- Explain reasoning for each suggestion
- Highlight any concerns or alternatives

## Configuration

```json
{
  "taxonomy_source": "graphql|dist|file",
  "dist_path": "./dist",
  "taxonomy_file": "./taxonomy.json",
  "graphql_endpoint": "https://wp.example.com/graphql",
  "limits": {
    "max_categories": 2,
    "max_tags": 5,
    "min_tag_posts": 3
  },
  "seo": {
    "title_max_length": 60,
    "description_max_length": 160,
    "site_name": "Your Blog"
  }
}
```

## Example Usage

### Basic Classification
```
User: "Classify this post for me: /content/drafts/morning-routine-guide.md"

Claude: [Reads file, analyzes content, fetches taxonomy]
        [Presents category/tag suggestions with rationale]
        [Generates SEO metadata]
```

### Quick Tag Check
```
User: "What tags should I use for a post about Bitcoin ETFs and institutional adoption?"

Claude: [Analyzes topic, checks existing tags]
        "Based on your existing tags, I recommend:
        - bitcoin (89 posts) - primary topic
        - cryptocurrency (45 posts) - broader category
        - investing (23 posts) - relevant angle

        Avoid creating new tags like 'etf' or 'institutional' unless you plan
        to write more content on these specific topics."
```

### SEO Focus
```
User: "Generate SEO metadata for my post about productivity apps for remote workers"

Claude: [Analyzes topic and search intent]

        Title: "Best Productivity Apps for Remote Workers in 2025 | Your Blog"

        Description: "Discover the top productivity apps that remote workers
        swear by. From task management to focus tools, find the perfect
        stack for your home office."

        Focus Keyphrase: "productivity apps remote workers"
```

## Best Practices Enforced

1. **No tag pollution** - Won't suggest creating new tags unless justified
2. **Balanced distribution** - Warns if category is becoming oversized
3. **SEO compliance** - Enforces character limits and keyword placement
4. **Existing taxonomy** - Always checks against actual site data
5. **Transparent reasoning** - Every suggestion includes rationale
