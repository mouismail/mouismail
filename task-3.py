from extratypes import Tree  # Import the Tree class from extratypes module

def solution(tree, leaf_id):
    """
    This function reroots the tree at the specified leaf node.
    """
    # Helper function to recursively find the path from root to the leaf
    def find_path(node, leaf_id, path):
        if node is None:
            return False
        if node.x == leaf_id:
            path.append(node)
            return True
        if find_path(node.l, leaf_id, path) or find_path(node.r, leaf_id, path):
            path.append(node)
            return True
        return False

    # Reverse the parent-child relationship along the path
    def reverse_relationship(path):
        for i in range(len(path) - 1):
            child = path[i]
            parent = path[i + 1]

            # Swap the child with the parent's other subtree
            if parent.l == child:
                parent.l, child.r = child.r, parent
            elif parent.r == child:
                parent.r, child.l = child.l, parent

        # The root of the new tree
        return path[-1]

    path = []
    find_path(tree, leaf_id, path)
    return reverse_relationship(path) if path else None

# Example usage
root = Tree(3, Tree(1, Tree(2), Tree(6)), Tree(5, None, Tree(4)))
new_root = solution(root, 2)
