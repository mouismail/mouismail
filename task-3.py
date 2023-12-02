class Tree:
    def __init__(self, x, l=None, r=None):
        self.x = x
        self.l = l
        self.r = r

def solution(T, leaf_id):
    # Helper function to recursively reroot the tree
    def reroot_rec(node, parent):
        if node is None:
            return None, None
        if node.x == leaf_id:
            # Make the current node the new root, and its parent a child
            new_root = Tree(node.x)
            if parent:
                # Disconnect the parent from this node
                if parent.l is node:
                    parent.l = None
                else:
                    parent.r = None
                # Recursively continue rerooting with the parent
                left_child, right_child = reroot_rec(parent, None)
                # Add parent as a child to the new root
                new_root.l = left_child
                new_root.r = right_child
            return new_root, None  # Return new root and None for the parent
        else:
            # Recur for the left and right subtrees
            left_child, from_left = reroot_rec(node.l, node)
            right_child, from_right = reroot_rec(node.r, node)
            # If the new root was found in the left or right subtree
            if from_left:
                # Add the current node as a child to the new root
                from_left.r = Tree(node.x, None, right_child if node.l is from_left else left_child)
                return from_left, None
            elif from_right:
                # Add the current node as a child to the new root
                from_right.l = Tree(node.x, left_child if node.r is from_right else right_child, None)
                return from_right, None
            else:
                # Return the current node if the new root is not part of this subtree
                return Tree(node.x, left_child, right_child), None

    # Start the rerooting process
    new_root, _ = reroot_rec(T, None)
    return new_root
