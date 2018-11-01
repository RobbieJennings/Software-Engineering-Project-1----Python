import unittest
import BinaryTree
import LCA


class TestLCAWithNullRoot(unittest.TestCase):
    "Tests that Lowest Common Ancestor works when root is null"""

    def test(self):
        self.assertEqual(LCA.findLCA(None, 1, 2), -1)


class TestLCAWithRootNode(unittest.TestCase):
    """Tests that Lowest Common Ancestor works when searching with root"""

    def test(self):
        root = BinaryTree.Node(1)
        a = BinaryTree.Node(2)
        b = BinaryTree.Node(3)

        root.insertLeft(a)
        root.insertRight(b)

        self.assertEqual(LCA.findLCA(root.getGraph(), root.getKey(), 2), 1)
        self.assertEqual(LCA.findLCA(root.getGraph(), 3, root.getKey()), 1)


class TestLCAWithEqualNodes(unittest.TestCase):
    """Tests that Lowest Common Ancestor works
    when searching for the same node"""

    def test(self):
        root = BinaryTree.Node(1)
        a = BinaryTree.Node(2)
        b = BinaryTree.Node(3)

        root.insertLeft(a)
        root.insertRight(b)

        self.assertEqual(LCA.findLCA(root.getGraph(), 2, 2), 2)
        self.assertEqual(LCA.findLCA(root.getGraph(), 3, 3), 3)


class TestLCAWithAncestor(unittest.TestCase):
    """Tests that Lowest Common Ancestor works
    when one node is already an ancestor of the other"""

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

        self.assertEqual(LCA.findLCA(root.getGraph(), 2, 5), 2)
        self.assertEqual(LCA.findLCA(root.getGraph(), 3, 6), 3)


class TestLCAWithNoPath(unittest.TestCase):
    """Tests that Lowest Common Ancestor works when
    there exists no path from root to nodes"""

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

        self.assertEqual(LCA.findLCA(root.getGraph(), 1, 8), -1)
        self.assertEqual(LCA.findLCA(b.getGraph(), 6, 4), -1)


class TestLCAWithPath(unittest.TestCase):
    """Tests that Lowest Common Ancestor works when
    there exists a path from root to nodes"""

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

        self.assertEqual(LCA.findLCA(root.getGraph(), 4, 5), 2)
        self.assertEqual(LCA.findLCA(root.getGraph(), 4, 6), 1)
        self.assertEqual(LCA.findLCA(root.getGraph(), 3, 4), 1)
        self.assertEqual(LCA.findLCA(root.getGraph(), 2, 4), 2)


if __name__ == '__main__':
    unittest.main()
