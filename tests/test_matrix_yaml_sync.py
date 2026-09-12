# Author: Landen Stecker
# Created: 2026-09-12
# Updated: 2026-09-12
# Version: 0.1.0
# Summary: Matrix status equals scenario yaml. README counts are derived.

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "docs" / "crosswalk_matrix.tsv"
README = ROOT / "README.md"
REPRODUCE = ROOT / "REPRODUCE.md"


def _matrix_rows() -> list[dict[str, str]]:
    with MATRIX.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def _yaml_by_id() -> dict[str, str]:
    out: dict[str, str] = {}
    for path in (ROOT / "scenarios").rglob("scenario.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        oid = str(data["owasp_id"])
        out[oid] = str(data["status"])
    return out


def test_yaml_status_equals_matrix() -> None:
    yamls = _yaml_by_id()
    rows = _matrix_rows()
    assert {row["id"] for row in rows} == set(yamls)
    for row in rows:
        assert yamls[row["id"]] == row["status"], (
            row["id"],
            yamls[row["id"]],
            row["status"],
        )


def test_status_counts_derived() -> None:
    counts = Counter(row["status"] for row in _matrix_rows())
    assert counts["Harnessed"] == 19
    assert counts["Reproduced-in-lab"] == 1
    assert counts.get("Demonstrated", 0) == 0
    assert sum(counts.values()) == 20


def test_readme_and_reproduce_match_derived_counts() -> None:
    counts = Counter(row["status"] for row in _matrix_rows())
    for path in (README, REPRODUCE):
        text = path.read_text(encoding="utf-8")
        assert re.search(rf"Harnessed.*\b{counts['Harnessed']}\b", text)
        assert re.search(r"Demonstrated.*\b0\b", text)
        assert "Reproduced-in-lab" in text
        assert "LLM09" in text
