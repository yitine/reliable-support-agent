from app.services.llm import generate_answer


def test_generate_answer():
    answer = generate_answer("Explain RAG in one sentence.")

    assert isinstance(answer, str)
    assert len(answer) > 0
    
def test_generate_answer_with_empty_prompt():
    answer = generate_answer("")

    assert isinstance(answer, str)
    assert len(answer) > 0


def test_generate_answer_handles_api_error(monkeypatch):
    def mock_chat_completion(*args, **kwargs):
        raise RuntimeError("Hugging Face API error")

    monkeypatch.setattr(
        "app.services.llm.client.chat_completion",
        mock_chat_completion,
    )

    answer = generate_answer("Explain RAG.")

    assert answer == "Sorry, I was unable to generate an answer at this time."