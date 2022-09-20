from typing import List


a = [2, 9, 10, 3, 7]


def handle_list(input_list:List[int]) -> List[int]:
    ii = 0
    jj = 1
    while ii < len(input_list):
        # handle the tail
        if ii == len(input_list) - 2 and input_list[ii] < input_list[ii] + input_list[jj]:
            input_list[ii] = input_list[ii] + input_list[jj]
            input_list.pop(jj)
            if ii > 0:
                ii -= 1
                jj -= 1
        elif input_list[ii] < input_list[ii] + input_list[jj] and input_list[jj] > input_list[jj+1]:
            input_list[ii] = input_list[ii]+input_list[jj]
            input_list.pop(jj)
            if ii > 0:
                ii -= 1
                jj -= 1
        else:
            ii += 1
            jj += 1
        if jj == len(input_list) - 1:
            break
    return input_list

print(handle_list(a))


# this does not return the right answer
