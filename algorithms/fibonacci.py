NAME = "Fibonacci"
TYPE = "sort"


def run(numbers):
    steps = []
    if not numbers:
        steps.append({
            "type": "finished",
            "array": [0],
        })
        return steps

    limit = max(0, int(numbers[0]))
    sequence = []
    a, b = 0, 1

    for _ in range(limit):
        steps.append({
            "type": "compare",
            "index": len(sequence),
            "array": sequence.copy(),
        })
        sequence.append(a)
        a, b = b, a + b

    steps.append({
        "type": "finished",
        "array": sequence,
    })
    return steps