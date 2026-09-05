from huggingface_hub import HfApi


api = HfApi()


def search_models(
    search: str | None = None,
    pipeline_tag: str | None = None,
    limit: int = 5,
):
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