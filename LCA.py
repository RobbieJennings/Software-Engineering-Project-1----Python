def findLCA(graph, n1, n2):
    """Returns Lowest Common Ancestor of n1 and n2
    if n1 and n2 are present in the given tree,
    Otherwise returns -1

    Keyword arguments:
    root -- the Node object that is the root of the Tree
    n1 -- the first Node Object to search for the Lowest Common Ancestor
    n2 -- the second Node Object to search for the Lowest Common Ancestor"""
    if graph is None:
        return -1

    if n1 not in graph or n2 not in graph:
        return -1

    indexn1 = graph.keys().index(n1)
    indexn2 = graph.keys().index(n2)
    dist = getDistances(graph)
    shortestPath = float("inf")
    lca = None

    for i in range(0, len(dist)):
        if dist[i][indexn1] + dist[i][indexn2] < shortestPath:
            shortestPath = dist[i][indexn1] + dist[i][indexn2]
            lca = graph.keys()[i]

    return lca


def getDistances(graph):
    """Does Floyd Warshall's Algorithm and returns an array of the
    shortest paths from each node in the graph to each other node

    Keyword arguments:
    graph -- an OrderedDict representation of the Binary Tree or DAG"""
    dist = []

    # Initialise array
    for i in range(0, len(graph)):
        dist.insert(i, [])
        for j in range(0, len(graph)):
            dist[i].insert(j, float("inf"))

    # Insert nodes and edges
    for i in graph:
        indexi = graph.keys().index(i)
        dist[indexi][indexi] = 0
        for j in graph[i]:
            indexj = graph.keys().index(j)
            dist[indexi][indexj] = 1

    # Floyd Warshall Algorithm
    v = len(dist)
    for k in range(0, v):
        for i in range(0, v):
            for j in range(0, v):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
