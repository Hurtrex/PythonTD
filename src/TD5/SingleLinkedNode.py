class SingleLinkedNode:
    def __init__(self, item):
        self.data = item
        self.next = None

    def __str__(self) -> str:
        return str(self.data)