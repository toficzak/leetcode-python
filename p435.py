import unittest
from typing import List

# n = intervals.length
# - theoretical lower bound: O(n), cause each element needs to be inspected at least once
class P435:
    # - time complexity: O(n log n) - sort and one time iteration
    # - space complexity: O(n) - sorting

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x[1])

        last = sorted_intervals[0]
        saved = 1

        for interval in sorted_intervals[1:]:
            if interval[0] >= last[1]:
                saved += 1
                last = interval

        return len(intervals) - saved


class Test(unittest.TestCase):
    testcases = [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0)
    ]

    def test(self):
        for intervals, expected in self.testcases:
            with self.subTest(intervals):
                result = P435().eraseOverlapIntervals(intervals)
                self.assertEqual(expected, result)
