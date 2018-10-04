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

    def getTreeString(self):
        string = "("
        if self.left is not None:
            string += self.left.getTreeString()
        string += ")" + str(self.key) + "("
        if self.right is not None:
            string += self.right.getTreeString()
        string += ")"
        return string


# Finds the path from k node to given root of the tree.
# Stores the path in a list path[], returns true if path
# exists otherwise false
def findPath(root, path, k):

    # Base Case
    if root is None:
        return False

    # Store this node is path vector. The node will be
    # removed if not in path from root to k
    path.append(root.getKey())

    # See if the k is same as root's key
    if root.getKey() == k:
        return True

    # Check if k is found in left or right subtree
    right = root.getRightChild()
    left = root.getLeftChild()
    if ((left is not None and findPath(left, path, k))
            or (right is not None and findPath(right, path, k))):
        return True

    # If not present in subtree rooted with root, remove
    # root from path and return False
    path.pop()
    return False


# Returns LCA if node n1, n2 are present in the given
# binary tre otherwise return -1
def findLCA(root, n1, n2):

    # To store paths to n1 and n2 fromthe root
    path1 = []
    path2 = []

    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

    # Compare the paths to get the first different value
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


root = Node(1)
a = Node(2)
b = Node(3)
c = Node(4)
d = Node(5)
e = Node(6)
f = Node(7)
root.insertLeft(a)
root.insertRight(b)
a.insertLeft(c)
a.insertRight(d)
b.insertLeft(e)
b.insertRight(f)

print("LCA(4, 5) = %d" % (findLCA(root, 4, 5)))
print("LCA(4, 6) = %d" % (findLCA(root, 4, 6)))
print("LCA(3, 4) = %d" % (findLCA(root, 3, 4)))
print("LCA(2, 4) = %d" % (findLCA(root, 2, 4)))

print(root.getTreeString())
print(root.getLeftChild().getRightChild().getParent().getParent().getKey())
