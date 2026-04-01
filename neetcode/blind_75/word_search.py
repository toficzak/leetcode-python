import unittest
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows_len, cols_len = len(board), len(board[0])
        visited = set()

        def dfs(row, col, i):
            if (row, col) in visited:
                return False

            if i == len(word):
                return True

            if row < 0 or row >= rows_len or col < 0 or col >= cols_len or board[row][col] != word[i]:
                return False

            visited.add((row, col))

            found = (
                    dfs(row + 1, col, i + 1) or
                    dfs(row - 1, col, i + 1) or
                    dfs(row, col + 1, i + 1) or
                    dfs(row, col - 1, i + 1)
            )
            visited.remove((row, col))
            return found

        for row in range(rows_len):
            for col in range(cols_len):
                if dfs(row, col, 0):
                    return True
        return False


class Test(unittest.TestCase):
    testcases = [
        ([
             ["A", "B", "C", "D"],
             ["S", "A", "A", "T"],
             ["A", "C", "A", "E"]
         ],
         "CAT",
         True
        ),
        (
            [
                ["A", "B", "C", "D"],
                ["S", "A", "A", "T"],
                ["A", "C", "A", "E"]
            ],
            "BAT",
            False
        )
    ]

    def test(self):
        for board, word, expected in self.testcases:
            with self.subTest(word=word):
                result = Solution().exist(board, word)
                self.assertEqual(expected, result)
