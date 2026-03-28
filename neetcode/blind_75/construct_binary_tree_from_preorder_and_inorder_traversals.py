import unittest
from typing import List, Optional

from neetcode.blind_75.TreeNode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {value: index for index, value in enumerate(inorder)}
        preorder_index = 0

        def helper(left, right):
            nonlocal preorder_index
            if left > right:
                return None

            root_val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode(root_val)

            mid = index_map[root_val]
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)



class Test(unittest.TestCase):
    testcases = [
        (
            [1, 2, 3, 4],
            [2, 1, 3, 4],
            TreeNode(1,
                     TreeNode(2),
                     TreeNode(3,
                              None,
                              TreeNode(4)))
        )
    ]

    def test(self):
        for preorder, inorder, expected in self.testcases:
            with self.subTest(preorder=preorder, inorder=inorder):
                result = Solution().buildTree(preorder, inorder)
                self.assertEqual(expected.getValueAsArray(), result.getValueAsArray())
