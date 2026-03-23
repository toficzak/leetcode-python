import unittest

from neetcode.blind_75.TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


class Test(unittest.TestCase):
    testcases = [
        (
            TreeNode(5,
                     TreeNode(3,
                              TreeNode(1,
                                       None,
                                       TreeNode(2)),
                              TreeNode(4)),
                     TreeNode(8,
                              TreeNode(7),
                              TreeNode(9)),
                     ),
            TreeNode(3),
            TreeNode(8),
            TreeNode(5)
        ),
        (
            TreeNode(5,
                     TreeNode(3,
                              TreeNode(1,
                                       None,
                                       TreeNode(2)),
                              TreeNode(4)),
                     TreeNode(8,
                              TreeNode(7),
                              TreeNode(9)),
                     ),
            TreeNode(3),
            TreeNode(4),
            TreeNode(3)
        )
    ]

    def test(self):
        for root, p, q, expected in self.testcases:
            with self.subTest(root=root, p=p, q=q):
                result = Solution().lowestCommonAncestor(root, p, q)
                self.assertEqual(expected.val, result.val)
