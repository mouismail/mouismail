class Tree:
    def __init__(self, x, left=None, right=None):
        self.x = x
        self.l = left
        self.r = right

def reroot(tree, parent):
    if tree is None:
        return parent
    
    left_subtree = reroot(tree.l, Tree(tree.x, None, parent))
    right_subtree = reroot(tree.r, left_subtree)
    
    tree.l = None
    tree.r = None
    
    return right_subtree

def solution(T, leaf_id):
    # Helper function to find the leaf node to reroot the tree
    def find_leaf_and_reroot(current, parent):
        if current is None:
            return None
        if current.x == leaf_id:
            return reroot(current, parent)
        left_result = find_leaf_and_reroot(current.l, Tree(current.x, None, parent))
        if left_result is not None:
            return left_result
        right_result = find_leaf_and_reroot(current.r, Tree(current.x, parent, None))
        return right_result
    
    return find_leaf_and_reroot(T, None)
