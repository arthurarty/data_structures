import heapq


heap = [1, 5, 6, 2, 4]
heapq.heapify(heap)
# print(heap)
# heapq.heappush(heap, -10)
# print(heap)


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, -value)
    return [heapq.heappop(h) for i in range(len(h))]


print(heapsort([10, 3, 6, 2, 9, 105, 22, 1]))
