from src.HashTable.Pair import pair


class HashTable:
    #we assume size is 20 so 0-19
    def __init__(self, size):
        self.ht = ArrayList(size)

    def hash(self, key):
        return hash(key) % self.ht.size()

    def put(self, k, v):
        index = self.hash(k)
        list = self.ht.get(index)
        if list is None:
            LL = LinkedList()
            #The data inside the LinkedList is the pair
            LL.add_Back(pair(k, v))
            self.ht.put(index, LL)
            return
        exist = self.find(list, k)
        if exist >= 0:
            list.put(exist, pair(k, v))
        else:
            list.add_Back(pair(k, v))

    def find(self, list, key):
        for i in range(list.size()):
            p = list.get(i)
            if p.key == key:
                return i
        return -1