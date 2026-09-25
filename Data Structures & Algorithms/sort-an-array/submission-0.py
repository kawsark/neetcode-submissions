class Solution:
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        p = len(nums) // 2
        left = nums[:p]
        right = nums[p:]

        left = self.sortArray(left)      
        right = self.sortArray(right)

        return self.merge(left,right)

    
    def merge(self, left: list[int], right: list[int]) -> list[int]:

        result = []
        l = r = 0
        
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
            
        while l < len(left):
            result.append(left[l])
            l += 1

        while r < len(right):
            result.append(right[r])
            r += 1
        
        return result

