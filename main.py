from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import openai
import os
from uuid import uuid4

from kicad_integration import save_design_to_project, open_in_kicad
from vscode_workspace import create_workspace, open_in_vscode

load_dotenv()

app = FastAPI()


@app.on_event("startup")
def init_openai() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OpenAI API key not configured")
    openai.api_key = api_key


class Prompt(BaseModel):
    text: str

@app.post("/generate-circuit")
async def generate_circuit(prompt: Prompt):

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt.text}]
    )
    result = response["choices"][0]["message"]["content"]
    return {"design": result}


@app.post("/generate-circuit-kicad")
async def generate_circuit_kicad(prompt: Prompt):
    """Generate a circuit and attempt to open it with KiCad."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt.text}],
    )
    design = response["choices"][0]["message"]["content"]
    project_dir = f"project_{uuid4().hex}"
    sch_path = save_design_to_project(design, project_dir)
    opened = open_in_kicad(str(sch_path))
    return {"design": design, "kicad_project": project_dir, "opened_in_kicad": opened}


@app.post("/generate-circuit-workspace")
async def generate_circuit_workspace(prompt: Prompt):
    """Generate a circuit and create a VS Code workspace."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt.text}],
    )
    design = response["choices"][0]["message"]["content"]
    project_dir = f"project_{uuid4().hex}"
    sch_path = save_design_to_project(design, project_dir)
    workspace = f"{project_dir}.code-workspace"
    create_workspace(project_dir, workspace)
    opened_kicad = open_in_kicad(str(sch_path))
    opened_vscode = open_in_vscode(workspace)
    return {
        "design": design,
        "workspace": workspace,
        "kicad_project": project_dir,
        "opened_in_kicad": opened_kicad,
        "opened_in_vscode": opened_vscode,
    }
