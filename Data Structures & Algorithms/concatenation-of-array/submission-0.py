class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        s = len(nums)
        for i in range(s):
            nums.append(nums[i])
        
        return nums