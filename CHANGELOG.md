# Changelog - MilkDrop3 Omni-Workspace

All notable changes to this project will be documented in this file.

## [2.7.0] - 2026-05-20
### Added
- Scaffolded **Ecosystem Mood Stream** in AIOS (`moodRouter.ts`) for real-time visualization data.
- Implemented "INSANELY GREAT" branch consolidation (`--consolidate` flag in CLI).
- Created per-submodule `IDEAS.md` for all 10 core projects with deep ecosystem synergies.
- Established persistent workspace memory in `src/workspace/core/memory.py`.
- Refactored entire management layer into `src.workspace` sub-packages.
- Unified versioning (2.7.0) across `VERSION.md` and `pyproject.toml`.
- Transitioned project into Phase 4: Convergence.
- Fixed submodule mapping errors for `bg`, `itgmania`, `okgame`, and `raindropioapp`.

## [2.5.0] - 2026-05-20
### Added
- Refactored `src.workspace` into a structured sub-package hierarchy (core, maintenance, documentation, execution, ui).
- Implemented consolidated build system in `src.workspace.execution.build`.
- Added `build` subcommand to Workspace CLI.
- Integrated automated session transition management into the core hierarchy.
- Professionalized package structure with domain-specific modularity.

## [2.4.1] - 2026-05-20
### Fixed
- Stabilized GitHub Actions CI by adding submodule initialization step.
- Enhanced `check_health.py` to be environment-aware and handle CI pointer drift.
- Suppressed Node.js deprecation warnings in CI environment.

[... Rest of changelog continues here ...]
