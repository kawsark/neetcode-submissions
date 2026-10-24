class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:            
            mid = left + ((right - left) // 2)
            val = nums[mid]
            if target == val:
                return mid
            elif val < target: # Check right
                left = mid+1
            elif val > target: # Check left
                right = mid-1
            
        return left
