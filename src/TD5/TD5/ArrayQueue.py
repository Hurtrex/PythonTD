class ArrayQueue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):       # O(1) amorti
        self.__items.append(item)

    def dequeue(self):             # O(n) — décalage de tous les éléments
        if not self.is_empty():
            return self.__items.pop(0)

    def peek(self):                # O(1)
        if not self.is_empty():
            return self.__items[0]

    def is_empty(self):            # O(1)
        return len(self.__items) == 0

    def size(self):                # O(1)
        return len(self.__items)