import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Loads GOOGLE_API_KEY from your .env file

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")
response = model.generate_content("Say something smart.")
print(response.text)
