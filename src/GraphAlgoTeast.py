import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo



class MyTestCase(unittest.TestCase):
    def test_save_load(self):
        g = self.creat_graph()
        graph = GraphAlgo(g)
        print(graph)
        graph.save_to_json("graph.json")
        graph.load_from_json("graph.json")

    def test_shortest_path(self):
        g = self.creat_graph()
        graph = GraphAlgo(g)
        print(graph.shortest_path(0,2))

    def test_connected_component(self):
        g=self.creat_graph()
        graph =GraphAlgo(g)
        print(graph.connected_component(0))
        print(graph.connected_component(2))

        # graph2=GraphAlgo(g2)
    def test_connected_components(self):
        g=self.creat_graph()
        graph =GraphAlgo(g)
        print(graph.connected_components())



    def creat_graph(self):
        g = DiGraph()
        for i in range(0, 3):
            g.add_node(i)
        g.add_edge(0, 1, 1.2)
        g.add_edge(1, 2, 1.2)
        g.add_edge(0,2,1.0)
        g.add_edge(1,0,1.0)

        return g

if __name__ == '__main__':
    unittest.main()
