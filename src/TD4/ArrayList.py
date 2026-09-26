import src.TD4.IList as IList
class ArrayList(IList):

    def __init__(self):
        self.data = []

    def add(self, element):
        self.data.append(element)

    def add_at(self, index, element):
        self.data.insert(index, element)

    def get(self, index):
        return self.data[index]

    def remove(self, index):
        return self.data.pop(index)

    def size(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def contains(self, element):
        return element in self.data

    def clear(self):
        self.data = []