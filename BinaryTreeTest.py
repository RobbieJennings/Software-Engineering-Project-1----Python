import unittest
import BinaryTree


class TestNullNode(unittest.TestCase):
    """Tests that getting a non-existant node returns null"""

    def test(self):
        root = BinaryTree.Node(1)

        self.assertEqual(root.getLeftChild(), None)
        self.assertEqual(root.getRightChild(), None)


class TestSingleNode(unittest.TestCase):
    """Tests that a tree containing one node works"""

    def test(self):
        root = BinaryTree.Node(1)

        self.assertEqual(root.getTreeString(), "()1()")
        self.assertEqual(root.getKey(), 1)


class TestInsertingLeaves(unittest.TestCase):
    """Tests that inserting Leaves onto a node works"""

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


class TestInsertingLeavesOntoLeaves(unittest.TestCase):
    """Tests inserting Leaves onto a tree
    containing more than one node works"""

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


class TestInsertingBetweenNodes(unittest.TestCase):
    """Tests that inserting nodes onto nodes with children works"""

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


if __name__ == '__main__':
    unittest.main()
