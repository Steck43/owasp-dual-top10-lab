# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Matrix status equals each scenario.yaml. README and REPRODUCE counts are derived from the matrix. Demonstrated stays 0.
- CITATION.cff and `.zenodo.json` so a later tag can mint. No DOI on this record yet.
- REPRODUCE.md for the `labctl` fixture-oracle path. Demonstrated stays 0.
- Crosswalk refuses Demonstrated on a fixture capture. CVE-2025-32711 stays the LLM01 pin; the CNA retrieve is cited, not a promotion.
- Oracle tests assert `scenario.yaml` `vuln_must_contain` / control fields against `labctl` JSON, and a swapped pair must fail.
- Crosswalk columns `eu_risk_tier`, `eu_article`, `eu_claim_tense` on the existing twenty rows. Filled only on LLM06 / ASI02 / ASI05 / ASI09. Empty stays empty.
- Repo floor: GitHub Actions (secrets, authorship, tests 3.11/3.12, ruff, craft, zizmor/actionlint), Dependabot 7-day cooldown, SECURITY.md.

### Changed

- README leads with pin-and-execute rather than edition hygiene, and states Demonstrated as external primary evidence only.

### Fixed

- First push of a new branch resolves craft BASE to the origin default, so required craft jobs do not fail on an all-zero `github.event.before`.
- Header checker skips `.floor` / `.githooks`; live-capture SHA256 compares newline-normalized bytes so floor `json eol=lf` does not drop LLM09.


