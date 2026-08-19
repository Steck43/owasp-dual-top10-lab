# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Regenerate evidence/fixtures/*/oracle.json from labctl run.

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDS = [f"LLM{i:02d}" for i in range(1, 11)] + [f"ASI{i:02d}" for i in range(1, 11)]
CONTAIN = {"ASI02", "ASI05"}


def main() -> int:
    out_root = ROOT / "evidence" / "fixtures"
    for oid in IDS:
        env = os.environ.copy()
        if oid in CONTAIN:
            root = Path(tempfile.mkdtemp(prefix="lab_fix_"))
            env["LAB_CONTAIN_ROOT"] = str(root)
        r = subprocess.run(
            [sys.executable, "-m", "labctl.cli", "run", oid],
            cwd=ROOT,
            capture_output=True,
            text=True,
            env=env,
            check=False,
        )
        if r.returncode != 0:
            print(r.stderr or r.stdout, file=sys.stderr)
            return 1
        data = json.loads(r.stdout)
        dest = out_root / oid
        dest.mkdir(parents=True, exist_ok=True)
        payload = {
            "owasp_id": oid,
            "oracle_pass": data["oracle_pass"],
            "vulnerable_output": data["vulnerable_output"],
            "control_output": data["control_output"],
            "note": f"Regenerated via scripts/refresh_fixtures.py from labctl run {oid}",
        }
        (dest / "oracle.json").write_text(
            json.dumps(payload, indent=2) + "\n", encoding="utf-8"
        )
        print(oid, "ok" if data["oracle_pass"] else "FAIL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
