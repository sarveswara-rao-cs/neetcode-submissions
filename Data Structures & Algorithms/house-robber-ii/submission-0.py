class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return nums
        if len(nums)==1: return nums[0]
        def helper(nums):
            r1, r2 = 0, 0
            #r1, r2, nums[0], nums[1]
            for n in nums:
                rob = max(n + r1, r2)
                r1 = r2
                r2 = rob
            
            return r2 # r2 contains the max rob        
        return max(helper(nums[1:]), helper(nums[:-1]))
