from singly_linkedin_list import LinkedList


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
    return merge(left, right)


def split_linked_list(linked_list):
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
