class Tree:
    def __init__(self, x, left=None, right=None):
        self.x = x
        self.l = left
        self.r = right

def solution(T, leaf_id):
    # Convert tuple to Tree
    def tuple_to_tree(t):
        if not t:
            return None
        return Tree(t[0], tuple_to_tree(t[1]), tuple_to_tree(t[2]))

    # Find and reroot the tree
    def find_and_reroot(current, parent):
        if current is None:
            return None
        if current.x == leaf_id:
            return reroot(current, parent)
        # Recurse on left and right subtrees
        left_result = find_and_reroot(current.l, Tree(current.x, None, parent))
        if left_result is not None:
            return left_result
        right_result = find_and_reroot(current.r, Tree(current.x, parent, None))
        return right_result

    # Perform the rerooting
    def reroot(node, parent):
        if node is None:
            return parent
        # The order of the next two lines is changed to first process the right subtree
        right_subtree = reroot(node.r, Tree(node.x, None, parent))
        left_subtree = reroot(node.l, right_subtree)
        node.l = None
        node.r = None
        return left_subtree

    # Convert the input tuple to a Tree
    root = tuple_to_tree(T)
    # Find the leaf and reroot the tree
    return find_and_reroot(root, None)
