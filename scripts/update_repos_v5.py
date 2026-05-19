#!/usr/bin/env python3
import os
import subprocess
import sys

def run_command(command, cwd=None):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd=cwd)
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
    result = run_command("git submodule update --init --recursive")
    print(result if result else "Submodules updated successfully.")

def main():
    print("MilkDrop3 Omni-Workspace Submodule Manager v5")

    if not os.path.exists(".git"):
        print("Error: Must be run from the root of a git repository.")
        sys.exit(1)

    get_submodule_status()
    # update_submodules() # Uncomment when submodules are added

if __name__ == "__main__":
    main()
