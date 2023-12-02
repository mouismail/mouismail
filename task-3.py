class Tree:
    def __init__(self, x, l=None, r=None):
        self.x = x
        self.l = l
        self.r = r

def solution(T, leaf_id):
    # Helper function to recursively find the leaf node and its parents
    def find_leaf_and_parents(node, parent=None):
        if node is None:
            return None, []
        if node.x == leaf_id:
            return node, [parent]
        # Recur for the left and right subtrees
        left_leaf, left_parents = find_leaf_and_parents(node.l, node)
        if left_leaf:
            return left_leaf, [parent] + left_parents
        right_leaf, right_parents = find_leaf_and_parents(node.r, node)
        if right_leaf:
            return right_leaf, [parent] + right_parents
        return None, []

    # Find the leaf node and its parents
    leaf_node, parents = find_leaf_and_parents(T)
    # Reroot the tree by reversing the parent-child relationship
    for i in range(len(parents) - 1):
        if parents[i].l is parents[i + 1]:
            parents[i].l = parents[i - 1] if i > 0 else None
        else:
            parents[i].r = parents[i - 1] if i > 0 else None
    if parents[-1].l is leaf_node:
        parents[-1].l = parents[-2] if len(parents) > 1 else None
    else:
        parents[-1].r = parents[-2] if len(parents) > 1 else None
    leaf_node.l = leaf_node.r = None
    leaf_node.l = parents[0] if parents else None
    return leaf_node
