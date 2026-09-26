from collections import deque

class Queue(object):
    def __init__(self):
        self.__items = deque()

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        self.__items.popleft()

    def peek(self):
        return self.__items[0]

    def is_empty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)