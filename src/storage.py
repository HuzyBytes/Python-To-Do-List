import json
from pathlib import Path

# Use a relative path to the data folder
DATA_PATH = Path("data/tasks.json")

def load_tasks():
    """Loads tasks from the JSON file."""
    if DATA_PATH.exists():
        with open(DATA_PATH, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Saves the current task list to the JSON file."""
    # Create the data directory if it doesn't exist
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w") as f:
        json.dump(tasks, f, indent=2)