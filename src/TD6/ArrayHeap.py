class ArrayHeap:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)
        self.heapify_up(self.items.len - 1)

    def heapify_up(self,start):
        i = start
        while (i>0):
            if(self.items[i] > self.items[(i-1)%2]):
                break
        else:
            swap(i,(i-1)%2)
            i = (i-1)%2