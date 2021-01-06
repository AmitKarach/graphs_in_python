import unittest
from DiGraph import DiGraph

class MyTestCase(unittest.TestCase):
    def test_something(self):
        g= self.creat_graph()

        self.assertEqual(True, False)

    def creat_graph (self):
        g= DiGraph()
        for i in range(0,10):
            g.add_node(i)
        g.add_edge(0,1,1.2)
        g.add_edge(0,2,1.2)
        g.add_edge(2,1,1.2)
        g.add_edge(0,4,1.2)
        return g


if __name__ == '__main__':
    unittest.main()
