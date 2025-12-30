import unittest
from typing import List


# Binary search
# https://leetcode.com/problems/binary-search/description/

# sorted in asc order
# return target's index or -1
# complexity O(log n)
# all integers unique

# sorted in asc order, search and complexity O(log n) -> binary search

# theoretical lower bound - O(log n) for sorted array using comparisons

# 1) bruteforce
#   perform linear search
#   - time complexity: O(n), too long considering constraint
#   - space complexity: O(1), no additional variables required
#
# 2) binary search - iterative/recursive
#   skip half of the input on each step depending on the middle element of the input
#   - time complexity: O(log n)
#   - space complexity:
#       - iterative: O(1), no additional variables required
#       - recursive: O(log n) - call stack
#
# invariant in iterative version: all elements inside left <= right are possible candidate, all outside this bounds
# are already rejected.

class Solution:
    def search_iterative(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return -1

    def search_recursive(self, nums: List[int], target: int) -> int:
        def helper(left, right):
            if left > right:
                return -1
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                return helper(left, middle - 1)
            else:
                return helper(middle + 1, right)

        return helper(0, len(nums) - 1)


class Test(unittest.TestCase):
    testcases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([], 1, -1),
        ([1], 1, 0)
    ]

    def test_search_imperative(self):
        for input_array, target, expected in self.testcases:
            with self.subTest(input_array):
                result = Solution().search_iterative(input_array, target)
                self.assertEqual(result, expected)

    def test_search_recursive(self):
        for input_array, target, expected in self.testcases:
            with self.subTest(input_array):
                result = Solution().search_recursive(input_array, target)
                self.assertEqual(result, expected)
