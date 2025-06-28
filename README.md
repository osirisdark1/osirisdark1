# FastAPI Circuit Generator

This project exposes a small API built with [FastAPI](https://fastapi.tiangolo.com/) that uses the OpenAI API to generate circuit designs from text prompts.

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the server

Set the `OPENAI_API_KEY` environment variable and start the development server with:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000` by default.
