# Meta: '{"felt" : "medium", "time": 9, "help": "none" }'
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        res = 0
        while sell < len(prices):
            d = prices[sell] - prices[buy]
            if d < 0:
                buy += 1
            else:
                res = max(res,d)
                sell += 1
    
        return res




        