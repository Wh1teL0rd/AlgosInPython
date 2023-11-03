from algo_functions.invert_binary_tree import BinaryTree


def are_trees_equal(tree1: BinaryTree, tree2: BinaryTree) -> bool:
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    return (tree1.value == tree2.value and
            are_trees_equal(tree1.left, tree2.left) and
            are_trees_equal(tree1.right, tree2.right))
