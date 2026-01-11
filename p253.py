import unittest
from typing import List

from Interval import Interval


class P253:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        start_times = sorted([interval.start for interval in intervals])
        end_times = sorted([interval.end for interval in intervals])

        current_meetings = 0
        max_meetings = 0

        end = 0

        for start in start_times:
            while end < len(end_times) and start >= end_times[end]:
                current_meetings -= 1
                end += 1

            current_meetings += 1
            max_meetings = max(max_meetings, current_meetings)

        return max_meetings


class Test(unittest.TestCase):
    testcases = [
        ([Interval(0, 40), Interval(5, 10), Interval(15, 20)], 2),
        ([
             Interval(1, 2),
             Interval(3, 4),
             Interval(5, 6),
             Interval(7, 8),
             Interval(2, 10)
         ], 2),
        ([Interval(4, 9)], 1),
        (
            [
                Interval(0, 10),
                Interval(1, 9),
                Interval(2, 8),
                Interval(3, 7),
                Interval(4, 6)
            ],
            5
        ),
        (
            [
                Interval(0, 5),
                Interval(5, 10),
                Interval(10, 15),
                Interval(15, 20)
            ],
            1
        ),
        (
            [
                Interval(0, 30),
                Interval(5, 10),
                Interval(15, 20),
                Interval(6, 25),
                Interval(20, 35),
                Interval(28, 40)
            ],
            3
        ),
        (
            [],
            0
        )
    ]

    def test(self):
        for intervals, expected in self.testcases:
            with self.subTest(intervals):
                result = P253().minMeetingRooms(intervals)
                self.assertEqual(expected, result)
