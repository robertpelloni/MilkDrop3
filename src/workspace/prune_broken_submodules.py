#!/usr/bin/env python3
import subprocess
import sys
import os


def run_command(command, cwd=None):
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, cwd=cwd
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"


def get_gitlinks():
    """Returns a list of paths that are gitlinks (mode 160000)."""
    output = run_command("git ls-files -s")
    gitlinks = []
    for line in output.split('\n'):
        if line.startswith('160000'):
            parts = line.split()
            if len(parts) >= 4:
                gitlinks.append(parts[3])
    return gitlinks


def get_configured_submodules():
    """Returns a list of paths configured in .gitmodules."""
    if not os.path.exists(".gitmodules"):
        return []
    output = run_command("git config -f .gitmodules --get-regexp path")
    paths = []
    for line in output.split('\n'):
        if line.strip():
            parts = line.split()
            if len(parts) >= 2:
                paths.append(parts[1])
    return paths


def prune_broken(dry_run=True):
    print(f"--- Pruning Broken Submodules (Dry Run: {dry_run}) ---")
    gitlinks = get_gitlinks()
    configured = get_configured_submodules()

    orphans = [g for f in gitlinks if (g := f) not in configured]

    if not orphans:
        print("No orphaned gitlinks found.")
        return

    for orphan in orphans:
        if dry_run:
            print(f"[WOULD PRUNE] Orphaned gitlink: {orphan}")
        else:
            print(f"[PRUNING] Orphaned gitlink: {orphan}")
            run_command(f"git rm -r --cached {orphan}")

    if not dry_run and orphans:
        print("\nPruning complete. Please commit the changes.")


def main():
    print("MilkDrop3 Omni-Workspace Submodule Pruner")
    dry_run = "--fix" not in sys.argv
    prune_broken(dry_run=dry_run)


if __name__ == "__main__":
    main()
