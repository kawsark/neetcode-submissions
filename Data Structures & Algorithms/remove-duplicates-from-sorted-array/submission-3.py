class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curUnique = nums[0]
        unique = 0
        i = 1

        for i in range(1, len(nums)):
            if nums[i] == curUnique:
                pass # Not a unique value
            else: # Unique value
                curUnique = nums[i]
                unique += 1
                nums[unique] = nums[i]
        
        return unique + 1
        