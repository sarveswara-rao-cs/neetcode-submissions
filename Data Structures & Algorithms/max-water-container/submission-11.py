"""
Problem: Container With Most Water
Level: Medium

You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Input: height = [1,7,2,5,4,7,3,6]

Output: 36

Explanation: The bars at indices 1 and 7 have heights 7 and 6. The container has width 7 - 1 = 6 and height min(7, 6) = 6, so it can store 6 * 6 = 36 units of water. This is the maximum possible area.


Example 2:

Input: height = [2,2,2]

Output: 4
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