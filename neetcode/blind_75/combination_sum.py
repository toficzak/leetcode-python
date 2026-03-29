import unittest
from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path: List[int], total):
            nonlocal result
            if total == target:
                result.append(path[:])
                return
            elif total > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, path, total + nums[i])
                path.pop()

        backtrack(0, [], 0)
        return result


class Test(unittest.TestCase):
    testcases = [
        ([2, 5, 6, 9], 9, [[2, 2, 5], [9]]),
        ([3,4,5], 16, [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]),
        ([3], 5, [])
    ]

    def test(self):
        for nums, target, expected in self.testcases:
            with self.subTest(nums=nums, target=target):
                result = Solution().combinationSum(nums, target)
                self.assertCountEqual(expected, result)
