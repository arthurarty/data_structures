import bisect


this_list = [1, 3, 10, 30]
# print(bisect.bisect(this_list, 6))
bisect.insort(this_list, 6)
print(this_list)
