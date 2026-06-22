"""
Trie (Prefix Tree) Implementation
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def display(self):
        result = []
        self._display(self.root, "", result)
        return result

    def _display(self, node, prefix, result):
        if node.is_end:
            result.append(prefix)
        for char, child in node.children.items():
            self._display(child, prefix + char, result)


def main():
    trie = Trie()
    words = ["cat", "car", "dog", "door"]

    for w in words:
        trie.insert(w)

    print("All words:", trie.display())
    print("Search 'car':", trie.search("car"))
    print("Search 'ca':", trie.search("ca"))
    print("Starts with 'do':", trie.starts_with("do"))


if __name__ == "__main__":
    main()