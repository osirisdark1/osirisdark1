import os
import subprocess
from pathlib import Path
from typing import Optional


def save_design_to_project(design_text: str, project_dir: str) -> Path:
    """Save design text to a KiCad project directory."""
    os.makedirs(project_dir, exist_ok=True)
    sch_path = Path(project_dir) / "design.kicad_sch"
    with sch_path.open("w") as f:
        f.write(design_text)
    return sch_path


def open_in_kicad(sch_path: str) -> bool:
    """Attempt to open the schematic using the kicad-cli tool."""
    try:
        subprocess.run(["kicad-cli", "sch", "edit", sch_path], check=True)
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        return False
