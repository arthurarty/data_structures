import collections

with_class = collections.namedtuple('Person', 'name age gender title', rename=True)
print(with_class._fields)

two_ages = collections.namedtuple('Person', 'name age gender', rename=True)
bill = two_ages('bill', 34, 'male')
print(two_ages._fields)
print(*bill)

str = ''
for item in bill._fields:
    print(getattr(bill, item))


def convertTuple(tup):
    str = ' ,'.join(tup)
    return str

# Driver code
str = convertTuple(two_ages._fields)
print(str)