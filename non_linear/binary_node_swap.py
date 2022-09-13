from typing import Optional
from collections import deque


class Node:
    """
    Binary tree node.
    """

    def __init__(self, level: int, data: Optional[int] = None):
        self.level = level
        self.data = data
        self.left = None
        self.right = None

    def print_tree(self):
        output = []
        if not self.data:
            return output
        if self.left:
            output.extend(self.left.print_tree())
        output.append(self.data)
        if self.right:
            output.extend(self.right.print_tree())
        return output


class BinaryTree:
    """
    This is different from a binary search tree
    Because a binary search tree, left is always smaller than right.
    This is not the case here.
    """
    def __init__(self, root=None):
        self.root = root if root else Node(1, 1)

    def insert(self, value, level):
        # works on a binary search tree
        current = self.root
        while current:
            if value > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(level, value)
                    break
            else:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(level, value)
                    break
        return 1

    def custom_insert(self, indexes):
        queue = deque([self.root])
        for count, value in enumerate(indexes):
            if len(queue) > 0:
                node_of_interest = queue.popleft()
                left_value, right_value = value[0], value[1]
                if left_value > 0:
                    node_of_interest.left = Node(node_of_interest.level + 1, left_value)
                    queue.append(node_of_interest.left)
                if right_value > 0:
                    node_of_interest.right = Node(node_of_interest.level + 1, right_value)
                    queue.append(node_of_interest.right)
        return 1

    def swap(self, level_to_swap):
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.level % level_to_swap == 0:
                node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def print_tree(root: Node):
    output = []
    if not root:
        return output
    if root.left:
        output.extend(print_tree(root.left))
    output.append(root.data)
    if root.right:
        output.extend(print_tree(root.right))
    return output


def swap_nodes(indexes, queries):
    output = []
    binary_tree = BinaryTree(Node(1, 1))
    binary_tree.custom_insert(indexes)
    for query in queries:
        binary_tree.swap(query)
        output.append(binary_tree.root.print_tree())
    return 0


if __name__ == "__main__":
    # above solution is running into a runtime error when given larger data sets
    # swap_nodes([[2, 3], [-1, 4], [-1, 5], [-1, -1], [-1, -1]], [2])
    swap_nodes([[2, 3]], [1])
