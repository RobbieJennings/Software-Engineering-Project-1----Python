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


def findPath(root, path, k):
    """Finds the path from k node to given root of the tree.
    Stores the path in a list path[],
    Returns true if path exists,
    Otherwise Returns False

    Keyword arguments:
    root -- the Node object that represents the root of the tree
    path -- the array in which to insert the path
    k -- the key of the Node object intended to be reached"""

    # Base Case
    if root is None:
        return False

    # Store this node in path vector. The node will be
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


def findLCA(root, n1, n2):
    """Returns Lowest Common Ancestor of n1 and n2
    if n1 and n2 are present in the given tree,
    Otherwise returns -1

    Keyword attributes:
    root -- the Node object that is the root of the Tree
    n1 -- the first Node Object to search for the Lowest Common Ancestor
    n2 -- the second Node Object to search for the Lowest Common Ancestor"""

    # To store paths to n1 and n2 from the root
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
