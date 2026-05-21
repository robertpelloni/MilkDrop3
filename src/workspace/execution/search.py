#!/usr/bin/env python3
import subprocess
from ..core import workspace_log


def run_search(query, path="."):
    """
    Performs a grep-based search across the ecosystem.
    """
    workspace_log.info(f"--- Omni-Search: '{query}' ---")

    # Use grep to find matches, excluding common noise
    exclude_dirs = [
        ".git", "node_modules", "vendor", "__pycache__", "dist", "build"
    ]
    grep_cmd = [
        "grep", "-rni",
        "--exclude-dir={" + ",".join(exclude_dirs) + "}",
        query, path
    ]

    # Use shell=True for brace expansion in grep
    cmd_str = " ".join(grep_cmd)

    try:
        result = subprocess.run(
            cmd_str, shell=True, capture_output=True, text=True
        )
        stdout = result.stdout.strip()
        if not stdout:
            workspace_log.info("No matches found.")
            return []

        matches = stdout.split('\n')
        workspace_log.success(f"Found {len(matches)} matches.")
        for match in matches[:50]:  # Limit output to first 50 matches
            print(match)
        if len(matches) > 50:
            print(f"... and {len(matches) - 50} more.")

        return matches
    except Exception as e:
        workspace_log.error(f"Search failed: {str(e)}")
        return []
