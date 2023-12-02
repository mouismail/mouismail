class Tree:
    def __init__(self, x, l=None, r=None):
        self.x = x
        self.l = l
        self.r = r

# Helper function to perform DFS on the tree and find all possible three-digit numbers
def dfs(node, path, all_numbers):
    if node is None:
        return
    # Adding the current node to the path
    new_path = path + [node.x]
    # If the path has three nodes, convert it to a number and add to the set
    if len(new_path) == 3:
        number = int(''.join(map(str, new_path)))
        all_numbers.add(number)
        return
    # Continue the search in the left and right subtrees
    dfs(node.l, new_path, all_numbers)
    dfs(node.r, new_path, all_numbers)

def solution(T):
    # Set to store all unique three-digit numbers
    all_numbers = set()
    # Start DFS from every node
    def start_dfs_from_every_node(node):
        if node is None:
            return
        dfs(node, [], all_numbers)
        start_dfs_from_every_node(node.l)
        start_dfs_from_every_node(node.r)
    
    start_dfs_from_every_node(T)
    # The number of unique three-digit numbers that can be formed
    return len(all_numbers)
