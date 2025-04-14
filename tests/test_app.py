import pytest
from app.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_chat_success(client, monkeypatch):
    def mock_response(prompt):
        return "Mocked Gemini reply!"

    # ✅ Patch the function inside *app.routes*, not just langchain_integration
    import app.routes
    monkeypatch.setattr(app.routes, "get_answer_from_llm", mock_response)

    response = client.post("/chat", json={"message": "Hello"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["answer"] == "Mocked Gemini reply!"


def test_chat_empty_message(client):
    response = client.post("/chat", json={"message": ""})
    assert response.status_code == 400
    assert response.get_json()["error"] == "No message provided"


def test_chat_missing_json(client):
    response = client.post("/chat", data="not-json", content_type="application/json")
    assert response.status_code == 400 or response.status_code == 500

