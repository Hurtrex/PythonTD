from collections import deque

class DequeQueue:

    def __init__(self):
        self.__items = deque()

    def enqueue(self, item):    # O(1)
        self.__items.append(item)

    def dequeue(self):          # O(1)
        if not self.is_empty():
            return self.__items.popleft()

    def peek(self):             # O(1)
        if not self.is_empty():
            return self.__items[0]

    def is_empty(self):         # O(1)
        return len(self.__items) == 0

    def size(self):             # O(1)
        return len(self.__items)