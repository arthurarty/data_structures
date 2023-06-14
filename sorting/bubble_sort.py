"""Playing with the bubble sort """
"""
Works by swapping two items depending
on which is smaller
"""


def bubble_sort(input_list):
    # loop through and check the numbers
    for number in range(len(input_list) - 1, 0, -1):
        for idx in range(number):
            if input_list[idx+1] < input_list[idx]:
                input_list[idx], input_list[idx + 1] = input_list[idx+1], input_list[idx]
    return input_list


print(bubble_sort([19, 2, 31, 45, 6, 11, 121, 27, 3]))
print(bubble_sort([19, 2, 31, 45, 6, 11, 121, 27, 8, 100, 43, 91]))


def custom_bubble_sort(input_list):
    # input_list = [5, 70, 1, 6, 19, 100, 2]
    for _ in range(len(input_list)):
        for index in range(len(input_list) - 1):
            if input_list[index] > input_list[index+1]:
                input_list[index], input_list[index+1] = input_list[index+1], input_list[index]
    return input_list
print(custom_bubble_sort([5, 70, 1, 6, 19, 100, 2]))
