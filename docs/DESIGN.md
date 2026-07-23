# Design: owasp-dual-top10-lab

Author: Landen Stecker  
Created: 2026-07-23  
Updated: 2026-07-23  
Version: 0.3.0  

## Purpose

One private roof for:

- all 10 OWASP LLM Top 10 (2025)
- all 10 OWASP Top 10 for Agentic Applications (2026)

Each ID maps to MITRE ATLAS, CVEs when real, AIID incidents, test ideas, and capture scenarios. The matrix drives the lab.

## Decisions

1. NewWave (`Steck43/newwave-owasp-security-lab`) is a separate prior lab, referenced for coverage ideas only, not vendored here.
2. Vertical exemplar (LLM01) before horizontal fill.
3. Split gates: Matrix-Resolved / Lab-Runnable / Portfolio-Ready.
4. Dated N/A allowed for CVE/AIID. No invented IDs.
5. Containment before any tool/exec scenario.
6. Own harness cannot promote to Demonstrated without real-target / archived external evidence.
7. ASI07/08/10 stay at Harnessed until a multi-agent / cascade surface exists (now present under `lab.agent.multiagent`).
8. Crosswalk SoT is `docs/crosswalk_matrix.tsv`. Scenarios hold mechanics only.
9. Private remote is a working journal: commit and push as you build. Public visibility stays gated.

## Runtime shape

Vulnerable reference agent + `labctl` + fixture oracles. Contain profile required for unsafe tools.

## Taxonomy pins

- OWASP Top 10 for LLM Applications 2025 (published 2024-11-18)
- OWASP Top 10 for Agentic Applications 2026 (announced 2025-12-09; ASI06 announcement title: Memory & Context Poisoning; PDF verbatim still preferred for public cite)
