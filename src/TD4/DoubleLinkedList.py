from src.TD4.IList import IList


class DoublyLinkedList(IList):

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def add(self, element):
        new_node = self.Node(element)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def add_at(self, index, element):
        new_node = self.Node(element)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            new_node.next = curr.next
            new_node.prev = curr
            if curr.next:
                curr.next.prev = new_node
            else:
                self.tail = new_node
            curr.next = new_node
        self._size += 1

    def get(self, index):
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.data

    def remove(self, index):
        if index == 0:
            removed = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            removed = curr.data
            if curr.prev:
                curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
            else:
                self.tail = curr.prev
        self._size -= 1
        return removed

    def size(self):
        return self._size

    def is_empty(self):
        return self.head is None

    def contains(self, element):
        curr = self.head
        while curr:
            if curr.data == element:
                return True
            curr = curr.next
        return False

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0