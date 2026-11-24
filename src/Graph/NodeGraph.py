class NodeGraph:
    def __init__(self,k,data):
        self.key = k
        self.neighbours = SLL()
        self.load = data