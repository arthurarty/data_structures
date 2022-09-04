from typing import List


def merge_sort_list(input_list: List[int]) -> List[int]:
    """
    Sorts a list in ascending order.
    returns a new sorted list.

    Divide: Find the midpoint of the list and divide into sublists.
    Conquer: recursively sort the sublists created in previous step.
    Combine: Merge the sorted sublists created in previous step.
    """
    if len(input_list) <= 1:
        return input_list

    left_half, right_half = split(input_list)
    left = merge_sort_list(left_half)
    right = merge_sort_list(right_half)

    return merge(left, right)


def split(the_list: List[int]):
    """
    Divides the unsorted list at midpoint into sublists.
    Returns two sublists - left and right.
    :param the_list:
    :return:
    """
    midpoint = len(the_list)//2
    return the_list[:midpoint], the_list[midpoint:]


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merges two lists (arrays), sorting them in the process.
    Returns a new merged list
    :param left:
    :param right:
    :return:
    """
    output_list = []
    ii = 0
    jj = 0

    while ii < len(left):
        pass
