from src.TD6.DoubleLinkedNodeQueue import DoubleLinkedNodeQueue


class DoubleLinkedQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, item):
         new_node = DoubleLinkedNodeQueue(item)
         if self.head is None:
             self.head = new_node
         else:
             self.head.previous = new_node
             new_node.next = self.head
             new_node.previous = self.head.previous
             self.head.previous.next = new_node