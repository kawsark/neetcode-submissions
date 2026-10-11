class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        mp = 0
        while r < len(prices):
            p = prices[r] - prices[l]
            if p > 0: # Buy day
                mp = max(p, mp)
            else:
                l = r
            r += 1
        
        return mp