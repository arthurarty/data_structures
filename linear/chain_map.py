import collections

"""
best use of ChainMap is to search through multiple dictionaries
at a time and get the proper key-value pair mapping
"""

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

# create a single dictionary from the two
res = collections.ChainMap(dict1, dict2)

print(res.maps, '\n')

print(f'Keys are {list(res.keys())}')
print(f'Values are {list(res.values())}')

print('These are the elements')
for key, value in res.items():
    print(f'key is {key} value is {value}')
print()
