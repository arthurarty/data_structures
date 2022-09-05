from typing import List

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def print_tree(root: Node):
    """
    This is a Depth First Traversal using inorder.
    i.e <left> <root> <right>
    Where root is the current node.
    :param root:
    :return: None
    """
    if root is None:
        return
    if root.left:
        print_tree(root.left)
    print(root.info)
    if root.right:
        print_tree(root.right)


def height(root):
    """
    Depth first approach to finding the height.
    :param root:
    :return:
    """
    if root is None:
        return -1
    left_side = height(root.left)
    right_side = height(root.right)
    return max(left_side, right_side) + 1


def level_order(root: Node) -> str:
    """
    Breadth First approach to visiting all nodes in a tree.
    :param root:
    :return: None
    """
    if root is None:
        return ""
    queue: List[Node] = [root]
    output_str = ''
    while len(queue) > 0:
        output_str += f"{queue[0].info} "
        current_node = queue.pop(0)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return output_str


def print_level_order(root: Node):
    print(level_order(root))


if __name__ == "__main__":
    tree = BinarySearchTree()
    # t = int(input())
    #
    # arr = list(map(int, input().split()))
    # for i in range(t):
    #     tree.create(arr[i])

    arr = [3, 5, 2, 1, 4, 6, 7]
    for ii in arr:
        tree.create(ii)
    # print(height(tree.root))
    # print_tree(tree.root)
    print_level_order(tree.root)
