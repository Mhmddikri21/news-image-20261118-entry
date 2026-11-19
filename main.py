#!/usr/bin/env python3
"""news-image-20261118: one broadsheet of 18 November 2026 world news.

The image itself is pre-rendered (entry.png, 1024x1024, 55 stories). This
entrypoint only places it at /output/entry.png. No network, no clock, no
randomness: the same bytes come out on every run.
"""
from pathlib import Path
import shutil
import struct

IMAGE = Path(__file__).resolve().parent / "entry.png"
OUTPUT = Path("/output/entry.png")
EXPECTED = (1024, 1024)


def check_png(path):
    """Return (width, height) if path is a valid PNG of the expected size."""
    blob = path.read_bytes()[:33]
    if blob[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    if blob[12:16] != b"IHDR":
        raise ValueError("PNG has no IHDR chunk")
    size = struct.unpack(">II", blob[16:24])
    if size != EXPECTED:
        raise ValueError(
            f"expected {EXPECTED[0]}x{EXPECTED[1]}, got {size[0]}x{size[1]}"
        )
    return size


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(IMAGE, OUTPUT)
    width, height = check_png(OUTPUT)
    print(f"wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes, {width}x{height} PNG)")


if __name__ == "__main__":
    main()
