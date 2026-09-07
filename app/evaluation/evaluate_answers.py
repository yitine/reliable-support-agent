import json
from pathlib import Path


DATA_PATH = Path(__file__).parent / "evaluation_queries.json"


def load_evaluation_dataset():
    with open(DATA_PATH, "r") as f:
        return json.load(f)


def evaluate_answer(generated_answer: str, expected_answer: str) -> float:
    """Measure simple lexical content coverage."""

    expected_words = set(expected_answer.lower().split())
    answer_words = set(generated_answer.lower().split())

    if not expected_words:
        return 0.0

    overlap = expected_words & answer_words

    return len(overlap) / len(expected_words)


def evaluate_answers():
    dataset = load_evaluation_dataset()

    total = 0
    passed = 0

    for item in dataset:
        if "expected_answer" not in item:
            continue

        query = item["query"]
        expected_answer = item["expected_answer"]

        # Placeholder generated answers for deterministic evaluation.
        # These can later be replaced with cached LLM outputs.
        generated_answer = item.get("generated_answer", "")

        score = evaluate_answer(
            generated_answer,
            expected_answer,
        )

        passed_query = score >= 0.5

        if passed_query:
            passed += 1

        total += 1

        print(
            f"Query: {query}\n"
            f"Expected: {expected_answer}\n"
            f"Generated: {generated_answer}\n"
            f"Content coverage: {score:.2%}\n"
            f"Passed: {passed_query}\n"
        )

    overall_score = passed / total if total else 0.0

    print("=" * 40)
    print(f"Answer evaluation: {overall_score:.2%} ({passed}/{total})")


if __name__ == "__main__":
    evaluate_answers()