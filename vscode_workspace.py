import json
from pathlib import Path


def create_workspace(project_dir: str, workspace_path: str) -> None:
    """Create a Visual Studio Code workspace referencing the project."""
    ws = {
        "folders": [{"path": project_dir}],
        "settings": {"kicad.projectPath": project_dir},
    }
    Path(workspace_path).write_text(json.dumps(ws, indent=2))
