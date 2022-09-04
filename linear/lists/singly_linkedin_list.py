from typing import Optional


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
    head = None

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

    def add(self, data):
        """
        Adds a new node containing data at the head of the linked list.
        Takes 0(1) time.
        :param data:
        :return:
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, search_key) -> Optional[Node]:
        """
        Search for the first node containing data that matches the key.
        Linked list can have the value multiple times.

        Takes 0(n) time a.k.a linear time.
        :param search_key:
        :return:
        """
        current = self.head

        while current:
            if current.data == search_key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data: int, index: int):
        """
        Inserting into the linked list is 0(1) however finding the position to insert
        at is 0(n) since we go through the list to find the node at the index
        :param data:
        :param index:
        :return:
        """
        if index == 0:
            self.add(data)
            return

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                """
                We are counting how many steps we are moving from head.
                i.e Index is how many steps from head.
                When we reach position 1, that is where we want to insert.
                """
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node.next_node

    def remove_by_index(self, index: int) -> bool:
        if index == 0:
            current = self.head
            next_node = current.next_node
            self.head = next_node
            return True
        elif index < 0:
            """
            Element is not in linked list. indexs are normally >= 0
            """
            return False

        current_node = self.head
        while index > 1:
            current_node = current_node.next_node
            index = -1
        prev_node = current_node
        node_to_delete = current_node.next_node
        prev_node.next_node = node_to_delete.next_node
        return True

    def remove(self, search_key):
        current = self.head
        previous = None

        while current:
            if current.data == search_key:
                if previous:
                    previous.next_node = current.next_node
                else:
                    self.head = current.next_node
                break
            previous = current
            current = current.next_node

    def __repr__(self) -> str:
        """
        Return a string representation of the list.
        Takes 0(n) time i.e linear time because it goes over every item in the list.
        :return: str
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)


if __name__ == '__main__':
    N1 = Node(5)
    N3 = Node(65)
    N2 = Node(89, N3)
    N1.next_node = N2
    ll = LinkedList()
    ll.head = N1
    print(ll.size())
    print(ll.head)
    ll.add(781)
    ll.add(9099)
    ll.add(532)
    print(ll.head)
    print(ll.head.next_node)
    print(ll)
    print(ll.search(65))
    print(ll.search(4524))
    ll.insert(88, 3)
    print(ll)
    ll.remove_by_index(2)
    print(ll)
    ll.remove(88)
    print(ll)
