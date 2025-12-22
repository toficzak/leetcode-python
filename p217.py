import unittest
from typing import List


# list has duplicates if any value appears more than once

# Time complexity: O(n^2)
# Space complexity: O(1)
class BruteforceSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                print(f"Testing pair: {i}, {j}")
                if nums[i] == nums[j]:
                    return True
        return False


# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memory = set()

        for num in nums:
            if num in memory:
                return True
            memory.add(num)
        return False


class Test(unittest.TestCase):
    def test_contain_duplicates_bruteforce(self):
        testcases = [
            ([1, 2, 3, 1], True),
            ([3, 4, 5, 6], False),
            ([4], False),
            ([0, 0], True)
        ]

        for array, expectedResult in testcases:
            with self.subTest(array=array):
                self.assertEqual(BruteforceSolution().containsDuplicate(array), expectedResult)

    def test_contain_duplicates_with_set(self):
        testcases = [
            ([1, 2, 3, 1], True),
            ([3, 4, 5, 6], False),
            ([4], False),
            ([0, 0], True),
            ([], False)
        ]

        for array, expectedResult in testcases:
            with self.subTest(array=array):
                self.assertEqual(Solution().containsDuplicate(array), expectedResult)
