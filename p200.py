import unittest
from typing import List


class P200:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1
                    stack = [(i, j)]
                    grid[i][j] = "0"

                    while stack:
                        x, y = stack.pop()

                        if grid[x + 1][y] == "1":
                            stack.append((x + 1, y))
                        if grid[x][y + 1] == "1":
                            stack.append((x, y + 1))
                        if grid[x - 1][y] == "1":
                            stack.append((x - 1, y))
                        if grid[x][y - 1] == "1":
                            stack.append((x, y - 1))
        return islands


class Test(unittest.TestCase):
    testcases = [
        ([
             ["1", "1", "1", "1", "0"],
             ["1", "1", "0", "1", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]
         ], 1),
        ([
             ["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]
         ], 3)
    ]

    def test(self):
        for grid, expected in self.testcases:
            with self.subTest(grid):
                result = P200().numIslands(grid)
                self.assertEqual(expected, result)
