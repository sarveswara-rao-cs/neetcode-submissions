class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums = set(nums)
        l = 0
        for num in nums:
            if (num-1) not in nums:
                le = 1
                while (num + le) in nums:
                    le += 1
                l = max(le, l)


        return l

