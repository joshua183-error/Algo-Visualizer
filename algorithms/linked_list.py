NAME = "Linked List"
TYPE = "sort"


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def run(numbers):
    steps = []
    data = list(numbers)
    head = None
    tail = None

    for value in data:
        node = Node(value)
        if head is None:
            head = node
        else:
            tail.next = node
        tail = node

        steps.append({
            "type": "compare",
            "index": len(data) - 1,
            "array": data.copy(),
        })

    values = []
    current = head
    while current is not None:
        values.append(current.value)
        current = current.next

    steps.append({
        "type": "finished",
        "array": values,
    })
    return steps