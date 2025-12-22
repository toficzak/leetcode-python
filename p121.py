import unittest
from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price_so_far = prices[0]
#         max_profit = 0
#
#         for price in prices:
#             profit = price - min_price_so_far
#             max_profit = max(max_profit, profit)
#             min_price_so_far = min(min_price_so_far, price)
#
#         return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0

        for price in prices:
            current_profit = price - lowest_price
            max_profit = max(max_profit, current_profit)
            lowest_price = min(lowest_price, price)

        return max_profit

class Test(unittest.TestCase):
    testcases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0)
    ]

    def test(self):
        for prices, expected in self.testcases:
            with self.subTest(prices):
                result = Solution().maxProfit(prices)
                self.assertEqual(result, expected)
