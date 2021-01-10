import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo



class MyTestCase(unittest.TestCase):
    def test_something(self):
        g = self.creat_graph()
        graph = GraphAlgo(g)
        print(graph)
        graph.save_to_json("graph.json")
        graph.load_from_json("graph.json")

    def creat_graph(self):
        g = DiGraph()
        for i in range(0, 3):
            g.add_node(i)
        g.add_edge(0, 1, 1.2)
        return g

if __name__ == '__main__':
    unittest.main()
