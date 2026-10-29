class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 1: return heights[0]
        if len(heights) == 0: return 0

        # i, j = 0, len(heights)-1
        m = 0

        # def recur(heights, i, j, m): # this takes more time
        #     if i < j:
        #         min_val = min(heights[i], heights[j])
        #         diff = abs(i - j)
        #         m_c = min_val * diff
        #         m = max(m, m_c)
        #         m1 = max(recur(heights, i+1, j, m), recur(heights, i, j-1, m))
        #         m = max(m, m1)
        #         return m
        #     return 0
        
        # m = recur(heights, 0, len(heights)-1, 0)
        
        i, j = 0, len(heights)-1
        m = 0
        while i < j:
            min_val = min(heights[i], heights[j])
            diff = abs(i - j)
            m_c = min_val * diff
            m = max(m, m_c)

            if min_val == heights[i]:
                i += 1
            else:
                j -= 1
        
        return m
