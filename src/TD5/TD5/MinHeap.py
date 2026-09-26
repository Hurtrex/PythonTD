class MinHeap:

    def __init__(self):
        self.__items = []

    # --- helpers ---
    def __parent(self, i):  return (i - 1) // 2
    def __left(self, i):    return 2 * i + 1
    def __right(self, i):   return 2 * i + 2

    def __swap(self, i, j):
        self.__items[i], self.__items[j] = self.__items[j], self.__items[i]

    def __bubble_up(self, i):          # O(log n)
        while i > 0:
            p = self.__parent(i)
            if self.__items[i] < self.__items[p]:
                self.__swap(i, p)
                i = p
            else:
                break

    def __bubble_down(self, i):        # O(log n)
        n = len(self.__items)
        while True:
            smallest = i
            l, r = self.__left(i), self.__right(i)
            if l < n and self.__items[l] < self.__items[smallest]:
                smallest = l
            if r < n and self.__items[r] < self.__items[smallest]:
                smallest = r
            if smallest != i:
                self.__swap(i, smallest)
                i = smallest
            else:
                break

    def enqueue(self, key):            # O(log n)
        self.__items.append(key)
        self.__bubble_up(len(self.__items) - 1)

    def dequeue(self):                 # O(log n)
        if self.is_empty():
            return None
        self.__swap(0, len(self.__items) - 1)
        removed = self.__items.pop()
        self.__bubble_down(0)
        return removed

    def peek(self):                    # O(1)
        if not self.is_empty():
            return self.__items[0]

    def clear(self):                   # O(1)
        self.__items = []

    def length(self):                  # O(1)
        return len(self.__items)

    def is_empty(self):
        return len(self.__items) == 0