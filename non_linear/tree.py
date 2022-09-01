"""
Tree structure how to add to a tree and how to print a tree.
"""
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def insert(self, data):
        # compare the new value with the parent value
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find_value(self, search_value_key):
        if search_value_key < self.data:
            if self.left is None:
                return f'{str(search_value_key)} Not found'
            return self.left.find_value(search_value_key)
        elif search_value_key > self.data:
            if self.right is None:
                return f'{str(search_value_key)} Not found'
            return self.right.find_value(search_value_key)
        else:
            print(f'{str(self.data)} is found')

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.print_tree()
print(root.find_value(7))
print(root.find_value(14))
