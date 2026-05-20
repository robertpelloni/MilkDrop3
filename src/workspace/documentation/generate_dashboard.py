#!/usr/bin/env python3
import os
import subprocess
import datetime
from ..core import workspace_log


def run_command(command):
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"


SUBMODULE_INFO = {
    "aios": "AI Operating System & Agent Infrastructure. "
            "Centralized layer for autonomous agent execution.",
    "borg": "Local Control Plane for AI tools, MCP servers, and "
            "model routing. Designed for high observability.",
    "metamcp": "Unified MCP tool discovery and management. "
               "Bridges multiple tool providers and models.",
    "bobmani": "Rhythm game engine suite. Modern, AI-integrated "
               "continuation of rhythm gaming tech.",
    "fwber": "Full-stack social platform (Laravel/Next.js). "
             "Experimental social networking layer.",
    "bobcoin": "Blockchain and cryptocurrency project "
               "integrated into the ecosystem.",
    "itgmania": "Cross-platform rhythm game engine based on StepMania. "
                "Part of the core rhythm game suite.",
    "okgame": "Open source game engine and experimental "
              "gaming framework.",
    "bg": "Board game engine and digital tabletop platform.",
    "raindropioapp": "Web platform and productivity tool integrated "
                     "with the workspace ecosystem.",
}


def generate_dashboard():
    workspace_log.info("Generating submodule dashboard...")

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    dashboard_content = f"""# Submodule Dashboard

Last Updated: {now}

## Overview
This dashboard tracks the status and purpose of all submodules within the \
MilkDrop3 Omni-Workspace.

| Submodule | Path | Current Commit | Status | Purpose |
|-----------|------|----------------|--------|---------|
"""

    submodule_status = run_command("git submodule status")

    if not submodule_status:
        dashboard_content += (
            "| None | N/A | N/A | No submodules configured | N/A |\n"
        )
    else:
        for line in submodule_status.split('\n'):
            if not line.strip():
                continue
            parts = line.strip().split()
            commit = parts[0].strip('+-')
            path = parts[1]
            name = os.path.basename(path)
            status = "Synced"
            if line.startswith('+'):
                status = "Modified/Outdated"
            elif line.startswith('-'):
                status = "Not Initialized"
            elif line.startswith('U'):
                status = "Conflict"

            purpose = SUBMODULE_INFO.get(name, "Purpose not documented.")

            dashboard_content += (
                f"| {name} | {path} | {commit[:8]} | "
                f"{status} | {purpose} |\n"
            )

    with open("SUBMODULE_DASHBOARD.md", "w") as f:
        f.write(dashboard_content)

    workspace_log.success("SUBMODULE_DASHBOARD.md updated.")


if __name__ == "__main__":
    generate_dashboard()
