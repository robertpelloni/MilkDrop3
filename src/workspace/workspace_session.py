#!/usr/bin/env python3
import json
import os
import datetime
from . import workspace_log

SESSION_FILE = os.path.join("logs", "session_state.json")


def load_session():
    if os.path.exists(SESSION_FILE):
        try:
            with open(SESSION_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            workspace_log.error(f"Failed to load session state: {str(e)}")
    return {
        "active_model": "Unknown",
        "session_start": None,
        "last_update": None
    }


def save_session(state):
    try:
        with open(SESSION_FILE, "w") as f:
            json.dump(state, f, indent=4)
        return True
    except Exception as e:
        workspace_log.error(f"Failed to save session state: {str(e)}")
        return False


def start_session(model_name):
    state = load_session()
    state["active_model"] = model_name
    state["session_start"] = datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    state["last_update"] = state["session_start"]
    save_session(state)
    workspace_log.info(f"Session started for model: {model_name}")


def get_session_info():
    state = load_session()
    workspace_log.info("Current Session Info:")
    workspace_log.info(f"  Active Model: {state.get('active_model')}")
    workspace_log.info(f"  Started: {state.get('session_start')}")


def main():
    start_session("Jules")
    get_session_info()


if __name__ == "__main__":
    main()
