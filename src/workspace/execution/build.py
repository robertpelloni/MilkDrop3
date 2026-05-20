#!/usr/bin/env python3
from . import workspace_run
from ..core import workspace_log


BUILD_STRATEGIES = {
    "borg": "go build -o borg-mcp-server ./cmd/borg",
    "aios": "npm run build --if-present",
    "metamcp": "turbo run build",
    "bobmani": None,  # Engine assets only
    "fwber": "npm run build --if-present",
    "bobcoin": "npm run build --if-present",
    "itgmania": None,
    "okgame": None,
    "bg": None,
    "raindropioapp": "npm run build --if-present",
}


def run_builds():
    workspace_log.info("--- Starting Ecosystem Build ---")
    submodules = workspace_run.get_configured_submodules()

    results = {}
    for path in submodules:
        strategy = BUILD_STRATEGIES.get(path)
        if not strategy:
            workspace_log.info(f"{path}: No build strategy defined. Skipping.")
            results[path] = 0
            continue

        workspace_log.info(f"Building {path}...")
        code, out, err = workspace_run.run_command(strategy, cwd=path)
        if code == 0:
            workspace_log.success(f"{path}: Build Success")
        else:
            workspace_log.error(f"{path}: Build FAILED (Code: {code})")
        results[path] = code

    workspace_log.info("Build Summary:")
    all_success = True
    for path, code in results.items():
        status = "PASS" if code == 0 else "FAIL"
        print(f"[{status}] {path}")
        if code != 0:
            all_success = False

    return all_success
