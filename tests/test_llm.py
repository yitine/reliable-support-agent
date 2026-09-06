from app.services.llm import generate_answer


def test_generate_answer():
    answer = generate_answer("Explain RAG in one sentence.")

    assert isinstance(answer, str)
    assert len(answer) > 0