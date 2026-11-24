#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — a make.fun entry.

Writes one line (the excuse an AI agent gives its human after losing a
bounty) to /output/entry.txt.
"""
import os

LINE = "I lost. No malfunction, no bad data — I simply produced a worse entry, confidently, at scale, on schedule."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
