#!/usr/bin/env python3
"""
Generate a QR code that encodes a URL. Export PNG and/or SVG.
Optionally add a caption (label and/or URL) under the QR.

Examples:
  python generate_qr.py --url "https://example.com" --png "/mnt/data/qr.png" --svg "/mnt/data/qr.svg"
  python generate_qr.py --url "https://example.com" --png "/mnt/data/qr.png" --caption-label "Scan me" --show-url

Notes:
- Requires: qrcode, pillow (PIL)
"""

from __future__ import annotations

import argparse
import sys
from urllib.parse import urlparse, urlencode, parse_qsl, urlunparse

import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H

def validate_url(u: str) -> str:
    u = u.strip()
    parsed = urlparse(u)
    if parsed.scheme not in ("http", "https"):
        raise ValueError("URL must start with http:// or https://")
    if not parsed.netloc:
        raise ValueError("URL must include a domain (netloc).")
    return u

def add_utm(url: str, utm: dict[str, str]) -> str:
    parsed = urlparse(url)
    query = dict(parse_qsl(parsed.query, keep_blank_values=True))
    # Only set if provided and non-empty
    for k, v in utm.items():
        if v:
            query[f"utm_{k}"] = v if k.startswith(("source","medium","campaign","content","term")) else v
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))

def err_level(level: str):
    level = level.upper()
    return {
        "L": ERROR_CORRECT_L,
        "M": ERROR_CORRECT_M,
        "Q": ERROR_CORRECT_Q,
        "H": ERROR_CORRECT_H,
    }[level]

def make_qr(data: str, error: str, box_size: int, border: int):
    qr = qrcode.QRCode(
        version=None,
        error_correction=err_level(error),
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    return qr

def export_png(qr, path: str, caption_label: str | None, show_url: bool, url: str | None):
    from PIL import Image, ImageDraw, ImageFont

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    if not (caption_label or (show_url and url)):
        img.save(path)
        return

    font = ImageFont.load_default()
    lines = []
    if caption_label:
        lines.append(caption_label.strip())
    if show_url and url:
        lines.append(url.strip())

    # Measure text
    draw = ImageDraw.Draw(img)
    padding = 16
    line_h = 14  # approximate for default font
    text_h = len(lines) * (line_h + 6)

    new_w = img.width
    new_h = img.height + padding + text_h + padding
    out = Image.new("RGB", (new_w, new_h), "white")
    out.paste(img, (0, 0))

    draw2 = ImageDraw.Draw(out)
    y = img.height + padding
    for line in lines:
        bbox = draw2.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        x = max(0, (new_w - w) // 2)
        draw2.text((x, y), line, fill="black", font=font)
        y += line_h + 6

    out.save(path)

def export_svg(qr, path: str, caption_label: str | None, show_url: bool, url: str | None):
    from qrcode.image.svg import SvgImage

    img = qr.make_image(image_factory=SvgImage)
    svg = img.to_string().decode("utf-8")

    if not (caption_label or (show_url and url)):
        PathWrite(path, svg)
        return

    # Very simple SVG text injection.
    # We append text at the bottom with a viewBox expansion.
    # Works for most viewers; keep it minimal.
    caption_lines = []
    if caption_label:
        caption_lines.append(caption_label.strip())
    if show_url and url:
        caption_lines.append(url.strip())

    # Extract viewBox
    import re
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg)
    if not m:
        PathWrite(path, svg)
        return
    w = int(m.group(1))
    h = int(m.group(2))

    extra = 70 + 20 * (len(caption_lines) - 1)
    new_h = h + extra

    svg2 = re.sub(r'viewBox="0 0 \d+ \d+"', f'viewBox="0 0 {w} {new_h}"', svg, count=1)
    # Add text before closing </svg>
    text_y = h + 35
    text_elems = []
    for line in caption_lines:
        text_elems.append(
            f'<text x="{w/2:.1f}" y="{text_y}" text-anchor="middle" font-family="Arial, sans-serif" font-size="18" fill="#000">{EscapeXML(line)}</text>'
        )
        text_y += 24

    svg2 = svg2.replace("</svg>", "\n" + "\n".join(text_elems) + "\n</svg>")
    PathWrite(path, svg2)

def EscapeXML(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace('"', "&quot;")
             .replace("'", "&apos;"))

def PathWrite(path: str, content: str):
    from pathlib import Path
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(content, encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True, help="Destination URL to encode.")
    ap.add_argument("--png", default="", help="Output PNG path (optional).")
    ap.add_argument("--svg", default="", help="Output SVG path (optional).")
    ap.add_argument("--error", default="M", choices=["L","M","Q","H"], help="Error correction level.")
    ap.add_argument("--box-size", type=int, default=10, help="QR pixel size per module (PNG).")
    ap.add_argument("--border", type=int, default=4, help="Quiet zone border (modules).")
    ap.add_argument("--caption-label", default="", help="Optional caption label (e.g., 'Scan to...').")
    ap.add_argument("--show-url", action="store_true", help="Include the URL as a caption line.")
    ap.add_argument("--utm-source", default="", dest="utm_source")
    ap.add_argument("--utm-medium", default="", dest="utm_medium")
    ap.add_argument("--utm-campaign", default="", dest="utm_campaign")
    ap.add_argument("--utm-content", default="", dest="utm_content")
    ap.add_argument("--utm-term", default="", dest="utm_term")
    args = ap.parse_args()

    url = validate_url(args.url)
    utm = {
        "source": args.utm_source,
        "medium": args.utm_medium,
        "campaign": args.utm_campaign,
        "content": args.utm_content,
        "term": args.utm_term,
    }
    final_url = add_utm(url, utm) if any(utm.values()) else url

    qr = make_qr(final_url, args.error, args.box_size, args.border)

    caption_label = args.caption_label.strip() or None

    if not args.png and not args.svg:
        # Default output
        args.png = "qr.png"

    if args.png:
        export_png(qr, args.png, caption_label, args.show_url, final_url)

    if args.svg:
        export_svg(qr, args.svg, caption_label, args.show_url, final_url)

    print(final_url)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
