from typing import List, Optional


def linear_search(input_list: List[int], search_target: int) -> Optional[int]:
    """
    Returns the index position of the target, if found. Else return None
    """
    for index, value in enumerate(input_list):
        if value == search_target:
            return index
    return None


output = linear_search([5, 2, 3, 9], 3)
print(output)
