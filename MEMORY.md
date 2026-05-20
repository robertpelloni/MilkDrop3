# Memory - MilkDrop3 Omni-Workspace

## Ongoing Observations
- **Submodule Heterogeneity:** The workspace manages Go, Node.js (with Turbo/PNPM), and C++ (ITGMania). The `workspace_cli.py` must remain flexible to handle these diverse build environments.
- **Pointer Drift in Forks:** Upstream forks often have broken internal submodule references. The "gitlink pruning" strategy in `prune_broken_submodules.py` is critical for maintenance.
- **CI Environment Constraints:** The GitHub Actions environment lacks some local tools (like `turbo` in certain paths). Documentation in `DEPLOY.md` and `HANDOFF.md` must highlight these environment-specific requirements.
- **The "robertpelloni" Pattern:** Most submodules follow the `github.com/robertpelloni/<repo>` pattern. Automation scripts leverage this for upstream discovery.

## Design Preferences
- **Single Source of Truth:** Versioning must be tied to `VERSION.md`.
- **Modular Management:** The shift from flat `scripts/` to `src/workspace/` sub-packages is the preferred architecture for the Control Plane.
- **Verbose Documentation:** Code should be heavily commented with the "why" and "architectural intent."
- **Terminal-First:** While a web dashboard exists, the primary interface for power-users (and AI agents) is the CLI and TUI.

## Codebase Quirks
- `metamcp` requires a specific `pnpm` workspace setup that is sensitive to the local environment.
- `itgmania` and `okgame` have extremely large codebases; health checks should remain non-recursive to maintain speed.
- `aios` and `borg` are closely linked and often share development cycles.

## Session Learnings
- **Session 17:** Realized that `turbo` must be globally available for `metamcp` tests to pass reliably in restricted environments.
- **Session 18 (Current):** User emphasized "Don't stop the party" and "Merge intelligently," highlighting the need for more aggressive automated branch consolidation.
