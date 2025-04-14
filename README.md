# 🧠 LangChain Gemini Chatbot (Fullstack + Docker)

A fullstack AI chatbot powered by Google Gemini (via LangChain), built with Flask, and bundled in Docker. Includes frontend, backend, testing, and Gemini LLM integration.

---

## 🧰 Tech Stack

- Python + Flask
- LangChain + Google Generative AI (Gemini)
- HTML + TailwindCSS + JavaScript
- Docker
- Pytest

---

## ⚙️ Setup Instructions

```bash
1. Clone the Project


git clone

https://github.com/yourname/langchain-chat.git

cd langchain-chat

2. Set Up Python & Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt


🔑 3. Configure Your Gemini API Key

Create a .env file in the root of your project:

GOOGLE_API_KEY=your-gemini-api-key


4. Run the App Locally

python -m app.app


5. Run Tests Locally

pytest


6. Run with Docker (Tests First, Then App)

docker build -t gemini-chat .
docker run -p 5000:5000 -e GOOGLE_API_KEY=your-gemini-api-key gemini-chat


---


