# Meta: '{"felt":"hard", "time": 45, "help": "Solution", "Comment": "Use comments to help articulate if moving left or right. And in this case we iterate over not the data array itself but just a list of integers which is the rate"}'

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_b = max(piles)
        l , r = 1, max_b
        res = None

        while l <= r:
            mid = (l + r) // 2
            total_hours = self.getTotalHours(piles,mid)
            
            if total_hours <= h: # Rate might be too high
                if res:
                    res = min(mid,res)
                else:
                    res = mid
                    
                r = mid - 1
            else: # Rate is too low
                l = mid + 1
        
        return res
            

    
    def getTotalHours(self, piles: List[int], k: int) -> int:
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)

        return hours