import unittest
from typing import List


# n = strs.length
# k = avg str.length
# - theoretical lower bound: O(n), each element needs to be inspected at least once
class P49:
    # pattern: hashing with canonical representation
    # - time complexity: O(n * k), one iteration, cache works with O(1)
    # - space complexity: O(n * 26) = O(n)
    # and cache has max n elements
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for string in strs:
            arr = [0] * 26
            for c in string:
                arr[ord(c) - ord('a')] += 1

            key = tuple(arr)

            if key not in cache:
                cache[key] = []
            cache[key].append(string)
        return list(cache.values())


class Test(unittest.TestCase):
    testcases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["bdddddddddd", "bbbbbbbbbbc"], [["bbbbbbbbbbc"], ["bdddddddddd"]])

    ]

    def test(self):
        for strs, expected in self.testcases:
            with self.subTest(strs):
                result = P49().groupAnagrams(strs)
                expected_sorted = sorted([sorted(group) for group in expected])
                result_sorted = sorted([sorted(group) for group in result])
                self.assertEqual(expected_sorted, result_sorted)
