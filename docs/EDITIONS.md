# Editions

This lab maps three external taxonomies, and all three are versioned. An ID without an
edition is not an identifier, it is a guess. Every row in
[`crosswalk_matrix.tsv`](crosswalk_matrix.tsv) therefore carries its edition, and every
receipt keeps the edition it was captured under, permanently.

**Editions targeted as of 2026-08-19**

| Taxonomy | Edition | Published | Notes |
|---|---|---|---|
| OWASP Top 10 for LLM Applications | **2026** | 2026-08-04 | Eight of ten entries moved; one renamed |
| OWASP Top 10 for Agentic Applications | **for 2026** | 2025-12-09 | CC BY-SA 4.0. See version note below. |
| MITRE ATLAS | **v2026.06** | — | Technique IDs are version-scoped |

### Version note on the Agentic list

`ASSUMPTION (verify):` the Agentic Top 10 document is **"OWASP Top 10 for Agentic
Applications for 2026," dated 2025-12-09**. A separate resource on the same OWASP page
carries **v2.01 dated 2026-06-01** and is a *different document* - *State of Agentic AI
Security and Governance*. These are not the same publication, and a secondary source that
says "the Agentic Top 10 was updated to v2.01" has conflated them.

Do not write "Agentic Top 10 v2.01." Cite the Top 10 by its own date. Name both documents
in the matrix if both are used. The official page returned HTTP 403 to automated fetch on
2026-08-19, so this note stands until the primary PDF is read directly.

Rows carried under a prior edition are not renumbered. See *Why receipts keep their
edition* below.

---

## OWASP LLM Top 10: 2025 to 2026

`SOURCE:` **Primary.** `GenAI-Security-Project/GenAI-LLM-Top10`, path `2026/final/`,
read 2026-08-19. The entry filenames are the authoritative ordering and titles, and
`LLM00_Preface.md` states the rank migration and the scope growths in the project's own
words. The mapping is a clean bijection: every 2025 ID lands on exactly one 2026 ID, no
repeats, no orphans.

`RECORD` The genai.owasp.org resource page returns HTTP 403 to automated fetch, but the
project's own repository does not. Read `2026/final/` there instead. Two secondaries had
agreed on all ten transitions and were correct on ordering; they were **wrong by omission
on scope**, naming two growths where the preface names five. Agreement between secondaries
is not coverage.

| 2025 ID | 2025 title | → | 2026 ID | 2026 title | Move | Scope delta |
|---|---|---|---|---|---|---|
| LLM01 | Prompt Injection | → | **LLM01** | Prompt Injection | held | **widened**: now covers cross-modal attacks that hide instructions inside an image or audio track |
| LLM02 | Sensitive Information Disclosure | → | **LLM02** | Sensitive Information Disclosure | held | none known |
| LLM03 | Supply Chain | → | **LLM04** | Supply Chain | down 1 | **widened**: now accounts for the trust failure when a promoted model artifact is not what it claims to be |
| LLM04 | Data and Model Poisoning | → | **LLM05** | Data and Model Poisoning | down 1 | **widened** — absorbs fine-tuning subversion; covers training, fine-tuning *and* retrieval-stage corruption |
| LLM05 | Improper Output Handling | → | **LLM10** | Improper Output Handling | **down 5** | **widened**: now spans the insecure code that assistants generate at scale, despite the rank fall |
| LLM06 | Excessive Agency | → | **LLM03** | Excessive Agency | **up 3** | largest promotion; driven by production agent incidents |
| LLM07 | System Prompt Leakage | → | **LLM08** | **Hidden Context Exposure** | down 1, **renamed** | **widened** — beyond the system prompt to tool and function schemas, RAG-retrieved policy text, developer instructions, and any context-window material not visible to the user |
| LLM08 | Vector and Embedding Weaknesses | → | **LLM09** | Vector and Embedding Weaknesses | down 1 | covers RAG, memory, semantic cache |
| LLM09 | Misinformation | → | **LLM07** | Misinformation | up 2 | rose on incident data against lower voter preference |
| LLM10 | Unbounded Consumption | → | **LLM06** | Unbounded Consumption | **up 4** | reframed around cost asymmetry; "Denial of Wallet" is now a finding |

### Methodology change worth recording

The 2026 edition is the first LLM list weighted by real-world incident data: community
vote at 75%, incident corpus at 25%.

`SOURCE:` **Primary.** `LLM00_Preface.md` in `GenAI-LLM-Top10` `2026/final/` (read 2026-08-19) states both figures as stages of the same corpus, not competing secondaries: **7,714** incidents in the corpus, **6,639** classified. Weighting is vote 75% / incidents 25%. Cite both with those roles, or cite neither.

