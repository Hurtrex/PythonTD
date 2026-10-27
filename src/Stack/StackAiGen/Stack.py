from src.Stack.StackAiGen.Node import Node


class Stack:
    """Stack built on a linked list -- no Python list is used."""

    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        self.top = Node(value, self.top)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size

    def clear(self):
        self.top = None
        self._size = 0
