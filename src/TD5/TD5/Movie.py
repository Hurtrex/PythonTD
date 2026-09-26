from src.TD5.TD5.MinHeap import MinHeap


class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    # Min Heap compare par année (plus ancien = plus prioritaire)
    def __lt__(self, other): return self.year < other.year
    def __le__(self, other): return self.year <= other.year
    def __gt__(self, other): return self.year > other.year

    def __repr__(self):
        return f"Movie({self.title}, {self.year})"


class PriorityQueue:

    def __init__(self):
        self.__heap = MinHeap()

    def enqueue(self, key):     # O(log n)
        self.__heap.enqueue(key)

    def dequeue(self):          # O(log n)
        return self.__heap.dequeue()

    def peek(self):             # O(1)
        return self.__heap.peek()

    def clear(self):            # O(1)
        self.__heap.clear()

    def length(self):           # O(1)
        return self.__heap.length()


# --- Test ---
pq = PriorityQueue()
pq.enqueue(Movie("Inception",    2010))
pq.enqueue(Movie("The Godfather",1972))
pq.enqueue(Movie("Interstellar", 2014))
pq.enqueue(Movie("Parasite",     2019))

print("Peek:", pq.peek())           # The Godfather (1972)

while pq.length() > 0:
    print(pq.dequeue())
# The Godfather 1972
# Inception     2010
# Interstellar  2014
# Parasite      2019