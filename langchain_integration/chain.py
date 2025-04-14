import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


def get_answer_from_llm(prompt: str) -> str:

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text
