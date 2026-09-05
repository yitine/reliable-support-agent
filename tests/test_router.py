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