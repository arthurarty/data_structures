"""Playing with the bubble sort """

input_list = [3, 2, 4, 1, 5]

# loop through and check the numbers
for number in range(len(input_list) - 1, 0, -1):
    for idx in range(number):
        current = idx
        next_number = idx+1
        hold = 0
        if input_list[next_number] < input_list[idx]:
            hold = input_list[idx]
            input_list[idx] = input_list[next_number]
            input_list[next_number] = hold

print(input_list)
