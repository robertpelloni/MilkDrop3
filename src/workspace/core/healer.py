#!/usr/bin/env python3
import subprocess
from ..core import workspace_log


class WorkspaceHealer:
    """
    Automated Ecosystem Repair logic.
    Diagnoses and attempts to fix failing builds or health checks.
    """

    def __init__(self):
        self.known_issues = {
            "pnpm: not found": "npm install -g pnpm",
            "turbo: not found": "npm install -g turbo"
        }

    def diagnose_and_heal(self, error_output, cwd="."):
        workspace_log.info("Healer analyzing failure...")

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
