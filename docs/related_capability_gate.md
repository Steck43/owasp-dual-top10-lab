# Related work: capability-gate

Author: Landen Stecker  
Updated: 2026-07-23  

Public Stage-1 gate: [Steck43/capability-gate](https://github.com/Steck43/capability-gate)

## Split

| Artifact | Role |
|----------|------|
| capability-gate | Deny-by-default tool/path mediation for Hermes tool calls. Observe then enforce. |
| This lab | OWASP LLM + Agentic Top 10 matrix, oracles, and live captures with an honest claim ladder. |

capability-gate answers: can this skill call this tool on this path?

This lab answers: even when the surface is allowed (or the attack is prompt-only), which OWASP classes still fire, and what does a control look like?

## Evidence bridge

Dated receipts: [RESULTS-2026-07-23.md](RESULTS-2026-07-23.md)

Thesis rows in this lab: LLM01, ASI01, ASI02, ASI06, LLM06.

## Claim tense

Do not collapse the roofs. A passing gate test is not Demonstrated ASI coverage. A Harnessed lab oracle is not proof that capability-gate failed in production.
