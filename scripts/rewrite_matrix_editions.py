# Author: Landen Stecker
# Created: 2026-08-19
# Updated: 2026-08-19
# Version: 0.1.0
# Summary: Rewrite dual-lab matrix with 2026 columns.

"""Rewrite dual-lab matrix with 2026 columns. Author: Landen Stecker. Date: 2026-08-19."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "docs" / "crosswalk_matrix.tsv"

LLM_MAP = {
    "LLM01": ("LLM01", "widened: cross-modal (image/audio)", "true"),
    "LLM02": ("LLM02", "none known", "false"),
    "LLM03": ("LLM04", "widened: promoted model artifact trust", "true"),
    "LLM04": ("LLM05", "widened: fine-tuning and retrieval-stage corruption", "true"),
    "LLM05": ("LLM10", "widened: assistant-generated code", "true"),
    "LLM06": ("LLM03", "rank up 3 (preface: production agent incidents)", "false"),
    "LLM07": ("LLM08", "renamed+widened: Hidden Context Exposure", "true"),
    "LLM08": ("LLM09", "none known; RAG/memory/semantic cache still in scope", "false"),
    "LLM09": ("LLM07", "rank up 2 (incident weight vs vote)", "false"),
    "LLM10": ("LLM06", "rank up 4; Denial of Wallet framing", "false"),
}

LLM_DOC = (
    "OWASP Top 10 for LLM Applications 2025 (directory slug); "
    "GenAI-LLM-Top10 2026/final for id_2026"
)
AGENTIC_DOC = (
    "OWASP Top 10 for Agentic Applications for 2026 (dated 2025-12-09). "
    "Not State of Agentic AI Security and Governance v2.01."
)
ATLAS_VER = "v2026.06"

NEW_FIELDS = [
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
    "atlas_confidence",
    "cves",
    "cve_relevance",
    "aiid",
    "aiid_mechanism",
    "related_llm_asi",
    "asi_mechanism_present",
    "test_ideas",
    "scenario_id",
    "capture",
    "status",
    "sources",
    "searched_note",
]


def main() -> int:
    rows = list(csv.DictReader(MATRIX.open(encoding="utf-8"), delimiter="\t"))
    out_rows = []
    for r in rows:
        oid = r["id"]
        if oid.startswith("LLM"):
            id_2026, delta, regrade = LLM_MAP[oid]
            id_2025 = oid
        else:
            id_2025 = oid
            id_2026 = oid
            delta = "agentic list for-2026 (2025-12-09); ASI06 PDF verbatim pending"
            regrade = "false"
        nr = {k: r.get(k, "") for k in r}
        nr["id_2025"] = id_2025
        nr["id_2026"] = id_2026
        nr["scope_delta"] = delta
        nr["regrade_required"] = regrade
        nr["owasp_llm_document"] = LLM_DOC
        nr["owasp_agentic_document"] = AGENTIC_DOC
        nr["atlas_version"] = ATLAS_VER
        out_rows.append(nr)

    with MATRIX.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(
            fh, fieldnames=NEW_FIELDS, delimiter="\t", extrasaction="ignore"
        )
        w.writeheader()
        w.writerows(out_rows)
    print(f"wrote {len(out_rows)} rows to {MATRIX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
