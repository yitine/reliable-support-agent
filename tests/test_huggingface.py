from app.services.huggingface import search_models


results = search_models(
    pipeline_tag="image-classification",
    limit=5,
)

for model in results:
    print(model)