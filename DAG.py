# DAG code mostly taken from https://github.com/thieman/py-dag

from copy import deepcopy
from collections import deque

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict


class DAGValidationError(Exception):
    pass


class DAG(object):
    """ Directed acyclic graph implementation. """

    def __init__(self):
        """ Construct a new DAG with no nodes or edges. """
        self.reset_graph()

    def add_node(self, node_name, graph=None):
        """ Add a node if it does not exist yet, or error out. """
        if not graph:
            graph = self.graph
        if node_name in graph:
            raise KeyError('node %s already exists' % node_name)
        graph[node_name] = set()

    def add_edge(self, ind_node, dep_node, graph=None):
        """ Add an edge (dependency) between the specified nodes. """
        if not graph:
            graph = self.graph
        if ind_node not in graph or dep_node not in graph:
            raise KeyError('one or more nodes do not exist in graph')
        test_graph = deepcopy(graph)
        test_graph[ind_node].add(dep_node)
        is_valid, message = self.validate(test_graph)
        if is_valid:
            graph[ind_node].add(dep_node)
        else:
            raise DAGValidationError()

    def reset_graph(self):
        """ Restore the graph to an empty state. """
        self.graph = OrderedDict()

    def validate(self, graph=None):
        """ Returns (Boolean, message) of whether DAG is valid. """
        graph = graph if graph is not None else self.graph
        if len(self.ind_nodes(graph)) == 0:
            return (False, 'no independent nodes detected')
        try:
            self.topological_sort(graph)
        except ValueError:
            return (False, 'failed topological sort')
        return (True, 'valid')

    def topological_sort(self, graph=None):
        """ Returns a topological ordering of the DAG.
        Raises an error if this is not possible (graph is not valid).
        """
        if graph is None:
            graph = self.graph

        in_degree = {}
        for u in graph:
            in_degree[u] = 0

        for u in graph:
            for v in graph[u]:
                in_degree[v] += 1

        queue = deque()
        for u in in_degree:
            if in_degree[u] == 0:
                queue.appendleft(u)

        sorted = []
        while queue:
            u = queue.pop()
            sorted.append(u)
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.appendleft(v)

        if len(sorted) == len(graph):
            return sorted
        else:
            raise ValueError('graph is not acyclic')

    def size(self):
        return len(self.graph)
