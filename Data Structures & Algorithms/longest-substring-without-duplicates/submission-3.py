class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0

        j = -1
        seen = set()
        #s="pwwkew"
        for i in range(len(s)):
            print(seen)
            while j < i:
                if s[i] in seen:
                    j += 1
                    seen.remove(s[j])
                else:
                    seen.add(s[i])
                    break
            l = max(l, len(seen))
            # print(seen) 
        return l
                
