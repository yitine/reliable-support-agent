def compute_confidence(
    route: str,
    sources_count: int,
    answer_valid: bool,
) -> float:
    """Compute a simple, interpretable confidence score."""

    if route == "unknown":
        return 0.1

    if sources_count == 0:
        return 0.1

    if answer_valid:
        return 0.9

    return 0.4