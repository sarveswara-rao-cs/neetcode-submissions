class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # count = 0
        # while n:
        #     n = n & (n-1) # this will remove the last bit
        #     count += 1
        # return count

        count = 0
        while n:
            r = n % 2
            if r == 1:
                count += 1
            n = n // 2
        return count