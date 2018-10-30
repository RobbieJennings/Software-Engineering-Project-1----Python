import unittest
import DAG


class TestNullNode(unittest.TestCase):
    """Tests that getting a non-existant node returns null"""

    def test(self):
        dag = DAG.DAG()
        assert dag.graph == {}


class TestSingleNode(unittest.TestCase):
    """Tests that a tree containing one node works"""

    def test(self):
        dag = DAG.DAG()
        dag.add_node('a')
        assert dag.graph == {'a': set()}


class TestSingleEdge(unittest.TestCase):
    """Tests that creating a graph with one edge works"""

    def test(self):
        dag = DAG.DAG()
        dag.add_node('a')
        dag.add_node('b')
        dag.add_edge('a', 'b')
        assert dag.graph == {'a': set('b'), 'b': set()}


class TestMultipleEdges(unittest.TestCase):
    """Tests that creating a graph
    containing more than one edge works"""

    def test(self):
        dag = DAG.DAG()
        dag.add_node('a')
        dag.add_node('b')
        dag.add_node('c')
        dag.add_edge('a', 'b')
        dag.add_edge('b', 'c')
        assert dag.graph == {'a': set('b'), 'b': set('c'), 'c': set()}


class TestMultipleEdgedNodes(unittest.TestCase):
    """Tests that creating a graph with
    nodes containing multiple edges works"""

    def test(self):
        dag = DAG.DAG()
        dag.add_node('a')
        dag.add_node('b')
        dag.add_node('c')
        dag.add_node('d')
        dag.add_node('e')
        dag.add_edge('a', 'b')
        dag.add_edge('a', 'c')
        dag.add_edge('b', 'c')
        dag.add_edge('b', 'd')
        dag.add_edge('d', 'e')
        assert dag.graph == {'a': set({'b', 'c'}), 'b': set(
            {'c', 'd'}), 'c': set(), 'd': set('e'), 'e': set()}


if __name__ == '__main__':
    unittest.main()
