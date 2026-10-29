class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = [0] * len(nums)
        res = dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            res = max(dp[i], res)
        
        print(dp)
        return res