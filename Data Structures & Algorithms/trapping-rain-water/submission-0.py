class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax, min_ij = [], [0]*len(height), [0]*len(height)

        leftMax.append(0)
        for i in range(1, len(height)):
            leftMax.append(max(leftMax[i-1], height[i-1]))
        # print(leftMax)        
        
        for i in range(len(height)-2, 0, -1):
            rightMax[i] = max(rightMax[i+1], height[i+1])
        

        for i in range(len(height)):
            min_ij[i] = min(leftMax[i], rightMax[i])
        
        print(leftMax)
        print(rightMax)
        print()
        print(height)
        print(min_ij)

        res = 0
        for i in range(len(height)):
            if min_ij[i] - height[i] > 0:
                res += min_ij[i] - height[i]
        

        return res
