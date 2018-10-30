import unittest
import DAG


class TestEmpty(unittest.TestCase):
    """Tests that a tree with no nodes returns works"""

    def test(self):
        dag = DAG.DAG()
        assert dag.graph == {}


class TestSingleNode(unittest.TestCase):
    """Tests that a tree containing one node works"""

    def test(self):
        dag = DAG.DAG()
        assert dag.add_node('a')
        assert dag.graph == {'a': set()}


class TestSingleEdge(unittest.TestCase):
    """Tests that creating a graph with one edge works"""

    def test(self):
        dag = DAG.DAG()
        assert dag.add_node('a')
        assert dag.add_node('b')
        assert dag.add_edge('a', 'b')
        assert dag.graph == {'a': set('b'), 'b': set()}


class TestMultipleEdges(unittest.TestCase):
    """Tests that creating a graph
    containing more than one edge works"""

    def test(self):
        dag = DAG.DAG()
        assert dag.add_node('a')
        assert dag.add_node('b')
        assert dag.add_node('c')
        assert dag.add_edge('a', 'b')
        assert dag.add_edge('b', 'c')
        assert dag.graph == {'a': set('b'), 'b': set('c'), 'c': set()}


class TestMultipleEdgedNodes(unittest.TestCase):
    """Tests that creating a graph with
    nodes containing multiple edges works"""

    def test(self):
        dag = DAG.DAG()
        assert dag.add_node('a')
        assert dag.add_node('b')
        assert dag.add_node('c')
        assert dag.add_node('d')
        assert dag.add_node('e')
        assert dag.add_edge('a', 'b')
        assert dag.add_edge('a', 'c')
        assert dag.add_edge('b', 'c')
        assert dag.add_edge('b', 'd')
        assert dag.add_edge('d', 'e')
        assert dag.graph == {'a': set({'b', 'c'}), 'b': set(
            {'c', 'd'}), 'c': set(), 'd': set('e'), 'e': set()}


if __name__ == '__main__':
    unittest.main()
