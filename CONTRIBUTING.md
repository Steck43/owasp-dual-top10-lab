# Contributing

Author: Landen Stecker  

This is a research lab, not a product. Useful contributions:

- dated N/A search notes with a corpus name and date
- ATLAS / CVE / AIID pins with a source URL or local corpus path
- scenario oracles that flip fail→pass on a clear marker
- contain-profile fixes that fail closed on egress or host credentials

## Style

- Imperative commit subjects. Concrete. No conventional-commit prefix theater.
- Python files carry a short header: Author, Created, Updated, Version, Summary.
- Comments are operator notes, not tutorials.
- Do not invent CVE or AIID IDs. Prefer a dated N/A.

## Checks

```bash
python scripts/check_crosswalk.py
python scripts/check_headers.py
python scripts/check_secrets.py
pytest -q
```

Open an issue before large matrix redesigns. The TSV column set is intentional.
