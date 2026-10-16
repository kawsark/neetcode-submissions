class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixmap = {0 : 1}
        sum = 0
        r = 0
        for i in range(len(nums)):
            sum += nums[i]        
            diff = sum - k

            r += prefixmap.get(diff,0)

            if sum in prefixmap:
                prefixmap[sum] += 1
            else:
                prefixmap[sum] = 1
        
        return r


