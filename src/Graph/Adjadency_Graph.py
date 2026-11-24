from src.Graph.Graph_Edge import Graph_Edge
from src.Graph.NodeGraph import NodeGraph


class Adjacency_Graph:
    def __init__(self):
        self.ht = hastable()

    def add_node(self,load,key):
        node = self.ht.get(key) #the node is a pair
        if node is not None:
            node.load = load
            return
        self.ht.put(key,NodeGraph(key,load)) #the pair, the load and the voisin

#1 to 2
    def add_edge(self,from_key,to_key,data):
        ge = Graph_Edge(to_key,data)
        self.attach(from_key,ge)

    def attach(self,key,ge):
        gn = self.ht.get(key)
        gn.neighbours.add_back(ge)