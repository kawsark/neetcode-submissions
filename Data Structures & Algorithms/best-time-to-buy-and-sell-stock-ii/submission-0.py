# Meta: '{ "felt":"hard", "time": 25, "help": "Video solution", "Comment": "This is similar to Strava vertical elevation calculation"}'
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0,1

        profit = 0
        while sell < len(prices):
            diff = prices[sell] - prices[buy]
            if diff > 0:
                profit += diff
            else:
                # Assume hold or no change
                pass

            buy += 1
            sell += 1
            
        return profit
        