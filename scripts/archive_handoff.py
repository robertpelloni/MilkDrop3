#!/usr/bin/env python3
import shutil
import os
import datetime
import workspace_log
import workspace_version


def archive_handoff():
    archive_dir = os.path.join("logs", "handoffs")
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
        workspace_log.info(f"Created archive directory: {archive_dir}")

    if not os.path.exists("HANDOFF.md"):
        workspace_log.warn("HANDOFF.md not found. Nothing to archive.")
        return False

    version = workspace_version.get_current_version()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_filename = f"HANDOFF_v{version}_{timestamp}.md"
    archive_path = os.path.join(archive_dir, archive_filename)

    try:
        shutil.copy2("HANDOFF.md", archive_path)
        workspace_log.success(f"Archived HANDOFF.md to {archive_path}")
        return True
    except Exception as e:
        workspace_log.error(f"Failed to archive handoff: {str(e)}")
        return False


def main():
    archive_handoff()


if __name__ == "__main__":
    main()
