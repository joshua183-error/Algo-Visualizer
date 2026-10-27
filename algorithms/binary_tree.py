NAME = "Binary Tree"
TYPE = "sort"


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def _insert(root, value, steps):
    if root is None:
        return Node(value)

    steps.append({
        "type": "compare",
        "index": value,
        "array": [value],
    })

    if value < root.value:
        root.left = _insert(root.left, value, steps)
    else:
        root.right = _insert(root.right, value, steps)

    return root


def _in_order(node, values):
    if node is None:
        return
    _in_order(node.left, values)
    values.append(node.value)
    _in_order(node.right, values)


def run(numbers):
    steps = []
    if not numbers:
        steps.append({
            "type": "finished",
            "array": [],
        })
        return steps

    root = None
    for value in numbers:
        root = _insert(root, value, steps)

    ordered = []
    _in_order(root, ordered)

    steps.append({
        "type": "finished",
        "array": ordered.copy(),
    })
    return steps