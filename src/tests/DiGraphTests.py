import unittest
from src.DiGraph import DiGraph



class MyTestCase(unittest.TestCase):
    def test_addEdge(self):
        g1 = self.creat_graph()
        g1.add_edge(0, 1, 1.2)
        g2 =self.creat_graph()
        # self.assertEqual(g1, g2)

    def test_removeEdge(self):
        g1 = self.creat_graph()
        g1.remove_edge(0,1)
        g1.remove_edge(1,0)

        self.assertEqual(g1.edges_size,1)

    def test_vSize(self):
        g1 = self.creat_graph()
        print (g1.v_size())
        self.assertEqual(g1.v_size(),3)

    def test_all_in_edges_of_node(self):
        g1 = self.creat_graph()
        self.assertEqual(len(g1.all_in_edges_of_node(1)), 1)
        self.assertEqual(g1.all_in_edges_of_node(0), None)
        print(g1.all_in_edges_of_node(1))
        print(g1.all_in_edges_of_node(0))

    def test_all_out_edges_of_node(self):
        g1 = self.creat_graph()
        print(g1.all_out_edges_of_node(0))
        self.assertEqual(len(g1.all_out_edges_of_node(0)), 1)
        self.assertEqual(g1.all_out_edges_of_node(2), {})

    def test_removeNode(self):
        g1 = self.creat_graph()
        g1.remove_node(0)
        g1.remove_node(4)

        self.assertEqual(g1.v_size(),2)

    def creat_graph(self):
        g = DiGraph()
        for i in range(0, 3):
            g.add_node(i)
        g.add_edge(0, 1, 1.2)
        g.add_edge(1, 2, 1.2)

        return g


if __name__ == '__main__':
    unittest.main()
