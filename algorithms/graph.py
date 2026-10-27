NAME = "Graph"
TYPE = "sort"


def run(numbers):
    steps = []
    data = list(numbers)

    if not data:
        steps.append({
            "type": "finished",
            "array": [],
        })
        return steps

    visited = []
    queue = [data[0]]

    while queue:
        current = queue.pop(0)
        if current in visited:
            continue

        visited.append(current)
        steps.append({
            "type": "compare",
            "index": data.index(current),
            "array": visited.copy(),
        })

        for neighbor in range(1, len(data)):
            if neighbor not in visited and data[neighbor] > current:
                queue.append(data[neighbor])

    steps.append({
        "type": "finished",
        "array": visited.copy(),
    })
    return steps        