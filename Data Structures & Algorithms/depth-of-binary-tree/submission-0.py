# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def find_depth(node):
            if not node: return 0

            m = max(1+find_depth(node.left), 1+find_depth(node.right))

            return m
        return find_depth(root)