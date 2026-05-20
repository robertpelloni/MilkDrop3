#!/usr/bin/env python3
import os
import subprocess
import sys
import generate_dashboard
import generate_project_structure
import prune_broken_submodules
import check_health
import test_ecosystem
import workspace_log


def run_command(command, cwd=None):
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True,
            cwd=cwd
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        workspace_log.error(f"Command failed: {command}")
        return f"Error: {e.stderr.strip()}"


def get_submodule_status():
    workspace_log.info("Checking submodule status...")
    status = run_command("git submodule status")
    if not status:
        workspace_log.info("No submodules found.")
    else:
        print(status)


def update_submodules():
    workspace_log.info("Updating submodules...")
    result = run_command("git submodule update --init")
    if "Error" not in result:
        workspace_log.success("Submodules updated successfully.")


def sync_upstream():
    workspace_log.info("Syncing upstream changes...")
    submodule_status = run_command("git submodule status")
    if not submodule_status:
        workspace_log.warn("No submodules to sync.")
        return

    for line in submodule_status.split('\n'):
        if not line.strip():
            continue
        parts = line.strip().split()
        path = parts[1]

        workspace_log.info(f"Checking {path}...")
        remotes = run_command("git remote", cwd=path)
        if "upstream" not in remotes:
            origin_url = run_command("git remote get-url origin", cwd=path)
            if "github.com/robertpelloni/" in origin_url:
                repo_name = os.path.basename(path)
                upstream_url = (
                    f"https://github.com/robertpelloni/{repo_name}.git"
                )
                workspace_log.info(f"Adding upstream: {upstream_url}")
                run_command(f"git remote add upstream {upstream_url}",
                            cwd=path)
            else:
                workspace_log.info(f"No upstream remote in {path}. "
                                   "Fetching from origin...")
                run_command("git fetch origin", cwd=path)
                continue

        workspace_log.info(f"Fetching from upstream in {path}...")
        run_command("git fetch upstream", cwd=path)
        merge_result = run_command("git merge upstream/main --ff-only",
                                   cwd=path)
        if "Error" in merge_result:
            run_command("git merge upstream/master --ff-only", cwd=path)


def orchestrate_update(sync=False):
    workspace_log.info("Starting workspace update workflow...")
    get_submodule_status()
    update_submodules()

    if sync:
        sync_upstream()

    workspace_log.info("Running maintenance utilities...")
    prune_broken_submodules.prune_broken(dry_run=True)
    generate_project_structure.generate_project_structure()
    generate_dashboard.generate_dashboard()

    workspace_log.info("Running ecosystem validation...")
    test_ecosystem.run_ecosystem_tests()

    workspace_log.info("Running health check...")
    check_health.run_health_check()


def main():
    workspace_log.info("MilkDrop3 Omni-Workspace Submodule Manager v5")

    if not os.path.exists(".git"):
        workspace_log.error("Must be run from the root of a git repository.")
        sys.exit(1)

    sync = "--sync" in sys.argv
    orchestrate_update(sync=sync)


if __name__ == "__main__":
    main()
