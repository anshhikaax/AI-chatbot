from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

# Root route (for sanity check)
@app.get("/")
def read_root():
    return {"message": "Hello from AI Agent Backend!"}

# Request body model for /ask
class AskRequest(BaseModel):
    question: str

# Response route for AI QnA
@app.post("/ask")
def ask_question(data: AskRequest):
    # For now, fake answer logic
    question = data.question
    fake_answer = f"You asked: '{question}', and I say: Just chill, I'm working on it 😉"
    return {"answer": fake_answer}
