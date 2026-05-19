#!/usr/bin/env python3
import os
import subprocess
import datetime

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def generate_dashboard():
    print("Generating Submodule Dashboard...")

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    dashboard_content = f"""# Submodule Dashboard

Last Updated: {now}

## Overview
This dashboard tracks the status of all submodules within the MilkDrop3 Omni-Workspace.

| Submodule | Path | Current Commit | Status |
|-----------|------|----------------|--------|
"""

    # Use non-recursive status to avoid breakage from internal submodule issues in forks
    submodule_status = run_command("git submodule status")

    if not submodule_status:
        dashboard_content += "| None | N/A | N/A | No submodules configured |\n"
    else:
        for line in submodule_status.split('\n'):
            if not line.strip():
                continue
            parts = line.strip().split()
            # git submodule status output: [-|+]commit_hash path (branch/tag)
            commit = parts[0].strip('+-')
            path = parts[1]
            status = "Synced"
            if line.startswith('+'):
                status = "Modified/Outdated"
            elif line.startswith('-'):
                status = "Not Initialized"
            elif line.startswith('U'):
                status = "Conflict"

            dashboard_content += f"| {os.path.basename(path)} | {path} | {commit[:8]} | {status} |\n"

    with open("SUBMODULE_DASHBOARD.md", "w") as f:
        f.write(dashboard_content)

    print("SUBMODULE_DASHBOARD.md generated successfully.")

if __name__ == "__main__":
    generate_dashboard()
