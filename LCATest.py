import unittest
import BinaryTree


# Tests that getting non-existant nodes returns null
class TestNullNode(unittest.TestCase):
    def test(self):
        root = BinaryTree.Node(1)

        self.assertEqual(root.getLeftChild(), None)
        self.assertEqual(root.getRightChild(), None)


# Tests that a tree containing one node works
class TestSingleNode(unittest.TestCase):
    def test(self):
        root = BinaryTree.Node(1)

        self.assertEqual(root.getTreeString(), "()1()")
        self.assertEqual(root.getKey(), 1)


# Tests that inserting Leaves onto a node works
class TestInsertingLeaves(unittest.TestCase):
    def test(self):
        root = BinaryTree.Node(1)
        a = BinaryTree.Node(2)
        b = BinaryTree.Node(3)

        root.insertLeft(a)
        root.insertRight(b)

        self.assertEqual(root.getTreeString(), "(()2())1(()3())")
        self.assertEqual(root.getKey(), 1)
        self.assertEqual(root.getLeftChild().getKey(), 2)
        self.assertEqual(root.getRightChild().getKey(), 3)
        self.assertEqual(root.getLeftChild().getParent().getKey(), 1)
        self.assertEqual(root.getRightChild().getParent().getKey(), 1)


# Tests inserting Leaves onto a tree containing more than one node works
class TestInsertingLeavesOntoLeaves(unittest.TestCase):
    def test(self):
        root = BinaryTree.Node(1)
        a = BinaryTree.Node(2)
        b = BinaryTree.Node(3)
        c = BinaryTree.Node(4)
        d = BinaryTree.Node(5)
        e = BinaryTree.Node(6)
        f = BinaryTree.Node(7)

        root.insertLeft(a)
        root.insertRight(b)
        a.insertLeft(c)
        a.insertRight(d)
        b.insertLeft(e)
        b.insertRight(f)

        self.assertEqual(root.getTreeString(),
                         "((()4())2(()5()))1((()6())3(()7()))")
        self.assertEqual(root.getKey(), 1)
        self.assertEqual(root.getLeftChild().getKey(), 2)
        self.assertEqual(root.getRightChild().getKey(), 3)
        self.assertEqual(root.getLeftChild().getLeftChild().getKey(), 4)
        self.assertEqual(root.getLeftChild().getRightChild().getKey(), 5)
        self.assertEqual(root.getRightChild().getLeftChild().getKey(), 6)
        self.assertEqual(root.getRightChild().getRightChild().getKey(), 7)
        self.assertEqual(root.getLeftChild().getParent().getKey(), 1)
        self.assertEqual(root.getRightChild().getParent().getKey(), 1)
        self.assertEqual(root.getLeftChild().getLeftChild()
                         .getParent().getKey(), 2)
        self.assertEqual(root.getLeftChild().getRightChild().getParent()
                         .getKey(), 2)
        self.assertEqual(root.getRightChild().getLeftChild().getParent()
                         .getKey(), 3)
        self.assertEqual(root.getRightChild().getRightChild().getParent()
                         .getKey(), 3)


# Tests that inserting nodes onto nodes with children works
class TestInsertingBetweenNodes(unittest.TestCase):
    def test(self):
        root = BinaryTree.Node(1)
        a = BinaryTree.Node(2)
        b = BinaryTree.Node(3)
        c = BinaryTree.Node(4)
        d = BinaryTree.Node(5)
        e = BinaryTree.Node(6)
        f = BinaryTree.Node(7)
        g = BinaryTree.Node(8)
        h = BinaryTree.Node(9)

        root.insertLeft(a)
        root.insertRight(b)
        a.insertLeft(c)
        a.insertRight(d)
        b.insertLeft(e)
        b.insertRight(f)
        a.insertLeft(g)
        b.insertRight(h)

        self.assertEqual(root.getTreeString(),
                         "(((()4())8())2(()5()))1((()6())3(()9(()7())))")
        self.assertEqual(root.getKey(), 1)
        self.assertEqual(root.getLeftChild().getKey(), 2)
        self.assertEqual(root.getRightChild().getKey(), 3)
        self.assertEqual(root.getLeftChild().getLeftChild().getKey(), 8)
        self.assertEqual(root.getLeftChild().getRightChild().getKey(), 5)
        self.assertEqual(root.getRightChild().getLeftChild().getKey(), 6)
        self.assertEqual(root.getRightChild().getRightChild().getKey(), 9)
        self.assertEqual(root.getLeftChild().getLeftChild().getLeftChild()
                         .getKey(), 4)
        self.assertEqual(root.getRightChild().getRightChild().getRightChild()
                         .getKey(), 7)
        self.assertEqual(root.getLeftChild().getParent().getKey(), 1)
        self.assertEqual(root.getRightChild().getParent().getKey(), 1)
        self.assertEqual(root.getLeftChild().getLeftChild().getParent()
                         .getKey(), 2)
        self.assertEqual(root.getLeftChild().getRightChild().getParent()
                         .getKey(), 2)
        self.assertEqual(root.getRightChild().getLeftChild().getParent()
                         .getKey(), 3)
        self.assertEqual(root.getRightChild().getRightChild().getParent()
                         .getKey(), 3)
        self.assertEqual(root.getLeftChild().getLeftChild().getLeftChild()
                         .getParent().getKey(), 8)
        self.assertEqual(root.getRightChild().getRightChild().getRightChild()
                         .getParent().getKey(), 9)


