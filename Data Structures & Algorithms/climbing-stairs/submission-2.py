"""
Climbing Stairs
Easy


You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:

Input: n = 2

Output: 2
Explanation:

1 + 1 = 2
2 = 2
Example 2:

Input: n = 3

Output: 3
Explanation:

1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3


Imagine you are standing on the very top step (step n). Because you can only take 1 or 2 steps at a time, there are only two possible places you could have jumped from to get to the top:
1. The step right below it: (n - 1)
2. The step two choices below it: (n - 2)
Therefore, the total number of unique ways to reach step n is simply the sum of the ways to reach step n - 1 and step n - 2.

"""


class Solution:

  def climbStairs(self, n: int) -> int:
    # Base cases: 1 way to climb 1 step, 2 ways to climb 2 steps
    if n <= 2:
      return n

    # Initialize the base cases for the DP steps
    # 'first' represents solutions for (i - 2) steps
    # 'second' represents solutions for (i - 1) steps
    first = 1
    second = 2

    # Fill up the choices iteratively up to n steps
    # The number of ways to reach step i is the sum of ways to reach (i-1) and (i-2)
    for i in range(3, n + 1):
      current = first + second
      first = second  # Shift variables forward for the next iteration
      second = current

    return second