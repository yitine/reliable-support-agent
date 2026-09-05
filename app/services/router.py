from app.services.knowledge_base import search_kb


def route_query(query: str) -> str:
    """
    Decide which source should handle the query.
    """

    kb_results = search_kb(query)

    if kb_results:
        return "knowledge_base"

    return "huggingface"