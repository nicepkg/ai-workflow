# /// script
# dependencies = ["google-genai"]
# ///
"""
Nano Banana Pro image generator using Google's gemini-3-pro-image-preview model.

Usage:
    uv run generate_image.py "your prompt here" -o output.png
    uv run generate_image.py "transform this image" -i input.png -o output.png
"""

import argparse
import mimetypes
import sys
from pathlib import Path

from google import genai
from google.genai import types


def get_mime_type(file_path: str) -> str:
    """Get MIME type for an image file."""
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type and mime_type.startswith("image/"):
        return mime_type
    ext = Path(file_path).suffix.lower()
    mime_map = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    return mime_map.get(ext, "image/jpeg")


def main():
    parser = argparse.ArgumentParser(
        description="Generate images using Nano Banana Pro (gemini-3-pro-image-preview)"
    )
    parser.add_argument("prompt", help="Text description of the image to generate")
    parser.add_argument(
        "-o", "--output", required=True, help="Output filename (e.g., output.png)"
    )
    parser.add_argument(
        "--aspect-ratio",
        choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
        default="1:1",
        help="Aspect ratio of the generated image (default: 1:1)",
    )
    parser.add_argument(
        "--size",
        choices=["1K", "2K", "4K"],
        default="1K",
        help="Image size (default: 1K)",
    )
    parser.add_argument(
        "-i",
        "--image",
        action="append",
        dest="images",
        help="Input image(s) for editing/transformation or as context/reference (can be used multiple times)",
    )
    args = parser.parse_args()

    client = genai.Client()

    # Build contents list
    contents = []

    # Add input images if provided (for editing/transformation)
    if args.images:
        for image_path in args.images:
            path = Path(image_path)
            if not path.exists():
                print(f"Error: Image file not found: {image_path}", file=sys.stderr)
                sys.exit(1)
            with open(path, "rb") as f:
                image_bytes = f.read()
            mime_type = get_mime_type(image_path)
            contents.append(
                types.Part.from_bytes(data=image_bytes, mime_type=mime_type)
            )
            print(f"Including input image: {image_path}")

    # Add text prompt
    contents.append(args.prompt)

    print(f"Generating image with prompt: {args.prompt[:100]}...")

    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=args.aspect_ratio,
                image_size=args.size,
            ),
        ),
    )

    image_saved = False
    text_response = []

    for part in response.candidates[0].content.parts:
        if hasattr(part, "inline_data") and part.inline_data:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            image = part.as_image()
            image.save(str(output_path))
            print(f"Image saved to: {output_path.absolute()}")
            image_saved = True
        elif hasattr(part, "text") and part.text:
            text_response.append(part.text)

    if text_response:
        print(f"Model response: {' '.join(text_response)}")

    if not image_saved:
        print("Warning: No image was generated in the response", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
