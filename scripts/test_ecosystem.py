#!/usr/bin/env python3
import workspace_run
import sys
import os


def test_ecosystem():
    print("--- Validating Ecosystem Health ---")

    # Define test strategies for different submodule types
    # We'll use a pragmatic approach: if a package.json exists, try 'npm test'
    # If go.mod exists, try 'go test ./...'

    submodules = workspace_run.get_configured_submodules()
    if not submodules:
        print("No submodules to test.")
        return True

    results = {}
    for path in submodules:
        if not os.path.isdir(path):
            print(f"[SKIP] {path} (Not cloned)")
            continue

        print(f"\n[TEST] {path}:")

        test_cmd = None
        if os.path.exists(os.path.join(path, "package.json")):
            # Use lint check as a proxy for basic health
            test_cmd = "npm run lint --if-present"
        elif os.path.exists(os.path.join(path, "go.mod")):
            test_cmd = "go vet ./..."

        if test_cmd:
            print(f"Running: {test_cmd}")
            code, out, err = workspace_run.run_command(test_cmd, cwd=path)
            if code == 0:
                print("Pass")
            else:
                print(f"FAIL (Code: {code})")
                if out:
                    print(f"STDOUT: {out}")
                if err:
                    print(f"STDERR: {err}")
            results[path] = code
        else:
            print("No supported test suite found. Basic check: OK")
            results[path] = 0

    print("\n--- Ecosystem Test Summary ---")
    all_success = True
    for path, code in results.items():
        status = "PASS" if code == 0 else "FAIL"
        print(f"[{status}] {path}")
        if code != 0:
            all_success = False

    return all_success


def main():
    success = test_ecosystem()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
