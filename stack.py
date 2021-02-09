""" Name: Matthew Strange
    Class: CS2420
    Date: 02/08/2021
    Description: Contains Stack class that
    modifies stack for postfix and infix functions.
"""


class Stack:
    """Class that modifies stack for postfix and infix functions"""
    def __init__(self):
        self.stack = []
        self._size = 0

    def push(self, item):
        """pushes new item to stack"""
        self._size += 1
        return self.stack.append(item)

    def pop(self):
        """pops last item off of stack"""
        if not self.stack:
            raise IndexError
        self._size -= 1
        return self.stack.pop()

    def top(self):
        """returns top item of stack"""
        if not self.stack:
            raise IndexError
        return self.stack[-1]

    def size(self):
        """returns the size of the stack"""
        return self._size

    def clear(self):
        """clears the stack"""
        self.stack = []
