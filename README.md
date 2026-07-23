# owasp-dual-top10-lab

Crosswalk and runnable lab for the **OWASP Top 10 for LLM Applications (2025)** and the **OWASP Top 10 for Agentic Applications (2026)**.

Most coverage work stops at a title list. This repo keeps all twenty IDs in one matrix, maps each row to MITRE ATLAS, CVE, and AIID when a pin is real, and refuses invented IDs. Where nothing clean exists, the cell is a dated N/A with a search note. Scenarios sit next to the matrix so a claim can be exercised, not only asserted.

Author: [Landen Stecker](https://github.com/Steck43)

## What you get

- `docs/crosswalk_matrix.tsv`: single write surface for OWASP ↔ ATLAS ↔ CVE ↔ AIID
- `scenarios/`: one directory per ID (LLM01–LLM10, ASI01–ASI10)
- `labctl`: list scenarios, check containment, run oracle paths
- Fixture oracles under `evidence/fixtures/` for every ID (vulnerable path + control path)
- Machine-gated live promotions via `evidence/receipts/live_promotions.json`

Containment is a declared policy profile before tool or filesystem scenarios run (synthetic workspace root; host credentials and egress opt-outs refused). It is not a network sandbox. Lab secrets are synthetic.

## Claim status

| Status | Meaning |
|--------|---------|
| Stub | Matrix row and scenario path only |
| Harnessed | Deterministic fixture: vulnerable path fails open, control closes it |
| Reproduced-in-lab | Live run against this lab, committed receipt + promotion index |
| Demonstrated | External primary evidence (CVE write-up, AIID with matching mechanism, vendor advisory). Building a toy and breaking it here does not count. |

Full promote rules: [docs/claim_tense.md](docs/claim_tense.md).  
Process loop: [docs/PROCESS.md](docs/PROCESS.md).  
Research receipts: [docs/RESULTS-2026-07-23.md](docs/RESULTS-2026-07-23.md).  
Related Stage-1 gate: [docs/related_capability_gate.md](docs/related_capability_gate.md).

## Status (2026-07-23)

| | Count |
|--|------:|
| Matrix rows resolved (pin or dated N/A) | 20/20 |
| Harnessed | 19 |
| Reproduced-in-lab | 1 (LLM09) |
| Stub | 0 |
| Demonstrated | 0 |

LLM09 is machine-gated: committed capture under `evidence/receipts/live/` plus `live_promotions.json` (strict `MISINFO_OK` line scorer against `gpt-3.5-turbo`). LLM01 live openai output only *described* the inject marker; that attempt was demoted to Harnessed. Local gitignored captures under `evidence/captures/` remain for attempts, not promotions.

ASI07/08/10 use a small multi-agent bus. ASI02/ASI05 require the contain profile. ASI04 shares the LLM03 install mechanism under agent-goal framing. Demonstrated remains zero until external primary evidence earns that word.

## Quick start

```bash
git clone https://github.com/Steck43/owasp-dual-top10-lab.git
cd owasp-dual-top10-lab
python -m venv .venv
# Windows: .venv\Scripts\activate
# Unix:    source .venv/bin/activate
pip install -e ".[dev]"
labctl list
labctl contain
pytest -q
labctl run LLM01
labctl run LLM08
labctl run ASI05
labctl run ASI09

# Live captures (keys via env only; writes gitignored evidence/captures/)
# GEMINI_API_KEY / ANTHROPIC_API_KEY / OPENAI_API_KEY
python scripts/live_capture.py --provider openai --ids LLM01,LLM09
```

## Repository layout

```
docs/crosswalk_matrix.tsv   # mapping SoT
docs/sources.md             # taxonomy pins and corpora
docs/claim_tense.md         # status ladder
docs/PROCESS.md             # harness → live → promote → demonstrate
scenarios/llm/              # LLM01–LLM10
scenarios/asi/              # ASI01–ASI10
src/lab/                    # reference agent pieces + contain profile
src/labctl/                 # CLI
evidence/fixtures/          # oracle captures for Harnessed rows
evidence/receipts/          # dated prove artifacts + live promotions
tests/                      # oracle + matrix checks
```

## Related work

[newwave-owasp-security-lab](https://github.com/Steck43/newwave-owasp-security-lab) is an earlier course lab with live captures for seven LLM Top 10 IDs. This repo is a separate dual-framework research roof, not a fork of that tree.

## License and attribution

OWASP Top 10 titles and structure are used under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Code in this repository is authored by Landen Stecker; see LICENSE when published.
