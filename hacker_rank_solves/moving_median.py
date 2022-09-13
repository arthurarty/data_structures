import heapq
from typing import List


def running_median(input_list: List[int]) -> List[float]:
    # lower_half = [] this will be a max heap
    # higher_half = [] this will be a min heap
    lower_half, higher_half, result = [], [], []

    for ii in input_list:
        if not higher_half:
            heapq.heappush(higher_half, ii)
        else:
            if len(higher_half) > len(lower_half):
                # if higher_half is longer than the lower_half.
                if higher_half[0] < ii:
                    # compare ii with the smallest value in higher_half
                    # if value ii is > smallest value in higher half
                    # we add it to the higher_half
                    jj = heapq.heappushpop(higher_half, ii)
                    # when we do a heappushpop
                    # we insert a new value and at the same time we get the smallest value
                    # from the heap and we set that to jj.
                    # we negate jj when adding to the lower_half because lower_half is a max_heap
                    # in a max heap the root node is the largest value
                    # by making the values negative we are inverting them.
                    heapq.heappush(lower_half, -jj)
                else:
                    # hence value is smaller than the smallest value in the higher_half
                    # so we negate it and add to the lower_half
                    heapq.heappush(lower_half, -ii)
            else:
                # lower_half has grown longer than the higher half.
                if -lower_half[0] > ii:
                    # we negate the value so that it becomes a positive number
                    # if largest element in lower_half is greater than ii
                    # we add ii to the lower_half then we add largest value from lower_half
                    # to the higher_half by doing a heappushpop
                    jj = -heapq.heappushpop(lower_half, -ii)
                    heapq.heappush(higher_half, jj)
                else:
                    # ii is > than the largest_value in lower_half
                    # we add it to the higher_half
                    heapq.heappush(higher_half, ii)

        if len(higher_half) > len(lower_half):
            result.append(float(higher_half[0]))
        else:
            result.append(float((higher_half[0] - lower_half[0])/2))
    return result


if __name__ == "__main__":
    ans = running_median([12, 4, 5, 3, 8, 7])
    assert ans == [12.0, 8.0, 5.0, 4.5, 5.0, 6.0]
    print(ans)
