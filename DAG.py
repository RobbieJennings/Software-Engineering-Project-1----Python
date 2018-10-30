# DAG code mostly taken from https://github.com/thieman/py-dag

from copy import deepcopy
from collections import deque
from collections import OrderedDict


def itervalues(d, **kw):
    return iter(d.values(**kw))


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
            return False
        graph[node_name] = set()
        return True

    def add_edge(self, ind_node, dep_node, graph=None):
        """ Add an edge (dependency) between the specified nodes. """
        if not graph:
            graph = self.graph
        if ind_node not in graph or dep_node not in graph:
            return False
        test_graph = deepcopy(graph)
        test_graph[ind_node].add(dep_node)
        if self.validate(test_graph):
            graph[ind_node].add(dep_node)
            return True
        return False

    def reset_graph(self):
        """ Restore the graph to an empty state. """
        self.graph = OrderedDict()
        return True

    def ind_nodes(self, graph=None):
        """ Returns a list of all nodes in the graph with no dependencies. """
        dependent_nodes = set(
            node for dependents in itervalues(graph) for node in dependents
        )
        return [node for node in graph.keys() if node not in dependent_nodes]

    def validate(self, graph=None):
        """ Returns Boolean of whether DAG is valid. """
        graph = graph if graph is not None else self.graph
        if len(self.ind_nodes(graph)) == 0:
            return False
        if self.topological_sort(graph):
            return True
        return False

    def topological_sort(self, graph=None):
        """ Returns a topological ordering of the DAG.
        Raises an error if this is not possible (graph is not valid).
        """
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
        return False
