import unittest


class PrefixTree:
    class Node:
        def __init__(self):
            self.map = {}
            self.end = False

    def __init__(self):
        self.root = PrefixTree.Node()

    def insert(self, word: str) -> None:
        current_node = self.root

        for w in word:
            if w not in current_node.map:
                current_node.map[w] = PrefixTree.Node()
            current_node = current_node.map[w]
        current_node.end = True

    def search(self, word: str) -> bool:
        current_node = self.root

        for w in word:
            if w not in current_node.map:
                return False
            current_node = current_node.map[w]

        return current_node.end

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root

        for w in prefix:
            if w not in current_node.map:
                return False
            current_node = current_node.map[w]
        return True


class Test(unittest.TestCase):

    def test(self):
        prefixTree = PrefixTree()
        prefixTree.insert("dog")
        self.assertTrue(prefixTree.search("dog"))
        self.assertFalse(prefixTree.search("do"))
        self.assertTrue(prefixTree.startsWith("do"))
        prefixTree.insert("do")
        self.assertTrue(prefixTree.search("do"))