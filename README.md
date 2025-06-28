# FastAPI Circuit Generator

This project exposes a small API built with [FastAPI](https://fastapi.tiangolo.com/) that uses the OpenAI API to generate circuit designs from text prompts.

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

Example `.env` file:

```env
OPENAI_API_KEY=sk-...
```
