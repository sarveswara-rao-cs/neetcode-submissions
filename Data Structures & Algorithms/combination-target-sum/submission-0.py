class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, cur, total):

            if total > target: return
            if i >= len(nums): return
            if total == target:
                res.append(cur.copy())
                return

            # consider the ith element
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # if the cur element at i is not considered

            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)

        return res