# https://leetcode.com/problems/contains-duplicate-ii/
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        sub = set()
        # Populate the set initially
        i = 0
        while i <= k and i < len(nums):
            if nums[i] in sub:
                return True
            else:
                sub.add(nums[i])
            
            i += 1
        
        #print(f"Sub now: {sub}")


        left, right = 1, k+1

        while right < len(nums):
            sub.remove(nums[left-1])
            if nums[right] in sub:
                return True
            else:
                sub.add(nums[right])
            
            # Shift the window
            right += 1
            left += 1
        
        return False