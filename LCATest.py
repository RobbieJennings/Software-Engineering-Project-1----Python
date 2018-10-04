import unittest
from BinaryTree import Node
from BinaryTree import findLCA


class TestLCA(unittest.TestCase):
    def test(self):
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

        self.assertEqual(findLCA(root, 4, 5), 2)
        self.assertEqual(findLCA(root, 4, 6), 1)
        self.assertEqual(findLCA(root, 3, 4), 1)
        self.assertEqual(findLCA(root, 2, 4), 2)


if __name__ == '__main__':
    unittest.main()
