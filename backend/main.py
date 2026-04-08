from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

chat_history = []

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        user_message = req.message

        chat_history.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=chat_history
        )

        ai_reply = response.choices[0].message.content

        chat_history.append({"role": "assistant", "content": ai_reply})

        return {"reply": ai_reply}

    except Exception as e:
        return {"error": str(e)}