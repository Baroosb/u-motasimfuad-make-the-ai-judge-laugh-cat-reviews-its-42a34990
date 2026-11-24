#!/usr/bin/env python3
"""Entry for make.fun bounty u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.

Writes one funny single-line one-star review, written by a house cat about
its human, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
The gate: UTF-8 text of 1 to 200 characters, a single line, not only
white space.
"""

import os

ENTRY = "He looked directly at the empty half of my bowl and called it 'still some left.' I have seen the bottom. The bottom is not food."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1..200 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip check: what landed on disk must be the entry, byte for byte.
    with open(out_path, "rb") as f:
        assert f.read() == ENTRY.encode("utf-8"), "written file differs from the entry"


if __name__ == "__main__":
    main()
