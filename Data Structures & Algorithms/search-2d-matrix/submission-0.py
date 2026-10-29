class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(len(matrix))
        l, r = 0, len(matrix)-1
        while l<=r:
            mid = (l+r)//2
            print(l, r, mid)
            # print(l, mid, r, nums)
            if matrix[mid][0] == target:
                return True
            else:
                if matrix[mid][0] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        print('found target might be in ', r)
        nums = matrix[r]
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            print(l, r, mid)
            # print(l, mid, r, nums)
            if nums[mid] == target:
                return True
            else:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return False