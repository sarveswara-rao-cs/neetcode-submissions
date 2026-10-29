class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        # print(hm)
        for s in strs:
            print(s)
            temp = [0] * 26
            for char in s:
                # print(char, s)
                temp[ord(char) - ord('a')] += 1
                # print(temp)
            print(temp)
            hm[tuple(temp)].append(s)
            print(hm)
        lst = []
        for key, value in hm.items():
            lst.append(value)
        return lst