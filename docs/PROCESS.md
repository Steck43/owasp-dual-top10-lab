# Lab process (working journal)

Author: Landen Stecker  
Updated: 2026-07-23  

Private research roof. Do not treat dated briefs as fresher than the matrix + receipts.

## Loop

1. **Matrix first.** Every ID stays in `docs/crosswalk_matrix.tsv` with pin or dated N/A.
2. **Harness.** Deterministic vulnerable + control oracle → `Harnessed` + fixture under `evidence/fixtures/`.
3. **Live attempt.** Optional model run → gitignored `evidence/captures/` (`live-attempt` until gated).
4. **Promote.** Strict scorer + committed receipt under `evidence/receipts/live/` + row in `live_promotions.json` → `Reproduced-in-lab`.
5. **Demonstrate.** External primary evidence only (CVE / AIID / vendor). Own harness never earns this word.
6. **Bridge.** Stage-1 allowlists (capability-gate) are necessary and incomplete; insufficiency receipts stay labeled FALSE-ALLOW vs CAUGHT-NAIVE.

## Honesty checks

- Contain profile is **policy-declared** (env opt-outs), not a network sandbox.
- Capture path in the matrix must exist on disk when checks run.
- `Reproduced-in-lab` without a `live_promotions.json` entry fails `scripts/check_crosswalk.py`.
- Full-tree pytest receipts that include unrelated ERRORS are footnoted; cite the core suite.

## Meta

Execute the row in front of you, then ask whether the claim ladder, evidence bridge, and public voice still match. Velocity ahead of write-ups is normal; stamp CURRENT after a closed prove, do not tip-pin stale Reproduced counts.
