def solution(tree, leaf_id):
    def find_path(node, path):
        if node is None:
            return False
        path.append(node)
        if node.x == leaf_id:
            return True
        if find_path(node.l, path) or find_path(node.r, path):
            return True
        path.pop()
        return False

    path = []
    find_path(tree, path)

    for i in range(len(path) - 1, 0, -1):
        current_node = path[i]
        parent_node = path[i - 1]
        # Swap children and parent
        if parent_node.l == current_node:
            parent_node.l = parent_node.r
            parent_node.r = None
        else:
            parent_node.r = parent_node.l
            parent_node.l = None

        if current_node.l is None:
            current_node.l = parent_node
        else:
            current_node.r = parent_node

    # The last node in the path is the new root
    if path:
        path[-1].l = path[-1].r = None
        return path[-1]
