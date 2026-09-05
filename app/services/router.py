from app.services.knowledge_base import search_kb
from app.services.task_mapping import detect_task


def route_query(query: str) -> str:
    """
    Decide which source should handle the query.
    """
    # First, check whether the internal knowledge base can answer it.
    kb_results = search_kb(query)

    if kb_results:
        return "knowledge_base"

    # If not, check whether the query corresponds to a Hugging Face task.
    task = detect_task(query)

    if task:
        return "huggingface"

    # No suitable source was found.
    return "unknown"