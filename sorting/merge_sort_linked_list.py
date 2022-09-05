from singly_linkedin_list import LinkedList, Node


def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - recursively divide the linked list into sublists containing a single node.
    - repeatedly merget the sublists to produce sorted sublists util one remains.

    returns a sorted linked list.
    :param linked_list:
    :return:
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split_linked_list(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge_linked_list(left, right)


def split_linked_list(linked_list: LinkedList):
    """
    Divide the unsorted list at midpoint into sublists.
    :param linked_list:
    :return:
    """
    if linked_list is None or linked_list.head is None:
        return linked_list, None
    else:
        size = linked_list.size()
        mid_point = size//2

        mid_node = linked_list.node_at_index(mid_point - 1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        return left_half, right_half


def merge_linked_list(left_list, right_list):
    """
    Merges two linked lists, sorting by data in nodes.
    Returns a new, merged list.
    :param left_list:
    :param right_list:
    :return:
    """

    # create a new linked list that contains nodes from merging left and right.
    merged = LinkedList()
    # add a fake head that is discarded later
    merged.add(0)

    # set current to the head of the linked list
    current = merged.head

    # obtain head nodes for left and right linked lists
    left_head = left_list.head
    right_head = right_list.head

    # iterate over left and right, till we reach the tail of either.
    while left_head or right_head:
        if left_head is None:  # we have passed the tail of the left. Ad the node from right
            current.next_node = right_head
            # call next on right to set loop condition to false
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            # call next to left to set loop condition to false
            left_head = left_head.next_node
        else:
            left_data = left_head.data
            right_data = right_head.data
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node

    # disregard fake node.
    head = merged.head.next_node
    merged.head = head
    return merged


if __name__ == "__main__":
    new_ll = LinkedList()
    new_ll.add(10)
    new_ll.add(3)
    new_ll.add(5)
    new_ll.add(93)
    new_ll.add(1)
    new_ll.add(2)
    new_ll.add(90)
    new_ll.add(101)
    new_ll.add(130)
    print(new_ll)
    sorted_ll = merge_sort(new_ll)
    print(sorted_ll)
    # print(new_ll.size())
    # print(sorted_ll)
