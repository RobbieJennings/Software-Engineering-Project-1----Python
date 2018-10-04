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
            self.right = newNode
            newNode.parent = self
        else:
            newNode.right = self.right
            self.right = newNode
            newNode.parent = self

    def insertLeft(self, newNode):
        if self.left is None:
            self.left = newNode
            newNode.parent = self
        else:
            newNode.left = self.left
            self.left = newNode
            newNode.parent = self

    def toString(self):
        string = "("
        if self.left is not None:
            string += self.left.toString()
        string += ")" + str(self.key) + "("
        if self.right is not None:
            string += self.right.toString()
        string += ")"
        return string


class Tree():

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def setRoot(self, newNode):
        self.root = newNode

    def printTree(self):
        print(self.root.toString())


x = Tree()
a = Node(key=1)
b = Node(key=2)
c = Node(key=3)
d = Node(key=4)
e = Node(key=5)
x.setRoot(newNode=a)
a.insertLeft(newNode=b)
b.insertLeft(newNode=c)
a.insertLeft(newNode=e)
x.getRoot().insertRight(newNode=d)
x.printTree()
print(c.getParent().getKey())
print(x.getRoot().getLeftChild().getParent().getKey())
