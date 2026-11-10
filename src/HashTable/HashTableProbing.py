from src.HashTable.Pair import pair


class HashTableProbing:
    def __init__(self, size):
        self.ht = []
        for i in range(size):
            self.ht.append(None)

    def prob(self, step):
        return step * step

    def hash(self, key):
        return hash(key) % len(self.ht)

    def put(self, key, value):
        h = self.hash(key)
        step = 0
        while step < len(self.ht):
            index = (h + self.prob(step)) % len(self.ht)
            if self.ht[index] is None:
                self.ht[index] = pair(key, value)
                return
            if self.ht[index].key == key:
                self.ht[index].value = value
                return
            step += 1
        raise Exception("HashTable full")
