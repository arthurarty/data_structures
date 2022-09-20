def twoNumberSum(array, targetSum):
    result = []
    hash_map = dict.fromkeys(array)
    for ii in array:
        jj = targetSum - ii
        if jj == ii:
            continue
        if jj in hash_map.keys():
            result.extend([ii, jj])
            break
    return result


def two_number_sub_sort(array, target_sum):
    array.sort()
    ii = 0
    jj = len(array) - 1
    while ii < len(array) and jj > 0:
        potential_sum = array[ii] + array[jj]
        if potential_sum == target_sum:
            return [array[ii], array[jj]]
        elif potential_sum > target_sum:
            jj -= 1
        elif potential_sum < target_sum:
            ii += 1
        if ii == jj:
            break
    return []


if __name__ == "__main__":
    input_dict = {
        "array": [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47],
        "targetSum": 163
    }
    print(twoNumberSum(input_dict.get('array'), input_dict.get('targetSum')))
    print(two_number_sub_sort(input_dict.get('array'), input_dict.get('targetSum')))
