import unittest
from typing import List, Optional

from TreeNode import TreeNode


# - theoretical lower bound: O(n)
class P94:
    """
    - time complexity: O(n)
    - space complexity: O(n), cause new array and stack for recursion
    """

    def inorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def traverse(node: Optional[TreeNode], result: List[int]):

            if not node:
                return None

            traverse(node.left, result)
            result.append(node.val)
            traverse(node.right, result)

        result = []
        traverse(root, result)
        return result

    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        node = root

        while node or stack:

            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result.append(node.val)

            node = node.right
        return result


class Test(unittest.TestCase):
    testcases = [
        # (TreeNode(1, None, TreeNode(2, TreeNode(3), None)), [1, 3, 2]),
        # (TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
        #           TreeNode(3, None, TreeNode(8, TreeNode(9), None))), [4, 2, 6, 5, 7, 1, 3, 9, 8]),
        # (None, []),
        (TreeNode(1), [1])
    ]

    def test_recursive(self):
        for root, expected in self.testcases:
            with self.subTest(root):
                result = P94().inorderTraversal_recursive(root)
                self.assertEqual(expected, result)

    def test_iterative(self):
        for root, expected in self.testcases:
            with self.subTest(root):
                result = P94().inorderTraversal_iterative(root)
                self.assertEqual(expected, result)