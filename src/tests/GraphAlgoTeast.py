import unittest
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo



class MyTestCase(unittest.TestCase):
    def test_save_load(self):
        g = self.creat_graph()
        graph = GraphAlgo(g)
        graph2= GraphAlgo()
        graph.save_to_json("graph.json")
        graph2.load_from_json("graph.json")
        print(graph)
        print(graph2)
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

    def test_plot_graph(self):
        g = self.creat_graph()
        graph = GraphAlgo(g)
        # graph = GraphAlgo()
        # graph.load_from_json("A0.json")
        graph.plot_graph()

    def creat_graph(self):
        g = DiGraph()
        for i in range(0, 5):
            g.add_node(i)
        g.add_edge(0, 1, 1.2)
        g.add_edge(0,2,1.0)
        g.add_edge(1,0,1.0)
        g.add_edge(2,3,1.0)
        g.add_edge(3,2,1.0)



        return g

if __name__ == '__main__':
    unittest.main()
