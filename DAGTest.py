import unittest
import DAG


class TestEmpty(unittest.TestCase):
    """Tests that a tree with no nodes returns works"""

    def test(self):
        dag = DAG.DAG()
        self.assertTrue(dag.get_graph() == {})


class TestSingleNode(unittest.TestCase):
    """Tests that a tree containing one node works"""

    def test(self):
        dag = DAG.DAG()
        self.assertTrue(dag.add_node('a'))
        self.assertTrue(dag.get_graph() == {'a': set()})


class TestSingleEdge(unittest.TestCase):
    """Tests that creating a graph with one edge works"""

    def test(self):
        dag = DAG.DAG()
        self.assertTrue(dag.add_node('a'))
        self.assertTrue(dag.add_node('b'))
        self.assertTrue(dag.add_edge('a', 'b'))
        self.assertTrue(dag.get_graph() == {'a': set('b'), 'b': set()})


class TestMultipleEdges(unittest.TestCase):
    """Tests that creating a graph
    containing more than one edge works"""

    def test(self):
        dag = DAG.DAG()
        self.assertTrue(dag.add_node('a'))
        self.assertTrue(dag.add_node('b'))
        self.assertTrue(dag.add_node('c'))
        self.assertTrue(dag.add_edge('a', 'b'))
        self.assertTrue(dag.add_edge('b', 'c'))
        self.assertTrue(dag.get_graph() == {'a': set(
            'b'), 'b': set('c'), 'c': set()})


class TestMultipleEdgedNodes(unittest.TestCase):
    """Tests that creating a graph with
    nodes containing multiple edges works"""

    def test(self):
        dag = DAG.DAG()
        self.assertTrue(dag.add_node('a'))
        self.assertTrue(dag.add_node('b'))
        self.assertTrue(dag.add_node('c'))
        self.assertTrue(dag.add_node('d'))
        self.assertTrue(dag.add_node('e'))
        self.assertTrue(dag.add_edge('a', 'b'))
        self.assertTrue(dag.add_edge('a', 'c'))
        self.assertTrue(dag.add_edge('b', 'c'))
        self.assertTrue(dag.add_edge('b', 'd'))
        self.assertTrue(dag.add_edge('d', 'e'))
        self.assertTrue(dag.get_graph() == {'a': set({'b', 'c'}), 'b': set(
            {'c', 'd'}), 'c': set(), 'd': set('e'), 'e': set()})


class TestNotCreateCycle(unittest.TestCase):
    """Tests that creating cycles does not work"""

    def test(self):
        dag = DAG.DAG()
        self.assertTrue(dag.add_node('a'))
        self.assertTrue(dag.add_node('b'))
        self.assertTrue(dag.add_node('c'))
        self.assertTrue(dag.add_node('d'))
        self.assertTrue(dag.add_edge('a', 'b'))
        self.assertTrue(dag.add_edge('b', 'c'))
        self.assertFalse(dag.add_edge('c', 'a'))
        self.assertTrue(dag.add_edge('c', 'd'))
        self.assertFalse(dag.add_edge('d', 'c'))
        self.assertFalse(dag.add_edge('d', 'a'))


class TestNotAddExistingNode(unittest.TestCase):
    """Tests that adding a pre-existing node does not work"""

    def test(self):
        dag = DAG.DAG()
        self.assertTrue(dag.add_node('a'))
        self.assertTrue(dag.add_node('b'))
        self.assertFalse(dag.add_node('a'))


class TestNotAddImpossibleEdge(unittest.TestCase):
    """Tests that adding an edge between
    non-existant nodes does not work"""

    def test(self):
        dag = DAG.DAG()
        self.assertTrue(dag.add_node('a'))
        self.assertTrue(dag.add_node('b'))
        self.assertFalse(dag.add_edge('a', 'c'))
        self.assertFalse(dag.add_edge('c', 'a'))


if __name__ == '__main__':
    unittest.main()
