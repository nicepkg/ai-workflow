# Astro CTA Injector - Reference Guide

## Placement Strategy Details

### `end` - After Content
Injects the CTA after all post content, before closing tags.

**Best for:**
- General promotional CTAs
- "Related posts" sections
- Author bios with newsletter links

**Implementation:**
```python
content = content + cta_html
```

### `after-paragraph-50%` - Mid-Content
Injects after approximately 50% of the paragraphs.

**Best for:**
- Newsletter signups (highest conversion point)
- "Want more?" interrupts
- Long-form content

**Implementation:**
```python
paragraphs = content.split('</p>')
mid_point = len(paragraphs) // 2
paragraphs.insert(mid_point, cta_html)
```

### `after-paragraph-60%` - Later Content
Injects after 60% of paragraphs - gives reader more content first.

**Best for:**
- Product recommendations
- When context is important
- Educational content

### `after-heading` - After First H2
Injects immediately after the first `<h2>` element.

**Best for:**
- Important announcements
- Time-sensitive CTAs
- High-priority promotions

### `before-conclusion` - Before Last Paragraph
Injects before the final paragraph of content.

**Best for:**
- Summary-related CTAs
- "Before you go" messages
- Strong finishes

## Content Scoring Algorithm

### Keyword Matching
```python
def calculate_keyword_score(content: str, keywords: list[str]) -> float:
    content_lower = content.lower()
    total_matches = sum(content_lower.count(kw.lower()) for kw in keywords)
    # Normalize by content length (per 1000 words)
    word_count = len(content.split())
    normalized = (total_matches / max(word_count, 1)) * 1000
    return min(normalized, 5.0)  # Cap at 5 points
```

### Length Bonus
```python
def calculate_length_score(word_count: int) -> float:
    if word_count < 300:
        return 0.0
    elif word_count < 600:
        return 1.0
    elif word_count < 1000:
        return 2.0
    elif word_count < 2000:
        return 3.0
    else:
        return 4.0  # Long-form content bonus
```

### Title Match
```python
def calculate_title_score(title: str, keywords: list[str]) -> float:
    title_lower = title.lower()
    matches = sum(1 for kw in keywords if kw.lower() in title_lower)
    return min(matches * 0.5, 1.0)  # Max 1 point
```

### Total Score
```python
total_score = keyword_score + length_score + title_score
# Range: 0-10
```

## Template Variables

### Standard Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `{{title}}` | CTA headline | "Subscribe Now" |
| `{{description}}` | Body text | "Get weekly tips..." |
| `{{button_text}}` | Button label | "Sign Up" |
| `{{form_url}}` | Form action URL | "/api/subscribe" |

### Product Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `{{product_name}}` | Product name | "TaskManager Pro" |
| `{{product_url}}` | Product page URL | "/products/taskmanager" |
| `{{product_price}}` | Price display | "$9.99/mo" |
| `{{image_url}}` | Product image | "/images/product.png" |

### Dynamic Variables
| Variable | Description | Populated From |
|----------|-------------|----------------|
| `{{post_title}}` | Current post title | Post frontmatter |
| `{{post_category}}` | Post category | Post frontmatter |
| `{{related_keyword}}` | Matched keyword | Scoring algorithm |

## Astro File Structure

### Standard Astro Component (`.astro`)
```astro
---
// Frontmatter
const { title, description } = Astro.props;
---

<article>
  <h1>{title}</h1>
  <div class="content">
    <!-- Post content here -->
    <!-- CTA will be injected based on placement strategy -->
  </div>
</article>
```

### Markdown with Frontmatter (`.md`)
```markdown
---
title: "My Post"
description: "Post description"
---

Post content here...

<!-- CTA injection point depends on placement -->
```

## CSS Classes for CTAs

### Recommended Structure
```html
<aside class="cta cta-{{type}}" data-cta-type="{{type}}">
  <div class="cta-inner">
    <h3 class="cta-title">{{title}}</h3>
    <p class="cta-description">{{description}}</p>
    <div class="cta-action">
      <!-- Form or link -->
    </div>
  </div>
</aside>
```

### Suggested CSS
```css
.cta {
  margin: 2rem 0;
  padding: 1.5rem;
  border-radius: 8px;
  background: var(--cta-bg, #f5f5f5);
}

.cta-newsletter {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.cta-product {
  border: 2px solid var(--accent-color);
}

.cta-title {
  margin: 0 0 0.5rem;
  font-size: 1.25rem;
}

.cta-description {
  margin: 0 0 1rem;
  opacity: 0.9;
}
```

## Duplicate Detection

The injector checks for existing CTAs before injection:

```python
def has_existing_cta(content: str, cta_type: str) -> bool:
    patterns = [
        f'data-cta-type="{cta_type}"',
        f'class="cta-{cta_type}"',
        f'<!-- CTA:{cta_type} -->',
    ]
    return any(pattern in content for pattern in patterns)
```

## Backup & Rollback

### Backup Structure
```
backups/
├── 2025-01-15_143022/
│   ├── manifest.json
│   ├── src/content/blog/
│   │   ├── post-1.astro.bak
│   │   └── post-2.astro.bak
```

### Manifest Format
```json
{
  "created_at": "2025-01-15T14:30:22Z",
  "cta_type": "newsletter",
  "files_modified": [
    "src/content/blog/post-1.astro",
    "src/content/blog/post-2.astro"
  ],
  "placement": "after-paragraph-50%"
}
```

### Rollback Command
```bash
python scripts/inject_ctas.py --rollback 2025-01-15_143022
```

## Common Keywords by CTA Type

### Newsletter
```json
["tip", "guide", "learn", "strategy", "how to", "tutorial",
 "method", "approach", "framework", "system", "growth",
 "improve", "better", "success", "habit"]
```

### Product (Productivity App)
```json
["productivity", "task", "todo", "organize", "planning",
 "goal", "habit", "focus", "time management", "workflow",
 "gtd", "getting things done", "schedule", "routine"]
```

### Course/Education
```json
["course", "learn", "training", "workshop", "masterclass",
 "education", "skill", "certification", "program", "lesson"]
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| `FileNotFoundError` | Content path invalid | Check `content_path` config |
| `TemplateNotFoundError` | Template file missing | Create template in `templates/` |
| `DuplicateCTAError` | CTA already exists | Skip or use `--force` flag |
| `ParseError` | Invalid HTML/Astro | Check file syntax |
