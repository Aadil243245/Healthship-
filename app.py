from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow browser requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserQuery(BaseModel):
    question: str

# Simple health answers
health_answers = {
    "fever": "Drink plenty of fluids, get rest, and monitor your temperature. If it persists for more than 3 days, see a doctor.",
    "headache": "Stay hydrated, rest, and avoid screen time. If severe or persistent, consult a doctor.",
    "cold": "Drink warm fluids, rest well, and keep yourself warm.",
    "stomach pain": "Eat light meals, drink water, and rest. If pain is severe or persistent, seek medical help.",
}

@app.get("/")
def home():
    return {"message": "Welcome to Healthship API"}

@app.post("/chat")
def chat(query: UserQuery):
    question_lower = query.question.lower()
    for key in health_answers:
        if key in question_lower:
            return {"answer": health_answers[key]}
    return {"answer": "I'm not sure about that. Please consult a doctor for proper medical advice."}
