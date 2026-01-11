import unittest
from typing import List

from Interval import Interval


# n = intervals.length
# - theoretical lower bound: O(n), each interval must be inspected at least once
class P252:
    # - time complexity: O(n log n), sorting and then one loop iteration
    # - space complexity: O(n) due to sorting
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        last_end = sorted_intervals[0].end
        for interval in sorted_intervals[1:]:
            if interval.start < last_end:
                return False
            last_end = interval.end
        return True


class Test(unittest.TestCase):
    testcases = [
        ([], True),
        ([Interval(10, 8), Interval(9, 15)], False),
        ([Interval(0, 30), Interval(5, 10), Interval(15, 20)], False),
        ([Interval(5, 8), Interval(9, 15)], True)
    ]

    def test(self):
        for intervals, expected in self.testcases:
            with self.subTest(intervals):
                result = P252().canAttendMeetings(intervals)
                self.assertEqual(expected, result)
