import unittest


class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return -1 if dp[amount] == float('inf') else dp[amount]


class Test(unittest.TestCase):
    testcases = [
        ([1, 5, 10], 12, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 100, 10),
        ([1, 5, 10, 25], 9999, 405)
    ]

    def test(self):
        for coins, amount, expected in self.testcases:
            with self.subTest(coins=coins, amount=amount):
                result = Solution().coinChange(coins, amount)
                self.assertEqual(expected, result)
