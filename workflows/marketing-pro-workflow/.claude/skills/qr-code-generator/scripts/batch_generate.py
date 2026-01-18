#!/usr/bin/env python3
"""
Batch-generate QR codes from a CSV with columns:
  id,url,label

Example:
  python batch_generate.py --csv inputs.csv --outdir /mnt/data/qrs --format svg --error H

Requires: qrcode, pillow (for PNG)
"""
from __future__ import annotations

import argparse
import csv
import os
import subprocess
import sys
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True, help="Path to CSV file with id,url,label columns.")
    ap.add_argument("--outdir", required=True, help="Output directory.")
    ap.add_argument("--format", default="svg", choices=["png","svg","both"])
    ap.add_argument("--error", default="H", choices=["L","M","Q","H"])
    ap.add_argument("--show-url", action="store_true")
    args = ap.parse_args()

    Path(args.outdir).mkdir(parents=True, exist_ok=True)

    script = Path(__file__).with_name("generate_qr.py")
    with open(args.csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            _id = (row.get("id") or "").strip()
            url = (row.get("url") or "").strip()
            label = (row.get("label") or "").strip()
            if not _id or not url:
                continue

            png = os.path.join(args.outdir, f"{_id}.png") if args.format in ("png","both") else ""
            svg = os.path.join(args.outdir, f"{_id}.svg") if args.format in ("svg","both") else ""

            cmd = [sys.executable, str(script), "--url", url, "--error", args.error]
            if png: cmd += ["--png", png]
            if svg: cmd += ["--svg", svg]
            if label: cmd += ["--caption-label", label]
            if args.show_url: cmd += ["--show-url"]

            subprocess.check_call(cmd)

if __name__ == "__main__":
    main()
