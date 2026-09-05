from app.services.huggingface import search_models, search_models_for_query



results = search_models(
    pipeline_tag="image-classification",
    limit=5,
)

for model in results:
    print(model)
    


def test_search_image_classification_models():
    results = search_models(
        pipeline_tag="image-classification",
        limit=5,
    )

    assert len(results) > 0
    assert all("id" in model for model in results)
    
def test_search_models_for_image_classification():
    results = search_models_for_query(
        "What models are suitable for image classification?",
        limit=5,
    )

    assert len(results) > 0
    assert all("id" in model for model in results)


def test_search_models_for_unknown_query():
    results = search_models_for_query(
        "What is LoRA?",
        limit=5,
    )

    assert results == []