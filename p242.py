# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        array1 = self._find_frequencies(s)
        array2 = self._find_frequencies(t)

        # print(array1)
        # print(array2)

        return array1 == array2

    def _find_frequencies(self, word):
        array = [0] * 26
        for char in word:
            array[ord(char) - 97] += 1
        return array


if __name__ == '__main__':
    testcases = [
        # ("a", "b"),
        ("anagram", "nagaram"),
        ("rat", "car")
    ]

    for testcase in testcases:
        print(Solution().isAnagram(testcase[0], testcase[1]))
