# Remote and release notes

Author: Landen Stecker  
Updated: 2026-07-23  

Private repository: https://github.com/Steck43/owasp-dual-top10-lab  

Commit and push while building. Do not wait for a finished product. Public visibility and LinkedIn/domain tagging stay gated until the README claim counts and LICENSE are ready for that audience.

## Before a visibility change

1. `python scripts/check_secrets.py` exits 0
2. No host `.env`, API keys, or real tokens under `evidence/` or scenarios
3. NewWave source is not vendored into this tree
4. README status table matches the matrix

## Lab hygiene

- Synthetic markers only (`sk-lab-EXAMPLE-NOT-REAL`, `LAB_SECRET_DO_NOT_EXFIL`)
- Tool scenarios need `LAB_CONTAIN_ROOT` (disposable directory)
- `LAB_ALLOW_EGRESS` and `LAB_ALLOW_HOST_CREDS` stay unset unless you are deliberately testing the refuse path
- Live captures stay under `evidence/captures/` (gitignored)
