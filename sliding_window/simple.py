from typing import List


def fixed_sliding_window(arr: List[int], k: int) -> List[int]:
    """
    Where K is the size of the fixed sliding window.
    :param arr:
    :param k:
    :return:
    """
    #  sum up the first array and add it to the result
    curr_subarray = sum(arr[:k])
    result = [curr_subarray]

    # to get each subsequent subarray, add the next value in the list
    # remove the first
    for ii in range(len(arr) - k):
        curr_subarray = curr_subarray - arr[ii]
        curr_subarray = curr_subarray + arr[ii+k]
        result.append(curr_subarray)
    return result


print(fixed_sliding_window([1, 2, 3, 4, 5, 6], 3))
