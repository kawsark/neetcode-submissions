# Meta: '{"felt":"easy","Time":5,"Help":"none","Comment":""}'
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 1
        res = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == res:
                freq += 1
            else:
                freq -= 1
            
            if freq == 0:
                res = nums[i]
                freq = 1
        
        return res
