"""
AVL Tree Implementation
"""


class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        if node is not None:
            node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, old_root):
        new_root = old_root.left
        moved_subtree = new_root.right

        new_root.right = old_root
        old_root.left = moved_subtree

        self._update_height(old_root)
        self._update_height(new_root)

        return new_root

    def _rotate_left(self, old_root):
        new_root = old_root.right
        moved_subtree = new_root.left

        new_root.left = old_root
        old_root.right = moved_subtree

        self._update_height(old_root)
        self._update_height(new_root)

        return new_root

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return AVLNode(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node

        self._update_height(node)

        balance = self._balance_factor(node)

        # LL
        if balance > 1 and value < node.left.value:
            return self._rotate_right(node)

        # RR
        if balance < -1 and value > node.right.value:
            return self._rotate_left(node)

        # LR
        if balance > 1 and value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # RL
        if balance < -1 and value < node.right.value:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)


def main():
    avl = AVLTree()
    for v in [10, 20, 30, 40, 50, 25]:
        avl.insert(v)

    print("Inorder:", avl.inorder(avl.root))


if __name__ == "__main__":
    main()