class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(numbers)):
            hm[numbers[i]] = i
        
        # print(hm)
        for i in range(len(numbers)):
            diff = target-numbers[i]
            if diff in hm and hm[diff] > i:
                f, s = i, hm[diff]
                return [i+1, hm[diff]+1]
            
                
