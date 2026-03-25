import unittest
from typing import Optional

from neetcode.blind_75.TreeNode import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0

        def dfs(root: TreeNode, target):
            nonlocal counter
            if root.left:
                result = dfs(root.left, target)
                if result is not None:
                    return result

            counter += 1
            if counter == target:
                return root.val

            if root.right:
                result = dfs(root.right, target)
                if result is not None:
                    return result
            return None

        return dfs(root, k)


class Test(unittest.TestCase):
    testcases = [
        (TreeNode(2,
                  TreeNode(1),
                  TreeNode(3)),
         1,
         1),
        (TreeNode(4,
                  TreeNode(3,
                           TreeNode(2)),
                  TreeNode(5)),
         4,
         5),
        (TreeNode(2,
                  TreeNode(1,
                           TreeNode(0),
                           TreeNode(-3)),
                  TreeNode(3,
                           None,
                           TreeNode(10))),
         6,
         10)
    ]

    def test(self):
        for root, k, expected in self.testcases:
            with self.subTest(root=root, k=k):
                result = Solution().kthSmallest(root, k)
                self.assertEqual(expected, result)
