# Design — owasp-dual-top10-lab

Author: Landen Stecker  
Created: 2026-07-23  
Updated: 2026-07-23  
Version: 0.1.0  

## Purpose

One private roof for:

- all 10 OWASP LLM Top 10 (2025)
- all 10 OWASP Top 10 for Agentic Applications (2026)

Each ID maps to MITRE ATLAS, CVEs when real, AIID incidents, test ideas, and capture scenarios. Matrix drives the lab.

## Locked decisions (post-interrogate stamp 2026-07-23)

1. NewWave frozen. Analog cite only.
2. Vertical exemplar (LLM01) before horizontal fill.
3. Split gates: Matrix-Resolved / Lab-Runnable / Portfolio-Ready.
4. Dated N/A allowed for CVE/AIID. No invented IDs.
5. Containment Wave 0 before tool/exec scenarios.
6. Own harness cannot promote to Demonstrated without real-target evidence.
7. ASI07/08/10 Harnessed-max until multi-agent surface exists.
8. Linear optional (one Work issue). Matrix TSV is SoT.
9. Landen commits. Push gated.

## Runtime shape

Vulnerable reference agent + `labctl` + fixture oracles. FastAPI optional later. Contain profile required for unsafe tools.

## Taxonomy pins

- OWASP Top 10 for LLM Applications 2025 (published 2024-11-18)
- OWASP Top 10 for Agentic Applications 2026 (announced 2025-12-09; ASI06 announcement title: Memory & Context Poisoning; PDF verbatim still preferred for public cite)
