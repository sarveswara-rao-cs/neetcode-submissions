class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hm and i != hm[diff]:
                return [i, hm[diff]]
        return []
        