### Scope boundary, stated by OWASP itself

The 2026 LLM list covers **the model as a component inside an application**. When the
model becomes an **actor**, calling tools and setting downstream consequences in motion,
the risk moves to the Agentic Top 10.

That boundary is why this lab maps both lists in one matrix rather than treating them as
alternatives. It is now the taxonomy's own stated division, not this lab's editorial
choice.

---

## Why directory names do not change

`scenarios/llm/LLM04_data_model_poisoning/` and `evidence/fixtures/LLM04/` keep their
names under the 2026 edition.

Directory names here are **stable slugs**, not identifiers. They appear in twenty fixture
and scenario paths, in the `scenario_id` and `capture` columns of the crosswalk, and
inside committed receipts. Renaming them to chase a renumber would:

- break every path a committed receipt refers to,
- sever the provenance of oracles generated under 2025 semantics, and
- gain nothing evidentiary, because the slug was never the claim.

Edition lives in a column. The slug is an address.

---

## Why receipts keep their edition

A receipt records what was true when it ran, under the definitions in force at that time.

**Five** of the 2026 entries grew. The preface says why: newer risks were folded into the
entries that already own them rather than splintering the list into thin new categories.
Prompt Injection took cross-modal. Supply Chain took model-artifact trust failure. Data
and Model Poisoning took fine-tuning subversion. Improper Output Handling took
assistant-generated insecure code. System Prompt Leakage became Hidden Context Exposure, a
broader frame for the same failure.

An artifact demonstrating `LLM07:2025 System Prompt Leakage` does **not** demonstrate
`LLM08:2026 Hidden Context Exposure`; it covers part of it. The same holds for every grown
entry: a 2025 capture is a subset of its 2026 category.

**Correction, 2026-08-19.** REV 1 named two growths and marked three of these rows
`none known`, read from secondary summaries. This file states that an empty `scope_delta`
is an assertion rather than an absence. Three of those assertions were wrong. The primary
preface is the source now.

So this lab distinguishes two operations:

- **Renumber** — an ID moves, the category does not. Safe as a column edit.
- **Re-grade** — the category moved. The claim must be re-earned at its rung, or it drops
  until new evidence exists.

Silently renumbering across a category change would promote a claim by editing a
taxonomy column. That is the precise failure the claim-tense ladder in
[`claim_tense.md`](claim_tense.md) exists to prevent.

### Consequence for fixture-backed versus capture-backed claims

**Fixture-backed claims survive a taxonomy move.** A fixture oracle tests a *mechanism*:
a vulnerable path that fails open and a control path that closes it. Goal hijack is goal
hijack whether it is filed under LLM04 or LLM05. This lab's twenty rungs are fixture
oracles, so the 2026 migration costs a column edit and no rung loss.

**Capture-backed claims do not.** A live model capture is bound to the category
*definition* it was taken against. Where a category widened, the capture now covers a
subset, and the rung must be re-earned.

This is why the sibling live-evidence lab stays labelled at its own edition rather than
being renumbered. Different evidence kinds migrate differently, and the honest move is to
say which kind a claim rests on.

---

## Schema

`crosswalk_matrix.tsv` carries edition as data, not as an assumption:

| Column | Meaning |
|---|---|
| `id_2025` | OWASP LLM Top 10 2025 identifier, or empty |
| `id_2026` | OWASP LLM Top 10 2026 identifier, or empty |
| `agentic_id` | OWASP Agentic Top 10 identifier |
| `owasp_llm_edition` | edition this row's mapping targets |
| `agentic_edition` | the Agentic Top 10 document date, e.g. `for-2026 (2025-12-09)` - never `v2.01` |
| `atlas_version` | e.g. `v2026.06` — ATLAS technique IDs are version-scoped |
| `scope_delta` | stated only where the category itself moved; empty is a claim that it did not |
| `regrade_required` | `true` where a capture-backed claim needs re-earning under the new definition |

An empty `scope_delta` is an assertion, not an absence. Its basis here is that `LLM00_Preface.md` **enumerates** the entries that grew. A row outside that enumeration is claimed unchanged on the project's own accounting, not on nobody having looked. It says someone checked and the
category held.

---

## Open against this file

- Confirm the ten-row table against the primary OWASP 2026 release. The 403 stands.
- Resolve the incident-corpus figure, or keep it out.
- Diff the Agentic Top 10 (2025-12-09) titles against the matrix. ASI06 already carries
  `title Memory & Context Poisoning; PDF verbatim pending`, which is this same version
  question surfacing as a note instead of a field.
