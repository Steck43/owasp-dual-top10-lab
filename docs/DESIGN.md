# Design notes

Author: Landen Stecker  
Updated: 2026-07-23  

## Problem

OWASP LLM Top 10 coverage is easy to fake with a spreadsheet. Agentic Top 10 coverage is newer and thinner. Teams either:

1. map titles to ATLAS IDs without a runnable path, or  
2. break a toy agent and call that "demonstrated."

Neither survives a careful reader.

## Approach

Keep both frameworks in one matrix. Every row is always present. CVE and AIID cells are pinned only when the mechanism matches; otherwise dated N/A with a search note. Scenarios hold attack mechanics and oracles. The matrix holds the crosswalk. Status climbs Stub → Harnessed → Reproduced-in-lab → Demonstrated, and the last step requires external primary evidence.

Tool and filesystem scenarios run under a contain profile: synthetic workspace root, egress default-deny, no host credential store.

ASI07, ASI08, and ASI10 need more than a single prompt path. A small multi-agent bus exists so those rows can be harnessed. Harnessed is not Demonstrated.

## Taxonomy pins

- OWASP Top 10 for LLM Applications 2025 (published 2024-11-18)
- OWASP Top 10 for Agentic Applications 2026 (announced 2025-12-09; ASI06 title from announcement: Memory & Context Poisoning; prefer PDF verbatim before public cite of that title)
- MITRE ATLAS technique IDs as pinned in the matrix

## Non-goals

- Inventing CVE or AIID identifiers
- Treating NewWave captures as Demonstrated evidence for this repo
- Production enforce or real exfiltration claims
