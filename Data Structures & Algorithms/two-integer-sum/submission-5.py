class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        h = {}
        for i, num in enumerate(nums):
            h[num] = i
        for i, num in enumerate(nums):
            k = target - num
            if k in h and i != h[k]:
                print(i, h[k])
                if i > h[k]:
                    return [h[k], i]
                else:
                    return [i, h[k]]
