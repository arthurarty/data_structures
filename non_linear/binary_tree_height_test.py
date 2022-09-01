from binary_tree_height import BinarySearchTree, height

def test_binary_search_tree():
    input_tree = [3, 5, 2,  1, 4, 6, 7]
    tree = BinarySearchTree()
    for ii in input_tree:
        tree.create(ii)
    assert height(tree) == 3
