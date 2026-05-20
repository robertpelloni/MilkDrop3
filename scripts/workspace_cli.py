#!/usr/bin/env python3
import argparse
import sys
import os

# Ensure the scripts directory is in the path for modular imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import update_repos_v5             # noqa: E402
import check_health                # noqa: E402
import test_ecosystem              # noqa: E402
import generate_dashboard          # noqa: E402
import generate_project_structure  # noqa: E402
import workspace_run               # noqa: E402
import prune_broken_submodules     # noqa: E402
import workspace_version           # noqa: E402


def main():
    parser = argparse.ArgumentParser(
        description="MilkDrop3 Omni-Workspace CLI"
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Status/List submodules
    subparsers.add_parser("list", help="List all submodules and their status")

    # Update/Sync
    update_parser = subparsers.add_parser("update", help="Update submodules")
    update_parser.add_argument(
        "--sync", action="store_true", help="Sync with upstream remotes"
    )

    # Health Check
    subparsers.add_parser("health", help="Run workspace health check")

    # Test
    subparsers.add_parser("test", help="Run ecosystem-wide tests")

    # Documentation
    subparsers.add_parser("docs", help="Refresh project documentation")

    # Prune
    prune_parser = subparsers.add_parser("prune", help="Prune broken gitlinks")
    prune_parser.add_argument(
        "--fix", action="store_true", help="Apply fixes"
    )

    # Version
    version_parser = subparsers.add_parser("version", help="Manage versioning")
    version_parser.add_argument(
        "--bump", choices=["major", "minor", "patch"], default="minor",
        help="Part of version to bump"
    )

    # Run bulk command
    run_parser = subparsers.add_parser("run", help="Run command in submodules")
    run_parser.add_argument("shell_command", help="Command to execute")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "list":
        update_repos_v5.get_submodule_status()
    elif args.command == "update":
        update_repos_v5.orchestrate_update(sync=args.sync)
    elif args.command == "health":
        success = check_health.run_health_check()
        sys.exit(0 if success else 1)
    elif args.command == "test":
        success = test_ecosystem.run_ecosystem_tests()
        sys.exit(0 if success else 1)
    elif args.command == "docs":
        generate_project_structure.generate_project_structure()
        generate_dashboard.generate_dashboard()
    elif args.command == "prune":
        prune_broken_submodules.prune_broken(dry_run=not args.fix)
    elif args.command == "version":
        new_ver = workspace_version.bump_version(args.bump)
        workspace_version.update_version_file(new_ver)
    elif args.command == "run":
        success = workspace_run.workspace_run(args.shell_command)
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
