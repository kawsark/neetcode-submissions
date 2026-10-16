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
        
        return unique+1
            

    def removeDuplicates2(self, nums: List[int]) -> int:
        i = r = 0
        k = len(nums)-1

        while i < k:
            j = i
            d = 0
            while j+1 < k and nums[j] == nums[j+1]:
                d += 1
                r += 1
                j += 1
                k -= 1
            
            # i = 0, d = 1, k = 2 ->
            if d > 0:
                for k in range(i+d+1,len(nums)):
                    nums[k-d] = nums[k]

            i += 1

        return len(nums) - r
        