# Slidev Themes Reference

## Built-in Themes

### default

The standard Slidev theme. Clean, minimal design suitable for most presentations.

```yaml
---
theme: default
---
```

### seriph

Elegant theme with serif fonts. Good for formal or academic presentations.

```yaml
---
theme: seriph
---
```

## Popular Community Themes

### @slidev/theme-apple-basic

Apple-inspired minimal design.

```bash
npm install @slidev/theme-apple-basic
```

```yaml
---
theme: apple-basic
---
```

### @slidev/theme-bricks

Bold, colorful theme with brick-like sections.

```bash
npm install @slidev/theme-bricks
```

### slidev-theme-dracula

Dark theme based on the Dracula color palette.

```bash
npm install slidev-theme-dracula
```

```yaml
---
theme: dracula
---
```

### slidev-theme-geist

Inspired by Vercel's Geist design system.

```bash
npm install slidev-theme-geist
```

### slidev-theme-penguin

Playful theme with rounded corners.

```bash
npm install slidev-theme-penguin
```

### slidev-theme-academic

Designed for academic presentations with LaTeX support.

```bash
npm install slidev-theme-academic
```

## Theme Configuration

Themes can expose configuration options via frontmatter:

```yaml
---
theme: default
themeConfig:
  primary: '#5d8392'
  secondary: '#6b7280'
---
```

Check each theme's documentation for available options.

## Custom Styling

Override theme styles in any slide:

```html
<style>
/* Scoped to this slide */
h1 {
  color: #2B90B6;
  background: linear-gradient(45deg, #4EC5D4 10%, #146b8c 90%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
```

Global styles (affects all slides):

```html
<style global>
.slidev-layout {
  background: #1a1a1a;
}
</style>
```

## Creating Custom Themes

Directory structure:

```text
my-theme/
├── package.json
├── styles/
│   ├── index.ts
│   └── layouts.css
├── layouts/
│   ├── default.vue
│   ├── cover.vue
│   └── center.vue
├── components/
│   └── MyComponent.vue
└── setup/
    └── main.ts
```

Minimal `package.json`:

```json
{
  "name": "slidev-theme-my-theme",
  "version": "1.0.0",
  "engines": {
    "slidev": ">=0.40.0"
  },
  "slidev": {
    "colorSchema": "both",
    "highlighter": "shiki"
  }
}
```

## Theme Selection Guidelines

| Audience            | Recommended Themes            |
| ------------------- | ----------------------------- |
| Technical/Developer | `default`, `dracula`, `geist` |
| Business/Corporate  | `default`, `apple-basic`      |
| Academic            | `seriph`, `academic`          |
| Creative/Casual     | `bricks`, `penguin`           |
| Dark presentations  | `dracula`                     |

## Color Scheme

Force light or dark mode:

```yaml
---
colorSchema: dark
---
```

Options: `auto`, `light`, `dark`, `both` (allows toggle)
