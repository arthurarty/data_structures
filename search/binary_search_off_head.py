from typing import List, Optional


def binary_search(input_list: List[int], target: int) -> Optional[int]:
    """
    Returns the index at which the target was found.
    :param input_list:
    :param target:
    :return:
    """
    if len(input_list) == 0:
        return None
    input_list.sort()
    first = 0
    last = len(input_list) - 1

    while first <= last:
        midpoint = (first + last)//2
        if input_list[midpoint] == target:
            return midpoint
        if input_list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


the_list = [2, 7, 19, 34, 53, 72]
print(binary_search(the_list, 72))
print(binary_search(the_list, 78))
print(binary_search([72, 34, 7, 2, 29, 19], 72))
