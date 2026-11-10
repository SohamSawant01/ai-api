import os
from fastapi import FastAPI
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI API is running!"}

@app.get("/ask")
def ask(question: str):
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=question
    )
    return {"question": question, "answer": response.text}