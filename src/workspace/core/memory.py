import json
import os
from datetime import datetime


class WorkspaceMemory:
    """
    Manages persistent memory for the workspace, allowing AI agents
    to track observations, preferences, and state across sessions.
    """
    def __init__(self, memory_file="logs/workspace_memory.json"):
        self.memory_file = memory_file
        self.state = self._load()

    def _load(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except Exception:
                return {"observations": [], "preferences": {}, "sessions": []}
        return {"observations": [], "preferences": {}, "sessions": []}

    def save(self):
        os.makedirs(os.path.dirname(self.memory_file), exist_ok=True)
        with open(self.memory_file, 'w') as f:
            json.dump(self.state, f, indent=2)

    def add_observation(self, content, category="general"):
        self.state["observations"].append({
            "timestamp": datetime.now().isoformat(),
            "category": category,
            "content": content
        })
        self.save()

    def set_preference(self, key, value):
        self.state["preferences"][key] = value
        self.save()

    def get_preferences(self):
        return self.state["preferences"]

    def log_session(self, model_name, changes_summary):
        self.state["sessions"].append({
            "timestamp": datetime.now().isoformat(),
            "model": model_name,
            "summary": changes_summary
        })
        self.save()


# Global memory instance
memory = WorkspaceMemory()
