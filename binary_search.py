from typing import Optional, List

def binary_search(input_list: List[int], val: int) -> Optional[int]:
    input_list.sort()  # we cannot assume the list will be sorted.
    low = 0
    high = len(input_list) - 1

    """find the middle most value"""
    while low <= high:
        mid_val = (low + high)//2

        if input_list[mid_val] == val:
            return mid_val

        """compare the value with the middle most value"""
        if val > input_list[mid_val]:
            low = mid_val + 1
        else:
            high = mid_val - 1
    return None

the_list = [2, 7, 19, 34, 53, 72]
print(binary_search(the_list, 72))
print(binary_search(the_list, 78))
print(binary_search([72, 34, 7, 2, 29, 19], 72))