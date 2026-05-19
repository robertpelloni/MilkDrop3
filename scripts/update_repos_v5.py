#!/usr/bin/env python3
import os
import subprocess
import sys
import generate_dashboard
import generate_project_structure
import prune_broken_submodules
import check_health


def run_command(command, cwd=None):
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True,
            cwd=cwd
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"


def get_submodule_status():
    print("--- Submodule Status ---")
    status = run_command("git submodule status")
    if not status:
        print("No submodules found.")
    else:
        print(status)


def update_submodules():
    print("--- Updating Submodules ---")
    result = run_command("git submodule update --init")
    print(result if result else "Submodules updated successfully.")


def sync_upstream():
    print("--- Syncing Upstream Changes ---")
    submodule_status = run_command("git submodule status")
    if not submodule_status:
        print("No submodules to sync.")
        return

    for line in submodule_status.split('\n'):
        if not line.strip():
            continue
        parts = line.strip().split()
        path = parts[1]

        print(f"Checking {path}...")
        remotes = run_command("git remote", cwd=path)
        if "upstream" not in remotes:
            print(f"No upstream remote in {path}. Fetching from origin...")
            run_command("git fetch origin", cwd=path)
        else:
            print(f"Fetching from upstream in {path}...")
            run_command("git fetch upstream", cwd=path)
            run_command("git merge upstream/main --ff-only", cwd=path)


def main():
    print("MilkDrop3 Omni-Workspace Submodule Manager v5")

    if not os.path.exists(".git"):
        print("Error: Must be run from the root of a git repository.")
        sys.exit(1)

    get_submodule_status()
    update_submodules()

    if "--sync" in sys.argv:
        sync_upstream()

    print("--- Running Maintenance Utilities ---")
    prune_broken_submodules.prune_broken(dry_run=True)
    generate_project_structure.generate_project_structure()
    generate_dashboard.generate_dashboard()

    print("--- Running Health Check ---")
    check_health.main()


if __name__ == "__main__":
    main()
