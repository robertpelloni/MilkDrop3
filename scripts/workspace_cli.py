#!/usr/bin/env python3
import argparse
import sys
import os

# Add src to path for package imports
sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
)

from src.workspace import (  # noqa: E402
    update_repos_v5,
    consolidate_branches,
    check_health,
    test_ecosystem,
    generate_dashboard,
    generate_project_structure,
    workspace_run,
    prune_broken_submodules,
    workspace_version,
    archive_handoff,
    workspace_monitor,
    web_dashboard,
    session_orchestrator,
    build,
    search,
    release_manager
)
from src.workspace.core import hypercode, healer  # noqa: E402


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
    update_parser.add_argument(
        "--consolidate", action="store_true",
        help="Merge local feature branches"
    )

    # Health Check
    subparsers.add_parser("health", help="Run workspace health check")

    # Test
    subparsers.add_parser("test", help="Run ecosystem-wide tests")

    # Build
    subparsers.add_parser("build", help="Run ecosystem-wide builds")

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

    # Archive
    subparsers.add_parser("archive", help="Archive current handoff")

    # Release
    release_parser = subparsers.add_parser(
        "release", help="Automate release cycle"
    )
    release_parser.add_argument(
        "--bump", choices=["major", "minor", "patch"], default="minor",
        help="Part of version to bump"
    )

    # Session
    session_parser = subparsers.add_parser(
        "session", help="Manage development session lifecycle"
    )
    session_subparsers = session_parser.add_subparsers(
        dest="session_command", help="Session command"
    )
    start_parser = session_subparsers.add_parser(
        "start", help="Start a new session"
    )
    start_parser.add_argument("model", help="Active AI model name")
    finish_parser = session_subparsers.add_parser(
        "finish", help="Finish the current session"
    )
    finish_parser.add_argument(
        "--bump", choices=["major", "minor", "patch"], default="minor",
        help="Part of version to bump"
    )

    # Monitor
    monitor_parser = subparsers.add_parser(
        "monitor", help="Start real-time monitoring"
    )
    monitor_parser.add_argument(
        "--interval", type=int, default=5, help="Refresh interval in seconds"
    )

    # Web Dashboard
    web_parser = subparsers.add_parser(
        "web", help="Start web-based dashboard"
    )
    web_parser.add_argument(
        "--port", type=int, default=8080, help="Port to run server on"
    )

    # Run bulk command
    run_parser = subparsers.add_parser("run", help="Run command in submodules")
    run_parser.add_argument("shell_command", help="Command to execute")

    # Search
    search_parser = subparsers.add_parser(
        "search", help="Ecosystem-wide search"
    )
    search_parser.add_argument("query", help="Search query")

    # Hypercode
    hypercode_parser = subparsers.add_parser(
        "hypercode", help="Execute hypercode commands"
    )
    hypercode_parser.add_argument("cmd", help="Command to execute")

    # Healer
    healer_parser = subparsers.add_parser(
        "heal", help="Attempt to auto-heal ecosystem failures"
    )
    healer_parser.add_argument("error", help="Error string to diagnose")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "list":
        update_repos_v5.get_submodule_status()
    elif args.command == "update":
        update_repos_v5.orchestrate_update(sync=args.sync)
        if args.consolidate:
            consolidate_branches.orchestrate_consolidation()
    elif args.command == "health":
        success = check_health.run_health_check()
        sys.exit(0 if success else 1)
    elif args.command == "test":
        success = test_ecosystem.run_ecosystem_tests()
        sys.exit(0 if success else 1)
    elif args.command == "build":
        success = build.run_builds()
        sys.exit(0 if success else 1)
    elif args.command == "docs":
        generate_project_structure.generate_project_structure()
        generate_dashboard.generate_dashboard()
    elif args.command == "prune":
        prune_broken_submodules.prune_broken(dry_run=not args.fix)
    elif args.command == "version":
        new_ver = workspace_version.bump_version(args.bump)
        workspace_version.update_version_file(new_ver)
    elif args.command == "archive":
        archive_handoff.archive_handoff()
    elif args.command == "release":
        release_manager.prepare_release(args.bump)
    elif args.command == "session":
        if args.session_command == "start":
            session_orchestrator.start_session(args.model)
        elif args.session_command == "finish":
            success = session_orchestrator.finish_session(bump=args.bump)
            sys.exit(0 if success else 1)
        else:
            session_parser.print_help()
    elif args.command == "monitor":
        workspace_monitor.run_monitor(interval=args.interval)
    elif args.command == "web":
        web_dashboard.run_server(port=args.port)
    elif args.command == "run":
        success = workspace_run.workspace_run(args.shell_command)
        sys.exit(0 if success else 1)
    elif args.command == "search":
        search.run_search(args.query)
    elif args.command == "hypercode":
        success = hypercode.run_hypercode_command(args.cmd)
        sys.exit(0 if success else 1)
    elif args.command == "heal":
        success = healer.attempt_heal(args.error)
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
