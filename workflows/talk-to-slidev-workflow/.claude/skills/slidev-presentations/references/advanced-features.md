# Slidev Advanced Features

Advanced features for interactive presentations, animations, and customization.

## Table of Contents

- [Shiki Magic Move](#shiki-magic-move)
- [Monaco Editor](#monaco-editor)
- [Advanced Animations](#advanced-animations)
- [Themes](#themes)
- [Addons](#addons)
- [v-mark Annotations](#v-mark-annotations)
- [Live Drawing](#live-drawing)
- [Click-Synced Notes](#click-synced-notes)
- [Icons](#icons)

## Core Advanced Features

- **Shiki Magic Move** - Animated code transitions between states
- **Monaco Editor** - Interactive, editable code blocks
- **Vue Components** - Custom components in `components/` directory
- **UnoCSS** - Utility-first CSS classes (built-in)
- **LaTeX Math** - `$E = mc^2$` inline, `$$...$$` for blocks
- **MDC Syntax** - `[styled text]{style="color:red"}` (requires `mdc: true`)

## Shiki Magic Move

Animate code changes between states:

`````markdown
````md magic-move
```typescript
const greeting = "Hello"
```
```typescript
const greeting = "Hello, World!"
console.log(greeting)
```
`````

`````

## Monaco Editor

### Read-Only Interactive Editor

````markdown
```typescript {monaco}
// Audience can explore this code
function greet(name: string) {
  return `Hello, ${name}!`
}
```
`````

### Runnable Monaco Editor

Live code execution - perfect for workshops:

````markdown
```typescript {monaco-run}
// Audience can edit AND execute this code
const result = [1, 2, 3].map(x => x * 2)
console.log(result) // Output appears below!
```
````

Use `{monaco-run}` instead of `{monaco}` to enable execution with output display.

## Advanced Animations

### v-motion

Movement animations with @vueuse/motion:

```html
<div v-motion
  :initial="{ x: -80, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }"
  :click-1="{ scale: 1.2 }"
>
  Animates on enter and click
</div>
```

### Click Ranges

Control visibility windows:

```html
<div v-click="[2, 5]">Visible at clicks 2-4</div>
```

### Relative Positioning

Position clicks relative to previous:

```html
<div v-click="'+2'">Two clicks after previous</div>
```

## Themes

Official themes: `default`, `seriph`, `apple-basic`, `shibainu`, `bricks`

```yaml
---
theme: seriph
---
```

Browse themes: <https://sli.dev/resources/theme-gallery>

See [themes.md](./themes.md) for detailed theme customization.

## Addons

Extend Slidev with addons for Python execution, QR codes, diagrams, and more:

```yaml
---
addons:
  - slidev-addon-python-runner
  - slidev-addon-qrcode
---
```

Popular addons:

| Addon           | Purpose                     |
| --------------- | --------------------------- |
| `python-runner` | Execute Python in slides    |
| `rabbit`        | Timer and progress tracking |
| `excalidraw`    | Hand-drawn diagrams         |
| `qrcode`        | Generate QR codes           |
| `asciinema`     | Terminal recordings         |

Browse addons: <https://sli.dev/resources/addon-gallery>

## v-mark Annotations

Add hand-drawn style emphasis using RoughNotation:

```html
<span v-mark.underline>Important concept</span>
<span v-mark.circle>Key term</span>
<span v-mark.highlight="{ color: 'yellow' }">Highlighted</span>
<span v-mark.box>Boxed content</span>
<span v-mark.strike>Crossed out</span>
```

Click-triggered marks (appears on specific click):

```html
<span v-mark.underline="3">Appears on click 3</span>
```

Available types: `underline`, `circle`, `highlight`, `box`, `bracket`, `strike-through`

## Live Drawing

Built-in drawing tools (powered by drauu) for live annotation:

- Press `d` to toggle drawing mode
- Annotations persist across slide navigation

Configure in frontmatter:

```yaml
---
drawings:
  enabled: true
  persist: true
  presenterOnly: false
---
```

## Click-Synced Notes

Sync presenter notes to click animations using `[click]` markers:

```markdown
# Slide Title

<v-clicks>

- Point A
- Point B
- Point C

</v-clicks>

<!--
[click] Explain point A in detail
[click] Now discuss point B
[click] Finally cover point C
-->
```

The presenter view shows only the relevant note section as you progress through clicks.

## Icons

Access 100k+ icons from Iconify using UnoCSS class syntax:

```html
<div class="i-carbon-logo-github text-4xl" />
<div class="i-mdi-heart text-red-500 text-3xl" />
<div class="i-heroicons-check-circle text-green-500" />
```

Format: `i-{collection}-{icon-name}`

Browse icons: <https://icones.js.org/>

### Common Icon Collections

| Collection      | Prefix         | Examples                          |
| --------------- | -------------- | --------------------------------- |
| Carbon          | `i-carbon-`    | `logo-github`, `code`, `terminal` |
| Material Design | `i-mdi-`       | `heart`, `check`, `alert`         |
| Heroicons       | `i-heroicons-` | `check-circle`, `arrow-right`     |
| Phosphor        | `i-ph-`        | `code`, `user`, `gear`            |
