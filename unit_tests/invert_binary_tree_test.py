import unittest

from algo_functions.lab3.are_trees_equal import are_trees_equal
from algo_functions.lab3.invert_binary_tree import BinaryTree, invert_binary_tree


class TestInvertBinaryTree(unittest.TestCase):
    def test_invert_binary_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        inverted_tree = invert_binary_tree(root)

        expected_tree = BinaryTree(1)
        expected_tree.left = BinaryTree(3)
        expected_tree.right = BinaryTree(2)
        expected_tree.left.left = BinaryTree(7)
        expected_tree.left.right = BinaryTree(6)
        expected_tree.right.left = BinaryTree(5)
        expected_tree.right.right = BinaryTree(4)

        # Порівнюємо інвертоване дерево з очікуваним деревом
        self.assertTrue(are_trees_equal(inverted_tree, expected_tree))


if __name__ == '__main__':
    unittest.main()
