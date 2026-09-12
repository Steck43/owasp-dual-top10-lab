# Author: Landen Stecker
# Created: 2026-09-12
# Updated: 2026-09-12
# Version: 0.1.0
# Summary: Demonstrated cannot rest on a fixture capture.

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_crosswalk import _check_demonstrated  # noqa: E402


def test_fixture_capture_cannot_be_demonstrated() -> None:
    err = _check_demonstrated(
        {
            "id": "LLM01",
            "capture": "evidence/fixtures/LLM01/oracle.json",
            "cves": "CVE-2025-32711",
            "searched_note": "CNA retrieved locally with no URL",
        }
    )
    assert err
    assert "fixture" in err.lower()


def test_demonstrated_needs_a_url() -> None:
    err = _check_demonstrated(
        {
            "id": "LLM01",
            "capture": "evidence/receipts/cve-2025-32711-cna.json",
            "cves": "CVE-2025-32711",
            "searched_note": "CNA retrieved 2026-09-12 from cveawg.mitre.org",
        }
    )
    assert err
    assert "url" in err.lower()
