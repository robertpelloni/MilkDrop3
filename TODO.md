# TODO - MilkDrop3 Omni-Workspace

## Priority: Extreme (Next Implementation)
- [ ] **Automated Branch Consolidation:** Implement a script/CLI command to intelligently merge all `robertpelloni` local feature branches into their respective main branches across all submodules.
- [ ] **Submodule IDEAS Generation:** Create `IDEAS.md` for each of the 10 core submodules, analyzing their specific codebases in depth.
- [ ] **Metamcp Fix:** Resolve the `metamcp` linting/dependency failure in the sandbox environment (missing `@repo/eslint-config`).

## Priority: High
- [ ] **Unified Deployment:** Implement a `deploy` subcommand in `workspace_cli.py` to handle coordinated deployments.
- [ ] **Parallel Builds:** Expand `src/workspace/execution/build.py` to support parallel submodule builds.
- [ ] **Global Memory Implementation:** Finalize the connection between `borg`, `aios`, and the workspace root for persistent session memory.

## Priority: Medium
- [ ] **UI Polish:** Audit `src/workspace/ui/web_dashboard.py` and ensure all features are represented with full labels, descriptions, and tooltips.
- [ ] **Library Inventory:** Create a comprehensive `docs/LIBRARY_INVENTORY.md` listing every major dependency across the ecosystem.
- [ ] **TUI Dashboard:** Implement a rich Terminal UI (TUI) for the `monitor` command using a library like `rich` or `textual`.

## Priority: Low (Ongoing)
- [ ] **Upstream Vigilance:** Continuously monitor and merge changes from upstream parents of all forks.
- [ ] **Documentation Depth:** Regularly audit and expand the "why" comments in all management scripts.
- [ ] **Refactoring:** Continuous cleanup of `src/workspace` sub-packages.
