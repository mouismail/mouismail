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
        new_root = path[-1]
        for i in range(len(path) - 1, 0, -1):
            current = path[i]
            parent = path[i - 1]

            # Determine if current is left or right child of parent
            if parent.l == current:
                parent.l = None
                # Move parent's right subtree to current's left if it's empty
                if current.l is None:
                    current.l = parent.r
                else:
                    # Find the rightmost node of current's left subtree
                    rightmost = current.l
                    while rightmost.r is not None:
                        rightmost = rightmost.r
                    rightmost.r = parent.r
                parent.r = current
            elif parent.r == current:
                parent.r = None
                # Move parent's left subtree to current's right if it's empty
                if current.r is None:
                    current.r = parent.l
                else:
                    # Find the leftmost node of current's right subtree
                    leftmost = current.r
                    while leftmost.l is not None:
                        leftmost = leftmost.l
                    leftmost.l = parent.l
                parent.l = current

        return new_root

    path = []
    find_path(tree, leaf_id, path)
    return reverse_relationship(path) if path else None

# Example usage
root = Tree(3, Tree(1, Tree(2), Tree(6)), Tree(5, None, Tree(4)))
new_root = solution(root, 2)
