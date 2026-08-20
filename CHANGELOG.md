# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Repo floor: GitHub Actions (secrets, authorship, tests 3.11/3.12, ruff, craft, zizmor/actionlint), Dependabot 7-day cooldown, SECURITY.md.

### Changed

- README leads with pin-and-execute rather than edition hygiene, and states Demonstrated as external primary evidence only.

### Fixed

- First push of a new branch resolves craft BASE to the origin default, so required craft jobs do not fail on an all-zero `github.event.before`.
- Header checker skips `.floor` / `.githooks`; live-capture SHA256 compares newline-normalized bytes so floor `json eol=lf` does not drop LLM09.


