import unittest
from typing import List


# m, n = grid sides' lengths
#
# - theoretical lower bound: O(m * n), since each element needs to be inspected at least once
class P695:
    # pattern: DFS
    # - time complexity: O(m * n),
    #   outer loop checks each element, each "1" is pushed and pop'ed from stack exactly once, each pop generates O(4)
    #   checks in each direction
    # - space complexity: O(m * n) - worst case: whole grid is one big island, so it will all be on stack
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:

                    stack = [(i, j)]
                    area = 0

                    while stack:
                        area += 1
                        cx, cy = stack.pop()
                        grid[cx][cy] = 0

                        for dx, dy in dirs:
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                                stack.append((nx, ny))
                                grid[nx][ny] = 0
                    max_area = max(max_area, area)
        return max_area


class Test(unittest.TestCase):
    testcases = \
        [
            ([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]], 6),
            ([[0, 0, 0, 0, 0, 0, 0, 0]], 0),
            ([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]], 4)
        ]

    def test(self):
        for grid, expected in self.testcases:
            with self.subTest(grid):
                result = P695().maxAreaOfIsland(grid)
                self.assertEqual(expected, result)
