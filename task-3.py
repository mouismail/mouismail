class Tree:
    def __init__(self, x, l=None, r=None):
        self.x = x
        self.l = l
        self.r = r

def solution(T, leaf_id):
    # Helper function to recursively reroot the tree
    def reroot_rec(node, parent=None):
        if node is None:
            return None
        if node.x == leaf_id:
            return node
        # Recur for the left and right subtrees
        left_child = reroot_rec(node.l, node)
        right_child = reroot_rec(node.r, node)
        # If the new root was found in the left or right subtree
        if left_child:
            node.l = parent
            return node
        if right_child:
            node.r = parent
            return node
        return None

    # Start the rerooting process
    new_root = reroot_rec(T)
    return new_root
