import unittest
from typing import List


# n = intervals.length
# theoretical lower bound: O(n), each interval must be inspected
class P56:

    # first sort intervals
    # - time complexity: O(n log n)
    # - space complexity: O(n)
    # then in one iteration check ranges and merge if required
    # - time complexity: O(n)
    # - space complexity: O(1)
    #
    # - invariant: after each iteration all elements already processed are in properly merged ranges if applicable
    #
    # Overall
    # - time complexity: O(n log n)
    # - space complexity: O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda a: a[0])

        result_list = []
        current = []

        for interval in sorted_intervals:
            if not current:
                current = interval.copy()
            else:
                if current[1] >= interval[0]:
                    current[1] = max(current[1], interval[1])
                else:
                    result_list.append(current)
                    current = interval.copy()
        if current:
            result_list.append(current)
        return result_list


class Test(unittest.TestCase):
    testcases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[4, 7], [1, 4]], [[1, 7]])
    ]

    def test(self):
        for intervals, expected in self.testcases:
            with self.subTest(intervals):
                result = P56().merge(intervals)
                self.assertEqual(expected, result)
