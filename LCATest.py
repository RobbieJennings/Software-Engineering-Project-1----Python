import unittest
import BinaryTree


class TestLCA(unittest.TestCase):
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

        # test null node
        self.assertEqual(root.getLeftChild(), None)
        self.assertEqual(root.getRightChild(), None)

        # test single node
        self.assertEqual(root.getTreeString(), "()1()")
        self.assertEqual(root.getKey(), 1)

        # test inserting leaves
        root.insertLeft(a)
        root.insertRight(b)
        self.assertEqual(root.getTreeString(), "(()2())1(()3())")
        self.assertEqual(root.getKey(), 1)
        self.assertEqual(root.getLeftChild().getKey(), 2)
        self.assertEqual(root.getRightChild().getKey(), 3)
        self.assertEqual(root.getLeftChild().getParent().getKey(), 1)
        self.assertEqual(root.getRightChild().getParent().getKey(), 1)

        # test inserting leaves onto leaves
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

        # test inserting between nodes
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

        # test LCA with null root
        self.assertEqual(BinaryTree.findLCA(None, 1, 2), -1)

        # test LCA with no path
        self.assertEqual(BinaryTree.findLCA(root, 1, 10), -1)
        self.assertEqual(BinaryTree.findLCA(root, 10, 1), -1)

        # test LCA with path
        self.assertEqual(BinaryTree.findLCA(root, 4, 5), 2)
        self.assertEqual(BinaryTree.findLCA(root, 4, 6), 1)
        self.assertEqual(BinaryTree.findLCA(root, 3, 4), 1)
        self.assertEqual(BinaryTree.findLCA(root, 2, 4), 2)


if __name__ == '__main__':
    unittest.main()
