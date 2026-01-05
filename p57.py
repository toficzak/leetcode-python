import unittest
from typing import List


# n = intervals.length
# - theoretical lower bound: O(n), since all intervals need to be checked at least once, worst case is new interval
# spreading across all old intervals
class P57:
    # Interval Insertion Pattern, add intervals up to the new interval, then perform merge and add all that remain
    # Overall
    # - time complexity: O(n)
    # - space complexity: O(n)

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        start, end = newInterval
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        result.append([start, end])

        while i < n:
            result.append(intervals[i])
            i += 1

        return result


class Test(unittest.TestCase):
    testcases = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]])
    ]

    def test(self):
        for intervals, new_intervals, expected in self.testcases:
            with self.subTest(intervals):
                result = P57().insert(intervals, new_intervals)
                self.assertEqual(expected, result)
