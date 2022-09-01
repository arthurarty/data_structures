from binary_tree_height import BinarySearchTree, height, level_order
from typing import List


def create_binary_search_tree(input_list: List[int]):
    tree = BinarySearchTree()
    for ii in input_list:
        tree.create(ii)
    return tree

def test_binary_search_tree():
    tree = create_binary_search_tree([3, 5, 2,  1, 4, 6, 7])
    assert height(tree.root) == 3

def test_print_level_order():
    tree = create_binary_search_tree([3, 5, 2, 1, 4, 6, 7])
    output = level_order(tree.root)
    assert output == "3 2 5 1 4 6 7 "


if __name__ == "__main__":
    test_print_level_order()
    test_binary_search_tree()
