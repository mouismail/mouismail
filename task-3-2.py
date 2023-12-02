class Tree:
  """
  This class represents a binary tree node.
  """
  def __init__(self, x, l=None, r=None):
    self.x = x
    self.l = l
    self.r = r

def reroot(node, parent):
    # Base case: if the current node is None, return the parent node.
    if node is None:
        return parent
    # Recursively call reroot on the left child, passing in the current node modified to have
    # its right child as the left child and the parent as the right child.
    left_rerooted = reroot(node.l, Tree(node.x, node.r, parent))
    # After rerooting the left subtree, set the current node's left child to None.
    node.l = None
    # The left child of the rerooted subtree becomes the new rerooted subtree.
    node.r = None
    return left_rerooted

def find_and_reroot(current, parent, leaf_id):
    # If the current node is None, return None.
    if current is None:
        return None
    # If the current node is the one we want to reroot at, call reroot.
    if current.x == leaf_id:
        return reroot(current, parent)
    # Recursively search the left subtree for the leaf_id. If found, the left subtree will be rerooted.
    left = find_and_reroot(current.l, Tree(current.x, parent, current.r), leaf_id)
    if left:
        current.l = None  # Detach the left subtree after it's been rerooted.
        return left
    # Recursively search the right subtree for the leaf_id. If found, the right subtree will be rerooted.
    right = find_and_reroot(current.r, Tree(current.x, current.l, parent), leaf_id)
    if right:
        current.r = None  # Detach the right subtree after it's been rerooted.
        return right
    return None

def solution(tree, leaf_id):
    # Call the find_and_reroot function on the tree to start the rerooting process.
    return find_and_reroot(tree, None, leaf_id)



# Function to print the tree for verification purposes
def print_tree(node, level=0):
  if node is not None:
    print_tree(node.r, level + 1)
    print(' ' * 4 * level + '->', node.x)
    print_tree(node.l, level + 1)

# Create the tree using Tree instances
# Testing the function
tree = Tree(3, Tree(1, Tree(2), Tree(6)), Tree(5, None, Tree(4)))
leaf_id_to_reroot = 2
new_root = solution(tree, leaf_id_to_reroot)
print_tree(new_root)
