class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        maxL = 0
        start, end = 0, 0
        for i in range(len(s)):
            curL = 0

            # for even length and odd length
            for j in range(2):
                l, r = i, i + j

                while l>=0 and r < len(s) and s[l] == s[r]:
                    curL = r - l + 1
                    if curL > maxL:
                        maxL = curL
                        start, end = l, r
                    l -= 1
                    r += 1

        return s[start:end+1]
