from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_ask_with_knowledge_base():
    response = client.post(
        "/ask",
        json={"query": "What is RAG?"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["route"] == "knowledge_base"
    assert isinstance(data["answer"], str)
    assert len(data["answer"]) > 0
    assert len(data["sources"]) > 0
    assert data["query"] == "What is RAG?"