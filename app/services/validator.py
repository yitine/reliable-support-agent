def validate_answer(answer: str, context: str) -> bool:
    """
    Basic validation to check whether the generated answer
    is grounded in the provided context.
    """
    if not answer or not context:
        return False

    answer_words = set(answer.lower().split())
    context_words = set(context.lower().split())

    overlap = answer_words & context_words

    return len(overlap) >= 3