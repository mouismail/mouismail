from extratypes import Tree  # Import the Tree class from extratypes module

def solution(tree, leaf_id):
    """
    This function reroots the tree at the specified leaf node.
    """
    # Helper function to recursively find the path from root to the leaf
    def find_path(node, leaf_id, path):
        if node is None:
            return False
        path.append(node)
        if node.x == leaf_id or find_path(node.l, leaf_id, path) or find_path(node.r, leaf_id, path):
            return True
        path.pop()
        return False

    # Reversing the parent-child relationship
    def reverse_relationship(path):
        for i in range(len(path) - 1, 0, -1):
            current = path[i]
            parent = path[i - 1]
            # Swap children and parent
            if parent.l == current:
                current.r = parent
                parent.l = parent.r
                parent.r = None
            else:
                current.l = parent
                parent.r = parent.l
                parent.l = None

        # Handle the root of the tree
        if path:
            path[-1].l = path[-1].r = None
            return path[-1]
        return None

    path = []
    find_path(tree, leaf_id, path)
    return reverse_relationship(path) if path else None

# Example usage
root = Tree(3, Tree(1, Tree(2), Tree(6)), Tree(5, None, Tree(4)))
new_root = solution(root, 2)
# new_root is now the new root of the tree with the tree rerooted at the node with x=2
