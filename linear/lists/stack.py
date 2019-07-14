class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
        # use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # use peek to look at the top of the stack
    def peek(self):
        return self.stack[-1]

    # remove from the stack
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()
