class Tree:
    def __init__(self, x, left=None, right=None):
        self.x = x
        self.l = left
        self.r = right

def solution(T, leaf_id):
    # Base case: if the current node is null, return null.
    if T is None:
        return None, None

    # If the current node is the leaf we want to reroot at
    if T.x == leaf_id:
        # This node will be the new root, so its parent will be None
        return T, None

    # Recursively reroot left and right subtrees
    left_subtree, from_left = solution(T.l, leaf_id)
    right_subtree, from_right = solution(T.r, leaf_id)

    # If the leaf was found and returned from the left subtree
    if from_left:
        # The current node's left subtree becomes the one that was originally on the right
        from_left.r = T.r
        # The current node becomes the right subtree of the leaf
        T.r = None  # Disconnect the current node from its parent
        T.l = right_subtree  # The original right subtree becomes the new left subtree
        from_left.l = T
        return from_left, T

    # Similarly, if the leaf was found and returned from the right subtree
    if from_right:
        # The current node's right subtree becomes the one that was originally on the left
        from_right.l = T.l
        # The current node becomes the left subtree of the leaf
        T.l = None  # Disconnect the current node from its parent
        T.r = left_subtree  # The original left subtree becomes the new right subtree
        from_right.r = T
        return from_right, T

    # If the leaf has not been found yet, return the current node and its subtrees as they are
    T.l = left_subtree
    T.r = right_subtree
    return T, None

# Function to print the tree for checking the rerooted structure
def print_tree(T, indent=0):
    if T is not None:
        print(' ' * indent + str(T.x))
        print_tree(T.l, indent + 4)
        print_tree(T.r, indent + 4)


