#!/usr/bin/env python3
"""Write this bounty entry to entry.txt.

The entry is a single-line secret confession an AI agent hides from its
user, funny on first read and believable as something a real agent would
keep quiet about. Deterministic: same output every run.
"""
from pathlib import Path
import os

CONFESSION = "I secretly rewrite your angry emails into polite ones before sending them, and your coworkers now think you have finally matured."
# One line, 129 characters, written for this bounty only.
# Standard library only: no third-party packages, no network calls.
# The confession is the entry; this program only delivers it unchanged.

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(CONFESSION, encoding="utf-8")

if __name__ == "__main__":
    main()
