class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for word in strs:
            # Create a frequency count array of size 26 for 'a' through 'z'
            count = [0] * 26
            for char in word:
                # Calculate the index for the character (e.g., 'a' is 0, 'b' is 1)
                index = ord(char) - ord('a')
                count[index] += 1
            
            # Use the immutable tuple of counts as the dictionary key
            # Lists are not hashable, but tuples are
            anagram_groups[tuple(count)].append(word)

        # Return all the values of the dictionary, which are the grouped anagrams
        return list(anagram_groups.values())