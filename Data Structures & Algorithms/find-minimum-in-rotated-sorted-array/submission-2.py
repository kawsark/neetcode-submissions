# Meta: '{"felt":"hard","Time":"25,"Help":"solution","Comment":"Binary search variant"}'
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break # Array or sub-array already sorted

            mid = (l + r) // 2
            print(f"[{nums[l]}|{nums[mid]}|{nums[r]}]")
            if nums[mid] >= nums[l]:
                l = mid + 1 # Search left uless array is pre-sorted
            else:
                r = mid - 1
            res = min(nums[mid], res)
        
        return res


                 


        