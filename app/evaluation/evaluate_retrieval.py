import json
from pathlib import Path

from app.services.knowledge_base import search_kb


DATA_PATH = Path(__file__).parent / "evaluation_queries.json"


def load_evaluation_dataset():
    with open(DATA_PATH, "r") as f:
        return json.load(f)


def evaluate_retrieval(top_k: int = 3):
    dataset = load_evaluation_dataset()

    hits = 0
    total = 0

    for item in dataset:
        if item["expected_route"] != "knowledge_base":
            continue

        query = item["query"]
        expected_source = item["expected_source"]

        results = search_kb(query, top_k=top_k)
        retrieved_ids = [doc["id"] for doc in results]

        hit = expected_source in retrieved_ids

        if hit:
            hits += 1

        total += 1

        print(
            f"Query: {query}\n"
            f"Expected source: {expected_source}\n"
            f"Retrieved: {retrieved_ids}\n"
            f"Hit@{top_k}: {hit}\n"
        )

    recall_at_k = hits / total if total else 0.0

    print("=" * 40)
    print(f"Recall@{top_k}: {recall_at_k:.2%} ({hits}/{total})")


if __name__ == "__main__":
    evaluate_retrieval()
    
    