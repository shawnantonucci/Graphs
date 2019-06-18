class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def earliest_ancestor(root, n1, n2):
    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left_ancestor = earliest_ancestor(root.left, n1, n2)
    right_ancestor = earliest_ancestor(root.right, n1, n2)

    if left_ancestor and right_ancestor:
        return root

    return left_ancestor if left_ancestor is not None else right_ancestor


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(earliest_ancestor(root, 4, 5).key)
print(earliest_ancestor(root, 4, 6).key)
print(earliest_ancestor(root, 3, 4).key)
print(earliest_ancestor(root, 2, 4).key)
