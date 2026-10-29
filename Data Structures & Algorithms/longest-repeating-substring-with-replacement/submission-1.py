class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        res = 0
        mf = 0
        l = 0
        for r in range(len(s)):
            hm[s[r]] = 1 + hm.get(s[r], 0)

            mf = max(mf, hm[s[r]])

            print(l, r, mf, (r-l+1-mf) > k)

            while r-l + 1 - mf > k:
                print(s[l])
                hm[s[l]] -=1
                l += 1
            res = max(res, r-l+1)
        return res
