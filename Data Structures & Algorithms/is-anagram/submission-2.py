class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        h1, h2 = {}, {}

        for ch in s:
            if ch in h1:
                h1[ch] = h1[ch] + 1
            else:
                h1[ch] = 1
        for ch in t:
            if ch in h2:
                h2[ch] = h2[ch] + 1
            else:
                h2[ch] = 1
        print(h1.keys())
        print(h1, h2)
        for ch in h1.keys():
            # print(ch)
            # print(h1[ch], h2[ch])
            try:
                if h1[ch] != h2[ch]:
                    return False
            except:
                return False
        return True