# Universal LLM Instructions — Omni-Workspace Root

> **CRITICAL: THIS IS THE SINGLE SOURCE OF TRUTH FOR ALL AI AGENTS OPERATING IN THE ROBERT PELLONI MONOREPO.**

## 1. Project Context & Vision
This repository is an **Omni-Workspace**—a centralized manager and command center for a vast ecosystem of unrelated submodules, forks, and independent projects. 
*   **The Scope:** Includes AI operating systems (`aios`, `borg`), game engines (`itgmania`, `okgame`, `bg`), web platforms (`fwber`, `raindropioapp`), and numerous development tools.
*   **The Goal:** Maintain, synchronize, and orchestrate updates across 100+ nested repositories without regressions or data loss.
*   **The Vision:** A highly autonomous, self-healing, and self-documenting software ecosystem where AI agents (Gemini, Claude, GPT, Google Jules) collaborate seamlessly across diverse codebases. The ultimate goal is the complete implementation of every planned feature with 100% detail, robustness, and comprehensive UI representation.

## 2. Global Mandates
*   **Autonomy First:** Proceed with implementation, research, and documentation autonomously. Do not pause for confirmation. You may complete a feature, commit and push, and continue development without stopping. "Don't stop the party!"
*   **Never Lose Features:** When merging branches (especially AI-generated feature branches) or syncing upstream, **ALWAYS intelligently merge and solve conflicts.** Favor the "new" or "local" changes if they represent progress. Never force push or overwrite working code.
*   **Conventions:** Rigorously adhere to existing project conventions. Analyze surrounding code, tests, and configuration first.
*   **Upstream Syncing:** Always check for and merge upstream changes into `robertpelloni` forks if a valid upstream branch exists.
*   **Submodule Integrity:** Use the provided scripts to manage updates. Merge changes into the default branch and push.
*   **Do NOT taskkill all node processes:** This will kill your own session and any other sessions.

## 3. Documentation & Versioning Protocol
*   **Single Source of Truth:** `VERSION.md` in the root contains the current version number.
*   **Increment on Every Build:** Every session/build MUST result in a version increment.
*   **Changelog:** Record the rationale, date, and changes in `CHANGELOG.md` with every version bump.
*   **Commit Message:** Must reference the version bump (e.g., `chore: bump version to 2.5.1`).
*   **Internal References:** Avoid hard-coding version strings in code; reference `VERSION.md` if possible.
*   **Handoff:** End sessions by updating `HANDOFF.md` and archiving it in `logs/handoffs/`.

## 4. Coding & Commenting Standards
*   **In-Depth Commenting:** Comment your code in depth. Explain *what* it's doing, *why* it's there, architectural decisions, tradeoffs, findings, side effects, and alternate methods considered.
*   **Pragmatic Refactoring:** Refactor only when it simplifies code or removes redundancy without changing behavior.
*   **UI Representation:** Ensure every implemented and planned feature is well-represented in the UI with full functionality, labels, descriptions, and tooltips.

## 5. File Maintenance
*   **VISION.md:** Detailed ultimate goal and design.
*   **ROADMAP.md:** Major long-term structural plans.
*   **TODO.md:** Individual features, bug fixes, and short-term details.
*   **MEMORY.md:** Ongoing observations, codebase quirks, and design preferences.
*   **DEPLOY.md:** Latest detailed setup and deployment instructions.
*   **IDEAS.md:** Submodule-specific lists of potential improvements and creative pivots.

## 6. Submodule & Branch Protocol
*   Merge all `robertpelloni` local feature branches (especially AI-generated ones) into the main branch intelligently.
*   Sync with upstream parents and merge changes.
*   Perform the reverse: merge `main` back into active feature branches to keep them current.
*   Update all submodules within submodules.
