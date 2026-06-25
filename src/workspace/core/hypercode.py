#!/usr/bin/env python3
import subprocess
import urllib.parse
import os
from ..core import workspace_log


def parse_hypercode_url(url):
    """
    Parses a hypercode:// URL into its components.
    Format: hypercode://<submodule>/<command>?<args>
    """
    if not url.startswith("hypercode://"):
        return None

    try:
        parsed = urllib.parse.urlparse(url)
        submodule = parsed.netloc
        command = parsed.path.lstrip("/")

        # Parse query arguments into a list of flags/values
        args = []
        if parsed.query:
            query_params = urllib.parse.parse_qs(parsed.query)
            for key, values in query_params.items():
                for value in values:
                    args.extend([f"--{key}", value])

        return {
            "submodule": submodule,
            "command": command,
            "args": args
        }
    except Exception as e:
        workspace_log.error(f"Failed to parse hypercode URL: {str(e)}")
        return None


def run_hypercode_command(url, cwd="."):
    """
    Executes a parsed hypercode command across the ecosystem.
    """
    workspace_log.info(f"--- Unified Deep Linking: '{url}' ---")

    parsed_url = parse_hypercode_url(url)
    if not parsed_url:
        workspace_log.error("Invalid hypercode URL format.")
        return False

    submodule = parsed_url["submodule"]
    command = parsed_url["command"]
    args = parsed_url["args"]

    if not submodule or not command:
        workspace_log.error(
            "Hypercode URL must contain a submodule and a command."
        )
        return False

    target_dir = os.path.join(cwd, submodule)
    if not os.path.isdir(target_dir):
        workspace_log.error(f"Target submodule '{submodule}' not found.")
        return False

    workspace_log.info(f"Executing '{command}' in '{submodule}'...")

    # Safely construct the command array
    full_cmd = [command] + args

    try:
        result = subprocess.run(
            full_cmd, capture_output=True, text=True, cwd=target_dir
        )
        if result.returncode == 0:
            workspace_log.success("Hypercode execution successful.")
            if result.stdout:
                print(result.stdout.strip())
            return True
        else:
            workspace_log.error(
                f"Hypercode execution failed (Code: {result.returncode})"
            )
            if result.stderr:
                print(result.stderr.strip())
            return False
    except Exception as e:
        workspace_log.error(f"Hypercode execution exception: {str(e)}")
        return False
