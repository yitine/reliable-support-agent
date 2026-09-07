from app.evaluation.evaluate_answers import evaluate_answer


def test_answer_with_good_content_coverage():
    expected = (
        "RAG retrieves relevant information from a knowledge base "
        "and uses it to generate an answer."
    )

    generated = (
        "RAG retrieves relevant information from a knowledge base "
        "and uses it to generate an answer."
    )

    score = evaluate_answer(generated, expected)

    assert score == 1.0


def test_answer_with_partial_content_coverage():
    expected = (
        "RAG retrieves relevant information from a knowledge base "
        "and uses it to generate an answer."
    )

    generated = (
        "RAG retrieves relevant information from a knowledge base."
    )

    score = evaluate_answer(generated, expected)

    assert 0 < score < 1


def test_answer_with_no_content_coverage():
    expected = (
        "RAG retrieves relevant information from a knowledge base "
        "and uses it to generate an answer."
    )

    generated = "Paris is the capital of France."

    score = evaluate_answer(generated, expected)

    assert score == 0.0