"""
Palindromic Substrings
Medium

Given a string s, return the number of substrings within s that are palindromes.

A palindrome is a string that reads the same forward and backward.

Example 1:

Input: s = "abc"

Output: 3
Explanation: "a", "b", "c".

Example 2:

Input: s = "aaa"

Output: 6
Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.
"""


class Solution:

  def countSubstrings(self, s: str) -> int:
    count = 0

    # Consider every index 'i' as a potential palindrome center
    for i in range(len(s)):
      # Inner loop handles both types of centers:
      # j = 0 -> Odd length palindromes (e.g., center at 'a' in "aba")
      # j = 1 -> Even length palindromes (e.g., center between 'b' and 'b' in "abba")
      for j in range(2):
        l, r = i, i + j

        # Expand outwards from the center as long as characters match and stay in bounds
        while l >= 0 and r < len(s) and s[l] == s[r]:
          count += 1  # Found a valid palindromic substring! Increment count.
          l -= 1  # Move left pointer outward
          r += 1  # Move right pointer outward

    return count