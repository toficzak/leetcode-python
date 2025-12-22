from typing import Optional

from TreeNode import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        self.swap(root)

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def swap(self, root: TreeNode):
        temp_node = root.left
        root.left = root.right
        root.right = temp_node

if __name__ == '__main__':

    # [4,2,7,1,3,6,9]
    tree = TreeNode(4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7, TreeNode(6), TreeNode(9)))

    result = Solution().invertTree(tree)
    print(result)