#!/usr/bin/env python3
import os
import datetime

EXCLUDE_DIRS = {'.git', '__pycache__', 'node_modules', '.venv', 'venv'}


def generate_tree(startpath):
    tree = []
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        tree.append(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in sorted(files):
            tree.append(f"{subindent}{f}")
    return "\n".join(tree)


def generate_project_structure():
    print("Generating Project Structure...")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = f"""# Project Structure

Last Updated: {now}

## Overview
This file provides an automated visualization of the MilkDrop3 Omni-Workspace \
hierarchy.

```text
{generate_tree('.')}
```
"""

    with open("PROJECT_STRUCTURE.md", "w") as f:
        f.write(content)
    print("PROJECT_STRUCTURE.md generated successfully.")


if __name__ == "__main__":
    generate_project_structure()
