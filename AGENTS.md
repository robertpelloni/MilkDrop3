# Agent Instructions - MilkDrop3 Omni-Workspace

## Overview
All AI agents operating in this repository MUST strictly adhere to the guidelines set forth in `docs/UNIVERSAL_LLM_INSTRUCTIONS.md`. This file serves as the root-level entry point for agent-specific guidance within the MilkDrop3 Omni-Workspace.

## Core Mandates
1. **Reference the Source:** Always consult `docs/UNIVERSAL_LLM_INSTRUCTIONS.md` before performing any major actions.
2. **Autonomy:** Proceed with tasks independently. If a script (like `scripts/update_repos_v5.py`) is missing or broken, fix it or implement a functional version.
3. **Submodule Integrity:** Never break submodule links. Use the provided scripts to manage updates.
4. **Versioning:** Every session MUST result in a version increment in `VERSION.md` and a corresponding entry in `CHANGELOG.md`.

## Workflow
- **Analyze:** Use `ls -R` and `grep` to understand the current state across all submodules.
- **Audit:** Regularly update `HANDOFF.md` with findings.
- **Implement:** Favor pragmatic, project-aligned improvements.
- **Verify:** Run all available tests and build commands before submitting.
