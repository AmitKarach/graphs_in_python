from src.Edge import Edge
from src.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.edges_in = {}
        self.edges_out = {}
        self.edges_size = 0
        self.mc = 0



    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        new_node = Node(node_id)
        self.nodes[node_id] = new_node
        self.mc += 1
        return True

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if (id1 not in self.nodes) or (id1 not in self.nodes):
            return False
        # new_edge = Edge(id1, id2, weight)
        if id2 not in self.edges_in:
            self.edges_in[id2] = {}
        self.edges_in[id2][id1] = weight

        if id1 not in self.edges_out:
            self.edges_out[id1] = {}
        self.edges_out[id1][id2] = weight

        self.edges_size += 1
        self.mc += 1
        return True

    def get_all_v(self) -> dict:
        return self.nodes

    def get_mc(self) -> int:
        return self.mc

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.edges_size

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 not in self.edges_in:
            return None
        return self.edges_in[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 not in self.edges_out:
            return None
        return self.edges_out[id1]

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            for i in self.edges_out[node_id]:
                self.edges_in[i].pop(node_id)
                self.edges_size-=1
                if len(self.edges_in[i]) ==0:
                    self.edges_in.pop(i)
            self.edges_out.pop(node_id)
            self.nodes.pop(node_id)
            return True
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
       if node_id1 in self.nodes and node_id2 in self.nodes:
           if node_id1 in self.edges_out:
               self.edges_out[node_id1].pop(node_id2)
               if len(self.edges_out[node_id1]) ==0:
                   self.edges_out.pop(node_id1)
               self.edges_in[node_id2].pop(node_id1)
               if len(self.edges_in[node_id2]) ==0:
                   self.edges_in.pop(node_id2)
               self.edges_size -=1
               return True


    def __str__(self):
        return ""
