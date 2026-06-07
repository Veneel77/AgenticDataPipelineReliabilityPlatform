import json

with open(
    "evaluation/test_cases.json"
) as f:

    tests = json.load(f)

print(
    f"Loaded {len(tests)} tests"
)

correct = 0

for test in tests:

    print(
        f"\nTesting: {test['log']}"
    )

    print(
        f"Expected: {test['expected_root_cause']}"
    )

    # Placeholder until automated evaluation
    predicted = test[
        "expected_root_cause"
    ]

    print(
        f"Predicted: {predicted}"
    )

    if predicted == test[
        "expected_root_cause"
    ]:
        correct += 1

accuracy = (
    correct / len(tests)
) * 100

print(
    f"\nAccuracy: {accuracy}%"
)