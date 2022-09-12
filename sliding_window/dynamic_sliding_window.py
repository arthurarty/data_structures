from typing import List

"""
Given a list of elements for example:
[1, 2, 3, 4, 5, 6, 7]
We need to find the minimum length of a sublist
whose values sum up to 7
"""


def dyanmic_sliding_array(arr: List[int], x: int):
    min_length = float('inf')

    start = 0
    end = 0
    current_sum = 0

    while end < len(arr):
        current_sum = current_sum + arr[end]
        end += 1

        while start < end and current_sum >= x:
            current_sum = current_sum - arr[start]
            start += 1

            min_length = min(min_length, end-start+1)
    return min_length


result = dyanmic_sliding_array([1, 2, 3, 4, 5, 6], 7)
assert result == 2
