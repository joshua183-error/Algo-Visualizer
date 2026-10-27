NAME = "Factorial"
TYPE = "sort"


def run(numbers):
    steps = []
    if not numbers:
        steps.append({
            "type": "finished",
            "array": [1],
        })
        return steps

    value = int(numbers[0])
    result = 1

    for current in range(1, value + 1):
        steps.append({
            "type": "compare",
            "index": current,
            "array": [current],
        })
        result *= current

    steps.append({
        "type": "finished",
        "array": [result],
    })
    return steps