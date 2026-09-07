CONFIDENCE_THRESHOLD = 0.8

def determine_escalation(confidence: float) -> str:
    """Determine whether an answer can be returned automatically."""

    if confidence >= CONFIDENCE_THRESHOLD:
        return "auto"

    return "human"
