def find_number_of_items(input_list):
    temp_hold = []
    is_open = False
    counter = 0
    for ii in input_list:
        if ii == '|':
            is_open = True
            if counter != 0:
                temp_hold.append(counter)
            counter = 0
            continue
        if is_open and ii == '*':
            counter += 1
    return sum(temp_hold)


s = '|**|*|*'
res = find_number_of_items(s[0:6])
print(res)
