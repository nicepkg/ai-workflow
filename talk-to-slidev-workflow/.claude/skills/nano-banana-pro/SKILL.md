---
name: nano-banana-pro
description: Generate images using Google's Nano Banana Pro (gemini-3-pro-image-preview). Accepts text prompts and optionally images (for editing/transformation) as INPUT. Returns generated IMAGES as OUTPUT. Use when user asks to create, generate, edit, or draw images, infographics, visualizations, diagrams, charts, or illustrations. Excellent for data-accurate infographics and text rendering.
allowed-tools: Bash(uv:*), Write, Read
---

# Nano Banana Pro Image Generator

Generate images using Google's advanced Nano Banana Pro model (`gemini-3-pro-image-preview`).

## Prerequisites

The user must have `GEMINI_API_KEY` environment variable set with a valid Google AI API key.

## Usage

The script is located in the same directory as this SKILL.md file. Run it with `uv run`:

```bash
uv run /path/to/skills/nano-banana-pro/generate_image.py "your prompt" -o output.png
```

When this skill is invoked, locate `generate_image.py` in the skill directory and run it.

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `prompt` | Yes | Text description of the image to generate or transformation to apply |
| `-o`, `--output` | Yes | Output filename (you decide the path based on context) |
| `-i`, `--image` | No | Input image(s) for editing/transformation or as context/reference (can be used multiple times) |
| `--aspect-ratio` | No | One of: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9` (default: `1:1`) |
| `--size` | No | Image size: `1K`, `2K`, `4K` (default: `1K`) |

### Examples

Basic image generation:
```bash
uv run generate_image.py "A sunset over mountains" -o sunset.png
```

Infographic with specific aspect ratio:
```bash
uv run generate_image.py "Infographic showing the water cycle with labeled stages" -o water_cycle.png --aspect-ratio 9:16
```

High-resolution ultrawide:
```bash
uv run generate_image.py "Professional photo of a modern office space" -o office.png --aspect-ratio 21:9 --size 4K
```

Edit an existing image:
```bash
uv run generate_image.py "Add a sunset sky to this image" -i photo.png -o edited.png
```

Transform with style:
```bash
uv run generate_image.py "Make this look like a watercolor painting" -i input.jpg -o watercolor.png
```

Combine multiple images:
```bash
uv run generate_image.py "Create a collage blending these images together" -i img1.png -i img2.png -o collage.png
```

Use image as context/reference:
```bash
uv run generate_image.py "Generate a new landscape in the same style as this reference" -i reference.png -o new_landscape.png
```

## Model Capabilities

Nano Banana Pro excels at:
- **Accurate infographics** with real data (uses Google Search grounding)
- **Text rendering** in images
- **Image editing and transformation** from input images
- **Context-aware generation** using reference images for style, composition, or subject
- **Cartographic visualizations** and maps
- **Detailed instruction following**
- **Chain-of-thought reasoning** for complex visual tasks

## Output

The script prints:
- Progress message while generating
- Path to saved image on success
- Any text response from the model
- Error message if no image was generated
