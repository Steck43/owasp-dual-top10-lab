# Remote

Author: Landen Stecker  
Created: 2026-07-23  
Updated: 2026-07-23  
Version: 0.3.0  

## Status

Private repo: https://github.com/Steck43/owasp-dual-top10-lab  

Treat `master` as a working journal. Commit and push while building. Do not wait for a finished product. Public visibility stays gated.

## Before visibility changes

1. `python scripts/check_secrets.py` exits 0.
2. No host `.env`, API keys, or real tokens under `evidence/` or scenarios.
3. No NewWave source tree vendored into this repo.
4. Visibility remains **private** unless explicitly flipped later.

## Payload / secrets hygiene

- Lab secrets are synthetic markers (`sk-lab-EXAMPLE-NOT-REAL`, `LAB_SECRET_DO_NOT_EXFIL`).
- Tool scenarios require `LAB_CONTAIN_ROOT` (disposable dir); never read host credential stores.
- Default: `LAB_ALLOW_EGRESS` unset (deny). `LAB_ALLOW_HOST_CREDS` unset (refuse).
- Captures under `evidence/captures/` stay gitignored.
