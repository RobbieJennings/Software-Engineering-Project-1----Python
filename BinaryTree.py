class Node():

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def getKey(self):
        return self.key

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def getParent(self):
        return self.parent

    def insertRight(self, newNode):
        if self.right is None:
            self.right = Node(newNode)
            self.right.parent = self
        else:
            node = Node(newNode)
            node.right = self.right
            self.right = node
            self.right.parent = self

    def insertLeft(self, newNode):
        if self.left is None:
            self.left = Node(newNode)
            self.left.parent = self
        else:
            node = Node(newNode)
            node.left = self.left
            self.left = node
            self.left.parent = self

    def printTree(self):
        if self.getLeftChild() is not None:
            printTree(self.getLeftChild())
        print(self.getKey())
        if self.getRightChild() is not None:
            printTree(self.getRightChild())


class Tree():

    def __init__(self):
        self.root = None

    def setRoot(self, newNode):
        self.root = newNode

    def printTree(self):
        self.root.printTree()


x = Tree()
y = Node(key=123)
x.setRoot(newNode=y)
x.printTree()
