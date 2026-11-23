# Meta: '{"felt":"easy","Time":10,"Help":"none","Comment":"2 pointer variation"}'
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = len(nums) - 1
        l = 0
        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                nums[r] = val
                r -= 1
                print(f"{nums}")
            else:
                l += 1
        
        return l


        