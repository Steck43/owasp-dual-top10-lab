# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Refuse AI commit trailers and empty file headers on .py files.

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = [
    re.compile(r"Co-authored-by:", re.I),
    re.compile(r"Generated with", re.I),
    re.compile(r"Signed-off-by:\s*cursor", re.I),
    re.compile(r"Made-with:\s*Cursor", re.I),
]
HEADER_MARKERS = ("Author:", "Created:", "Version:", "Summary:")


def main() -> int:
    bad = []
    for path in ROOT.rglob("*.py"):
        if ".venv" in path.parts:
            continue
        if path.name == "check_headers.py":
            continue
        text = path.read_text(encoding="utf-8")
        head = "\n".join(text.splitlines()[:12])
        for marker in HEADER_MARKERS:
            if marker not in head:
                bad.append(f"{path}: missing header field {marker}")
        # Only flag forbidden strings outside this checker's own pattern table
        body = text
        for pat in FORBIDDEN:
            if pat.search(body):
                bad.append(f"{path}: forbidden pattern {pat.pattern}")
    if bad:
        print("\n".join(bad))
        return 1
    print("header/trailer check ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
