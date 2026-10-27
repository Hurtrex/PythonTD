from operator import index

from src.Stack import DLNode


class DoubleLinkedCircularList:
    def __init__(self):
        self.head = None
        #the tail would be equal head.prev cuz its circular

    def add_front(self,item):
        new_node = DLNode(item)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        new_node.previous = self.head.previous
        self.head.previous.next = new_node
        self.head.previous = new_node
        self.head = new_node

    def add_back(self,item):
        new_node = DLNode(item)
        if self.head is None:
            self.head = new_node
            return


    def remove_front(self,item):

    def remove_back(self,item):

    def get(self,index):
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def length(self)->int:
        if self.head is None:
            return 0
        current = self.head
        count = 0
        while current.next is not None:
            count =+1
            current = current.next
        return count

    #TODO
    #add_back
    #remove_front
    #remove_back
    #get(i)
    #lenght()