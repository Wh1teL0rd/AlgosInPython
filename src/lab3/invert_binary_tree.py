class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(tree: BinaryTree) -> BinaryTree | None:
    if tree is None:
        return None

    tree.left, tree.right = invert_binary_tree(tree.right), invert_binary_tree(tree.left)

    return tree
