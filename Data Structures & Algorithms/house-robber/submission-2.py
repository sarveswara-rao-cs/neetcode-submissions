"""
House Robber
Medium
Topics
Company Tags
Hints
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.


Example 1:

Input: nums = [1,1,3,3]

Output: 4
Explanation: nums[0] + nums[2] = 1 + 3 = 4.


Example 2:

Input: nums = [2,9,8,3,6]

Output: 16
Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.


"""


class Solution:

  def rob(self, nums: List[int]) -> int:
    # r1 represents the max loot possible up to two houses ago (i - 2)
    # r2 represents the max loot possible up to the previous house (i - 1)
    r1, r2 = 0, 0

    # Iterate through each house in the neighborhood
    for num in nums:
      # Decide the best option for the current house:
      # Option 1: Rob current house (num) + loot from two houses ago (r1)
      # Option 2: Skip current house and keep the loot from the previous house (r2)
      t = max(num + r1, r2)

      # Shift pointers forward for the next iteration:
      r1 = r2  # The previous house (i - 1) now becomes two houses ago (i - 2)
      r2 = t  # The current max loot (i) becomes the previous house (i - 1)

    # r2 holds the maximum accumulated loot after checking all houses
    return r2