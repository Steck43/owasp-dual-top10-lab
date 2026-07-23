# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.2.0
# Summary: Require 20 matrix rows; pinned or dated N/A; Harnessed wave set.

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "docs" / "crosswalk_matrix.tsv"
HARNESSED = {"LLM01", "LLM02", "ASI01", "ASI02", "ASI07", "ASI08", "ASI10"}


def _cell_ok(row: dict, key: str) -> bool:
    val = (row.get(key) or "").strip()
    note = (row.get("searched_note") or "").strip()
    if not val:
        return "searched" in note.lower() or "none" in note.lower()
    if val.lower().startswith("none"):
        return "searched" in note.lower() or "2026-" in note or "2026-" in val
    return True


def main() -> int:
    rows = list(csv.DictReader(MATRIX.open(encoding="utf-8"), delimiter="\t"))
    if len(rows) != 20:
        print(f"expected 20 rows, got {len(rows)}")
        return 1
    ids = {r["id"] for r in rows}
    need = {f"LLM{i:02d}" for i in range(1, 11)} | {f"ASI{i:02d}" for i in range(1, 11)}
    if ids != need:
        print("id set mismatch", sorted(need - ids), sorted(ids - need))
        return 1
    for r in rows:
        for key in ("atlas", "cves", "aiid"):
            if not _cell_ok(r, key):
                print(f"{r['id']}: {key} empty without dated N/A in searched_note")
                return 1
        if not (r.get("searched_note") or "").strip():
            print(f"{r['id']}: missing searched_note")
            return 1
    for hid in HARNESSED:
        row = next(r for r in rows if r["id"] == hid)
        if row["status"] != "Harnessed":
            print(f"{hid} must be Harnessed")
            return 1
        if not (row.get("capture") or "").strip():
            print(f"{hid} missing capture path")
            return 1
    print("crosswalk check ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
