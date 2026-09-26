from src.TD4.SingleLinkedList import SinglyLinkedList


class LinkedQueue(SinglyLinkedList):

    def enqueue(self, item):    # O(n) — parcourt jusqu'à la fin
        self.add(item)

    def dequeue(self):          # O(1) — supprime la tête
        if not self.is_empty():
            return self.remove(0)

    def peek(self):             # O(1)
        if not self.is_empty():
            return self.get(0)