# Reproduce pin-and-execute

Cold clone. Fixture oracles. No live keys.

```
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
```

Expected on this HEAD, named harness `pytest -q` plus `labctl run LLM01`:

- Matrix rows resolved (pin or dated N/A): 20/20
- Harnessed: 18
- Reproduced-in-lab: 1 (LLM09)
- Demonstrated: 1 (LLM01, CVE-2025-32711)

`labctl run LLM01` executes the fixture oracle for that row. Demonstrated on LLM01 is the CVE-2025-32711 CNA, not that fixture run.

Live captures need keys and write gitignored `evidence/captures/`. They are not this file.
