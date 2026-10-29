from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a default dictionary where every new key automatically gets an empty list
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Count frequencies of each character (a-z)
            char_counts = [0] * 26
            for char in s:
                char_counts[ord(char) - ord('a')] += 1
            
            # Convert list to a tuple so it can be used as a dictionary key
            anagram_map[tuple(char_counts)].append(s)
            
        # Return all the grouped lists directly
        return list(anagram_map.values())