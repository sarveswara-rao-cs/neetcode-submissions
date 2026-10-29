class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # for even length and odd length
            for j in range(2):
                l, r = i, i + j

                while l>=0 and r < len(s) and s[l] == s[r]:
                    count += 1# counts every palindromic substring
                    l -= 1
                    r += 1
        return count