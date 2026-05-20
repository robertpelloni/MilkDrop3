#!/usr/bin/env python3
import os
import time
import subprocess
from ..core import workspace_log


def get_submodule_status():
    try:
        result = subprocess.run(
            ["git", "submodule", "status"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"


def get_latest_logs(n=5):
    log_dir = "logs"
    if not os.path.exists(log_dir):
        return "No logs found."

    log_files = [f for f in os.listdir(log_dir) if f.endswith(".log")]
    if not log_files:
        return "No log files found."

    latest_log = os.path.join(log_dir, sorted(log_files)[-1])
    try:
        with open(latest_log, "r") as f:
            lines = f.readlines()
            return "".join(lines[-n:])
    except Exception as e:
        return f"Error reading logs: {str(e)}"


def run_monitor(interval=5):
    workspace_log.info(f"Starting Workspace Monitor (Interval: {interval}s)")
    try:
        while True:
            # Clear screen (portable)
            os.system('cls' if os.name == 'nt' else 'clear')

            print("=== MilkDrop3 Omni-Workspace Monitor ===")
            print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
            print("\n--- Submodule Status ---")
            print(get_submodule_status())

            print("\n--- Latest Activity ---")
            print(get_latest_logs())

            print("\n(Press Ctrl+C to stop)")
            time.sleep(interval)
    except KeyboardInterrupt:
        workspace_log.info("Monitor stopped.")


if __name__ == "__main__":
    run_monitor()
