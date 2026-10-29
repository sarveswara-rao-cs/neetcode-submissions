class Solution:

  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    prefix_p = [1] * n
    sufix_p = [1] * n
    res = [0] * n

    # Build prefix products
    for i in range(1, n):
      prefix_p[i] = prefix_p[i - 1] * nums[i - 1]

    # Build suffix products
    for i in range(n - 2, -1, -1):
      sufix_p[i] = sufix_p[i + 1] * nums[i + 1]

    # Combine prefix and suffix
    for i in range(n):
      res[i] = prefix_p[i] * sufix_p[i]

    return res