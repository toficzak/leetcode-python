import unittest
from typing import List


# - theoretical lower bound: O(n), because each element needs to be inspected at least once
class P26:
    """
    two pointer approach
    - time complexity: O(n)
        - one iteration with right pointer
    - space complexity: O(1)
        - just helper variables
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right - 1] != nums[right]:
                nums[left] = nums[right]
                left += 1
        return left

    """
    set solution - violates in-memory change
    - time complexity: O(n)
        - worst case: two iterations
    - space complexity: O(n)
        - set
    """

    def removeDuplicates_set(self, nums: List[int]) -> int:
        cache = set()  # keeps insertion order

        for num in nums:
            cache.add(num)

        for id, num in enumerate(cache):
            nums[id] = num

        return len(cache)


class Test(unittest.TestCase):
    testcases = [
        ([1, 1], 1),
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5)
    ]

    def test(self):
        for nums, expected in self.testcases:
            with self.subTest(nums):
                result = P26().removeDuplicates(nums.copy())
                self.assertEqual(expected, result)

    def test_set(self):
        for nums, expected in self.testcases:
            with self.subTest(nums):
                result = P26().removeDuplicates_set(nums.copy())
                self.assertEqual(expected, result)
