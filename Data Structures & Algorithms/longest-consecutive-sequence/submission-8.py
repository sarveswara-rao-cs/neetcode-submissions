class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        maxL = 0
        for num in nums:
            curL = 0
            if num-1 not in hs: # meaning that the cur element is the start
                while num in hs:
                    curL += 1
                    num += 1
            maxL = max(maxL, curL)
        return maxL
