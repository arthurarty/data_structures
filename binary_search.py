def bsearch(input_list, val):

    list_size = len(input_list) - 1

    idx0 = 0
    idxn = list_size

    """find the middle most value"""
    while idx0 <= idxn:
        midval = (idx0 + idxn)//2

        if input_list[midval] == val:
            return midval

        """compare the value with the middle most value"""
        if val > input_list[midval]:
            idx0 = midval + 1
        else:
            idxn = midval - 1

    if idx0 > idxn:
        return None

the_list = [2, 7, 19, 34, 53, 72]
print(bsearch(the_list, 72))