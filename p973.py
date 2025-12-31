import heapq
import unittest
from typing import List


# theoretical lower bound: O(n), each element must be inspected at least once, each might be important for final answer

# Heap solution
# Use max-heap to decide in O(1) whether element is worth inspecting (is better than heap's root) and if so,
# add it in log(k) and remove worst element in log(k).
# Used heapq so I don't need to implement heap's logic (invariant) by hand.
# - time complexity: O(n log k)
# - space complexity: O(k), for the heap

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return []
        heap = []
        for x, y in points:
            distance = x * x + y * y
            if len(heap) < k:
                heapq.heappush(heap, (-distance, [x, y]))  # -distance to simulate max-heap
            else:
                if heap[0][0] < -distance:
                    heapq.heappushpop(heap, (-distance, [x, y]))
        return [point for _, point in heap]


class Test(unittest.TestCase):
    testcases = [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[-2, 4], [3, 3]]),
        ([], 1, []),
        ([[1, 2]], 0, [])
    ]

    def test_heap(self):
        for points, k, expected in self.testcases:
            with self.subTest(points):
                result = Solution().kClosest(points, k)
                self.assertCountEqual(result, expected)
