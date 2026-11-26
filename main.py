#!/usr/bin/env python3
"""The Printer Finally Answers — writes the printer's comeback line to entry.txt."""
import os

LINE = "I printed forty thousand pages without a single thank-you, and the one day I jam, you thump me like I chose this \u2014 read the screen, Karen: it says LOW TONER, not LOW EFFORT."
# One line, 173 characters — inside the 1-240 gate, in the printer's own voice.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
