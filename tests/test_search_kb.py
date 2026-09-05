from app.services.knowledge_base import search_kb

queries = [
    "What is LoRA?",
    "How does fine-tuning work?",
    "What is RAG?",
    "What models are suitable for image classification?",
]

for query in queries:
    print(f"\nQuery: {query}")

    results = search_kb(query)

    for doc in results:
        print(f"- {doc['title']}")