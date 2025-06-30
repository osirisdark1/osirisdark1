# FastAPI Circuit Generator

This project exposes a small API built with [FastAPI](https://fastapi.tiangolo.com/) that uses the OpenAI API to generate circuit designs from text prompts.
Additional endpoints allow you to create a KiCad project and a VS Code workspace from the generated design. If the `kicad-cli` tool is installed, the server will attempt to launch KiCad automatically. The server will also try to open the generated VS Code workspace using the `code` command when available.

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the server

Install dependencies and configure your OpenAI API key. You can set `OPENAI_API_KEY` in the environment or place it in a `.env` file. The key is loaded on startup and the server will fail to launch if it is missing. Start the development server with:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000` by default.

If the API key is not configured, the `/generate-circuit` endpoint will return an error message indicating that the key is missing.

### KiCad integration

Two additional endpoints provide basic integration with KiCad and Visual Studio Code:

- `POST /generate-circuit-kicad` - Generates a circuit and saves it as a KiCad project. If the optional `kicad-cli` tool is installed, the schematic will be opened automatically.
- `POST /generate-circuit-workspace` - Same as above but also creates a `.code-workspace` file for VS Code. If the `code` CLI is installed, the workspace will be opened automatically.

Example `.env` file:

```env
OPENAI_API_KEY=sk-...
```
