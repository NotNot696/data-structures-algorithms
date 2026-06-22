"""
Binary Search Tree Implementation
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        return node

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node is not None

        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)


def main():
    bst = BST()
    values = [10, 5, 15, 3, 7, 20]

    for v in values:
        bst.insert(v)

    print("Inorder:", bst.inorder(bst.root))
    print("Search 7:", bst.search(7))
    print("Search 99:", bst.search(99))


if __name__ == "__main__":
    main()