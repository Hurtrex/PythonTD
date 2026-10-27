from src.Stack.DoubleLinkedCircularList import DoubleLinkedCircularList


class DLCLBasedStack:
    def __init__(self):
        self.items = DoubleLinkedCircularList()

    def push(self, item):
        self.items.add_front(item)
        #Or self.items.add_back(item)

    def pull(self):
        return self.items.remove_front()
        #Or return self.item.remove_back()

    def top(self):
        return self.items.get(0)
    #if if we use back
    #return self.items.get(self.items.lenght()-1)
