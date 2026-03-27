import unittest


class WordDictionary:
    class Node:
        def __init__(self):
            self.map = {}
            self.end = False

    def __init__(self):
        self.root = WordDictionary.Node()

    def addWord(self, word: str) -> None:
        current_node = self.root

        for w in word:
            if w not in current_node.map:
                current_node.map[w] = WordDictionary.Node()
            current_node = current_node.map[w]
        current_node.end = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: WordDictionary.Node) -> bool:
            if index == len(word):
                return node.end

            char = word[index]

            if char == ".":
                for child in node.map.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if char not in node.map:
                    return False
                return dfs(index + 1, node.map[char])

        return dfs(0, self.root)


class Test(unittest.TestCase):

    def test(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("day")
        wordDictionary.addWord("bay")
        wordDictionary.addWord("may")
        self.assertFalse(wordDictionary.search("say"))

        words = [
            "day",
            ".ay",
            "b.."
        ]

        for word in words:
            with self.subTest(word = word):
                self.assertTrue(wordDictionary.search(word))
