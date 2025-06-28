from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()
openai.api_key = os.environ["OPENAI_API_KEY"]

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
