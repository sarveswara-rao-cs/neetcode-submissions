"""
Problem: Longest Substring Without Repeating Characters
Level: Medium

Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.


Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.


Example 2:

Input: s = "xxxx"

Output: 1
"""

class Solution:

  def lengthOfLongestSubstring(self, s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
      # If a duplicate is found, shrink the window from the left
      while s[right] in seen:
        seen.remove(s[left])
        left += 1

      seen.add(s[right])
      max_len = max(max_len, right - left + 1)

    return max_len


