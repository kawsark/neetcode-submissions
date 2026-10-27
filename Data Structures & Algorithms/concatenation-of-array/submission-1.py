# Meta: '{ "time": 5, "felt": "easy", "help": "none" }'
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [None]*(2*len(nums))
        for i in range(len(nums)):
            res[i] = nums[i]
            res[i+len(nums)] = nums[i]
        
        return res