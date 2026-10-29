from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies using a hash map
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)
        
        # 2. Invert pairs to (frequency, number) for sorting
        lst = []
        for key, value in hm.items():
            lst.append((value, key))
        
        # 3. Sort by frequency in ascending order
        lst.sort()
        # 4. Extract the top k elements by iterating backwards
        final_lst = []
        for i in range(len(lst) - 1, -1, -1):
            final_lst.append(lst[i][1])
            if len(final_lst) == k:
                return final_lst
                
        return final_lst