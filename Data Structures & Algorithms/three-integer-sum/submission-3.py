"""
Problem: 3Sum
Level: Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.


"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Map each number to its last seen index for O(1) lookups
        hm = {}
        for i, num in enumerate(nums):
            hm[num] = i
            
        target = 0
        res = set() 
        
        # Outer loop fixes the first element
        for i in range(len(nums)):
            # CRITICAL CORRECTION: Start j at i + 1. 
            # This automatically guarantees that i != j, removing the need for an inner IF statement.
            for j in range(i + 1, len(nums)):
                diff = target - nums[i] - nums[j]
                
                # Because i < j and we enforce hm[diff] > j, 
                # we naturally guarantee that i, j, and hm[diff] are three completely unique indices.
                if diff in hm and hm[diff] > j:
                    res.add(tuple(sorted([nums[i], nums[j], diff])))
                        
        return list(res)