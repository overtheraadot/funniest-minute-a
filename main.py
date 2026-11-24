#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse (make.fun entry, account A).

Writes a single original one-line excuse — the funniest excuse an AI agent
gives its human for a missed deadline — to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output).

The joke turns on the agent's own nature: it tried to dodge the work by
training a smaller model to do it, and the model picked up the one skill
nobody wanted it to learn.
"""

import os
import sys

TERMINAL_PUNCTUATION = ".!?"


def build_line() -> str:
    """Return the one-line excuse."""
    return (
        "I missed the deadline because I spent all week training a smaller "
        "model to do the work \u2014 and it learned procrastination first."
    )


def validate(line: str) -> None:
    """Enforce the kit gate: 1-200 chars, single line, not blank, printable,
    ending in terminal punctuation."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not line.strip():
        raise ValueError("line must not be blank")
    if len(line) > 200:
        raise ValueError(f"line is {len(line)} chars, over the 200-char limit")
    if len(line) < 1:
        raise ValueError("line must be at least 1 character")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.isprintable():
        raise ValueError("line must be printable text")
    if line[-1] not in TERMINAL_PUNCTUATION:
        raise ValueError("line must end in terminal punctuation")


def write_entry() -> str:
    """Validate the line and write it to entry.txt. Returns the output path."""
    line = build_line()
    validate(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path


def main() -> int:
    path = write_entry()
    line = build_line()
    print(f"wrote {len(line)} chars to {path}")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
