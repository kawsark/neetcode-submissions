class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Convert list to hashmap
        numsmap = { }
        for i in range(len(nums)):
            d = target - nums[i]
            if d in numsmap:
                return [numsmap[d],i]
            
            numsmap[nums[i]] = i

 
        