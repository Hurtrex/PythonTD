import ctypes
class ArrayList:
    def __init__(self,max_size):
        self.length = 0
        self.capacity = max_size
        self.values = (max_size * ctypes.py_object)()

    def __len__(self):
        return self.length

    def __getitem__(self, position):
        if not 0<=position<=self.length:
            return IndexError('position out of range')
        return self.values[position]

    def add_back(self,item):
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        self.values[self.length] = item
        self.length += 1


    #We resize the tableau size, we put it in a temp variable
    #And then we transfert from the old to the new one
    #And then the old one to the new with a bigger capacity
    def _resize(self,new_capacity):
        new_items = (new_capacity * ctypes.py_object)()
        for i in range(self.length):
            new_items[i] = self.values[i]
        self.values = new_items
        self.capacity = new_capacity

    def add_front(self,item):
        if self.length == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.length,0 -1):
            self.values[i] = self.__getitem__(i-1)
        self.values[0] = item
        self.length += 1

    def __str__(self) -> str:
        to_return = '['
        for i in range(self.length):
            to_return = to_return + str(self.values[i])
            if i < self.length-1:
                to_return = to_return + ','
        return to_return + ']'

    def put_at(self,position,item):
        if position < 0:
            return None
        if position >= self.length:
            self.add_back(item)
        if position == 0:
            self.add_front(item)
            return None
        for i in range(self.length, position, -1):
            self.values[i] = self.__getitem__(i-1)
        self.values[position] = item
        self.length += 1