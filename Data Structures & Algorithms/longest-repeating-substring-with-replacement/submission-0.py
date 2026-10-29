class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        res = 0

        l = 0
        mf = 0

        for r in range(len(s)):
            if s[r] in hm:
                hm[s[r]] += 1
            else:
                hm[s[r]] = 1   
            
            mf = max(mf, hm[s[r]]) # max freq till now

            while (r - l + 1) - mf > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

                    

        return res
            