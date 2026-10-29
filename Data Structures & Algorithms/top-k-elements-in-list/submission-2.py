class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]] += 1
            else:
                hm[nums[i]] = 1
        
        arr = []
        for i in hm.keys():
            print(i, hm[i])
            arr.append([hm[i], i])
        
        arr.sort()

        lst = []
        while len(lst) < k:
            lst.append(arr.pop()[1])
        return lst
