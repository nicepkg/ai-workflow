# Slidev Layouts Guide

Layouts define the visual structure of individual slides. This guide covers all built-in layouts and when to use them.

## Layout Syntax

Set layout in slide frontmatter:

```yaml
---
layout: center
---
```

## Content Layouts

### default

Standard layout with padding. Use for regular content slides.

```markdown
---
layout: default
---

# Regular Slide

- Point one
- Point two
- Point three
```

### center

Centers content both horizontally and vertically. Use for impactful statements or transitions.

```markdown
---
layout: center
---

# This Will Be Centered

Both the heading and any content below
```

### full

No padding - content fills the entire slide. Use for custom layouts or embedded content.

```markdown
---
layout: full
---

<div class="w-full h-full bg-blue-500 flex items-center justify-center">
  Custom full-bleed content
</div>
```

## Opening/Closing Layouts

### cover

Title slide layout. Typically used for the first slide.

```markdown
---
layout: cover
background: /cover-image.jpg
---

# Presentation Title

Subtitle or author name
```

### intro

Introduction slide. Use after cover for speaker intro or agenda.

```markdown
---
layout: intro
---

# About the Speaker

Brief bio and credentials
```

### end

Closing slide layout. Use for the final slide.

```markdown
---
layout: end
---

# Thank You

Contact information
```

## Section Layouts

### section

Section divider. Use to separate major parts of your presentation.

```markdown
---
layout: section
---

# Part 2: Implementation
```

### statement

Bold statement layout. Use for key takeaways or provocative points.

```markdown
---
layout: statement
---

# Code should be written for humans to read
```

### fact

Highlight a statistic or fact. Use for impressive numbers.

```markdown
---
layout: fact
---

# 10x
Productivity improvement

<p class="text-gray-500">When using the right tools</p>
```

### quote

Display a quotation. Use for testimonials or famous quotes.

```markdown
---
layout: quote
---

# "The best way to predict the future is to invent it."

Alan Kay
```

## Image Layouts

### image

Full-screen image background.

```markdown
---
layout: image
image: /path/to/image.jpg
---

# Optional Title Overlay
```

### image-left

Image on left (40%), content on right (60%).

```markdown
---
layout: image-left
image: /path/to/image.jpg
---

# Content Title

Your content goes here on the right side.

- Point one
- Point two
```

### image-right

Image on right (40%), content on left (60%).

```markdown
---
layout: image-right
image: /path/to/image.jpg
---

# Content Title

Your content goes here on the left side.
```

## Multi-Column Layouts

### two-cols

Two equal columns. Use `::right::` to separate content.

```markdown
---
layout: two-cols
---

# Left Column

Content for the left side.

- Item one
- Item two

::right::

# Right Column

Content for the right side.

- Item three
- Item four
```

### two-cols-header

Two columns with a spanning header. Use `::left::` and `::right::` slots.

```markdown
---
layout: two-cols-header
---

# Header Spans Both Columns

::left::

## Left Section

Left content here.

::right::

## Right Section

Right content here.
```

## Embed Layouts

### iframe

Embed a webpage. The iframe fills the slide.

```markdown
---
layout: iframe
url: https://example.com
---
```

### iframe-left / iframe-right

Embed a webpage with content alongside.

```markdown
---
layout: iframe-right
url: https://example.com
---

# Related Content

Discussion points about the embedded page.
```

## Special Layouts

### none

No layout styling at all. Use for completely custom slides.

```markdown
---
layout: none
---

<div class="absolute inset-0 flex items-center justify-center">
  Completely custom layout
</div>
```

## Layout Selection Guide

| Content Type     | Recommended Layout                   |
| ---------------- | ------------------------------------ |
| Title/Opening    | `cover`                              |
| Regular content  | `default`                            |
| Key statement    | `statement`, `center`                |
| Statistics       | `fact`                               |
| Comparison       | `two-cols`                           |
| Code walkthrough | `default`, `two-cols`                |
| Demo/video       | `iframe`, `full`                     |
| Section break    | `section`                            |
| Testimonial      | `quote`                              |
| Photo showcase   | `image`, `image-left`, `image-right` |
| Closing          | `end`                                |

## Custom Layouts

Create custom layouts in `layouts/` directory:

```vue
<!-- layouts/my-layout.vue -->
<template>
  <div class="slidev-layout my-layout">
    <slot />
  </div>
</template>

<style scoped>
.my-layout {
  display: flex;
  flex-direction: column;
  padding: 2rem;
}
</style>
```

Use with:

```yaml
---
layout: my-layout
---
```

## Layout Props

Some layouts accept additional props:

```yaml
---
layout: image-right
image: /photo.jpg
backgroundSize: contain  # or 'cover' (default)
class: my-custom-class
---
```

## Combining with Classes

Add custom classes alongside layouts:

```yaml
---
layout: center
class: text-white bg-blue-900
---
```
