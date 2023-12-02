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

    # Reverse the parent-child relationship along the path
    def reverse_relationship(path):
        for i in range(len(path) - 1, 0, -1):
            current = path[i]
            parent = path[i - 1]

            # Check which side the current node is on and adjust accordingly
            if parent.l == current:
                parent.l = current.r
                current.r = parent
            elif parent.r == current:
                parent.r = current.l
                current.l = parent

        # The last node in the path is the new root
        if path:
            new_root = path[-1]
            new_root.l = new_root.r = None
            return new_root
        return None

    path = []
    find_path(tree, leaf_id, path)
    return reverse_relationship(path) if path else None

# Example usage
root = Tree(3, Tree(1, Tree(2), Tree(6)), Tree(5, None, Tree(4)))
new_root = solution(root, 2)
# new_root is now the new root of the tree with the tree rerooted at the node with x=2
