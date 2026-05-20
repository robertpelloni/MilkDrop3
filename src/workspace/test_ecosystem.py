#!/usr/bin/env python3
from . import workspace_run
import sys
import os
from . import workspace_log


def run_ecosystem_tests():
    workspace_log.info("Validating ecosystem health...")

    submodules = workspace_run.get_configured_submodules()
    if not submodules:
        workspace_log.warn("No submodules to test.")
        return True

    results = {}
    for path in submodules:
        if not os.path.isdir(path):
            workspace_log.warn(f"Skipping {path} (Not cloned)")
            continue

        workspace_log.info(f"Testing {path}...")

        test_cmd = None
        if os.path.exists(os.path.join(path, "package.json")):
            test_cmd = "npm run lint --if-present"
        elif os.path.exists(os.path.join(path, "go.mod")):
            test_cmd = "go vet ./..."

        if test_cmd:
            code, out, err = workspace_run.run_command(test_cmd, cwd=path)
            if code == 0:
                workspace_log.success(f"{path}: Pass")
            else:
                workspace_log.error(f"{path}: FAIL (Code: {code})")
                if out:
                    print(f"STDOUT: {out}")
                if err:
                    print(f"STDERR: {err}")
            results[path] = code
        else:
            workspace_log.info(f"{path}: No supported test suite. Basic OK.")
            results[path] = 0

    workspace_log.info("Ecosystem Test Summary:")
    all_success = True
    for path, code in results.items():
        status = "PASS" if code == 0 else "FAIL"
        print(f"[{status}] {path}")
        if code != 0:
            all_success = False

    return all_success


def main():
    success = run_ecosystem_tests()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
