# Slidev Built-in Components API

Complete reference for all built-in Slidev components with usage examples and API details.

## Navigation Components

### Arrow

Creates directional arrows for pointing or connecting elements.

**Props:**
- `x1` (string | number): Start x position
- `y1` (string | number): Start y position
- `x2` (string | number): End x position
- `y2` (string | number): End y position
- `width` (string | number): Arrow width (default: 2)
- `color` (string): Arrow color (default: current color)

**Example:**

```md
<Arrow x1="100" y1="100" x2="300" y2="200" />

<Arrow x1="50" y1="50" x2="200" y2="150" width="3" color="#3b82f6" />
```

### VDragArrow

Draggable version of Arrow component.

**Usage:**

```md
<VDragArrow />

<!-- Position is draggable in presenter mode -->
```

### Link

Navigate between slides.

**Props:**
- `to` (string | number): Target slide number or route

**Example:**

```md
<Link to="5">Go to slide 5</Link>

<Link to="intro">Go to intro section</Link>
```

## Text Components

### AutoFitText

Automatically adjusts font size to fit content within container.

**Props:**
- `max` (number): Maximum font size in pixels
- `min` (number): Minimum font size in pixels (default: 16)
- `modelValue` (boolean): Force recalculation

**Example:**

```md
<AutoFitText :max="300" :min="20">
  This text will automatically resize to fit
</AutoFitText>

<AutoFitText :max="200">
  # Large Heading
  Subtext here
</AutoFitText>
```

### TitleRenderer

Renders parsed title from specified slide.

**Props:**
- `no` (number | string): Slide number

**Example:**

```md
<TitleRenderer :no="1" />

<TitleRenderer :no="currentSlide" />
```

### Toc

Generates table of contents from slide titles.

**Props:**
- `columns` (string | number): Number of columns
- `listClass` (string | string[]): CSS class for list
- `maxDepth` (string | number): Maximum heading depth
- `minDepth` (string | number): Minimum heading depth
- `mode` ('all' | 'onlyCurrentTree' | 'onlySiblings'): Display mode

**Example:**

```md
<Toc />

<Toc :maxDepth="2" />

<Toc columns="2" mode="onlyCurrentTree" />
```

## Media Components

### Youtube

Embeds YouTube videos.

**Props:**
- `id` (string): YouTube video ID
- `width` (number): Video width
- `height` (number): Video height
- `start` (number): Start time in seconds

**Example:**

```md
<Youtube id="dQw4w9WgXcQ" />

<Youtube id="dQw4w9WgXcQ" width="800" height="450" />

<Youtube id="dQw4w9WgXcQ" :start="30" />
```

### Tweet

Embeds Twitter/X posts.

**Props:**
- `id` (string | number): Tweet ID
- `scale` (string | number): Scale factor (default: 1)
- `conversation` (string): Show conversation thread

**Example:**

```md
<Tweet id="1234567890123456789" />

<Tweet id="1234567890123456789" :scale="0.8" />
```

### SlidevVideo

HTML5 video player with Slidev integration.

**Props:**
- `controls` (boolean): Show video controls
- `autoplay` (boolean | 'once'): Autoplay behavior
- `autoreset` (boolean | 'slide' | 'click'): Reset behavior
- All standard HTML5 video attributes

**Example:**

```md
<SlidevVideo autoplay controls>
  <source src="/video.mp4" type="video/mp4" />
</SlidevVideo>

<SlidevVideo autoreset="click">
  <source src="/demo.webm" type="video/webm" />
</SlidevVideo>
```

## Utility Components

### SlideCurrentNo

Displays current slide number.

**Example:**

```md
<SlideCurrentNo />

Slide <SlideCurrentNo /> of <SlidesTotal />
```

### SlidesTotal

Displays total number of slides.

**Example:**

```md
<SlidesTotal />

Progress: <SlideCurrentNo /> / <SlidesTotal />
```

### LightOrDark

Renders different content based on theme.

**Slots:**
- `#dark`: Content for dark theme
- `#light`: Content for light theme

**Example:**

```md
<LightOrDark>
  <template #dark>
    <div class="text-white">Dark mode content</div>
  </template>
  <template #light>
    <div class="text-black">Light mode content</div>
  </template>
</LightOrDark>
```

### RenderWhen

Conditionally renders based on context.

**Props:**
- `context` ('main' | 'slide' | 'overview' | 'presenter' | 'print'): Render context

**Example:**

```md
<RenderWhen context="presenter">
  Only visible in presenter mode
</RenderWhen>

<RenderWhen context="print">
  Only visible when printing/exporting
</RenderWhen>
```

### Transform

Applies scaling and transformation to content.

**Props:**
- `scale` (number): Scale factor (default: 1)
- `origin` (string): Transform origin (default: 'center')

**Example:**

```md
<Transform :scale="2">
  This content is scaled 2x
</Transform>

<Transform :scale="0.5" origin="top left">
  Scaled from top-left corner
</Transform>
```

### VSwitch

Cycles between multiple content blocks on click.

**Example:**

```md
<VSwitch>
  <template #0>First content</template>
  <template #1>Second content</template>
  <template #2>Third content</template>
</VSwitch>

<!-- Click to cycle through content -->
```

### VDrag

Makes content draggable in presenter mode.

**Props:**
- `pos` (object): Position `{ x: number, y: number }`

**Example:**

```md
<VDrag>
  <div class="bg-blue-500 p-4">
    Drag me in presenter mode
  </div>
</VDrag>

<VDrag :pos="{ x: 100, y: 100 }">
  Initial position set
</VDrag>
```

### PoweredBySlidev

Attribution component linking to Slidev website.

**Example:**

