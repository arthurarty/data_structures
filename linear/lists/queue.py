"""
This implementation is slow because it used a list to store the values.
Lists/Arrays have a runtime of 0(n) Linear time when inserting values at the start.
A better implementation would have been to use a linked_list.
"""

class Queue:

    def __init__(self):
        self.queue = list()

    def addtoq(self, dataval):
        # insert method to add element
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False

    @property
    def size(self):
        return len(self.queue)

    def remove_from_queue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")

the_queue = Queue()
the_queue.addtoq("John")
the_queue.addtoq("Lamu")
the_queue.addtoq("Jemi")
the_queue.addtoq("Jibran")
print(the_queue.queue)
the_queue.remove_from_queue()
print(the_queue.queue)
