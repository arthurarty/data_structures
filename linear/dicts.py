import collections

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict['Name'])

# deletion options
del dict['Name']

# removes the name
dict.clear()

# removes all entries in dict
del dict

# deletes entire dict

"""
combine two dictionaries using chainmap
to make possible to read them all
"""

dict1 = {'day1': 'Mon', 'day2': 'Tue', 'day3': 'Wed'}
dict2 = {'day4': 'Thur', 'day5': 'Fri', 'day6': 'Sat'}

res = collections.ChainMap(dict1, dict2)
print(res.maps, '\n')
