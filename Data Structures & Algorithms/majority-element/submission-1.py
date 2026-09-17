class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        i = 0
        t = [nums[0], 1]
        for i in range(1, len(nums)):
            if nums[i] == t[0]:
                t[1] += 1
            elif t[1] > 0:
                t[1] -= 1
            else:
                t[0] = nums[i]
                t[1] = 1
            
            print(f"i {i}, current {t[0]}, count: {t[1]}")
        
        return t[0]