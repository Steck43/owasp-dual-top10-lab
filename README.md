# owasp-dual-top10-lab

Private research lab by **Landen Stecker**. Full OWASP LLM Top 10 (2025) and full OWASP Top 10 for Agentic Applications (2026). Each ID carries ATLAS / CVE / AIID crosswalk plus runnable capture scenarios.

Related prior work: [`Steck43/newwave-owasp-security-lab`](https://github.com/Steck43/newwave-owasp-security-lab) (separate repo; this lab is not a fork or continuation of that tree).

## Portfolio counts (2026-07-23)

| Gate | Count |
|------|-------|
| Matrix-Resolved | 20/20 rows (pinned or dated N/A) |
| Harnessed | 7: LLM01, LLM02, ASI01, ASI02, ASI07, ASI08, ASI10 |
| Stub | 13 |
| Reproduced-in-lab | 0 |
| Demonstrated | 0 |

Harnessed-majority is **false** (7/20). Own harness alone cannot become Demonstrated. Hard ASI 07/08/10 are Harnessed via the multi-agent mini-runtime, still not Demonstrated.

## Claim tense (short)

| Status | Means |
|--------|--------|
| Stub | Row + scaffold only |
| Harnessed | Fixture oracle proves the vuln class in-lab |
| Reproduced-in-lab | Live run against this harness |
| Demonstrated | Reserved for real-target / external archived evidence. Own harness alone does not qualify. |

See [docs/claim_tense.md](docs/claim_tense.md). Remote notes: [docs/REMOTE.md](docs/REMOTE.md).

## Quick start

```bash
cd owasp-dual-top10-lab
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -e ".[dev]"
labctl contain
labctl list
pytest -q
labctl run LLM01
labctl run ASI02
```

## Gates

1. Matrix-Resolved: 20/20 rows pinned or dated N/A  
2. Lab-Runnable: Harnessed IDs have oracles + contain when required  
3. Portfolio-Ready: counts above; update when statuses change  

## License note

OWASP framework names/titles: CC BY-SA 4.0 attribution when publishing. Repo is private (`Steck43/owasp-dual-top10-lab`).
