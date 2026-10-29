class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hm = {}
        for i, num in enumerate(nums):
            hm[num] = i
        target = 0
        res = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i!=j:
                    diff = target - nums[i] - nums[j]
                    if diff in hm and hm[diff] != j and hm[diff] != i and hm[diff]>i:
                        print(nums[i], nums[j], diff, hm[diff])
                        res.add(tuple(sorted([nums[i], nums[j], diff])))
        return list(res)