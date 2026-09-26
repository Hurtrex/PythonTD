from src.TD4.IList import IList


class SinglyLinkedList(IList):

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self._size = 0

    def add(self, element):
        new_node = self.Node(element)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def add_at(self, index, element):
        new_node = self.Node(element)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            new_node.next = curr.next
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
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            removed = curr.next.data
            curr.next = curr.next.next
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
        self._size = 0