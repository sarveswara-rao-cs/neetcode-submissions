"""
Longest Palindromic Substring
Medium

Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.

Example 1:

Input: s = "ababd"

Output: "bab"
Explanation: Both "aba" and "bab" are valid answers.

Example 2:

Input: s = "abbc"

Output: "bb"

"""

class Solution:

  def longestPalindrome(self, s: str) -> str:
    # Track the length and boundaries of the longest palindrome found so far
    maxL = 0
    start, end = 0, 0

    # Consider every index 'i' as the potential center of a palindrome
    for i in range(len(s)):
      curL = 0

      # Inner loop handles both palindrome structures:
      # j = 0 -> Odd length (center is s[i])
      # j = 1 -> Even length (center is between s[i] and s[i+1])
      for j in range(2):
        l, r = i, i + j

        # Expand outwards as long as pointers are in bounds and characters match
        while l >= 0 and r < len(s) and s[l] == s[r]:
          curL = r - l + 1  # Calculate current palindrome length

          # If the current palindrome is longer than our max, update boundaries
          if curL > maxL:
            maxL = curL
            start, end = l, r

          # Move pointers away from the center
          l -= 1
          r += 1

    # Return the longest palindromic substring using slicing
    return s[start : end + 1]
