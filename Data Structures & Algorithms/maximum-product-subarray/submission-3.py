class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = curMin = curMax = nums[0]
        # we are keeping track of curMin bcz if another negative values comes it becomes larger

        for num in nums[1:]:
            tempMax = curMax
            curMax = max(num, num * curMax, num*curMin)
            curMin = min(num, num*tempMax, num*curMin)

            res = max(res, curMax)
            print(res, num, curMin, curMax)
        return res