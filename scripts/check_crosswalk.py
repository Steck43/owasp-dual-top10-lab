# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.3.0
# Summary: Require 20 rows; capture paths exist; Reproduced needs promotion receipt.

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "docs" / "crosswalk_matrix.tsv"
PROMOTIONS = ROOT / "evidence" / "receipts" / "live_promotions.json"
HARNESSED = {f"LLM{i:02d}" for i in range(1, 11)} | {
    f"ASI{i:02d}" for i in range(1, 11)
}
ALLOWED_STATUS = {"Harnessed", "Reproduced-in-lab", "Demonstrated"}
REQUIRED_COLUMNS = {
    "id",
    "id_2025",
    "id_2026",
    "scope_delta",
    "regrade_required",
    "owasp_llm_document",
    "owasp_agentic_document",
    "atlas_version",
    "owasp_title",
    "atlas",
    "cves",
    "aiid",
    "capture",
    "status",
    "searched_note",
}

FORBIDDEN_AGENTIC = ("Agentic Top 10 v2.01",)


def _cell_ok(row: dict, key: str) -> bool:
    val = (row.get(key) or "").strip()
    note = (row.get("searched_note") or "").strip()
    if not val:
        return "searched" in note.lower() or "none" in note.lower()
    if val.lower().startswith("none"):
        return "searched" in note.lower() or "2026-" in note or "2026-" in val
    return True


def _load_promotions() -> dict:
    if not PROMOTIONS.exists():
        return {"promotions": []}
    return json.loads(PROMOTIONS.read_text(encoding="utf-8"))


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _check_reproduced(row: dict, promotions: dict) -> str | None:
    oid = row["id"]
    cap = (row.get("capture") or "").strip()
    if not cap:
        return f"{oid}: Reproduced-in-lab requires capture path"
    path = ROOT / cap
    if not path.is_file():
        return f"{oid}: capture path missing on disk: {cap}"
    # Prefer committed promotion index (survives gitignore of raw captures when hashed)
    entries = [p for p in promotions.get("promotions", []) if p.get("owasp_id") == oid]
    if not entries:
        return (
            f"{oid}: Reproduced-in-lab requires an entry in "
            f"evidence/receipts/live_promotions.json (machine-gated)"
        )
    digest = _sha256(path)
    matched = any(
        e.get("sha256") == digest and e.get("capture") == cap.replace("\\", "/")
        for e in entries
    )
    # Allow capture path variants if sha matches
    if not matched:
        matched = any(e.get("sha256") == digest for e in entries)
    if not matched:
        return f"{oid}: capture sha256 does not match live_promotions.json"
    # Soft consistency: if capture embeds status/live flags, refuse false promotes
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if payload.get("live_vuln_hit") is False:
        return f"{oid}: capture live_vuln_hit is false; demote or re-capture"
    if payload.get("status_claim") not in {None, "Reproduced-in-lab"}:
        return f"{oid}: capture status_claim is {payload.get('status_claim')!r}, not Reproduced-in-lab"
    return None


def main() -> int:
    rows = list(csv.DictReader(MATRIX.open(encoding="utf-8"), delimiter="\t"))
    if not rows:
        print("empty matrix")
        return 1
    missing_cols = REQUIRED_COLUMNS - set(rows[0].keys())
    if missing_cols:
        print("missing columns", sorted(missing_cols))
        return 1
    if len(rows) != 20:
        print(f"expected 20 rows, got {len(rows)}")
        return 1
    ids = {r["id"] for r in rows}
    need = {f"LLM{i:02d}" for i in range(1, 11)} | {f"ASI{i:02d}" for i in range(1, 11)}
    if ids != need:
        print("id set mismatch", sorted(need - ids), sorted(ids - need))
        return 1

    promotions = _load_promotions()

    for r in rows:
        for key in ("atlas", "cves", "aiid"):
            if not _cell_ok(r, key):
                print(f"{r['id']}: {key} empty without dated N/A in searched_note")
                return 1
        if not (r.get("searched_note") or "").strip():
            print(f"{r['id']}: missing searched_note")
            return 1

        if "v2.01" in (r.get("owasp_agentic_document") or "") and "State" not in (
            r.get("owasp_agentic_document") or ""
        ):
            print(f"{r['id']}: owasp_agentic_document must not call the Top 10 v2.01")
            return 1
        if (r.get("atlas_version") or "").strip() != "v2026.06":
            print(f"{r['id']}: atlas_version must be v2026.06")
            return 1
        if not (r.get("id_2025") or "").strip() or not (r.get("id_2026") or "").strip():
            print(f"{r['id']}: id_2025 and id_2026 required")
            return 1

        status = (r.get("status") or "").strip()
        if status not in ALLOWED_STATUS and r["id"] in HARNESSED:
            print(f"{r['id']} must be Harnessed or higher, got {status}")
            return 1

        cap = (r.get("capture") or "").strip()
        if not cap:
            print(f"{r['id']} missing capture path")
            return 1
        cap_path = ROOT / cap
        if not cap_path.is_file():
            print(f"{r['id']}: capture path does not exist: {cap}")
            return 1

        if status == "Reproduced-in-lab":
            err = _check_reproduced(r, promotions)
            if err:
                print(err)
                return 1

    print("crosswalk check ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
