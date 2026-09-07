from collections import defaultdict
import json
from pathlib import Path

from app.services.router import route_query


DATA_PATH = Path(__file__).parent / "evaluation_queries.json"


def load_evaluation_dataset():
    with open(DATA_PATH, "r") as f:
        return json.load(f)


def evaluate_routing():
    dataset = load_evaluation_dataset()

    total_correct = 0
    route_stats = defaultdict(lambda: {"correct": 0, "total": 0})

    for item in dataset:
        query = item["query"]
        expected = item["expected_route"]

        actual = route_query(query)
        correct = actual == expected

        if correct:
            total_correct += 1

        route_stats[expected]["total"] += 1

        if correct:
            route_stats[expected]["correct"] += 1

        print(
            f"Query: {query}\n"
            f"Expected: {expected}\n"
            f"Actual:   {actual}\n"
            f"Correct:  {correct}\n"
        )

    overall_accuracy = total_correct / len(dataset)

    print("=" * 40)
    print(f"Overall routing accuracy: {overall_accuracy:.2%}")
    print()

    for route, stats in route_stats.items():
        accuracy = stats["correct"] / stats["total"]

        print(
            f"{route}: "
            f"{accuracy:.2%} "
            f"({stats['correct']}/{stats['total']})"
        )


if __name__ == "__main__":
    evaluate_routing()