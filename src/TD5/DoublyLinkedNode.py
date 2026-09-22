class DoublyLinkedNode:
    def __init__(self, item):
        self.data = item
        self.next = None
        self.previous = None

    def __str__(self) -> str:
        return str(self.data)