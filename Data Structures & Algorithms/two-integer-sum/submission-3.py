# Meta: '{ "time": 5, "felt": "easy", "help": "none" }'
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Populate and lookup map as we go
        numsmap = { }
        for i in range(len(nums)):
            d = target - nums[i]
            if d in numsmap:
                return [numsmap[d],i]
            
            numsmap[nums[i]] = i

 
        