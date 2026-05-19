# Deployment & Setup - MilkDrop3 Omni-Workspace

## Prerequisites
- **Git:** Ensure Git is installed and configured.
- **Python 3.8+:** Required for running management scripts.
- **Node.js / Bun (Optional):** Required for certain frontend-related submodules.

## Initial Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/robertpelloni/MilkDrop3.git
   cd MilkDrop3
   ```
2. **Initialize Submodules:**
   ```bash
   # This will be handled by the update script in the future
   python scripts/update_repos_v5.py
   ```
3. **Environment Variables:**
   - Copy `.env.example` to `.env` if it exists.
   - Fill in any required API keys (e.g., for model providers in `borg`).

## Management
- **Updating Submodules:** Run `python scripts/update_repos_v5.py` regularly to stay in sync with upstream and internal changes.
- **Adding New Submodules:** Follow the protocol in `docs/UNIVERSAL_LLM_INSTRUCTIONS.md`.
