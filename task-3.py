class Tree:
  """
  This class represents a binary tree node.
  """
  def __init__(self, x, left=None, right=None):
    self.x = x
    self.l = left
    self.r = right

def reroot(node, parent):
    if node is None:
        return parent
    new_root = reroot(node.l, Tree(node.x, node.r, parent))
    node.l = None
    return new_root


def solution(tree, leaf_id):
  """
  This function reroots the tree at the specified leaf node.
  """
  # Helper function to convert tuple to Tree
  def tuple_to_tree(node_tuple):
    if node_tuple is None:
      return None
    return Tree(node_tuple[0], tuple_to_tree(node_tuple[1]), tuple_to_tree(node_tuple[2]))

  # Helper function to find and reroot the tree
  def find_and_reroot(current, parent, leaf_id):
    if current is None:
      return None
    if current.x == leaf_id:
      return reroot(current, parent)
    # Move left subtree up, if the leaf is in the left subtree
    left = find_and_reroot(current.l, Tree(current.x, parent, current.r), leaf_id)
    if left:
      return left
    # Move right subtree up, if the leaf is in the right subtree
    right = find_and_reroot(current.r, Tree(current.x, current.l, parent), leaf_id)
    if right:
      return right
    return None

  tree = tuple_to_tree(tree)
  return find_and_reroot(tree, None, leaf_id)

# Function to print the tree for verification purposes
def print_tree(node, level=0):
    if node is not None:
        print_tree(node.r, level + 1)
        print(' ' * 4 * level + '->', node.x)
        print_tree(node.l, level + 1)

# Convert the tuple to Tree instances
tree_as_tuple = (3, (1, (2, None, None), (6, None, None)), (5, None, (4, None, None)))
leaf_id_to_reroot = 2

# Call the solution function with the tuple representation
new_root = solution(tree_as_tuple, leaf_id_to_reroot)

# Print the rerooted tree
print_tree(new_root)
