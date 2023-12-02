class Tree:
    def __init__(self, x):
        self.x = x
        self.l = None
        self.r = None

def reroot(tree, leaf_id):
    # Helper function to perform rerooting
    def reroot_rec(node, parent):
        # If this node is the target leaf, we make it the new root
        # and return it with its parent as a child
        if node.x == leaf_id:
            if parent:
                if parent.l == node:
                    parent.l = None
                else:
                    parent.r = None
                node.l, node.r = reroot_rec(parent, node)
            return node
        # Recursive case: look for the leaf in left and right subtrees
        new_child = None
        if node.l:
            new_child = reroot_rec(node.l, node)
            if new_child:
                node.l = None
        if node.r and not new_child:
            new_child = reroot_rec(node.r, node)
            if new_child:
                node.r = None
        # If we have re-rooted at a child, this node becomes a child
        # of the new root and we return the new root
        if new_child:
            if node == parent.l:
                new_child.r = node
            else:
                new_child.l = node
            return new_child
        # If this node is not part of the path to the leaf, just return it
        return node

    # Call the recursive function with the original root
    return reroot_rec(tree, None)

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
