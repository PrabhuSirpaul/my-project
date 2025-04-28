from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

class TextData(BaseModel):
    text: str

def simple_summarize(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    if len(sentences) <= 2:
        return text
    else:
        return ' '.join(sentences[:2])

@app.post("/summarize")
def summarize_text(data: TextData):
    summary = simple_summarize(data.text)
    return {"summary": summary}
