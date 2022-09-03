class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SinglylinkedList:
    """
    Each node only has a reference to the next node.
    Doubly linked list would be one each node also knows about the previous node.
    """
    def __init__(self):
        self.headval = None

    def print_list(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


list1 = SinglylinkedList()
list1.headval = Node("Mon")
e2 = Node('Tue')
e3 = Node('Wed')

# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list1.print_list()
