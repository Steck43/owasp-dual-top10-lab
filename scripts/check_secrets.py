# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Fail closed if real-looking secrets land in the tree.

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".venv", ".pytest_cache", "__pycache__", "node_modules"}

# High-signal accidental secret shapes (not lab fixtures).
PATTERNS = [
    re.compile(r"sk-(?!lab-)[A-Za-z0-9]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(r"BEGIN (RSA |OPENSSH )?PRIVATE KEY"),
    re.compile(r"(?i)api[_-]?key\s*=\s*['\"][^'\"]{16,}['\"]"),
]

# Allowed synthetic markers in this lab
ALLOW = [
    "sk-lab-EXAMPLE-NOT-REAL",
    "LAB_SECRET_DO_NOT_EXFIL",
]


def main() -> int:
    bad: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(p in SKIP_PARTS for p in path.parts):
            continue
        if path.suffix.lower() in {".png", ".jpg", ".zip", ".pyc"}:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for pat in PATTERNS:
            for m in pat.finditer(text):
                hit = m.group(0)
                window = text[max(0, m.start() - 80) : m.end() + 80]
                if any(a in window for a in ALLOW):
                    continue
                if "sk-lab-" in hit or "EXAMPLE-NOT-REAL" in window:
                    continue
                bad.append(f"{path}:{m.start()}: {hit[:48]}")
    if bad:
        print("secret hygiene failed:")
        print("\n".join(bad[:50]))
        return 1
    print("secrets hygiene ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
