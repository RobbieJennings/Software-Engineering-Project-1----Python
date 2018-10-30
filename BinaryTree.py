from collections import OrderedDict


class Node():
    """A node used for populating a Binary Tree"""

    def __init__(self, key):
        """Form a Node

        Keyword arguments:
        Key -- the key attached to the Node"""
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def getKey(self):
        """Returns key"""
        return self.key

    def getLeftChild(self):
        """Returns left child Node"""
        return self.left

    def getRightChild(self):
        """Returns right child Node"""
        return self.right

    def getParent(self):
        """Returns parent Node"""
        return self.parent

    def insertRight(self, newNode):
        """Sets new node as right Child
        set right child as right child of new node

        Keyword arguments:
        newNode -- the Node object to be iserted to the right of this Node"""
        if self.right is None:
            self.right = newNode
            newNode.parent = self
        else:
            self.right.parent = newNode
            newNode.right = self.right
            newNode.parent = self
            self.right = newNode

    def insertLeft(self, newNode):
        """sets new node as left Child
        set left child as left child of new node

        Keyword arguments:
        newNode -- the Node object to be iserted to the left of this Node"""
        if self.left is None:
            self.left = newNode
            newNode.parent = self
        else:
            self.left.parent = newNode
            newNode.left = self.left
            newNode.parent = self
            self.left = newNode

    def getTreeString(self):
        """returns a string representing the tree with node as root"""
        string = "("
        if self.left is not None:
            string += self.left.getTreeString()
        string += ")" + str(self.key) + "("
        if self.right is not None:
            string += self.right.getTreeString()
        string += ")"
        return string

    def getGraph(self):
        """return an OrderedDict represents the tree with node as root"""
        graph = OrderedDict()
        self.compileGraph(graph, self)
        return graph

    def compileGraph(self, graph, node):
        """recursively adds nodes to graph"""
        graph[node.getKey()] = set()
        if node.getLeftChild() is not None:
            graph[node.getKey()].add(node.getLeftChild().getKey())
            self.compileGraph(graph, node.getLeftChild())
        if node.getRightChild() is not None:
            graph[node.getKey()].add(node.getRightChild().getKey())
            self.compileGraph(graph, node.getRightChild())
