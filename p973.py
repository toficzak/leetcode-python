import heapq
import random
import unittest
from typing import List


# theoretical lower bound: O(n), each element must be inspected at least once, each might be important for final answer

# Heap solution
# Use max-heap to decide in O(1) whether element is worth inspecting (is better than heap's root) and if so,
# add it in log(k) and remove worst element in log(k).
# Used heapq so I don't need to implement heap's logic (invariant) by hand.
# - time complexity: O(n log k)
# - space complexity: O(k), for the heap

# Quickselect
# choose random pivot, divide array by it on smaller/bigger, do it until k closest are found
#   - time complexity: avg O(n), worst O(n^2)
#   - space complexity: O(1) - in-place array modification


class Solution:
    def kClosestHeap(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return []
        if len(points) < k:
            return points
        heap = []
        for x, y in points:
            distance = x * x + y * y
            if len(heap) < k:
                heapq.heappush(heap, (-distance, [x, y]))  # -distance to simulate max-heap
            else:
                if heap[0][0] < -distance:
                    heapq.heappushpop(heap, (-distance, [x, y]))
        return [point for _, point in heap]

    def kClosestQuickselect(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == 0 or len(points) == 0:
            return []
        if len(points) < k:
            return points

        def dist(id: int) -> int:
            x, y = points[id]
            return x * x + y * y

        left = 0
        right = len(points) - 1

        while True:
            pivot_id = random.randint(left, right)
            pivot_dist = dist(pivot_id)

            points[pivot_id], points[right] = points[right], points[pivot_id]

            store = left
            for i in range(left, right):
                if dist(i) < pivot_dist:
                    points[i], points[store] = points[store], points[i]
                    store += 1

            points[store], points[right] = points[right], points[store]

            if store == k:
                break
            elif store < k:
                left = store + 1
            else:
                right = store - 1
        return points[:k]


class Test(unittest.TestCase):
    testcases = [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[-2, 4], [3, 3]]),
        ([], 1, []),
        ([[1, 2]], 0, []),
        ([[1, 1], 10, [1, 1]]),
        ([[1, 3], [-2, 2], [5, 8], [0, 1]], 2, [[0, 1], [-2, 2]])
    ]

    def test_heap(self):
        for points, k, expected in self.testcases:
            with self.subTest(points):
                result = Solution().kClosestHeap(points, k)
                self.assertCountEqual(result, expected)

    def test_quickselect(self):
        for points, k, expected in self.testcases:
            with self.subTest(points):
                result = Solution().kClosestQuickselect(points.copy(), k)
                self.assertCountEqual(result, expected)
