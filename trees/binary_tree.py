"""
Binary Tree Implementation
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self, node):
        if node is None:
            return []
        return [node.value] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.value]

    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))


def main():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.right = Node(15)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(7)

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))
    print("Height:", tree.height(tree.root))


if __name__ == "__main__":
    main()