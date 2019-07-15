import heapq

heap = [21, 1, 45, 78, 3, 5]
heapq.heapify(heap)
print(heap)

# add a new value to the heap
heapq.heappush(heap, 8)
print(heap)

# remove from the heap removes first value
heapq.heappop(heap)
print(heap)

# replace in heap removes the smallest and adds new without order
heapq.heapreplace(heap, 6)
print(heap)
