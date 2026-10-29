class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        max_water = 0
        while l<=r:
            # print(l, r)
            t = min(heights[l], heights[r]) * abs(l - r)
            max_water = max(t, max_water)
            print(l, r, heights[l], heights[r], t, max_water)
            # print(max_water)
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        
        return max_water