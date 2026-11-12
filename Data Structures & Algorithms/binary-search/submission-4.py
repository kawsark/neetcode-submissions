# Meta: '{"felt":"medium", "time": 10: , "help": "none", "Comment": "3 main things to remember to cover edge cases: l <= r (to cover single or 2 item array), l = mid + 1 (exclude current mid), and r = mid - 1 (exclude current mid)"}'
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = mid = 0
        r = len(nums)-1
        
        while l <= r:
            mid = l + ((r - l) // 2)
            m = nums[mid]
            if target == m:
                return mid
            elif target > m:
                l = mid + 1
            else:
                r = mid - 1

        return -1

