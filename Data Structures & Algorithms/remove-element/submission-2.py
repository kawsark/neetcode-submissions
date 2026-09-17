class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        k = 0
        i = 0
        while i < l:
            if nums[i] == val:
                nums.pop(i)
                l -= 1
                i -= 1
            else:
                k += 1

            i += 1

        return k
        