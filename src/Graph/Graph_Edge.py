class Graph_Edge:
    def __init__(self,tok,data):
        self.to_key = tok
        self.load = data
        self.next = None