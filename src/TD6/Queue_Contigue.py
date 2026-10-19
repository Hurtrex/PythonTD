class Queue:
    def __init__(self, capacity: int = 100):
        self.__capacity = capacity
        self.__front = 0
        self.__rear = 0
        self.__items = Queue.build_array(self.capacity)

    def enqueue(self,item):
        # 1. Is the dequeue empty?
        #       ↓
        #   Yes → return None
        if self.is_empty():
            print("Queue is empty")
            return
        # 2. We go to the rear
        #   self.__items[self.__rears]
        #   means going to the rear index
        #   the = item means that the item will go into rear
        self.__items[self.__rear] = item
        #   the __rear += simply moves the rear to +1
        self.__rear =+1

    def dequeue(self):
        # 1. Is it empty? Yes -> return None
        if self.is_empty():
            print("Queue is empty")
            return None
        # 2. Save the first item
        to_return = self.__items[0]
        # 3. Move front forward by 1
        self.__front += 1
        return to_return

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.__items[0]
    def is_empty(self):
        return self.__capacity == 0

    def size(self):
        return(self.__rear - self.__front + self.__capacity) % self.__capacity