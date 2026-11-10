def gen_bin_tree(height=5, root=18, left_leaf=None, right_leaf=None):

    if left_leaf is None:
        left_leaf = lambda r: (r - 8) * 3
    if right_leaf is None:
        right_leaf = lambda r: (r + 8) * 2

    if height <= 0:
        return None

    return {
        "value": root,
        "left": gen_bin_tree(height - 1, left_leaf(root), left_leaf, right_leaf),
        "right": gen_bin_tree(height - 1, right_leaf(root), left_leaf, right_leaf),
    }


def print_tree(node, level=0, prefix="Root: "):
    if node is None:
        return
    print("  " * level + prefix + str(node["value"]))
    print_tree(node["left"], level + 1, "L ")
    print_tree(node["right"], level + 1, "R ")

tree = gen_bin_tree()
print_tree(tree)