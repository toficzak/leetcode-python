import unittest
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        visited = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":

                    stack = [(i, j)]
                    while stack:
                        (ni, nj) = stack.pop()
                        visited.append((ni, nj))

                        if (ni + 1, nj) not in visited and ni + 1 < len(grid) and grid[ni + 1][nj] == "1":
                            stack.append((ni + 1, nj))
                        if (ni - 1, nj) not in visited and ni - 1 >= 0 and grid[ni - 1][nj] == "1":
                            stack.append((ni - 1, nj))
                        if (ni, nj + 1) not in visited and nj + 1 < len(grid[0]) and grid[ni][nj + 1] == "1":
                            stack.append((ni, nj + 1))
                        if (ni, nj - 1) not in visited and nj - 1 >= 0 and grid[ni][nj - 1] == "1":
                            stack.append((ni, nj - 1))
                    islands += 1

        return islands


class Test(unittest.TestCase):
    testcases = [
        ([
             ["0", "1", "1", "1", "0"],
             ["0", "1", "0", "1", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]
         ], 1),
        ([
             ["1", "1", "0", "0", "1"],
             ["1", "1", "0", "0", "1"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]
         ], 4)
    ]

    def test(self):
        for grid, expected in self.testcases:
            with self.subTest(grid=grid):
                result = Solution().numIslands(grid)
                self.assertEqual(result, expected)