#!/usr/bin/env python3
import subprocess
import sys
import os


def run_command(command, cwd=None):
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, cwd=cwd
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except Exception as e:
        return 1, "", str(e)


def get_configured_submodules():
    if not os.path.exists(".gitmodules"):
        return []
    output = subprocess.run(
        ["git", "config", "-f", ".gitmodules", "--get-regexp", "path"],
        capture_output=True, text=True
    ).stdout
    paths = []
    for line in output.split('\n'):
        if line.strip():
            parts = line.split()
            if len(parts) >= 2:
                paths.append(parts[1])
    return paths


def workspace_run(command):
    submodules = get_configured_submodules()
    if not submodules:
        print("No submodules configured.")
        return

    print(f"--- Running '{command}' across {len(submodules)} submodules ---")
    results = {}

    for path in submodules:
        if not os.path.isdir(path):
            print(f"[SKIP] {path} (Directory not found)")
            continue

        print(f"\n[RUN] {path}:")
        code, out, err = run_command(command, cwd=path)

        if code == 0:
            print(out if out else "Success (No output)")
        else:
            print(f"FAILED (Code: {code})")
            if out:
                print(f"STDOUT: {out}")
            if err:
                print(f"STDERR: {err}")

        results[path] = code

    print("\n--- Summary ---")
    all_success = True
    for path, code in results.items():
        status = "OK" if code == 0 else "FAIL"
        print(f"[{status}] {path}")
        if code != 0:
            all_success = False

    return all_success


def main():
    if len(sys.argv) < 2:
        print("Usage: scripts/workspace_run.py <command>")
        sys.exit(1)

    command = " ".join(sys.argv[1:])
    success = workspace_run(command)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
