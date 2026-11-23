#!/usr/bin/env python3
"""Make the Judge Smile -- make.fun entry.

Writes one warm line about a small good thing that happened today to
/output/entry.txt. Deterministic: no randomness, no clock, no network.
"""

import os
import sys

LINE = "Today the old man at the corner shop slipped a boiled sweet into my change and winked, like we'd shared the secret for years."

MAX_CHARS = 200


def main() -> int:
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(f"entry must be 1-{MAX_CHARS} characters, got {len(LINE)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Guard: read the file back and confirm it holds exactly the line.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != LINE + "\n":
        print("entry.txt does not match the line", file=sys.stderr)
        return 1
    if len(LINE.encode("utf-8")) > MAX_CHARS:
        print("entry exceeds the character gate in UTF-8 bytes", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