# Tests that Lowest Common Ancestor works when root is null
class TestLCAWithNullRoot(unittest.TestCase):
    def test(self):
        self.assertEqual(BinaryTree.findLCA(None, 1, 2), -1)


# Tests that Lowest Common Ancestor works when searching with root
class TestLCAWithRootNode(unittest.TestCase):
    def test(self):
        root = BinaryTree.Node(1)
        a = BinaryTree.Node(2)
        b = BinaryTree.Node(3)

        root.insertLeft(a)
        root.insertRight(b)

        self.assertEqual(BinaryTree.findLCA(root, root, 2), 1)
        self.assertEqual(BinaryTree.findLCA(root, 3, root), 1)


# Tests that Lowest Common Ancestor works when searching for the same node
class TestLCAWithEqualNodes(unittest.TestCase):
    def test(self):
        root = BinaryTree.Node(1)
        a = BinaryTree.Node(2)
        b = BinaryTree.Node(3)

        root.insertLeft(a)
        root.insertRight(b)

        self.assertEqual(BinaryTree.findLCA(root, 2, 2), 2)
        self.assertEqual(BinaryTree.findLCA(root, 3, 3), 3)


# Tests that Lowest Common Ancestor works
# when one node is already an ancestor of the other
class TestLCAWithAncestor(unittest.TestCase):
    def test(self):
        root = BinaryTree.Node(1)
        a = BinaryTree.Node(2)
        b = BinaryTree.Node(3)
        c = BinaryTree.Node(4)
        d = BinaryTree.Node(5)
        e = BinaryTree.Node(6)
        f = BinaryTree.Node(7)

        root.insertLeft(a)
        root.insertRight(b)
        a.insertLeft(c)
        a.insertRight(d)
        b.insertLeft(e)
        b.insertRight(f)

        self.assertEqual(BinaryTree.findLCA(root, 2, 5), 2)
        self.assertEqual(BinaryTree.findLCA(root, 3, 6), 3)


# Tests that Lowest Common Ancestor works when
# there exists no path from root to nodes
class TestLCAWithNoPath(unittest.TestCase):
    def test(self):
        root = BinaryTree.Node(1)
        a = BinaryTree.Node(2)
        b = BinaryTree.Node(3)
        c = BinaryTree.Node(4)
        d = BinaryTree.Node(5)
        e = BinaryTree.Node(6)
        f = BinaryTree.Node(7)

        root.insertLeft(a)
        root.insertRight(b)
        a.insertLeft(c)
        a.insertRight(d)
        b.insertLeft(e)
        b.insertRight(f)

        self.assertEqual(BinaryTree.findLCA(root, 1, 8), -1)
        self.assertEqual(BinaryTree.findLCA(b, 6, 4), -1)


# Tests that Lowest Common Ancestor works when
# there exists a path from root to nodes
class TestLCAWithPath(unittest.TestCase):
    def test(self):
        root = BinaryTree.Node(1)
        a = BinaryTree.Node(2)
        b = BinaryTree.Node(3)
        c = BinaryTree.Node(4)
        d = BinaryTree.Node(5)
        e = BinaryTree.Node(6)
        f = BinaryTree.Node(7)

        root.insertLeft(a)
        root.insertRight(b)
        a.insertLeft(c)
        a.insertRight(d)
        b.insertLeft(e)
        b.insertRight(f)

        self.assertEqual(BinaryTree.findLCA(root, 4, 5), 2)
        self.assertEqual(BinaryTree.findLCA(root, 4, 6), 1)
        self.assertEqual(BinaryTree.findLCA(root, 3, 4), 1)
        self.assertEqual(BinaryTree.findLCA(root, 2, 4), 2)


if __name__ == '__main__':
    unittest.main()
