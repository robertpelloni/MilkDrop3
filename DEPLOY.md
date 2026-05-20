# Deployment & Setup - MilkDrop3 Omni-Workspace

## Prerequisites
- **Git:** Ensure Git is installed and configured.
- **Python 3.8+:** Required for running management scripts.
- **Node.js / Bun:** Required for most core submodules.
- **Turbo & PNPM:** Essential for monorepo submodule management.
  ```bash
  npm install -g turbo pnpm
  ```
- **Go:** Required for `borg` and `aios` backend components.

## Initial Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/robertpelloni/MilkDrop3.git
   cd MilkDrop3
   ```
2. **Initialize & Sync Submodules:**
   ```bash
   # This will set up remotes and fetch the latest code
   python scripts/update_repos_v5.py --sync
   ```
3. **Environment Variables:**
   - Workspace level: Copy `.env.example` to `.env` if it exists.
   - Submodule level: Refer to individual submodule documentation (e.g., `borg/DEPLOY.md`).

## Submodule Management
- **Universal Update:** `python scripts/update_repos_v5.py`
- **Upstream Sync:** `python scripts/update_repos_v5.py --sync`
- **Bulk Commands:** Use `python scripts/workspace_run.py <command>` (e.g., `python scripts/workspace_run.py npm install`).

## Troubleshooting
### Missing 'turbo' or 'pnpm'
If tests fail with `turbo: not found`, ensure global tools are installed:
```bash
npm install -g turbo pnpm
```

### Submodule Health Issues
If `scripts/check_health.py` reports issues, try a forced recursive update:
```bash
git submodule update --init --recursive --force
```

### Broken Internal Gitlinks
The workspace automatically prunes broken mode 160000 entries found in some upstream forks. If you encounter "No url found for submodule" errors, run:
```bash
python scripts/update_repos_v5.py
```
This will trigger the pruning and maintenance workflow.
