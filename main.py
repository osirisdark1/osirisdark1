from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import openai
import os

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
