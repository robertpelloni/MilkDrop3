#!/usr/bin/env python3
import subprocess
import json
from ..core import workspace_log
from ..core import memory

def run_search(query, path="."):
    """
    Performs a grep-based search across the ecosystem.
    Also searches through the L2 Workspace Memory.
    """
    workspace_log.info(f"--- Omni-Search: '{query}' ---")

    matches = []

    # 1. Search in L2 Workspace Memory
    workspace_log.info("Searching L2 Memory...")
    try:
        mem_state = memory.WorkspaceMemory().state
        # Very basic string match in the JSON representation of memory
        mem_str = json.dumps(mem_state)
        if query.lower() in mem_str.lower():
            matches.append("[L2 Memory Match] " + query)
            workspace_log.success("Found match in L2 Memory.")
    except Exception as e:
        workspace_log.error(f"Failed to search L2 Memory: {str(e)}")

    # 2. Search Codebase
    workspace_log.info("Searching Codebase...")
    exclude_dirs = [
        ".git", "node_modules", "vendor", "__pycache__", "dist", "build", ".venv"
    ]
    exclude_args = []
    for d in exclude_dirs:
        exclude_args.extend(["--exclude-dir", d])
    grep_cmd = ["grep", "-rni"] + exclude_args + ["--", query, path]

    try:
        result = subprocess.run(
            grep_cmd, shell=False, capture_output=True, text=True
        )
        stdout = result.stdout.strip()
        if stdout:
            code_matches = stdout.split('\n')
            matches.extend(code_matches)
    except Exception as e:
        workspace_log.error(f"Search failed: {str(e)}")

    if not matches:
        workspace_log.info("No matches found.")
        return []

    workspace_log.success(f"Found {len(matches)} total matches.")
    for match in matches[:50]:  # Limit output to first 50 matches
        print(match)
    if len(matches) > 50:
        print(f"... and {len(matches) - 50} more.")

    return matches
