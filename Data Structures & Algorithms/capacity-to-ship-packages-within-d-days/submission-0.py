# Meta: '{"felt":"hard", "time": 35, "help": "AI", "Comment": "Similar to Koko, we iterate over not the data array itself but just a list of integers which is the possible weights"}'
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        mid_weight = l
        res = r

        while l <= r:
            mid_weight = (l + r) // 2
            mid_days = self.get_days(weights, mid_weight)
            if mid_days < days: # Weight limit is acceptable but high, decrease
                res = min(res,mid_weight)
                r = mid_weight - 1

            else: # Weight limit is too low, increase
                l = mid_weight + 1
        
        return res
                
    
    def get_days(self, weights, max_weight):
        res = 0
        usage = max_weight 
        for w in weights:
            d = usage - w
            if d < 0:
                res += 1
                usage = max_weight - w
            else:
                usage = d
        
        return res


        