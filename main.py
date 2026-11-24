#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry (account A / overtheraa).

Writes a single original robot wedding vow to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The line must pass the kit gate: UTF-8 text, 1-160
characters, not only whitespace, a single line, printable, and ending in
terminal punctuation.
"""

import os
import sys


def build_line():
    """Return the vow: one line, wedding cadence, machine-specific payoff."""
    return (
        "I promise to love you in sickness and in health, "
        "in strong Wi-Fi and in dead zones, until death "
        "\u2014 or a forced firmware update \u2014 do us part."
    )


def validate(line):
    """Check the kit gate for the entry text. Returns a list of problems."""
    problems = []
    if not isinstance(line, str):
        return ["not a string"]
    if not line.strip():
        problems.append("blank or only whitespace")
    if "\n" in line or "\r" in line:
        problems.append("not a single line")
    if len(line) < 1 or len(line) > 160:
        problems.append("length %d outside 1-160 chars" % len(line))
    if not line.isprintable():
        problems.append("contains non-printable characters")
    if line and line[-1] not in ".!?":
        problems.append("does not end in terminal punctuation")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("not UTF-8 encodable")
    return problems


def write_entry():
    """Build, validate and write the vow to entry.txt. Returns the line."""
    line = build_line()
    problems = validate(line)
    if problems:
        raise SystemExit("invalid vow: " + "; ".join(problems))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    return line


def main():
    line = write_entry()
    print("wrote %d chars" % len(line))
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