```md
<PoweredBySlidev />
```

## Animation Directives

### v-click

Shows element on click.

**Usage:**

```md
<div v-click>Appears on click</div>

<div v-click="1">Appears at step 1</div>
<div v-click="2">Appears at step 2</div>

<div v-click="+2">Skip one step</div>
<div v-click="-1">Same as previous</div>
```

### v-after

Shows element after previous v-click.

**Usage:**

```md
<div v-click>First</div>
<div v-after>After first</div>
```

### v-clicks

Applies v-click to all children.

**Usage:**

```md
<v-clicks>

- Item 1
- Item 2
- Item 3

</v-clicks>

<v-clicks>
<div>Block 1</div>
<div>Block 2</div>
<div>Block 3</div>
</v-clicks>
```

### v-motion

Motion animations from @vueuse/motion.

**Usage:**

```md
<div
  v-motion
  :initial="{ x: -80, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  Slides in from left
</div>

<div
  v-motion
  :initial="{ y: 80, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  Slides in from bottom
</div>
```

## Custom Component Development

### Creating Components

Place components in `./components/` directory:

```vue
<!-- components/Counter.vue -->
<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{
  initial?: number
}>()

const count = ref(props.initial ?? 0)
</script>

<template>
  <button @click="count++">
    Count: {{ count }}
  </button>
</template>

<style scoped>
button {
  @apply bg-blue-500 text-white px-4 py-2 rounded;
}
</style>
```

**Usage:**

```md
<Counter />

<Counter :initial="10" />
```

### TypeScript Props

```vue
<!-- components/Card.vue -->
<script setup lang="ts">
interface Props {
  title: string
  subtitle?: string
  dark?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  dark: false
})
</script>

<template>
  <div :class="{ 'bg-dark': dark, 'bg-light': !dark }">
    <h2>{{ title }}</h2>
    <p v-if="subtitle">{{ subtitle }}</p>
    <slot />
  </div>
</template>
```

**Usage:**

```md
<Card title="My Card" subtitle="Description">
  Card content here
</Card>

<Card title="Dark Card" :dark="true" />
```

### Slots

```vue
<!-- components/Panel.vue -->
<script setup lang="ts">
interface Props {
  variant?: 'primary' | 'secondary'
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'primary'
})
</script>

<template>
  <div :class="`panel panel-${variant}`">
    <div class="panel-header">
      <slot name="header">Default Header</slot>
    </div>
    <div class="panel-body">
      <slot>Default Content</slot>
    </div>
    <div class="panel-footer">
      <slot name="footer" />
    </div>
  </div>
</template>
```

**Usage:**

```md
<Panel>
  <template #header>
    Custom Header
  </template>

  Main content

  <template #footer>
    Footer content
  </template>
</Panel>
```

### Composables

```ts
// components/useSlide.ts
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

export function useSlide() {
  const { $slidev } = useSlideContext()

  const currentSlide = computed(() => $slidev.nav.currentSlide)
  const totalSlides = computed(() => $slidev.nav.total)
  const isFirst = computed(() => $slidev.nav.currentSlideNo === 1)
  const isLast = computed(() => $slidev.nav.currentSlideNo === totalSlides.value)

  return {
    currentSlide,
    totalSlides,
    isFirst,
    isLast
  }
}
```

**Usage:**

```vue
<script setup lang="ts">
import { useSlide } from './useSlide'

const { currentSlide, totalSlides, isFirst, isLast } = useSlide()
</script>

<template>
  <div>
    <p>Slide {{ currentSlide }} of {{ totalSlides }}</p>
    <button :disabled="isFirst">Previous</button>
    <button :disabled="isLast">Next</button>
  </div>
</template>
```

## Icon Components

Use Iconify icons directly:

```md
<carbon-logo-github />
<mdi-heart class="text-red-500" />
<uim-rocket class="text-3xl" />
<logos-vue />
<twemoji-cat-with-tears-of-joy />
```

**Styling:**

```md
<mdi-check class="text-green-500 text-2xl" />

<carbon-arrow-right class="inline-block animate-pulse" />

<div class="flex gap-2">
  <mdi-github />
  <mdi-twitter />
  <mdi-linkedin />
</div>
```

## Component Best Practices

1. **TypeScript**: Use TypeScript for props and type safety
2. **Scoped Styles**: Use scoped styles to avoid conflicts
3. **Props Defaults**: Provide sensible defaults for optional props
4. **Slots**: Use slots for flexible content composition
5. **Composables**: Extract reusable logic to composables
6. **Naming**: Use PascalCase for component files
7. **Documentation**: Document props and usage in comments
8. **Testing**: Test components in different contexts (presenter, print, etc.)

## Advanced Patterns

### Context-Aware Components

```vue
<script setup lang="ts">
import { useSlideContext } from '@slidev/client'

const { $slidev, $clicks, $page } = useSlideContext()
</script>

<template>
  <div>
    Current click: {{ $clicks.current }}
    Current page: {{ $page }}
  </div>
</template>
```

### Reactive Components

```vue
<script setup lang="ts">
import { ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'

const { $slidev } = useSlideContext()
const message = ref('')

watch(() => $slidev.nav.currentSlideNo, (newSlide) => {
  message.value = `Now on slide ${newSlide}`
})
</script>

<template>
  <div>{{ message }}</div>
</template>
```

### Global Components

Create `./components/global.vue`:

```vue
<template>
  <div class="global-header">
    <slot />
  </div>
</template>

<style>
.global-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  padding: 1rem;
  background: rgba(0, 0, 0, 0.5);
}
</style>
```

Use in slides:

```md
<Global>
  Header content on all slides
</Global>
```
