class Tree:
    def __init__(self, x):
        self.x = x
        self.l = None
        self.r = None

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
            return new_root, parent
        else:
            # Recur for the left and right subtrees
            left_child, from_left = reroot_rec(node.l, node)
            right_child, from_right = reroot_rec(node.r, node)
            # If the new root was found in the left or right subtree
            if from_left or from_right:
                # Add the current node as a child to the new root
                if from_left:
                    from_left.r = Tree(node.x, right_child, None)
                else:
                    from_left.l = Tree(node.x, None, left_child)
                return from_left, node
            else:
                # Return the current node if the new root is not part of this subtree
                return Tree(node.x, left_child, right_child), None
    
    # Start the rerooting process
    new_root, _ = reroot_rec(T, None)
    return new_root

# Create a binary tree as per the provided structure
# The structure is as follows:
#       3
#      / \
#     1   5
#    /   / \
#   2   6   4

# Create nodes
n1 = Tree(1)
n2 = Tree(2)
n3 = Tree(3)
n4 = Tree(4)
n5 = Tree(5)
n6 = Tree(6)

# Connect nodes
n3.l = n1
n3.r = n5
n1.l = n2
n5.l = n6
n5.r = n4

# Now, if we call reroot with n3 as the root and 2 as the new root id,
# it should return the tree rooted at 2
rerooted_tree = reroot(n3, 2)

# For validation purposes, let's write a function to print the tree
def print_tree(node, level=0):
    if node is not None:
        print_tree(node.r, level + 1)
        print(' ' * 4 * level + '->', node.x)
        print_tree(node.l, level + 1)

# Print the rerooted tree
print_tree(rerooted_tree)
