from src.Dictionnary.Entry import Entry


class VAD:
    def __init__(self):
        self.entries = []

    def put(self,k,v):
        index = self.find(k)
        if index >= 0:
            self.entries[index].value = v
            return
        self.entries.append(Entry(k,v))

    def find(self,k):
        for i in range(len(self.entries)):
            if self.entries[i].key == k:
                return i
        return -1

    def get(self,k):
        index = self.find(k)
        if index >= 0:
            return self.entries[index].value
        return -1
