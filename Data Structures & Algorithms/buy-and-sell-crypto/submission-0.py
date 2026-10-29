class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r, res = 0, 1, 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            print(prices[l], prices[r], res)
            r += 1
        return res


