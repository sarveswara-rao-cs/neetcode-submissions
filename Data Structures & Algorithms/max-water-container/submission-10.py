"""
Problem: Container With Most Water
Level: Medium

You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.


"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize two pointers at the far ends of the array
        l, r = 0, len(heights) - 1
        
        max_water = 0
        
        # Loop until the two pointers meet
        # CORRECTION: Using < instead of <= because a single line (l == r) has a width of 0 and holds no water
        while l < r:
            # The water volume is limited by the shorter line multiplied by the distance between them
            # Note: abs(l - r) is simplified to (r - l) since r is always greater than l
            cur_max = min(heights[l], heights[r]) * (r - l)
            
            # Update the global maximum water found so far
            max_water = max(cur_max, max_water)
            
            # Move the pointer pointing to the shorter line inward, 
            # as keeping it can never yield a larger area with a smaller width
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        
        return max_water