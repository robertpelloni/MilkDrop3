#!/usr/bin/env python3
import os
from . import workspace_log


def get_current_version():
    if os.path.exists("VERSION.md"):
        with open("VERSION.md", "r") as f:
            return f.read().strip()
    return "0.0.0"


def bump_version(part="patch"):
    current = get_current_version()
    parts = current.split('.')
    if len(parts) != 3:
        workspace_log.error(f"Invalid version format: {current}")
        return current

    major, minor, patch = map(int, parts)

    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    else:
        patch += 1

    new_version = f"{major}.{minor}.{patch}"
    workspace_log.info(f"Bumping version: {current} -> {new_version}")
    return new_version


def update_version_file(new_version):
    with open("VERSION.md", "w") as f:
        f.write(new_version + "\n")
    workspace_log.success(f"Updated VERSION.md to {new_version}")


def main():
    # Basic semver-lite implementation
    new_ver = bump_version("minor")
    print(f"Next version: {new_ver}")


if __name__ == "__main__":
    main()
