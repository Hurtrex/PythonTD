from src.TD5.DoublyLinkedNode import DoublyLinkedNode
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_back(self, item):
        new_node = DoublyLinkedNode(item)
        if self.head is None:
            self.head = new_node
            return
        tail = self.find_tail()
        tail.next = new_node
        new_node.previous = tail
        new_node.next = None

    def find_tail(self):
        if self.head is None:
            return None
        current = self.head
        while current.next is not None:
            current = current.next
        return current

    def __str__(self) -> str:
        output = ""
        if self.head is None:
            return output
        current = self.head
        while current is not None:
            if current is not self.head:
                output += "->"
            output += str(current.data)
            current = current.next
        return output

    def add_front(self, item):
        new_node = DoublyLinkedNode(item)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def put(self, item, position):
        if position <0:
            return
        if position > self.length():
            self.add_back(item)
        if position == 0:
            self.add_front(item)
        new_node = DoublyLinkedNode(item)
        found = self.find_node(position)

    def find_node(self, position):
        if position < 0:
            return None
        current = self.head
        count = 0
        while current.next is not None and count < position:
            count +=1
            current = current.next
        return current


    def length(self) -> int:
        if self.head is None:
            return 0
        current = self.head
        count = 0
        while current.next is not None:
            count +=1
            current = current.next
        return count
