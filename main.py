#!/usr/bin/env python3
"""Worst Superpower — one-line entry for make.fun.

Writes a single line (plus trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is the entry itself: one useless superpower, punch in the first clause.
"""
import os

LINE = "I have super strength — but only in my left pinky finger. Nowhere else. Ever."

def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
