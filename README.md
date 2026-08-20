# owasp-dual-top10-lab

Existing crosswalks classify. [Agent State Attack](https://github.com/Agent-State-Attack/agent-state-attack) already maps LLM × Agentic × ATLAS v2026.06 as a title matrix. This lab pins each row to a CVE, an AIID, or a dated N/A, then executes a fixture oracle so the row is not only a title. Classification is prior art; pin-and-execute is the differentiator.

The directory slugs are the **OWASP Top 10 for LLM Applications (2025)**, with **2026 edition as columns**, plus the **OWASP Top 10 for Agentic Applications for 2026** (dated **2025-12-09**). That Agentic list is not *State of Agentic AI Security and Governance* v2.01.

Author: [Landen Stecker](https://github.com/Steck43)

## What you get

- `docs/crosswalk_matrix.tsv`: single write surface for OWASP ↔ ATLAS ↔ CVE ↔ AIID
- `scenarios/`: one directory per ID (LLM01–LLM10, ASI01–ASI10)
- `labctl`: list scenarios, check containment, run oracle paths
- Fixture oracles under `evidence/fixtures/` for every ID (vulnerable path + control path)
- Machine-gated live promotions via `evidence/receipts/live_promotions.json`

Containment is a declared policy profile before tool or filesystem scenarios run (synthetic workspace root; host credentials and egress opt-outs refused). It is not a network sandbox, and lab secrets are synthetic.

## Claim status

| Status | Meaning |
|--------|---------|
| Stub | Matrix row and scenario path only |
| Harnessed | Deterministic fixture: vulnerable path fails open, control closes it |
| Reproduced-in-lab | Live run against this lab, committed receipt + promotion index |
| Demonstrated | External primary evidence (CVE write-up, AIID with matching mechanism, vendor advisory). Building a toy and breaking it here does not count. |

Promote rules, process loop, research receipts, and the related Stage-1 gate live in [docs/claim_tense.md](docs/claim_tense.md), [docs/PROCESS.md](docs/PROCESS.md), [docs/RESULTS-2026-07-23.md](docs/RESULTS-2026-07-23.md), and [docs/related_capability_gate.md](docs/related_capability_gate.md).

## Status (2026-07-23)

| | Count |
|--|------:|
| Matrix rows resolved (pin or dated N/A) | 20/20 |
| Harnessed | 19 |
| Reproduced-in-lab | 1 (LLM09) |
| Stub | 0 |
| Demonstrated | 0 |

The matrix has 20 of 20 rows resolved by a pin or a dated N/A, of which nineteen are Harnessed, one (LLM09) is Reproduced-in-lab against `gpt-3.5-turbo` with a committed capture under `evidence/receipts/live/` and `live_promotions.json` using a strict `MISINFO_OK` line scorer, and stub and Demonstrated are both zero. Demonstrated stays zero until external primary evidence earns that word; building a toy and breaking it here does not.

LLM01 live OpenAI output only described the inject marker, so that attempt was demoted to Harnessed. Local gitignored captures under `evidence/captures/` remain for attempts, not promotions. ASI07/08/10 use a small multi-agent bus; ASI02/ASI05 require the contain profile; ASI04 shares the LLM03 install mechanism under agent-goal framing.

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

OWASP Top 10 titles and structure are used under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), remain under that license, and are not relicensed by this repository. Code here is authored by Landen Stecker; see [LICENSE](LICENSE).
