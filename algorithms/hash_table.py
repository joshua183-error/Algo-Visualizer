NAME = "Hash Table"
TYPE = "sort"


def run(numbers):
    steps = []
    data = list(numbers)
    table = {}

    for value in data:
        key = value % 10
        steps.append({
            "type": "compare",
            "index": key,
            "array": data.copy(),
        })
        table[key] = value

    steps.append({
        "type": "finished",
        "array": sorted(table.values()),
    })
    return steps