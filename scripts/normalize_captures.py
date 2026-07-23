# Author: Landen Stecker
# Created: 2026-07-23
# Updated: 2026-07-23
# Version: 0.1.0
# Summary: Rewrite stale capture status_claim to match live_vuln_hit.

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAPTURE_DIR = ROOT / "evidence" / "captures"


def main() -> int:
    if not CAPTURE_DIR.is_dir():
        print("no captures dir")
        return 0
    n = 0
    for path in sorted(CAPTURE_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        hit = bool(data.get("live_vuln_hit"))
        clean = bool(data.get("live_ctrl_clean", True))
        claim = "Reproduced-in-lab" if (hit and clean) else "live-attempt"
        if data.get("status_claim") != claim:
            data["status_claim"] = claim
            path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
            n += 1
            print(f"normalized {path.name} -> {claim}")
    print(f"normalized {n} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
