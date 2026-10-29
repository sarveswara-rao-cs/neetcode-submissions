# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = collections.deque()

        q.append(root)
        res = []
        while q:
            level = []
            ql = len(q)
            for i in range(ql):
                c = q.popleft()
                if c:
                    level.append(c.val)
                    q.append(c.left)
                    q.append(c.right)
            if level:
                res.append(level)
        return res