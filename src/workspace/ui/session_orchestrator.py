#!/usr/bin/env python3
from ..core import workspace_log
from ..core import workspace_session
from ..maintenance import check_health
from ..maintenance import update_repos_v5
from ..documentation import archive_handoff
from ..documentation import generate_project_structure
from ..documentation import generate_dashboard
from ..core import workspace_version


def start_session(model_name):
    workspace_log.info(f"--- Automated Session Start: {model_name} ---")
    workspace_session.start_session(model_name)
    check_health.run_health_check()
    workspace_log.success(f"Session ready for {model_name}")


def finish_session(bump="minor"):
    workspace_log.info("--- Automated Session Finish ---")

    # 1. Update and Maintenance
    update_repos_v5.orchestrate_update(sync=True)

    # 2. Refresh Docs
    generate_project_structure.generate_project_structure()
    generate_dashboard.generate_dashboard()

    # 3. Final Health Check
    if not check_health.run_health_check():
        workspace_log.error(
            "Workspace is UNHEALTHY. Fix issues before finishing."
        )
        return False

    # 4. Version Bump
    new_ver = workspace_version.bump_version(bump)
    workspace_version.update_version_file(new_ver)

    # 5. Archive Handoff
    archive_handoff.archive_handoff()

    workspace_log.success("Session finished successfully. Ready for commit.")
    return True
