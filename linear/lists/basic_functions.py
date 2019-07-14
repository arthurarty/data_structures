thislist = ['apple', 'banana', 'cherry']

# add to list
thislist.append('orange')

# print list
print(thislist)

# insert into list
thislist.insert(1, "pawpaw")
print(thislist)

# updating a value
thislist[3] = 'pineapple'
print(thislist)

# remove item from list
thislist.remove("banana")

# del method del thislist[index]
print(thislist)

# ways to copy a list
mylist = thislist.copy()
# this avoids changes made in list1 from appearing list2

print("this is copied list")
print(mylist)

# remove the last item using the .pop() method
thislist.pop()
print("list after pop()")
print(mylist)

# combine two lists.
list2 = ['cabbage', 'carrots', 'green pepper']
thislist.extend(list2)
print(thislist)
