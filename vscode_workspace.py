import json
import subprocess
from pathlib import Path


def create_workspace(project_dir: str, workspace_path: str) -> None:
    """Create a Visual Studio Code workspace referencing the project."""
    ws = {
        "folders": [{"path": project_dir}],
        "settings": {"kicad.projectPath": project_dir},
    }
    Path(workspace_path).write_text(json.dumps(ws, indent=2))


def open_in_vscode(workspace_path: str) -> bool:
    """Attempt to open the workspace using the VS Code command line tool."""
    try:
        subprocess.run(["code", workspace_path], check=True)
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        return False
