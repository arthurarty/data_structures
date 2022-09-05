import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#


def count_ways_to_solve(remaining_sum: int, n: int, base: int = 1) -> int:
    result = int(math.pow(base, n))
    if result == remaining_sum:
        return 1
    if remaining_sum < result:
        return 0
    option_1 = count_ways_to_solve(remaining_sum - result, n, base + 1)
    option_2 = count_ways_to_solve(remaining_sum, n, base + 1)
    return option_1 + option_2


def powerSum(X, N):
    # Write your code here
    return count_ways_to_solve(X, N)


print(powerSum(10, 2))
print(powerSum(100, 2))
