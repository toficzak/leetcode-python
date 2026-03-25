import unittest
from math import inf
from typing import Optional

from neetcode.blind_75.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, (-inf, inf))]

        while stack:
            node, (min, max) = stack.pop()

            if node.val <= min or node.val >= max:
                return False

            if node.left:
                stack.append((node.left, (min, node.val)))
            if node.right:
                stack.append((node.right, (node.val, max)))
        return True


class Test(unittest.TestCase):
    testcases = [
        (TreeNode(2, TreeNode(1), TreeNode(3)), True),
        (TreeNode(1, TreeNode(2), TreeNode(3)), False),
        (TreeNode(2, TreeNode(2), TreeNode(2)), False)
    ]

    def test(self):
        for root, expected in self.testcases:
            with self.subTest(root=root):
                result = Solution().isValidBST(root)
                self.assertEqual(expected, result)
