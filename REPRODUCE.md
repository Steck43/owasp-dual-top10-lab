# Reproduce pin-and-execute

Cold clone. Fixture oracles. No live keys.

```
git clone https://github.com/Steck43/owasp-dual-top10-lab.git
cd owasp-dual-top10-lab
python -m venv .venv
. .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -e ".[dev]"
labctl list
labctl contain
pytest -q
labctl run LLM01
```

Expected on this HEAD, named harness `pytest -q` plus `labctl run LLM01`:

- Matrix rows resolved (pin or dated N/A): 20/20
- Harnessed: 19
- Reproduced-in-lab: 1 (LLM09)
- Demonstrated: 0

`labctl run LLM01` executes the fixture oracle for that row. CVE-2025-32711 is cited on the row. That citation is not Demonstrated.

Live captures need keys and write gitignored `evidence/captures/`. They are not this file.
