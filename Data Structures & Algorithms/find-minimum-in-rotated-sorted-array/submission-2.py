class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0] 

        res = nums[0]

        l, r = 0, len(nums) - 1

        while l<=r:

            mid = (l + r) // 2

            res = min(res, nums[mid])

            if nums[l] <= nums[mid]:
                if res <= nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if res <= nums[l]:
                    r = mid -1
                else:
                    l = mid + 1
        return res


            


