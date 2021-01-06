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
        new_edge = Edge(id1, id2, weight)
        if id2 not in self.edges_in:
            self.edges_in[id2] = {}
        self.edges_in[id2][id1] = new_edge

        if id1 not in self.edges_out:
            self.edges_out[id1] = {}
        self.edges_out[id1][id2] = new_edge

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
        return len(self.edges)

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.edges_in.get(self, id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edges_out.get(self, id1)

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        raise NotImplementedError

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        raise NotImplementedError
    def __str__(self):
        return ""
