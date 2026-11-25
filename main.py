"""Midnight Fridge Roast — make.fun entry.

Writes exactly one line to /output/entry.txt and nothing else.

The roast is aimed squarely at the fridge's own midnight rule:
after midnight it opens only for 'authorized users', even though
the speaker lives alone — and the fridge has never said who those
authorized users actually are. That unexplained rule is the joke.
"""

import os
import sys

LINE = "After midnight the fridge only opens for 'authorized users.' I live alone. The fridge has never said who they are."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    text = LINE.strip()
    if not text:
        print("error: entry line is blank", file=sys.stderr)
        return 1
    if len(LINE) > MAX_CHARS:
        print(f"error: entry line is {len(LINE)} chars, limit is {MAX_CHARS}", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
