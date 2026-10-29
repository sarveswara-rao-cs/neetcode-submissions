class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0

        prefix_p = [0] * len(nums)
        sufix_p = [0] * len(nums)
        res = [0] * len(nums)
        prefix_p[0] = 1
        sufix_p[-1] = 1
        for i, num in enumerate(nums):
            if num == 0: zero_count += 1
            if i != 0:
                prefix_p[i] = prefix_p[i-1] * nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            sufix_p[i] = sufix_p[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            res[i] = prefix_p[i] * sufix_p[i]
        print('prefix', prefix_p)
        print(sufix_p)
        print(zero_count)

        if zero_count > 1: return res
        return res

