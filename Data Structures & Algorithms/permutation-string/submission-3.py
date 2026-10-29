class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l1 = len(s1)
        hm1 = {}
        for ch in s1:
            hm1[ch] = 1 + hm1.get(ch, 0)

        for i in range(len(s2)-l1+1):
            print(s1, s2[i:i+l1])
            ss2 = s2[i:i+l1]
            hm2 = {}
            for ch in ss2:
                hm2[ch] = 1 + hm2.get(ch, 0)
            
            count = 0
            for k, v in hm1.items():
                try:
                    if hm1[k] == hm2[k]:
                        count += 1
                except:
                    continue
            if count == len(hm1):
                return True
        return False