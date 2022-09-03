class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f'<Node: {self.data}>'


class LinkedList:
    """
    Singly linked list.
    """

    def __int__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

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


if __name__ == '__main__':
    N1 = Node(5)
    N3 = Node(65)
    N2 = Node(89, N3)
    N1.next_node = N2
    ll = LinkedList()
    ll.head = N1
    print(ll.size())
