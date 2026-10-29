"""
Problem: Longest Consecutive Sequence
Level: Medium

Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 100,000
-10^9 <= nums[i] <= 10^9


"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set for O(1) lookups
        hs = set(nums)
        maxL = 0
        
        for num in nums:
            curL = 0
            
            # Check if 'num' is the absolute start of a consecutive sequence
            # If num-1 is in the set, then 'num' is part of a sequence but not the start
            if num - 1 not in hs: 
                
                # Incrementally build the sequence length as long as consecutive numbers exist
                while num in hs:
                    curL += 1
                    num += 1  # Move to the next consecutive integer
                
                # Keep track of the longest sequence found so far
                maxL = max(maxL, curL)
                
        return maxL