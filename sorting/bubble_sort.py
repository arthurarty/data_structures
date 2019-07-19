"""Playing with the bubble sort """
"""
Works by swapping two items depending
on which is smaller
"""


def bubble_sort(input_list):
    # loop through and check the numbers
    for number in range(len(input_list) - 1, 0, -1):
        for idx in range(number):
            hold = 0
            if input_list[idx+1] < input_list[idx]:
                hold = input_list[idx]
                input_list[idx] = input_list[idx+1]
                input_list[idx+1] = hold
    return input_list

print(bubble_sort([19,2,31,45,6,11,121,27]))
