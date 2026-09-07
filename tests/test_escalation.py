from app.services.escalation import determine_escalation


def test_high_confidence_is_automatic():
    assert determine_escalation(0.9) == "auto"


def test_threshold_confidence_is_automatic():
    assert determine_escalation(0.8) == "auto"


def test_low_confidence_requires_human_review():
    assert determine_escalation(0.4) == "human"


def test_unknown_route_confidence_requires_human_review():
    assert determine_escalation(0.1) == "human"