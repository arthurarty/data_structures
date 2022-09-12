from heapq import heappush, heappop, heapify


# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining the heap invarient
# heapify - transform list into heap, in place in linear time


class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1)/2

    def insert_key(self, key):
        heappush(self.heap, key)

    def extract_min(self):
        """
        Remove a minium element from the heap
        :return:
        """
        return heappop(self.heap)

    def decrease_key(self, ii, new_value):
        self.heap[ii] = new_value
        while ii != 0 and self.heap[self.parent(ii)] > self.heap[ii]:
            # Swap heap[i] with heap[parent(i)]
            self.heap[ii], self.heap[self.parent(ii)] = (self.heap[self.parent(ii)], self.heap[ii])

    def delete_key(self, ii):
        """
        Function to delete a key at index ii
        first reduces value to minus infinite and then calls extract_min
        :param ii:
        :return:
        """
        self.decreaseKey(ii, float("-inf"))
        self.extractMin()

    def get_min(self):
        """
        return the minimum element in the heap.
        :return:
        """
        return self.heap[0]
