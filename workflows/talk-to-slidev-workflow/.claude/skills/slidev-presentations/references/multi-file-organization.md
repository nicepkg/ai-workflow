# Multi-File Organization for Slidev

For large presentations or better linting compatibility, split slides across multiple files.

## Table of Contents

- [Directory Structure](#directory-structure)
- [Main Entry File](#main-entry-file)
- [Individual Slide Files](#individual-slide-files)
- [Importing Specific Slides](#importing-specific-slides)
- [When to Use Multi-File](#when-to-use-multi-file)
- [Benefits](#benefits)

## Directory Structure

```text
presentation/
├── slides.md              # Main entry - imports other files
├── slides/                # Individual slide files
│   ├── 01-intro.md
│   ├── 02-problem.md
│   ├── 03-solution.md
│   └── 04-demo.md
├── .markdownlint.json     # Linting config (required)
└── components/            # Custom Vue components (optional)
```

## Main Entry File

The main `slides.md` contains headmatter and imports:

```markdown
---
theme: default
title: My Presentation
transition: slide-left
---

---
src: ./slides/01-intro.md
---

---
src: ./slides/02-problem.md
---

---
src: ./slides/03-solution.md
---

---
src: ./slides/04-demo.md
---
```

## Individual Slide Files

Each file in `slides/` contains one or more slides with standard frontmatter:

```markdown
---
layout: section
---

# Introduction

Welcome to the presentation

---

# About Me

- Point 1
- Point 2
```

## Importing Specific Slides

Cherry-pick slides from other presentations using hash notation:

```markdown
---
src: ./other-presentation.md#2,5-7
---
```

This imports slides 2, 5, 6, and 7 from the referenced file.

### Import Syntax Examples

| Syntax                 | What It Imports       |
| ---------------------- | --------------------- |
| `src: ./file.md`       | All slides from file  |
| `src: ./file.md#3`     | Only slide 3          |
| `src: ./file.md#1-5`   | Slides 1 through 5    |
| `src: ./file.md#2,5-7` | Slides 2, 5, 6, and 7 |

## When to Use Multi-File

| Scenario                           | Recommendation     |
| ---------------------------------- | ------------------ |
| Small presentation (<15 slides)    | Single `slides.md` |
| Medium presentation (15-30 slides) | Either approach    |
| Large presentation (30+ slides)    | Multi-file         |
| Reusable slide sections            | Multi-file         |
| Team collaboration                 | Multi-file         |
| Strict linting requirements        | Multi-file         |

## Benefits

- **No linting conflicts** - Each file has single frontmatter
- **Easier reorganization** - Reorder by changing imports
- **Better version control** - Smaller, focused diffs
- **Reusable content** - Share slides across presentations
- **Clearer boundaries** - Sections are visually separated

## Frontmatter Merging

When importing slides, frontmatter can be merged. The main file's headmatter provides defaults, and individual files can override:

```markdown
# slides.md (main)
---
theme: default
transition: slide-left
---

# slides/intro.md (individual)
---
transition: fade
---
```

The intro slides will use `fade` transition while others use `slide-left`.

## Naming Conventions

Prefix files with numbers for clear ordering:

```text
slides/
├── 01-intro.md
├── 02-problem-statement.md
├── 03-solution-overview.md
├── 04-technical-deep-dive.md
├── 05-demo.md
└── 06-conclusion.md
```

This ensures consistent ordering in file explorers and import statements.
