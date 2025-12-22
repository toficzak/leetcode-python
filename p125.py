import unittest


# theoretical lower bound -> O(n), each element of the array must be inspected at least once

# short-circuit the logic - can I quickly say yes/no?
# - no visible at first

# bruteforce approach
# -
# first sanitize the input, create a list, add each element to the list until middle point
# then just check if remaining letters are the same as those in the list
# time complexity: O(n)
# space complexity: O(n)

# two-pointers approach
# -
# pointer left, pointer right, until left is smaller than right, check if referenced letters are the same
# and move to the next letter ignoring non-letter characters
# time complexity: O(n)
# space complexity: O(1)

class Solution:
    def is_palindrome_bruteforce(self, s: str) -> bool:
        sanitized = [c.lower() for c in s if c.isalpha()]
        return sanitized == sanitized[::-1]

    def is_palindrome_two_pointers(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while not s[left].isalpha() and left < right:
                left += 1
            while not s[right].isalpha() and right > left:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True


class Test(unittest.TestCase):
    testcases = [
        ("aaaa", True),
        ("aab", False),
        ("kaj,ak", True),
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("..._", True)
    ]

    def test_bruteforce(self):
        for text, expected in self.testcases:
            with self.subTest(text):
                self.assertEqual(Solution().is_palindrome_bruteforce(text), expected)

    def test_two_pointers(self):
        for text, expected in self.testcases:
            with self.subTest(text):
                self.assertEqual(Solution().is_palindrome_two_pointers(text), expected)
