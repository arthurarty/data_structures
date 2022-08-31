def print_value(input_value:int):
    print(f'{input_value:.6f}')


def plusMinus(arr):
    # Write your code here
    if not arr:
        return []
    arr.sort()
    zero_counter = arr.count(0)
    negative_counter = 0
    for i in arr:
        if i < 0:
            negative_counter += 1
        if i == 0:
            break
    positive_counter = len(arr) - (negative_counter + zero_counter)
    print_value(positive_counter/len(arr))
    print_value(negative_counter/len(arr))
    print_value(zero_counter/len(arr))

plusMinus([1, 1, 0, -1, -1])
plusMinus([-4, 3, -9, 0, 4, 1])