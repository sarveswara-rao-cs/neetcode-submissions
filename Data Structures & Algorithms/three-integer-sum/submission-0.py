class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <=2: return []

        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = i

        target = 0
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diff = target - nums[i] - nums[j]
                if diff in nums:
                    print('here', hm[diff], len(nums))
                    if hm[diff] > j:
                        if diff in hm and (i!=hm[diff]) and (j!=hm[diff]):
                            print(i, j, hm[diff])
                            r = [nums[i], nums[j], diff]
                            r = sorted(r)
                            if r in res:
                                continue
                            else:
                                res.append(r)
                        
        return res
