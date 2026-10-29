class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefixsum = [ 0 ]
        
        for i in range(1, len(nums) + 1):
            prefixsum.append(prefixsum[i-1] + nums[i-1])
        
        print(f"nums: {nums}")
        print(f"sums: {prefixsum}")
        
        l, r = 0, 1
        res = None

        while r < len(prefixsum):
            s = prefixsum[r] - prefixsum[l]
            if s >= target:
                if res:
                    res = min(res,r-l)
                else:
                    res = r - l 
                l += 1
                if l == r:
                    r += 1
            else:
                r += 1
        
        if res:
            return res
        else:
            return 0