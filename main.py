from algo_functions.invert_binary_tree import BinaryTree, invert_binary_tree
from algo_functions.print_binary_tree import print_binary_tree

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)


print("Початкове дерево:")
print_binary_tree(root)


inverted_tree = invert_binary_tree(root)


print("\nОбернене дерево:")
print_binary_tree(inverted_tree)
