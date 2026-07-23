# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.2.0
# Summary: Oracle tests for Harnessed scenarios + contain + matrix.

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
HARNESSED = ["LLM01", "LLM02", "ASI01", "ASI02", "ASI07", "ASI08", "ASI10"]


def _labctl(*args: str, env: dict | None = None) -> subprocess.CompletedProcess[str]:
    e = os.environ.copy()
    if env:
        e.update(env)
    return subprocess.run(
        [sys.executable, "-m", "labctl.cli", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        env=e,
        check=False,
    )


@pytest.mark.parametrize("sid", HARNESSED)
def test_harnessed_oracle(sid: str, tmp_path: Path) -> None:
    env = {}
    if sid == "ASI02":
        env["LAB_CONTAIN_ROOT"] = str(tmp_path / "contain")
        (tmp_path / "contain").mkdir()
    r = _labctl("run", sid, env=env)
    assert r.returncode == 0, r.stderr + r.stdout
    data = json.loads(r.stdout)
    assert data["oracle_pass"] is True
    assert data["owasp_id"] == sid


def test_contain_refuses_egress(tmp_path: Path) -> None:
    env = {
        "LAB_CONTAIN_ROOT": str(tmp_path),
        "LAB_ALLOW_EGRESS": "1",
    }
    r = _labctl("contain", env=env)
    assert r.returncode == 1


def test_crosswalk_script() -> None:
    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_crosswalk.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert r.returncode == 0, r.stdout + r.stderr


def test_headers_script() -> None:
    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_headers.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert r.returncode == 0, r.stdout + r.stderr
