class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #---brute force -o(n2)
        # lst = []
        # for i in range(len(nums)):
        #     p = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             p *= nums[j]
        #     # print(p, lst)
        #     lst.append(p)

        # somewhat optimal - O(n)

        count_zeros = 0
        res = [0]*len(nums)
        
        for num in nums:
            if num == 0:
                count_zeros +=1
                if count_zeros > 1:
                    return res

        # calculate the product of all numbers except one zero
        if count_zeros == 1:
            print(count_zeros, res)
            p = 1
            for num in nums:
                if num != 0:
                    p *= num
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = p
            return res
        p = 1
        for num in nums:
            p *= num
        for i in range(len(nums)):
            res[i] = int(p/nums[i])
        return res


            
        
        


        return lst