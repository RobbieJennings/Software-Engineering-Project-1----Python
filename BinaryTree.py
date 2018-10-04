import sys


class Node():

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def getKey(self):
        return self.key

    def getLeftChild(self):
        return self.left.key

    def getRightChild(self):
        return self.right.key

    def getParent(self):
        return self.parent.key

    def insertRight(self, newNode):
        if self.right is None:
            self.right = Node(newNode)
            newNode.parent = self
        else:
            node = Node(newNode)
            node.right = self.right
            self.right = node
            newNode.parent = self

    def insertLeft(self, newNode):
        if self.left is None:
            self.left = Node(newNode)
            newNode.parent = self
        else:
            node = Node(newNode)
            node.left = self.left
            self.left = node
            newNode.parent = self

    def writeTree(self):
        sys.stdout.write("(")
        if self.left is not None:
            self.left.key.writeTree()
        sys.stdout.write(")" + str(self.key) + "(")
        if self.right is not None:
            self.right.key.writeTree()
        sys.stdout.write(")")


class Tree():

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def setRoot(self, newNode):
        self.root = newNode

    def printTree(self):
        self.root.writeTree()
        sys.stdout.write("\n")


tree = Tree()
a = Node(key=1)
b = Node(key=2)
c = Node(key=3)
d = Node(key=4)
tree.setRoot(newNode=a)
a.insertLeft(newNode=b)
b.insertLeft(newNode=c)
tree.getRoot().insertRight(newNode=d)
tree.printTree()
print(c.getParent())
print(tree.getRoot().getLeftChild().getParent())
