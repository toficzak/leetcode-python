import unittest
from typing import List


# - theoretical lower bound: O(n), each element must be inspected at least once
class Solution:

    # bruteforce - pairwise comparison
    # - time complexity: O(n^2), two for loops on one structure
    # - space complexity: O(1), no additional structures
    def bruteforce(self, height: List[int]) -> int:
        max_area = 0
        for i in range(0, len(height)):
            for j in range(i + 1, len(height)):
                max_area = max(max_area, min(height[i], height[j]) * (j - i))
        return max_area

    # two-pointers solution
    # - time complexity: O(n), one sweep
    # - space complexity: O(1), no additional structures required
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        max_area = 0

        while left < right:
            min_height = min(height[left], height[right])
            max_area = max(max_area, min_height * (right - left))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area


class Test(unittest.TestCase):
    testcases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([0, 1], 0)
    ]

    def test_bruteforce(self):
        for height, expected in self.testcases:
            with self.subTest(height):
                result = Solution().bruteforce(height)
                self.assertEqual(expected, result)

    def test(self):
        for height, expected in self.testcases:
            with self.subTest(height):
                result = Solution().maxArea(height)
                self.assertEqual(expected, result)
