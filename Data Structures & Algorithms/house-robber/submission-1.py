class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 0

        # r1, r2, 1, 1, 3, 3
        for num in nums:
            t = max(num+r1, r2)
            r1 = r2
            r2 = t
            
        return r2

