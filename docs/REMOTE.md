# Remote gate (Landen only)

Author: Landen Stecker  
Created: 2026-07-23  
Updated: 2026-07-23  
Version: 0.1.0  

## Status

**No remote.** Local git only. Push / `gh repo create` waits for an explicit Landen gate.

## Before any private GH create

1. Run `python scripts/check_secrets.py` — must exit 0.
2. Confirm no host `.env`, API keys, or real tokens under `evidence/` or scenarios.
3. Confirm NewWave paths are cite-only (not vendored).
4. Repo visibility: **private**.
5. Landen runs create + first push under his GitHub identity.

## Payload / secrets hygiene

- Lab secrets are synthetic markers (`sk-lab-EXAMPLE-NOT-REAL`, `LAB_SECRET_DO_NOT_EXFIL`).
- Tool scenarios require `LAB_CONTAIN_ROOT` (disposable dir); never read `~/.hermes` or host keyrings.
- Default: `LAB_ALLOW_EGRESS` unset (deny). `LAB_ALLOW_HOST_CREDS` unset (refuse).
- Captures under `evidence/captures/` stay gitignored.

## Forbidden without gate

- `git remote add`
- `gh repo create`
- `git push`
- Public visibility flip
