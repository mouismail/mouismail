class Tree:
  """
  This class represents a binary tree node.
  """
  def __init__(self, x, l=None, r=None):
    self.x = x
    self.l = l
    self.r = r

def reroot(node, parent):
  if node is None:
    return parent
  new_node = reroot(node.l, Tree(node.x, node.r, parent))
  node.l = None
  return new_node

def solution(tree, leaf_id):
  """
  This function reroots the tree at the specified leaf node.
  """
  def find_and_reroot(current, parent, leaf_id):
    if current is None:
      return None
    if current.x == leaf_id:
      return reroot(current, parent)
    left = find_and_reroot(current.l, Tree(current.x, parent, current.r), leaf_id)
    if left:
      return left
    right = find_and_reroot(current.r, Tree(current.x, current.l, parent), leaf_id)
    if right:
      return right
    return None

  return find_and_reroot(tree, None, leaf_id)

# Function to print the tree for verification purposes
def print_tree(node, level=0):
  if node is not None:
    print_tree(node.r, level + 1)
    print(' ' * 4 * level + '->', node.x)
    print_tree(node.l, level + 1)

# Create the tree using Tree instances
tree = Tree(3, Tree(1, Tree(2), Tree(6)), Tree(5, None, Tree(4)))
leaf_id_to_reroot = 2

# Call the solution function with the Tree instance
new_root = solution(tree, leaf_id_to_reroot)

# Print the rerooted tree
print_tree(new_root)
