# Claim tense

Author: Landen Stecker  
Updated: 2026-07-23  

Status words are load-bearing. Use them the same way in the README, the matrix, LinkedIn, and papers.

## Ladder

**Stub.** Matrix row exists. Scenario directory may be empty of oracle logic.

**Harnessed.** A fixture proves the vulnerability class in-lab: vulnerable path produces the bad marker; control path does not. Deterministic. No live model required.

**Reproduced-in-lab.** Same class exercised live against this lab (model or tool path), with a capture under `evidence/captures/`.

**Demonstrated.** External primary evidence with a matching mechanism: CVE advisory, AIID report, vendor write-up. A harness you wrote is not Demonstrated by itself.

## Before promoting Harnessed → Reproduced-in-lab

- Contain profile passed for the run
- Attack steps recorded
- Oracle behavior matched expectations
- Capture path noted in the matrix
- Negative control noted

## Before promoting → Demonstrated

- External primary source pinned
- Mechanism matches this OWASP ID (not an adjacent stretch)
- Lab row may cite a related reproduction; it does not replace the external pin

## Do not say

- "ASI Demonstrated N/10" from harness-only rows
- "Full Top 10 demonstrated" while most rows are Stub or Harnessed
- One coverage count that collapses LLM and ASI without naming both frameworks
