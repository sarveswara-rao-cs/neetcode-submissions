# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        res = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []# for storing all values in a level
            ql = len(q)
            print(ql)
            for i in range(ql):
                c = q.popleft()
                if c:
                    # print(c)
                    level.append(c.val)
                    q.append(c.left)
                    q.append(c.right)
                # print(c.val, level, ql)
            if level:
                res.append(level)
            print(level, ql)
        return res

            


