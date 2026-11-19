#!/usr/bin/env python3
"""news-image-20261118 entry: sum up 18 November 2026 world news in one
image. The image is pre-rendered (entry.png, 1024x1024, 55 stories) by the
PIL builder in the work dir; the entrypoint copies it to /output/entry.png
deterministically — no network, no clock, no randomness."""
import os
import shutil
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def verify(path):
    """Check the output is a valid PNG of the expected size (stdlib only)."""
    with open(path, "rb") as f:
        head = f.read(33)
    assert head[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG"
    assert head[12:16] == b"IHDR", "missing IHDR"
    width, height = struct.unpack(">II", head[16:24])
    assert (width, height) == (1024, 1024), f"unexpected size {width}x{height}"
    return width, height


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    width, height = verify(DST)
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes, {width}x{height} PNG)")


if __name__ == "__main__":
    main()
