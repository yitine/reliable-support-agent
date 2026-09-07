from app.services.validator import validate_answer


def test_validate_grounded_answer():
    answer = "RAG is an AI framework that retrieves relevant information."
    context = (
        "Retrieval-Augmented Generation (RAG) is an AI framework "
        "that retrieves relevant information from a knowledge base."
    )

    assert validate_answer(answer, context) is True


def test_validate_ungrounded_answer():
    answer = "RAG was invented in 2018 by a specific company."
    context = "RAG retrieves relevant information from a knowledge base."

    assert validate_answer(answer, context) is False


def test_validate_empty_input():
    assert validate_answer("", "some context") is False
    assert validate_answer("some answer", "") is False