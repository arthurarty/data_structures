from collections import deque

# create deque
double_ended = deque(['Mon', 'Tue', 'Wed'])
print(double_ended)

# add to the right of the queue
print("ending to the right")
double_ended.append('Thur')
print(double_ended)


# add to the left
print("adding to the left")
double_ended.appendleft('Sun')
print(double_ended)


# remove from the left
print("we are going to pop from the left")
double_ended.popleft()
print(double_ended)

# remove from the right
print("We are moving from the right")
double_ended.pop()
print(double_ended)
