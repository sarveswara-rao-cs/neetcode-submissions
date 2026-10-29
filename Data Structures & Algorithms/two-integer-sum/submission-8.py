class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        h = {}

        for i in range(len(nums)):
            h[nums[i]] = i
        
        for i in range(len(nums)):
            c = target - nums[i] # calculating the compliment
            if c in h and i != h[c]:
                return [i, h[c]]

