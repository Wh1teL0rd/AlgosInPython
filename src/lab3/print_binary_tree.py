from src.lab3.invert_binary_tree import BinaryTree


def print_binary_tree(tree: BinaryTree, indent="", last=True):
    if tree is not None:
        print(indent, end="")
        if last:
            print("└── ", end="")
            indent += "    "
        else:
            print("├── ", end="")
            indent += "│   "

        print(tree.value)

        print_binary_tree(tree.right, indent, False)
        print_binary_tree(tree.left, indent, True)
