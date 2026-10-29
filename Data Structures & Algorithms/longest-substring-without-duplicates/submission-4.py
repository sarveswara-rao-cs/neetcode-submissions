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
        # Tracks the maximum length of a valid substring found so far
        max_len = 0
        
        # 'j' acts as the trailing boundary tracker (starts before the string)
        j = -1
        
        # A set to keep track of all unique characters in the current window
        seen = set()
        
        # 'i' acts as the leading boundary pointer, moving through the string
        for i in range(len(s)):
            # If the current character is already in our set, we have a duplicate.
            # We must slide the left boundary ('j') forward and remove characters 
            # until the duplicate character s[i] is completely cleared out.
            while s[i] in seen:
                j += 1
                seen.remove(s[j])
            
            # Once duplicates are cleared, it is safe to add the current character
            seen.add(s[i])
            
            # Update the maximum length found by checking the current size of our window
            max_len = max(max_len, len(seen))
            
        return max_len