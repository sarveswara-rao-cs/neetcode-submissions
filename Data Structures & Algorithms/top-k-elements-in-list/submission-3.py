class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
        print(hm)

        lst = []
        for key, value in hm.items():
            lst.append((value, key))
        lst = sorted(lst)
        final_lst = []
        for i in range(len(hm)-1, -1, -1):
            print('i', i, lst[i][1])

            final_lst.append(lst[i][1])
            if len(final_lst) == k:
                return final_lst

        print(final_lst)

        return []