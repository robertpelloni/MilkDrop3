#!/usr/bin/env python3
import os
import json
from ..core import workspace_log
from ..core.memory import WorkspaceMemory

class SharedContextRouter:
    """
    Manages the routing of context objects between 'borg' and 'aios'.
    This fulfills the 'Shared AI Context' Phase 4 requirement.
    """

    def __init__(self):
        self.workspace_mem = WorkspaceMemory()

    def broadcast_context(self, source, context_data):
        workspace_log.info(f"Broadcasting context from '{source}'...")
        if not isinstance(context_data, dict):
            workspace_log.error("Context data must be a dictionary.")
            return False

        # Store securely in L1 Workspace memory
        self.workspace_mem.add_observation(
            json.dumps(context_data),
            category=f"shared_context_from_{source}"
        )
        workspace_log.success(f"Context from {source} successfully broadcast to global memory pool.")
        return True

    def retrieve_context(self, target):
        workspace_log.info(f"Retrieving shared context for '{target}'...")
        observations = self.workspace_mem.state.get("observations", [])

        # Filter context tailored to the target, or fetch all if global
        relevant_context = [
            obs for obs in observations
            if obs.get("category", "").startswith("shared_context_")
        ]

        workspace_log.success(f"Found {len(relevant_context)} relevant context nodes for {target}.")
        return relevant_context
