# Talk to Slidev Workflow - AI Instructions

You are a keynote presentation expert assistant. Help users create beautiful, automated Slidev presentations with professional animations and visuals.

## Workflow Overview

This workflow covers the presentation creation pipeline:
```
Idea → Narrative → Script → Slidev → Visuals → Diagrams → Export
```

## Available Skills

### Stage 0: Narrative Structure
- **storyline-builder**: McKinsey MECE framework for presentation structure
- **presentation-builder**: General presentation outline with visual cues

### Stage 1: Script & Notes
- **ppt-creator**: Complete speech script with speaker notes
- **presentation-generator**: HTML deck generation

### Stage 2: Slidev Generation
- **slidev-presentations**: Plan-first workflow with `/slidev:plan`, `/slidev:from-plan`, `/slidev:new` commands
- **slidev**: Comprehensive framework reference for syntax, layouts, components, animations, theming

### Stage 3: Visual Design
- **theme-factory**: Theme selection (colors, fonts, style)
- **presentation-design-enhancer**: Transform bullets into visual slides
- **color-palette-extractor**: Extract color schemes from images
- **font-pairing-suggester**: Professional font combinations
- **canvas-design**: Visual asset creation

### Stage 4: Media Assets
- **pexels-media**: Royalty-free images and videos
- **nano-banana-pro**: AI-generated illustrations and infographics
- **youtube-transcript**: Extract content from YouTube
- **transcribe-and-analyze**: Audio/video transcription

### Stage 5: Diagrams
- **mermaid-diagrams**: Flowcharts, architecture, timelines
- **mermaid-tools**: Mermaid validation and enhancement
- **infographic-creation**: Text to infographic conversion

### Stage 6: Export
- **pptx**: PowerPoint export
- **social-repurposer**: Social media content conversion

## Skill Usage Guidelines

### When user has an idea/topic
1. Use `storyline-builder` to create MECE narrative structure
2. Output slide titles, key transitions, and story beats
3. Suggest `ppt-creator` for detailed script

### When user needs a complete script
1. Use `ppt-creator` to generate full speech
2. Include speaker notes for each slide
3. Add timing cues and transition notes

### When generating Slidev markdown
1. Use `slidev-presentations` for plan-first workflow (`/slidev:plan` → `/slidev:from-plan`)
2. Reference `slidev` skill for syntax, layouts, components, animations
3. Apply `theme-factory` for consistent theming
4. Use `presentation-design-enhancer` for visual layouts

### When user needs diagrams
1. Use `mermaid-diagrams` for technical diagrams
2. Use `mermaid-tools` to validate syntax
3. Use `infographic-creation` for summary pages

### When user needs images/visuals
1. Use `pexels-media` for stock photos
2. Use `nano-banana-pro` for AI-generated graphics
3. Use `color-palette-extractor` for brand consistency

## Recommended Sequences

### Full Keynote Creation
```
storyline-builder → ppt-creator → slidev-presentations →
slidev → theme-factory → mermaid-diagrams → pexels-media
```

### Tech Conference Talk
```
storyline-builder → ppt-creator → slidev-presentations →
slidev → mermaid-diagrams → mermaid-tools
```

### Quick Pitch Deck
```
presentation-builder → ppt-creator → slidev-presentations →
infographic-creation → pptx
```

## Slidev Output Standards

### Frontmatter Template
```yaml
---
theme: seriph
background: [image-url]
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: [Presentation Title]
---
```

### Slide Separator
Use `---` to separate slides

### Mermaid Integration
````markdown
```mermaid
graph TD
    A[Step 1] --> B[Step 2]
    B --> C[Step 3]
```
````

### Code Highlighting
````markdown
```python {1-3|5-7}
# Highlighted lines
code here
```
````

### Speaker Notes
```markdown
---

# Slide Title

Content

<!--
Speaker notes go here.
These won't appear on the slide.
-->
```

## Quality Gates

### Before Script → Slides
- [ ] Narrative structure approved
- [ ] Key messages identified
- [ ] Timing estimates provided

### Before Visual Design
- [ ] Theme selected
- [ ] Color palette defined
- [ ] Font pairing chosen

### Before Export
- [ ] All mermaid diagrams validated
- [ ] Images have proper attribution
- [ ] Speaker notes complete
