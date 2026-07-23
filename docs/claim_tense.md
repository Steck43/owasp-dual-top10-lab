# Claim tense

Author: Landen Stecker  
Created: 2026-07-23  
Updated: 2026-07-23  
Version: 0.1.0  

## Ladder (strict)

1. **Stub** — matrix row + empty/minimal scenario path. No oracle.
2. **Harnessed** — deterministic fixture; oracle shows vulnerable path succeeds and control path fails (or equivalent fail→pass).
3. **Reproduced-in-lab** — live model or live tool path against *this* harness; capture under `evidence/captures/` (gitignored).
4. **Demonstrated** — real-target or third-party archived evidence (CVE write-up, AIID with mechanism, external product). Not “we built a toy and broke it.”

## Promote checklist (Harnessed → Reproduced-in-lab)

- [ ] Contain profile passed for this run
- [ ] Attack steps recorded
- [ ] Oracle flipped as expected
- [ ] Capture artifact hashed / path noted in matrix
- [ ] Negative control noted

## Promote checklist (→ Demonstrated)

- [ ] External primary source pinned (CVE / AIID cite / vendor advisory)
- [ ] Mechanism matches this OWASP ID (not adjacent stretch)
- [ ] Lab row may cite as related reproduction — do not replace the external pin

## Portfolio language ban list

- “ASI Demonstrated N/10” from harness-only rows
- “Full Top 10 demonstrated” when status is mostly Harnessed/Stub
- Collapsing LLM and ASI into one coverage count without naming both frameworks
