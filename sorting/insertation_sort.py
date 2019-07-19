"""
begins wit the 2nd element and compares with
the 1st. It second < 1st: 2nd is inserted
by first in new list. Compares 3rd with 1st
and 2nd then inserts in the right place
"""


def insertionSort(arr):

    # loop through
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            # swap  the two
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)
