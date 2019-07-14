from collections import Counter
my_list = ['ab', 'bc', 'ab', 'gg']
print(Counter(my_list))
counted_list = Counter(my_list)
for counted in counted_list:
    if counted_list[counted] > 1:
        print(counted)
