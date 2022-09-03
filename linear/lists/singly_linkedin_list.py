class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'<Node: {self.data}>'


class LinkedList:
    """
    Singly linked list.
    """
    def __int__(self):
        self.head = None

    def is_empty(self):
        return True if self.head is None else False

    def size(self) -> int:
        """
        unlike len(list_a) which runs in constant time -> 0(1)
        Size of a linked_list has a linear run time. -> 0(n)
        :return:
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
