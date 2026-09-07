from app.services.confidence import compute_confidence


def test_high_confidence():
    confidence = compute_confidence(
        route="knowledge_base",
        sources_count=3,
        answer_valid=True,
    )

    assert confidence == 0.9


def test_low_confidence_for_unknown_route():
    confidence = compute_confidence(
        route="unknown",
        sources_count=0,
        answer_valid=False,
    )

    assert confidence == 0.1


def test_medium_confidence_for_invalid_answer():
    confidence = compute_confidence(
        route="knowledge_base",
        sources_count=3,
        answer_valid=False,
    )

    assert confidence == 0.4


def test_low_confidence_without_sources():
    confidence = compute_confidence(
        route="knowledge_base",
        sources_count=0,
        answer_valid=True,
    )

    assert confidence == 0.1