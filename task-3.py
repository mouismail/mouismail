from extratypes import Tree  # Import the Tree class from extratypes module

def invertTree(self, root):
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        if node:
            node.left, node.right = node.right, node.left
            q.append(node.left)
            q.append(node.right)
    return root
