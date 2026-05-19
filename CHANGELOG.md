# Changelog - MilkDrop3 Omni-Workspace

All notable changes to this project will be documented in this file.

## [1.5.0] - 2026-05-19
### Added
- Implemented `scripts/prune_broken_submodules.py` for automated workspace maintenance.
- Implemented `scripts/generate_project_structure.py` and created `PROJECT_STRUCTURE.md`.
- Consolidated all maintenance tasks into `scripts/update_repos_v5.py`.
- Automated the population of `SUBMODULE_DASHBOARD.md` and `PROJECT_STRUCTURE.md` in the update workflow.

## [1.4.0] - 2026-05-19
### Added
- Implemented `scripts/check_health.py` workspace integrity utility.
- Integrated automated dashboard generation into the update workflow.
- Established and enforced `flake8` linting for all workspace scripts.
- Resolved submodule pointer issues and documented findings in `HANDOFF.md`.

## [1.3.0] - 2026-05-19
### Added
- Enhanced `scripts/update_repos_v5.py` with `--sync` functionality for upstream updates.
- Improved `SUBMODULE_DASHBOARD.md` with documented purposes for all submodules.
- Fixed broken internal submodule mappings in `aios` and `borg`, enabling clean recursive updates.
- Performed detailed audit of internal submodule structures.

## [1.2.0] - 2026-05-19
### Added
- Integrated core AI submodules (`aios`, `metamcp`).
- Integrated application and engine submodules (`bobmani`, `fwber`, `bobcoin`).
- Updated `scripts/generate_dashboard.py` for increased robustness with recursive submodules.
- Performed comprehensive project audit after full submodule integration.

## [1.1.0] - 2026-05-19
### Added
- Integrated `borg` submodule at `borg/`.
- Implemented `scripts/generate_dashboard.py` for submodule tracking.
- Created `SUBMODULE_DASHBOARD.md`.
- Updated `ROADMAP.md` and `TODO.md` to reflect progress.

## [1.0.1] - 2026-05-19
### Added
- Initial workspace structure and core documentation.
- `VISION.md`, `ROADMAP.md`, `TODO.md`, `VERSION.md`.
- `DEPLOY.md`, `CHANGELOG.md`, `HANDOFF.md`.
- AI agent instructions (`AGENTS.md`, `CLAUDE.md`, etc.).
- Foundational management scripts (`scripts/update_repos_v5.py`).
- Root `README.md` and workspace directory structure.
