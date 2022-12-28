import unittest

from src.GraphAlgo import GraphAlgo
import networkx as nx

from timeit import default_timer as time

from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    def test_test_all_graphs(self):
        graph= GraphAlgo()

        list_of_graphs= ["../data/G_10_80_0.json", "../data/G_100_800_0.json", "../data/G_1000_8000_0.json",
             "../data""/G_10000_80000_0.json", "../data/G_20000_160000_0.json", "../data/G_30000_240000_0.json"]
        for i in list_of_graphs:
            print("graph:" , i )
            graph.load_from_json(i)
            nGraph = self.creat_nx_graph(graph.get_graph())
            randomid1= graph.graph.nodes[0]
            randomid2 = graph.graph.nodes[4]

            print("shortest path:")
            start = time()
            graph.shortest_path(randomid1,randomid2)
            end= time()
            print("our time:",(end-start)/10)
            start = time()
            nx.shortest_path_length(nGraph,0,9, weight="weight")
            end = time()
            print("networkx time:" , (end-start)/10)

            print("connected components:")
            start = time()
            graph.connected_components()
            end = time()
            print("our time:",(end-start)/10)
            start = time()
            nx.strongly_connected_components(nGraph)
            end = time()
            print("networkx time:" , (end-start)/10)


            print("connected components for node 0:")
            start = time()
            graph.connected_component(randomid1)
            end = time()
            print("our time:",(end-start)/10)

    def creat_nx_graph (self,graph:DiGraph):
        g= nx.DiGraph()
        for i in graph.nodes.keys():
            g.add_node(i)
        for i in graph.nodes.keys():
            for j in graph.all_out_edges_of_node(i).keys():
                g.add_edge(i,j,weight=graph.edges_out[i][j])
        return g

if __name__ == '__main__':
    unittest.main()
