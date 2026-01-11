import unittest
from typing import List


# - theoretical lower bound: O(n), each element needs to be checked at least once
class P1:
    # time complexity:  O(n^2)
    # space complexity: O(1)
    def two_sum_bruteforce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    #
    # (desired value -> index of previously met number)
    # then complexity should be O(n), but memory would rise to O(n), cause I would
    # allocate at worst same array as input

    # time complexity:  O(n)
    # space complexity: O(n)
    def two_sum_hashmap(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, c in enumerate(nums):
            remaining = target - c
            if c in cache:
                return [cache[c], i]
            cache[remaining] = i
        return []


class P1Test(unittest.TestCase):
    testcases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]

    def test_bruteforce(self):
        for nums, target, expected in self.testcases:
            with self.subTest(nums):
                result = P1().two_sum_bruteforce(nums, target)
                self.assertEqual(expected, result)

    def test_hashmap(self):
        for nums, target, expected in self.testcases:
            with self.subTest(nums):
                result = P1().two_sum_hashmap(nums, target)
                self.assertEqual(expected, result)
