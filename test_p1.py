import unittest

from p1 import two_sum


class MyTestCase(unittest.TestCase):
    def test_two_sum(self):
        assert two_sum([2, 7, 11, 15], 9) == [0, 1]
        assert two_sum([3, 2, 4], 6) == [1, 2]
        assert two_sum([3, 3], 6) == [0, 1]


if __name__ == '__main__':
    unittest.main()
