import heapq
import unittest
from typing import List


# n = nums.length
# theoretical lower bound: O(n), since each element need to be inspected to find the Kth largest one
class Solution:
    # time complexity: O(n log k)
    # space complexity: O(k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


class Test(unittest.TestCase):
    testcases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)
    ]

    def test(self):
        for nums, k, expected in self.testcases:
            with self.subTest(nums):
                result = Solution().findKthLargest(nums, k)
                self.assertEqual(expected, result)
