#!/usr/bin/env python3
import os
import subprocess
import sys


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
    print("--- Checking Mandatory Files ---")
    all_present = True
    for f in MANDATORY_FILES:
        if os.path.exists(f):
            print(f"[OK] {f}")
        else:
            print(f"[MISSING] {f}")
            all_present = False
    return all_present


def check_dirs():
    print("\n--- Checking Mandatory Directories ---")
    all_present = True
    for d in MANDATORY_DIRS:
        if os.path.isdir(d):
            print(f"[OK] {d}/")
        else:
            print(f"[MISSING] {d}/")
            all_present = False
    return all_present


def check_submodules():
    print("\n--- Checking Submodule Health ---")
    status_output = subprocess.run(
        ['git', 'submodule', 'status'], capture_output=True, text=True
    ).stdout
    if not status_output:
        print("No submodules found.")
        return True

    healthy = True
    for line in status_output.split('\n'):
        if not line.strip():
            continue
        # git submodule status output:
        # ' ' (space) means synced
        # '+' means modified/outdated
        # '-' means not initialized
        # 'U' means conflict
        if line.startswith(' ') or not line.startswith(('-', '+', 'U')):
            print(f"[OK] {line.strip()}")
        else:
            print(f"[ISSUE] {line.strip()}")
            healthy = False
    return healthy


def main():
    print("MilkDrop3 Omni-Workspace Health Check")
    f_ok = check_files()
    d_ok = check_dirs()
    s_ok = check_submodules()

    print("\n--- Summary ---")
    if f_ok and d_ok and s_ok:
        print("Workspace is HEALTHY.")
        sys.exit(0)
    else:
        print("Workspace has ISSUES.")
        sys.exit(1)


if __name__ == "__main__":
    main()
