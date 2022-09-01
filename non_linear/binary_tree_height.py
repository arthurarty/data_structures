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
    if root is None:
        return
    if root.left:
        print_tree(root.left)
    print(root.info)
    if root.right:
        print_tree(root.right)

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if root is None:
        return -1
    left_side = height(root.left)
    right_side = height(root.right)
    return max(left_side, right_side) + 1


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
    print_tree(tree.root)
