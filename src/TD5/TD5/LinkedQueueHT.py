class LinkedQueueHT:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, item):       # O(1) — ajout en tail
        new_node = self.Node(item)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):             # O(1) — supprime en head
        if not self.is_empty():
            removed = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return removed

    def peek(self):                # O(1)
        if not self.is_empty():
            return self.head.data

    def is_empty(self):            # O(1)
        return self.head is None

    def size(self):                # O(1)
        return self._size