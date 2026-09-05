from app.services.router import route_query

queries = [
    "What is RAG?",
    "What models are suitable for image classification?",
    "What is LoRA?",
]

for query in queries:
    route = route_query(query)
    print(f"{query}")
    print(f"→ {route}\n")
    

def test_route_to_knowledge_base():
    assert route_query("What is RAG?") == "knowledge_base"


def test_route_to_huggingface():
    assert (
        route_query("What models are suitable for image classification?")
        == "huggingface"
    )


def test_route_to_unknown():
    assert route_query("What is LoRA?") == "unknown"
   