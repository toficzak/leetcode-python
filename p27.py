import unittest
from typing import List


# n = nums.length
# - theoretical lower bound: O(n)
class P27:
    """
    two pointer

    - time complexity: O(n)
    - space complexity: O(1)
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left

    """
    two pointer

    - time complexity: O(n)
    - space complexity: O(1)
    """
    def removeElement_swap(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1

        return n


class Test(unittest.TestCase):
    testcases = [
        ([], 2, 0),
        ([3, 2, 2, 3], 3, 2),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5)
    ]

    def test(self):
        for nums, val, expected in self.testcases:
            with self.subTest(nums):
                nums_copy = nums.copy()
                original_nums = nums.copy()
                result = P27().removeElement(nums_copy, val)
                self.assertEqual(expected, result)
                self.assertCountEqual(
                    nums_copy[:result],
                    [x for x in original_nums if x != val]
                )

    def test_swap(self):
        for nums, val, expected in self.testcases:
            with self.subTest(nums):
                nums_copy = nums.copy()
                original_nums = nums.copy()
                result = P27().removeElement_swap(nums_copy, val)
                self.assertEqual(expected, result)
                self.assertCountEqual(
                    nums_copy[:result],
                    [x for x in original_nums if x != val]
                )
