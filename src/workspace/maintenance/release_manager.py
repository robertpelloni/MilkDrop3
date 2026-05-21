#!/usr/bin/env python3
from ..core import workspace_log
from ..core import workspace_version
from ..documentation import archive_handoff
from ..documentation import generate_dashboard
from ..documentation import generate_project_structure


def prepare_release(bump="minor"):
    """
    Automates the release cycle: version bump, docs refresh, and handoff.
    """
    workspace_log.info(f"--- Starting Release Cycle (Bump: {bump}) ---")

    # 1. Bump version
    new_ver = workspace_version.bump_version(bump)
    workspace_version.update_version_file(new_ver)
    workspace_log.success(f"Version bumped to {new_ver}")

    # 2. Refresh documentation
    workspace_log.info("Refreshing documentation dashboards...")
    generate_project_structure.generate_project_structure()
    generate_dashboard.generate_dashboard()
    workspace_log.success("Documentation refreshed.")

    # 3. Archive handoff
    workspace_log.info("Archiving session handoff...")
    archive_handoff.archive_handoff()

    workspace_log.success(f"Release v{new_ver} prepared successfully.")
    return new_ver


if __name__ == "__main__":
    import sys
    bump_type = sys.argv[1] if len(sys.argv) > 1 else "minor"
    prepare_release(bump_type)
