import unittest
from collections import deque
from typing import Optional, List

from neetcode.blind_75.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            nodes_size = len(queue)
            nodes = []

            for _ in range(nodes_size):
                node = queue.popleft()
                nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(nodes)
        return result


class Test(unittest.TestCase):
    testcases = [
        (
            TreeNode(1,
                     TreeNode(2,
                              TreeNode(4),
                              TreeNode(5)
                              ),
                     TreeNode(3,
                              TreeNode(6),
                              TreeNode(7)
                              )
                     ),
            [[1], [2, 3], [4, 5, 6, 7]]
        ),
        (TreeNode(1), [[1]]),
        (None, [])
    ]

    def test(self):
        for root, expected in self.testcases:
            with self.subTest(root=root):
                result = Solution().levelOrder(root)
                self.assertEqual(expected, result)
