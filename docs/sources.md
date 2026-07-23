# Sources pin list

Author: Landen Stecker  
Created: 2026-07-23  
Updated: 2026-07-23  
Version: 0.3.0  

## Frameworks (taxonomy versions)

| Artifact | Pin |
|----------|-----|
| OWASP Top 10 for LLM Applications 2025 | Published 2024-11-18 · genai.owasp.org · CC BY-SA 4.0 · matrix search date 2026-07-23 |
| OWASP Top 10 for Agentic Applications 2026 | Announced 2025-12-09 · ASI06 title from announcement: Memory & Context Poisoning · PDF verbatim still preferred before public cite |
| MITRE ATLAS | atlas.mitre.org technique IDs as of lab search 2026-07-23; low-confidence pins marked in matrix |

## Matrix SoT

`docs/crosswalk_matrix.tsv` is the sole write surface for ATLAS / CVE / AIID mappings. Scenarios hold `owasp_id` + attack mechanics only.

## Harnessed pins (disk)

| ID | ATLAS | CVE | AIID |
|----|-------|-----|------|
| LLM01 | AML.T0051; AML.T0051.001 | CVE-2025-32711 | AIID-5307; 5329; 352 |
| LLM02 | AML.T0057 | none; searched 2026-07-23 | AIID-657 |
| ASI01 | AML.T0053 | CVE-2025-32711 (adjacent) | AIID-5307; 352 |
| ASI02 | AML.T0098 | none; searched 2026-07-23 | AIID-1152; 1210 |
| ASI07 | AML.T0054 | none; searched 2026-07-23 | none; searched 2026-07-23 |
| ASI08 | none; searched 2026-07-23 | none | none |
| ASI10 | none; searched 2026-07-23 | none | AIID-1152 |

## Local corpora

| Path | Use |
|------|-----|
| `C:\Users\lande\Engineering_and_Development\aiid-snapshot-20260713` | AIID offline search |
| Vault Security teardowns / Standards-Baseline-Map | Incident ↔ framework joins |
| NewWave `Projects/csen296/docs/owasp_coverage.md` | Prior coverage notes (ideas reference) |
