days = set(['Mon', 'Tue', 'Wed', 'Sat'])
print(days)

# add to the set
days.add('Thurs')
print(days)

# remove from the set
days.discard('Mon')
days_b = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
interset_days = days & days_b
print(interset_days)
