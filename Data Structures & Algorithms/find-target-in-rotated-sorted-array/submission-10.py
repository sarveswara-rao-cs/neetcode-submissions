class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l <= r:

            mid = (l + r) // 2
            print(nums[l], nums[mid], nums[r])
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[l]: # left-sorted array
                if nums[mid] >= target and target >= nums[l]:
                    r =  mid - 1
                else:
                    l = mid + 1
            else: # right-sorted array
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

