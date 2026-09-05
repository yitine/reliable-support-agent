from huggingface_hub import HfApi
from app.services.task_mapping import detect_task


api = HfApi()

def search_models(
    search: str | None = None,
    pipeline_tag: str | None = None,
    limit: int = 5,
): 
    """
    Search Hugging Face models using optional keywords and pipeline tags.

    Results are sorted by download count to prioritize popular models.
    """
    models = api.list_models(
        search=search,
        pipeline_tag=pipeline_tag,
        sort="downloads",
        limit=limit,
    )
    
    return [
        {
            "id": model.id,
            "downloads": model.downloads,
            "likes": model.likes,
        }
        for model in models
    ]
    
def search_models_for_query(query: str, limit: int = 5):
    task = detect_task(query)
    """
    Detect the task from a natural-language query and search for
    relevant Hugging Face models.

    Returns an empty list when no supported task can be detected.
    """
    if task is None:
        return []

    return search_models(
        pipeline_tag=task,
        limit=limit,
    )