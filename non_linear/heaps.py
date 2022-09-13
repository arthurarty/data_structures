import heapq

"""
Python heapq uses the convention of the smallest element has the highest priority
Therefore in a heap a = [1, 2, 3, 5, 6, 8, 7]
a[0] = 1 which is the smallest value in the heap
"""

heap = [21, 1, 45, 78, 3, 5]
heapq.heapify(heap)
print(heap)

# add a new value to the heap
heapq.heappush(heap, 8)
print(heap)

# remove from the heap removes first value
# while maintaining the heap property
heapq.heappop(heap)
print(heap)

# replace in heap removes the smallest and adds new without order
heapq.heapreplace(heap, 6)
print(heap)
