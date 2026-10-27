NAME = "Bubble Sort"
TYPE = "sort"


def run(numbers):
    steps = []
    data = numbers.copy()

    for end in range(len(data) - 1, 0, -1):
        swapped = False

        for index in range(end):
            steps.append({
                "type": "compare",
                "index1": index,
                "index2": index + 1,
            })

            if data[index] > data[index + 1]:
                data[index], data[index + 1] = (
                    data[index + 1],
                    data[index],
                )
                swapped = True
                steps.append({
                    "type": "swap",
                    "index1": index,
                    "index2": index + 1,
                    "array": data.copy(),
                })

        if not swapped:
            break

    steps.append({
        "type": "finished",
        "array": data.copy(),
    })

    return steps