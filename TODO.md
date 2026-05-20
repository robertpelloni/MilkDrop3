# TODO - MilkDrop3 Omni-Workspace

## Priority: High (Immediate Actions)
- [x] **Project Setup:** Initialize root documentation (`VISION.md`, `ROADMAP.md`, etc.).
- [x] **Management Scripts:** Implement `scripts/workspace_cli.py` for submodule management.
- [x] **Workspace Structure:** Create placeholder directories for `aios/`, `borg/`, `scripts/`, `logs/`.
- [x] **Audit:** Perform a full audit of the current repository state and identify missing components.
- [x] **Submodule Fix:** Resolve broken internal submodule mappings in `aios` and `borg`.

## Priority: Medium (Next Steps)
- [x] **Submodule Integration:** Complete integration of core submodules (`aios`, `borg`, `metamcp`, `bobmani`, `fwber`, `bobcoin`).
 - [x] **CI/CD:** Established GitHub Actions for automated linting and health checks.
- [x] **Dashboard:** Implement `scripts/generate_dashboard.py` to track submodule status.

## Priority: Low (Long-Term)
- [x] **Documentation Gaps:** Expand `DEPLOY.md` with detailed submodule setup guides.
- [x] **Refactoring:** Consolidate redundant logic across workspace management scripts into a unified CLI.
- [x] **Submodule Expansion:** Integrate additional core repositories (`itgmania`, `okgame`, etc.).
- [x] **Automated Versioning:** Implement a semver-lite versioning utility within the CLI.
