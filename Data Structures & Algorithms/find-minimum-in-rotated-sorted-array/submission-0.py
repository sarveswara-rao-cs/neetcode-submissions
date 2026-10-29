class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            print(nums[l], nums[m], nums[r], res)
            res = min(nums[m], res)
            if nums[m] >= nums[l]:
                res = min(res, nums[l])
                l = m + 1
            else:
                r = m - 1
            
        return res