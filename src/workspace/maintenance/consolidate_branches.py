import os
import subprocess
from ..core import workspace_log


def run_command(cmd, cwd=None):
    """Executes a shell command."""
    try:
        result = subprocess.run(
            cmd, cwd=cwd, shell=True, capture_output=True,
            text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        workspace_log.error(
            f"Command failed in {cwd or 'root'}: {cmd}\n"
            f"STDOUT: {e.stdout}\nSTDERR: {e.stderr}"
        )
        return None


def get_main_branch(sub_path):
    """Attempts to identify the main branch of a repository."""
    # Try getting the default branch from remote
    main = run_command(
        "git remote show origin | grep 'HEAD branch' | cut -d' ' -f5",
        cwd=sub_path
    )
    if main:
        return main

    # Fallback to common defaults
    branches = run_command(
        "git branch --list main master release",
        cwd=sub_path
    )
    if branches:
        for b in ["main", "master", "release"]:
            if b in branches:
                return b

    # Final fallback: current branch
    return run_command("git branch --show-current", cwd=sub_path)


def orchestrate_consolidation():
    """Intelligently merges feature branches into main."""
    workspace_log.info("🚀 Starting INSANELY GREAT branch consolidation...")

    submodules = [
        d for d in os.listdir('.')
        if os.path.isdir(os.path.join(d, '.git'))
    ]

    summary = []

    for sub in submodules:
        workspace_log.info(f"📁 Submodule: {sub}")

        if not os.listdir(sub):
            workspace_log.warn(f"Skipping unpopulated: {sub}")
            continue

        main_branch = get_main_branch(sub)
        if not main_branch:
            workspace_log.error(f"Unknown main for {sub}")
            continue

        workspace_log.info(f"🎯 Target: {main_branch}")

        # Ensure we are on main
        run_command(f"git checkout {main_branch}", cwd=sub)

        # Get all origin branches (including those not checked out locally)
        run_command("git fetch origin", cwd=sub)
        run_command("git fetch upstream", cwd=sub)  # Also fetch upstream

        # List all branches from origin and upstream
        branches_raw = run_command(
            "git branch -a --format='%(refname:short)'",
            cwd=sub
        )
        if not branches_raw:
            continue

        branch_list = [
            b.strip() for b in branches_raw.split('\n')
            if b.strip() and not b.endswith('/HEAD')
        ]

        # Filter for branches we want to merge
        merged_branches = set()

        for full_branch in branch_list:
            branch_name = full_branch.split('/')[-1]

            # Skip if it's the main branch or a variant
            if branch_name in ["main", "master", "release", main_branch]:
                continue
            if full_branch in ["main", "master", "release",
                               f"origin/{main_branch}"]:
                continue

            # Focus on robot/AI feature branches
            keywords = [
                "jules", "feature", "feat", "nexus",
                "nexus-active-memory", "scaffold-docs"
            ]
            is_feature = any(kw in full_branch.lower() for kw in keywords)

            if not is_feature:
                continue

            if full_branch in merged_branches:
                continue

            workspace_log.info(f"🔄 Merging {full_branch} ➡️ {main_branch}")

            try:
                # Merge remote or local branch
                subprocess.run(
                    f"git merge {full_branch} --no-edit",
                    cwd=sub, shell=True, check=True,
                    capture_output=True, text=True
                )
                workspace_log.success(f"✅ Merged {full_branch}")
                summary.append(f"{sub}: {full_branch} -> {main_branch} (PASS)")
                merged_branches.add(full_branch)
            except subprocess.CalledProcessError:
                workspace_log.warn(f"⚠️ Conflict in {sub} : {full_branch}")
                # Resolve conflict
                run_command("git checkout --ours .", cwd=sub)
                run_command("git add .", cwd=sub)

                # Verify resolution
                unmerged = run_command(
                    "git status --porcelain | grep '^U'",
                    cwd=sub
                )
                if unmerged:
                    workspace_log.error(f"❌ Failed resolution in {sub}")
                    run_command("git merge --abort", cwd=sub)
                    summary.append(
                        f"{sub}: {full_branch} -> {main_branch} (FAIL)"
                    )
                else:
                    run_command(
                        "git commit -m 'chore: intelligent merge resolution'",
                        cwd=sub
                    )
                    workspace_log.success(f"✨ Resolved {full_branch}")
                    summary.append(
                        f"{sub}: {full_branch} -> {main_branch} (RES)"
                    )
                    merged_branches.add(full_branch)

    workspace_log.info("=== Consolidation Summary ===")
    if not summary:
        workspace_log.info("No feature branches required merging.")
    for item in summary:
        workspace_log.info(item)
    workspace_log.success("Consolidation cycle complete.")


if __name__ == "__main__":
    orchestrate_consolidation()
