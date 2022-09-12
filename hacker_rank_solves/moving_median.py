import heapq
from typing import List


def running_median(input_list: List[int]) -> List[int]:
    # lower_half = [] this will be a max heap
    # higher_half = [] this will be a min heap
    lower_half = []
    higher_half = []
    result = []
    for ii in input_list:
        if len(higher_half) == 0:
            heapq.heappush(higher_half, ii)
            continue
        elif ii >= higher_half[0]:
            heapq.heappush(higher_half, ii)
        elif ii <= higher_half[0]:
            heapq.heappush(lower_half, ii)
    print(lower_half)
    print(higher_half)
    return []


if __name__ == "__main__":
    ans = running_median([12, 4, 5, 3, 8, 7])
    print(ans)
