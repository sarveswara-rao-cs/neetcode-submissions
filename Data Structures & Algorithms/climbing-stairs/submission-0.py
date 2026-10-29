class Solution:
    def climbStairs(self, n: int) -> int:

        m = [-1] * n
        print(m)

        def dfs(i):

            if i >= n:
                return i == n
            if m[i] != -1:
                return m[i]
            m[i] = dfs(i+1) + dfs(i+2)
            print(m)
            return m[i]

        return dfs(0)