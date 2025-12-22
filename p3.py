import unittest


# theoretical lower bound is O(n), since each element must be inspected at least once
#
# 1) brute force - generate all substrings, for those with no repeating characters - keep max length
#   - time complexity: O(n^2)
#   - space complexity: O(1)
#
# 2) sliding window - keep state of valid substring, in case of repeated character remove chars from left pointer until valid
#    trade-off: space for time
#   - time complexity: O(n)
#   - space complexity: O(n) - in case input has no repeating chars


class Solution:
    def lengthOfLongestSubstringBruteforce(self, s: str) -> int:
        longest_substring = 0

        for index in range(len(s)):
            for i in range(index + 1, len(s) + 1):
                substring = s[index:i]
                if len(set(substring)) == len(substring):
                    longest_substring = max(longest_substring, len(substring))
                else:
                    # one repeating character is enough to break all other answers
                    break
        return longest_substring

    def lengthOfLongestSubstringWindow(self, s: str) -> int:

        if len(s) < 2:
            return len(s)

        longest_substring = 0
        state = set()
        left = 0
        right = 0

        while right < len(s):
            new_value = s[right]
            while new_value in state:
                state.remove(s[left])
                left += 1
            state.add(new_value)
            longest_substring = max(longest_substring, right - left + 1)
            right += 1

        return longest_substring

    def lengthOfLongestSubstringWindowCanonical(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            longest = max(longest, right - left + 1)

        return longest


class Test(unittest.TestCase):
    testcases = [
        ("abc", 3),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("abba", 2)
    ]

    def test_bruteforce(self):
        for input, expected in self.testcases:
            with self.subTest(input):
                self.assertEqual(Solution().lengthOfLongestSubstringBruteforce(input), expected)

    def test_window(self):
        for input, expected in self.testcases:
            with self.subTest(input):
                self.assertEqual(Solution().lengthOfLongestSubstringWindow(input), expected)

    def test_window_canonical(self):
        for input, expected in self.testcases:
            with self.subTest(input):
                self.assertEqual(Solution().lengthOfLongestSubstringWindowCanonical(input), expected)
