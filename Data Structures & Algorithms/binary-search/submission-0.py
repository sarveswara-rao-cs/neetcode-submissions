class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #nums=[-1,0,2,4,6,8], target = 4
        # l=0, mid=2, r=5
        # l=3, mid=4, r = 5
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            # print(l, mid, r, nums)
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
