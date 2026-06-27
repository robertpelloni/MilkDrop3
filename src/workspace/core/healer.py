#!/usr/bin/env python3
import subprocess
import os
import shutil
from ..core import workspace_log


class WorkspaceHealer:
    """
    Automated Ecosystem Repair logic.
    Diagnoses and attempts to fix failing builds or health checks.
    """

    def __init__(self):
        self.known_issues = {
            "pnpm: not found": "npm install -g pnpm",
            "turbo: not found": "npm install -g turbo",
            "fatal: reference is not a tree": "git submodule update --init --recursive --force",
            "Missing mandatory directory:": "python scripts/update_repos_v5.py"
        }

    def _auto_detect_missing_submodules(self, cwd="."):
        workspace_log.info("Checking for missing core submodules...")
        expected = ["aios", "bg", "bobcoin", "bobmani", "borg", "fwber", "itgmania", "metamcp", "okgame"]
        missing = []
        for d in expected:
            if not os.path.isdir(os.path.join(cwd, d)):
                missing.append(d)

        if missing:
            workspace_log.warn(f"Missing submodules detected: {missing}")
            workspace_log.info("Attempting to restore missing submodules...")
            try:
                subprocess.run("git submodule update --init --recursive", shell=True, cwd=cwd)
                return True
            except Exception as e:
                workspace_log.error(f"Failed to restore submodules: {str(e)}")
                return False
        return False

    def diagnose_and_heal(self, error_output, cwd="."):
        workspace_log.info("Healer analyzing failure...")

        # Pre-emptive environment checks
        self._auto_detect_missing_submodules(cwd)

        for signature, fix_cmd in self.known_issues.items():
            if signature in error_output:
                workspace_log.warn(
                    f"Known issue detected: '{signature}'. "
                    "Attempting auto-heal..."
                )
                try:
                    workspace_log.info(f"Running fix: {fix_cmd}")
                    result = subprocess.run(
                        fix_cmd, shell=True, capture_output=True,
                        text=True, cwd=cwd
                    )
                    if result.returncode == 0:
                        workspace_log.success(
                            "Auto-heal applied successfully. "
                            "You should retry the operation."
                        )
                        return True
                    else:
                        workspace_log.error(
                            f"Auto-heal failed: {result.stderr}"
                        )
                        return False
                except Exception as e:
                    workspace_log.error(
                        f"Healer exception during fix: {str(e)}"
                    )
                    return False

        workspace_log.warn(
            "Healer could not automatically diagnose or fix this issue."
        )
        return False


def attempt_heal(error_output, cwd="."):
    healer = WorkspaceHealer()
    return healer.diagnose_and_heal(error_output, cwd)
