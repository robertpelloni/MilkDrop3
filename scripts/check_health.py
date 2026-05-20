#!/usr/bin/env python3
import os
import subprocess
import sys
import workspace_log


MANDATORY_FILES = [
    "VISION.md",
    "ROADMAP.md",
    "TODO.md",
    "HANDOFF.md",
    "DEPLOY.md",
    "CHANGELOG.md",
    "VERSION.md",
    "AGENTS.md",
    "README.md",
    "SUBMODULE_DASHBOARD.md",
    "docs/UNIVERSAL_LLM_INSTRUCTIONS.md"
]

MANDATORY_DIRS = [
    "scripts",
    "logs",
    "aios",
    "borg",
    "metamcp",
    "bobmani",
    "fwber",
    "bobcoin"
]


def run_command(command, cwd=None):
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, cwd=cwd
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"


def check_files():
    workspace_log.info("Checking mandatory files...")
    all_present = True
    for f in MANDATORY_FILES:
        if os.path.exists(f):
            print(f"[OK] {f}")
        else:
            workspace_log.error(f"Missing mandatory file: {f}")
            all_present = False
    return all_present


def check_dirs():
    workspace_log.info("Checking mandatory directories...")
    all_present = True
    for d in MANDATORY_DIRS:
        if os.path.isdir(d):
            print(f"[OK] {d}/")
        else:
            workspace_log.error(f"Missing mandatory directory: {d}/")
            all_present = False
    return all_present


def check_submodules():
    workspace_log.info("Checking submodule health...")
    status_output = subprocess.run(
        ['git', 'submodule', 'status'], capture_output=True, text=True
    ).stdout
    if not status_output:
        workspace_log.info("No submodules found.")
        return True

    healthy = True
    for line in status_output.split('\n'):
        if not line.strip():
            continue
        if line.startswith(' ') or not line.startswith(('-', '+', 'U')):
            print(f"[OK] {line.strip()}")
        else:
            workspace_log.warn(f"Submodule issue detected: {line.strip()}")
            healthy = False
    return healthy


def main():
    workspace_log.info("Starting workspace health check...")
    f_ok = check_files()
    d_ok = check_dirs()
    s_ok = check_submodules()

    if f_ok and d_ok and s_ok:
        workspace_log.success("Workspace is HEALTHY.")
        # Return success instead of exiting to allow for script integration
        return True
    else:
        workspace_log.error("Workspace has ISSUES.")
        return False


if __name__ == "__main__":
    if main():
        sys.exit(0)
    else:
        sys.exit(1)
